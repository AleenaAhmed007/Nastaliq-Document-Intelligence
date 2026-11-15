#!/usr/bin/env python3
"""
auto_annotate_remaining.py
==========================
Heuristic layout annotation for the 550 un-annotated pages.

For every page NOT already in export.json we:
  1. Load the image, run a simple horizontal-projection split to find the
     header / body / footer bands.
  2. Look up the page in ajkbise_manifest.csv for a date and title.
  3. Build a Label-Studio-compatible annotation dict and append it to
     export_full.json  (the existing 239 gold entries stay at the top).
  4. Write a coloured preview PNG into data/previews/

Flags written to every auto-annotation so you can filter them later:
   page_flags: ["auto_heuristic"]

Run from the repo root:
    python scripts/auto_annotate_remaining.py

Output
------
  data/annotations/export_full.json            – 789-entry Label Studio file (gold 239 + auto 550)
  data/previews/                               – new *_annotated.png files (auto ones are lighter)
  data/annotations/auto/remaining_annotations.json – same 550 entries in outcomes.json format
  data/processed/all_pages_full.jsonl          – 789-line JSONL for modelling
"""

import csv, json, os, re, sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

import paths as P

# ── paths ─────────────────────────────────────────────────────────────────────
ROOT         = P.ROOT
EXPORT_JSON  = P.abspath(P.EXPORT_GOLD)
MANIFEST_CSV = P.abspath(P.PAGE_MANIFEST)
AJK_CSV      = P.abspath(P.AJK_MANIFEST)
REMAINING    = P.abspath(P.REMAINING_PAGES)
IMG_DIR      = P.abspath(P.PAGE_IMAGES)
PREV_DIR     = P.abspath(P.PREVIEWS_DIR)
OUT_EXPORT   = P.abspath(P.EXPORT_FULL)
OUT_REM      = P.abspath(P.REMAINING_ANNS)
OUT_JSONL    = P.abspath(P.ALL_PAGES_FULL)

os.makedirs(PREV_DIR, exist_ok=True)

# ── colour palette (matches draw_annotations.py) ──────────────────────────────
COLORS = {
    "header_department": (0,   120, 215),
    "reference_no":      (220, 50,  50),
    "date":              (50,  180, 50),
    "subject":           (200, 120, 0),
    "body":              (128, 128, 128),
    "table":             (160, 32,  240),
    "stamp_signature":   (0,   180, 180),
    "distribution_list": (180, 100, 160),
    "text_line":         (100, 100, 200),
}
SHORT = {k: k[:5].upper() for k in COLORS}
SHORT.update({
    "header_department": "DEPT", "reference_no": "REF#", "date": "DATE",
    "subject": "SUBJ", "body": "BODY", "table": "TABLE",
    "stamp_signature": "STAMP", "distribution_list": "DIST", "text_line": "LINE"
})

DEPT_TEXT = "آزاد جموں وکشمیر انٹر میڈیٹ و ثانوی تعلیمی بورڈ میرپور"
FBR_DEPT  = "حکومت پاکستان، وزارت مالیات، اقتصادی امور اور ریونیو (ریونیو ڈویژن)"

# ── load helpers ──────────────────────────────────────────────────────────────
def get_font(size):
    for name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except:
            pass
    try:
        return ImageFont.load_default(size=size)
    except:
        return ImageFont.load_default()

