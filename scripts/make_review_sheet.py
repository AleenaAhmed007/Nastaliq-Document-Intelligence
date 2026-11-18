#!/usr/bin/env python3
"""
make_review_sheet.py: build Excel sheets for human verification of the text_line transcriptions.

    python scripts/make_review_sheet.py --pred results/ocr/utrnet_large_w400_val.tsv --split val --batches 4

Writes data/review/<split>_review_b<N>.xlsx, one file per reviewer. Pages are never split across
files. Each row shows the line crop image, the original gold text, the UTRNet prediction, how
much the two disagree, and empty columns for the reviewer: status, verified_text, reviewer, notes.

The original gold (data/processed/lines.tsv) and the raw predictions are never modified.
scripts/merge_review.py reads the filled sheets back into data/annotations/verified_lines.tsv.

Every line in the sheet must be reviewed, not only the high-disagreement ones: the disagreement
column only helps reviewers spot likely errors. Verifying only lines where UTRNet disagrees with
the gold would bias the evaluation in UTRNet's favour against every other OCR system.

--overlap N  puts N random lines into TWO reviewers' files (double_review = yes) so that
             merge_review.py can measure inter-reviewer agreement. Reviewers must not compare notes.
--only TSV   builds a sheet for just the crops listed in TSV (e.g. the conflicts file from
             merge_review.py); use with --name val_adjudication to make an adjudication sheet.
A <name>_manifest.json records the dataset version (lines.tsv hash, git commit), the prediction
file and which crops went into which file.
"""
import argparse
import datetime
import hashlib
import io
import json
import os
import random
import re
import subprocess

from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from PIL import Image

import paths as P
from eval_ocr import URDU_LETTER, edit, handwritten_lines, normalise, read_tsv

STATUSES = ["gold_ok", "utrnet_ok", "corrected", "exclude", "illegible"]
COLUMNS = [  # header, width (chars)
    ("#", 5), ("crop image", 112), ("crop_id", 22), ("type", 7), ("category", 11), ("disagree %", 10),
    ("double_review", 9), ("original_gold", 60), ("utrnet_pred", 60), ("status", 12), ("verified_text", 60),
    ("reviewer", 12), ("review_date", 12), ("notes", 25)]
COL = {h: i + 1 for i, (h, _) in enumerate(COLUMNS)}
URDU_ALIGN = Alignment(horizontal="right", vertical="center", wrap_text=True, readingOrder=2)
CELL_ALIGN = Alignment(vertical="center", wrap_text=True)
URDU_FONT = Font(name="Jameel Noori Nastaleeq", size=14)
FILL_HIGH = PatternFill("solid", fgColor="F8CBAD")
FILL_MED = PatternFill("solid", fgColor="FFE699")
FILL_EDIT = PatternFill("solid", fgColor="E2EFDA")

INSTRUCTIONS = [
    "Line transcription review",
    "",
    "Goal: for every row, write down exactly what is printed or written in the crop image.",
    "Trust the IMAGE only. Both original_gold and utrnet_pred may be wrong.",
    "",
    "For each row, choose a status (dropdown in the green 'status' column):",
    "  gold_ok     original_gold matches the image exactly. Leave verified_text empty.",
    "  utrnet_ok   utrnet_pred matches the image exactly. Leave verified_text empty.",
    "  corrected   neither is exact. Type (or copy and fix) the correct text in verified_text.",
    "  exclude     not document text: CamScanner watermark, box cuts through text, stamp noise.",
    "  illegible   the crop cannot be read with confidence.",
    "Fill 'reviewer' with your name and 'review_date' with the day you reviewed it (e.g. 2026-11-20)",
    "on every row you review. Use 'notes' for anything unusual.",
    "",
    "Transcription rules:",
    "  - Use Urdu letters: ی not ي, ک not ك, ہ not ه, and ڈ ٹ ڑ (not ذ ث ر) where the image shows them.",
    "  - Write digits as they are printed: 2026 stays 2026, ۲۰۲۶ stays ۲۰۲۶ (the evaluation maps both).",
    "  - Keep the punctuation that is printed (۔ / - :). Do not add text that is not in the crop.",
    "  - Only transcribe what is inside this crop, even if the sentence continues on the next line.",
    "  - Handwritten dates / numbers: transcribe them too; mark illegible if you are unsure.",
    "",
    "'disagree %' = how different original_gold and utrnet_pred are. Orange/yellow rows are likely",
    "errors, but every row must be reviewed: low disagreement does not mean the gold is right.",
    "",
    "'double_review = yes' rows are also given to another reviewer to measure agreement.",
    "Review them like any other row and do NOT discuss them with the other reviewers.",
    "",
    "Do not edit the original_gold or utrnet_pred columns, and do not sort or delete rows.",
    "When done, send the file back; scripts/merge_review.py collects all sheets.",
]


def line_no(crop):
    m = re.search(r"_L(\d+)\.png$", crop)
    return int(m.group(1)) if m else 0


def crop_thumb(path, target_h, max_w):
    """Scale to target_h; lines wider than max_w are cut into right-to-left pieces stacked vertically."""
    img = Image.open(path).convert("RGB")
    w, h = img.size
    img = img.resize((max(1, round(w * target_h / h)), target_h), Image.Resampling.LANCZOS)
    w = img.size[0]
    if w > max_w:
        pieces, right = [], w
        while right > 0:                                  # Urdu reads right to left: right piece first
            left = max(0, right - max_w)
            pieces.append(img.crop((left, 0, right, target_h)))
            right = left
        gap = 6
        sheet = Image.new("RGB", (max_w, len(pieces) * (target_h + gap) - gap), "white")
        for k, p in enumerate(pieces):
            sheet.paste(p, (max_w - p.size[0], k * (target_h + gap)))   # right-aligned like the page
        img = sheet
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf, img.size


def assign_batches(rows, n):
    """Greedy: biggest pages first, each to the batch with the fewest lines. Keeps pages whole."""
    by_page = {}
    for r in rows:
        by_page.setdefault(r["page_id"], []).append(r)
    batches = [[] for _ in range(n)]
    for pid in sorted(by_page, key=lambda p: -len(by_page[p])):
        min(batches, key=len).extend(by_page[pid])
    for b in batches:
        b.sort(key=lambda r: (r["page_id"], line_no(r["crop"])))
    return [b for b in batches if b]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def write_sheet(path, rows, preds, hw, crop_root, img_h, max_w, overlap=frozenset()):
    wb = Workbook()
    ins = wb.active
    ins.title = "instructions"
    for i, t in enumerate(INSTRUCTIONS, 1):
        ins.cell(i, 1, t).font = Font(bold=(i == 1), size=14 if i == 1 else 11)
    ins.column_dimensions["A"].width = 120

    ws = wb.create_sheet("review")
    wb.active = 1
    for h, width in COLUMNS:
        c = ws.cell(1, COL[h], h)
        c.font = Font(bold=True)
        ws.column_dimensions[c.column_letter].width = width
    ws.freeze_panes = "C2"
    dv = DataValidation(type="list", formula1='"%s"' % ",".join(STATUSES), allow_blank=True,
                        showErrorMessage=True, errorTitle="status", error="Pick a status from the list")
    ws.add_data_validation(dv)

    for i, r in enumerate(rows, 2):
        crop_id = os.path.splitext(os.path.basename(r["crop"]))[0]
        gold, pred = r["text"], preds.get(r["crop"], "")
        ng, np_ = normalise(gold), normalise(pred)
        dis = edit(ng, np_) / max(len(ng), 1) if r["crop"] in preds else None
        if (r["page_id"], r["region_id"]) in hw:
            cat = "handwritten"
        elif URDU_LETTER.search(ng):
            cat = "urdu"
        else:
            cat = "num_latin"
        vals = {"#": i - 1, "crop_id": crop_id, "type": r["type"], "category": cat,
                "disagree %": round(100 * dis) if dis is not None else "",
                "double_review": "yes" if r["crop"] in overlap else "",
                "original_gold": gold, "utrnet_pred": pred}
        for h, v in vals.items():
            c = ws.cell(i, COL[h], v)
            c.alignment = URDU_ALIGN if h in ("original_gold", "utrnet_pred") else CELL_ALIGN
            if h in ("original_gold", "utrnet_pred"):
                c.font = URDU_FONT
        if dis is not None and dis >= 0.15:
            ws.cell(i, COL["disagree %"]).fill = FILL_HIGH if dis >= 0.3 else FILL_MED
        for h in ("status", "verified_text", "reviewer", "review_date", "notes"):
            c = ws.cell(i, COL[h])
            c.fill = FILL_EDIT
            c.alignment = URDU_ALIGN if h == "verified_text" else CELL_ALIGN
            if h == "verified_text":
                c.font = URDU_FONT
        dv.add(ws.cell(i, COL["status"]))

        buf, (w, h) = crop_thumb(os.path.join(crop_root, r["crop"]), img_h, max_w)
        xl = XLImage(buf)
        xl.width, xl.height = w, h
        ws.add_image(xl, ws.cell(i, COL["crop image"]).coordinate)
        text_lines = max(len(gold), len(pred)) // 45 + 1          # wrapped lines in the text columns
        ws.row_dimensions[i].height = max(h * 0.75 + 8, 22 * text_lines)
    wb.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pred", required=True, help="UTRNet predictions TSV (crop, pred)")
    ap.add_argument("--split", default="val")
    ap.add_argument("--batches", type=int, default=4, help="number of reviewer files")
    ap.add_argument("--lines", default=os.path.join(P.PROCESSED_DIR, "lines.tsv"))
    ap.add_argument("--pages", default=os.path.join(P.PROCESSED_DIR, "all_pages.jsonl"))
    ap.add_argument("--crop-root", default=P.PROCESSED_DIR)
    ap.add_argument("--out-dir", default=os.path.join("data", "review"))
    ap.add_argument("--img-h", type=int, default=44, help="crop display height in px")
    ap.add_argument("--max-w", type=int, default=780, help="crop display width cap in px")
    ap.add_argument("--overlap", type=int, default=0, help="lines given to two reviewers (agreement check)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--only", default=None, help="TSV with a crop column: build sheets for these crops only")
    ap.add_argument("--name", default=None, help="output name prefix; default <split>_review")
    args = ap.parse_args()

    rows = [r for r in read_tsv(args.lines) if r["split"] == args.split]
    if args.only:
        only = {r["crop"] for r in read_tsv(args.only)}
        rows = [r for r in rows if r["crop"] in only]
    if not rows:
        raise SystemExit("no %s lines selected" % args.split)
    preds = {r["crop"]: r["pred"] for r in read_tsv(args.pred)}
    missing = sum(r["crop"] not in preds for r in rows)
    if missing:
        print("warning: %d of %d %s lines have no prediction in %s" % (missing, len(rows), args.split, args.pred))
    hw = handwritten_lines(args.pages)
    name = args.name or "%s_review" % args.split

    batches = assign_batches(rows, args.batches)
    overlap = set()
    if args.overlap:
        if len(batches) < 2:
            raise SystemExit("--overlap needs at least 2 batches")
        picked = random.Random(args.seed).sample(rows, min(args.overlap, len(rows)))
        overlap = {r["crop"] for r in picked}
        home = {r["crop"]: k for k, b in enumerate(batches) for r in b}
        extra = [[] for _ in batches]
        for r in picked:                                        # second copy goes to the next reviewer's file
            extra[(home[r["crop"]] + 1) % len(batches)].append(r)
        for b, e in zip(batches, extra):
            b.extend(sorted(e, key=lambda r: (r["page_id"], line_no(r["crop"]))))

    os.makedirs(args.out_dir, exist_ok=True)
    paths = [os.path.join(args.out_dir, "%s_b%d.xlsx" % (name, k)) for k in range(1, len(batches) + 1)]
    manifest_path = os.path.join(args.out_dir, name + "_manifest.json")
    for p in paths + [manifest_path]:
        if os.path.exists(p):
            raise SystemExit("%s exists; it may hold review work. Move it away first." % p)
    for path, batch in zip(paths, batches):
        write_sheet(path, batch, preds, hw, args.crop_root, args.img_h, args.max_w, overlap)
        print("wrote %s  (%d lines, %d pages, %d double-review)"
              % (path, len(batch), len({r['page_id'] for r in batch}), sum(r["crop"] in overlap for r in batch)))

    manifest = {"created_at": datetime.datetime.now().isoformat(timespec="seconds"),
                "split": args.split, "lines_tsv": args.lines, "lines_tsv_sha256": sha256(args.lines),
                "git_commit": git_commit(), "pred_file": args.pred, "pred_sha256": sha256(args.pred),
                "only": args.only, "seed": args.seed, "overlap": sorted(overlap),
                "files": {os.path.basename(p): [r["crop"] for r in b] for p, b in zip(paths, batches)}}
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("wrote %s" % manifest_path)


if __name__ == "__main__":
    main()