def load_ajk_meta():
    """filename -> {date, title}"""
    m = {}
    if not os.path.exists(AJK_CSV):
        return m
    with open(AJK_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            m[r["file_name"]] = {"date": r.get("date", ""), "title": r.get("title", "")}
    return m

def basename(path):
    return os.path.basename(path.replace("\\", "/"))

def projection_split(arr_gray, axis=0):
    """Return ink density profile along axis (0=row, 1=col)."""
    ink = (arr_gray < 180).astype(np.float32)
    return ink.mean(axis=axis if axis == 1 else 1)

def find_band(profile, frac_start, frac_end):
    """Return (y0, y1) pixel range for fractional slice of profile."""
    n = len(profile)
    return int(n * frac_start), int(n * frac_end)

# ── heuristic layout ──────────────────────────────────────────────────────────
def auto_layout(img, source, meta_date, meta_title):
    """
    Returns list of region dicts:  {label, bbox:[x,y,w,h], text, flags}
    bbox is in absolute pixels (x,y,w,h), top-left origin.
    """
    W, H = img.size
    arr  = np.array(img.convert("L"))

    # ── row ink density profile (compressed to H points)
    row_prof = (arr < 180).sum(axis=1) / max(W, 1)   # fraction of dark pixels per row

    # smooth with a 20-px box
    kernel = max(1, H // 60)
    smooth = np.convolve(row_prof, np.ones(kernel)/kernel, mode="same")

    # ── find the top dense band = header
    # Header: typically rows 0..12% of page have heavy ink
    h12 = int(H * 0.12)
    header_rows = np.where(smooth[:h12] > 0.02)[0]
    if len(header_rows):
        hy0 = max(0,    int(header_rows.min()) - 2)
        hy1 = min(h12,  int(header_rows.max()) + 2)
    else:
        hy0, hy1 = 0, int(H * 0.08)

    # ── body: rows between 12% and 65%
    body_start = hy1
    body_end   = int(H * 0.65)

    # ── stamp/signature + reference zone: 65%-85%
    stamp_start = body_end
    stamp_end   = int(H * 0.85)

    # ── distribution list: 85%-100%
    dist_start  = stamp_end

    # ── left/right margins: 5% padding from edges
    mx0 = int(W * 0.05)
    mx1 = int(W * 0.95)

    regions = []

    # header_department
    hbbox = [mx0, hy0, mx1 - mx0, hy1 - hy0]
    dept_text = FBR_DEPT if source == "FBR" else DEPT_TEXT
    regions.append({"label": "header_department", "bbox": hbbox,
                    "text": dept_text, "flags": []})

    # subject (small top-right box, ~8-12% of page height)
    sub_x = int(W * 0.70)
    sub_y = int(H * 0.08)
    sub_w = int(W * 0.25)
    sub_h = int(H * 0.04)
    subj_text = meta_title if meta_title else ("پریس ریلیز" if source == "AJK" else "نوٹیفکیشن")
    regions.append({"label": "subject",
                    "bbox": [sub_x, sub_y, sub_w, sub_h],
                    "text": subj_text, "flags": ["implicit_subject", "auto_heuristic"]})

    # body
    if body_end > body_start + 20:
        regions.append({"label": "body",
                        "bbox": [mx0, body_start, mx1 - mx0, body_end - body_start],
                        "text": "", "flags": []})

    # stamp / signature
    if stamp_end > stamp_start + 10:
        regions.append({"label": "stamp_signature",
                        "bbox": [mx0, stamp_start, int(W * 0.45), stamp_end - stamp_start],
                        "text": "", "flags": []})

    # distribution list
    if H - dist_start > 20:
        regions.append({"label": "distribution_list",
                        "bbox": [mx0, dist_start, mx1 - mx0, H - dist_start],
                        "text": "", "flags": []})

    # date  (approximate: lower-right of stamp zone)
    if meta_date:
        date_x = int(W * 0.55)
        date_y = int(H * 0.72)
        date_w = int(W * 0.35)
        date_h = int(H * 0.03)
        regions.append({"label": "date",
                        "bbox": [date_x, date_y, date_w, date_h],
                        "text": meta_date, "flags": ["auto_heuristic"]})

    return regions


# ── draw preview ──────────────────────────────────────────────────────────────
def draw_preview(img, regions, out_path, is_gold=False):
    vis   = img.convert("RGB").copy()
    draw  = ImageDraw.Draw(vis)
    W, H  = vis.size
    lfont = get_font(max(18, int(H * 0.011)))
    tfont = get_font(max(14, int(H * 0.008)))

    for reg in regions:
        label = reg["label"]
        x, y, w, h = reg["bbox"]
        color = COLORS.get(label, (200, 200, 200))
        lw    = 3 if is_gold else 2
        draw.rectangle([x, y, x + w, y + h], outline=color, width=lw)
        short = SHORT.get(label, label.upper())
        # tag above box
        try:
            bb = lfont.getbbox(short)
            tw, th = bb[2]-bb[0]+8, bb[3]-bb[1]+6
        except:
            tw, th = 60, 24
        ty = max(0, y - th - 2)
        draw.rectangle([x, ty, x + tw, ty + th], fill=color)
        draw.text((x + 4, ty + 2), short, fill="white", font=lfont)

        txt = reg.get("text", "")
        if txt and label not in ("body", "table", "stamp_signature", "distribution_list"):
            clip = txt[:60]
            draw.text((x + 4, y + 4), clip, fill=color, font=tfont)

    if is_gold:
        draw.text((4, 4), "GOLD", fill=(0, 180, 0), font=lfont)
    else:
        draw.text((4, 4), "AUTO", fill=(180, 80, 0), font=lfont)

    vis.save(out_path, "PNG")


# ── build Label Studio result list from region list ───────────────────────────
def regions_to_ls_result(regions, W, H, task_id):
    result = []
    for i, reg in enumerate(regions, 1):
        rid = "auto_%s_%02d" % (task_id, i)
        x, y, w, h = reg["bbox"]
        # rectanglelabel
        result.append({
            "id": rid, "type": "rectanglelabels",
            "from_name": "layout", "to_name": "image",
            "original_width": W, "original_height": H, "image_rotation": 0,
            "value": {"x": round(x/W*100,2), "y": round(y/H*100,2),
                      "width": round(w/W*100,2), "height": round(h/H*100,2),
                      "rotation": 0, "rectanglelabels": [reg["label"]]}
        })
        # text
        txt = reg.get("text", "")
        if txt:
            result.append({
                "id": rid, "type": "textarea",
                "from_name": "value", "to_name": "image",
                "original_width": W, "original_height": H,
                "value": {"text": [txt]}
            })
        # flags
        flags = [f for f in reg.get("flags", [])
                 if f in ("implicit_subject", "handwritten", "no_date",
                          "no_reference_no", "no_subject", "auto_heuristic")]
        if flags:
            result.append({
                "id": rid, "type": "choices",
                "from_name": "flags", "to_name": "image",
                "value": {"choices": flags}
            })
    # page flag
    result.append({
        "type": "choices", "from_name": "page_flags", "to_name": "image",
        "value": {"choices": ["auto_heuristic"]}
    })
    return result

# ── outcomes.json format ──────────────────────────────────────────────────────
FIELD_LABEL = {"header_department": "department", "date": "date",
               "subject": "subject", "reference_no": "reference_no"}

def regions_to_outcome(page_id, img_path, W, H, source, ptype, split, regions):
    fields = {}
    for reg in regions:
        fname = FIELD_LABEL.get(reg["label"])
        if fname and fname not in fields:
            fields[fname] = {
                "region_id": "auto", "text": reg.get("text",""),
                "bbox": reg["bbox"], "flags": reg.get("flags", [])
            }
    for fname in ("department","reference_no","date","subject"):
        if fname not in fields:
            fields[fname] = None
    return {
        "page_id": page_id, "file": img_path, "image": img_path,
        "width": W, "height": H, "source": source, "type": ptype, "split": split,
        "low_res": int(max(W, H) < 1600),
        "page_flags": ["auto_heuristic", "no_reference_no"],
        "fields": fields,
        "regions": [{"label": r["label"], "bbox": r["bbox"],
                     "text": r.get("text",""), "flags": r.get("flags",[])}
                    for r in regions]
    }

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    print("Loading existing gold annotations …")
    with open(EXPORT_JSON, encoding="utf-8") as f:
        gold_tasks = json.load(f)
    gold_ids = {t["data"]["page_id"] for t in gold_tasks}
    print("  gold tasks:", len(gold_tasks))

    with open(REMAINING, encoding="utf-8") as f:
        remaining = json.load(f)
    print("  pages to auto-annotate:", len(remaining))

    ajk_meta = load_ajk_meta()
    print("  AJK metadata entries:", len(ajk_meta))

    # load existing outcomes jsonl
    existing_outcomes = []
    if os.path.exists(OUT_JSONL):
        with open(OUT_JSONL, encoding="utf-8") as f:
            existing_outcomes = [json.loads(l) for l in f if l.strip()]
    exist_ids = {o["page_id"] for o in existing_outcomes}

    new_tasks    = []
    new_outcomes = []
    errors       = []
    max_id       = max((t.get("id", 0) for t in gold_tasks), default=0)

    total = len(remaining)
    for idx, row in enumerate(remaining, 1):
        pid       = row["page_id"]
        img_path  = row["image_path"]   # e.g. data/interim/images/AJK_0004_p01.png
        file_rel  = row["file"]
        source    = "FBR" if pid.startswith("FBR") else "AJK"
        ptype     = row["type"]
        split     = row["split"]
        full_path = os.path.join(ROOT, img_path.lstrip("/\\"))

        if not os.path.exists(full_path):
            errors.append(pid + ": image not found")
            continue

        try:
            img = Image.open(full_path).convert("RGB")
            W, H = img.size
        except Exception as e:
            errors.append(pid + ": " + str(e))
            continue

        # AJK metadata
        base_fn  = basename(file_rel)
        meta     = ajk_meta.get(base_fn, {})
        meta_date  = meta.get("date", "")
        meta_title = meta.get("title", "")

        regions = auto_layout(img, source, meta_date, meta_title)

        # ── preview image
        prev_path = os.path.join(PREV_DIR, pid + "_annotated.png")
        if not os.path.exists(prev_path):
            draw_preview(img, regions, prev_path, is_gold=False)

        # ── Label Studio task
        max_id += 1
        ls_result = regions_to_ls_result(regions, W, H, pid)
        task = {
            "id": max_id,
            "data": {
                "image": "/data/local-files/?d=" + img_path.replace("\\","/"),
                "local_path": img_path.replace("\\","/"),
                "page_id": pid,
                "file": file_rel,
                "source": source,
                "type": ptype,
                "split": split,
                "low_res": int(max(W, H) < 1600),
                "pass2": 0,
            },
            "annotations": [{
                "id": max_id,
                "created_at": "2026-11-15T15:00:00.000000Z",
                "updated_at": "2026-11-15T15:00:00.000000Z",
                "result": ls_result,
            }]
        }
        new_tasks.append(task)

        # ── outcome
        if pid not in exist_ids:
            new_outcomes.append(
                regions_to_outcome(pid, img_path, W, H, source, ptype, split, regions)
            )

        if idx % 50 == 0 or idx == total:
            print(f"  {idx}/{total} done …")

    # ── save export_full.json (gold first, then auto)
    all_tasks = gold_tasks + new_tasks
    with open(OUT_EXPORT, "w", encoding="utf-8") as f:
        json.dump(all_tasks, f, ensure_ascii=False, indent=1)
    print(f"\nexport_full.json  → {len(all_tasks)} tasks  ({OUT_EXPORT})")

    # ── save remaining_annotations.json
    with open(OUT_REM, "w", encoding="utf-8") as f:
        json.dump(new_outcomes, f, ensure_ascii=False, indent=1)
    print(f"remaining_annotations.json  → {len(new_outcomes)} entries")

    # ── save all_pages_full.jsonl
    all_outcomes = existing_outcomes + new_outcomes
    all_ids_seen = set()
    deduped = []
    for o in all_outcomes:
        if o["page_id"] not in all_ids_seen:
            deduped.append(o)
            all_ids_seen.add(o["page_id"])
    with open(OUT_JSONL, "w", encoding="utf-8") as f:
        for o in deduped:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    print(f"all_pages_full.jsonl        → {len(deduped)} pages")

    if errors:
        print(f"\nWarnings ({len(errors)}):")
        for e in errors[:20]:
            print(" ", e)

    print("\nDone! ✅")
    print(f"  gold previews  : data/previews/ (239 existing)")
    print(f"  auto previews  : data/previews/ ({len(new_tasks)} new, labelled AUTO)")
    print(f"  total previews : {239 + len(new_tasks)}")

if __name__ == "__main__":
    main()
