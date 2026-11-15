#!/usr/bin/env python3
"""
export_to_json.py: Label Studio JSON export -> clean per page JSON + checks

In Label Studio: Export -> JSON (not JSON-MIN). Then:
    python scripts/export_to_json.py --export data/annotations/export.json --out data/processed --doc-root . --crops

Writes
  <out>/pages/<page_id>.json   regions (pixel boxes), fields linked to regions, page flags
  <out>/all_pages.jsonl        the same, one page per line
  <out>/lines.tsv + lines/*.png   one crop per text_line box (with --crops), for OCR CER/WER
  <out>/report.txt             counts and warnings. Read the warnings.
Pages flagged contains_personal_data or skip_bad_image are NOT written.
"""
import argparse
import json
import os
from collections import Counter, defaultdict

import paths as P

FIELD_OF = {"header_department": "department", "reference_no": "reference_no",
            "date": "date", "subject": "subject"}
ABSENT_FLAG = {"date": "no_date", "reference_no": "no_reference_no", "subject": "no_subject"}
EXCLUDE_FLAGS = {"contains_personal_data", "skip_bad_image"}


def latest_annotation(task):
    anns = [a for a in task.get("annotations", []) if not a.get("was_cancelled")]
    if not anns:
        return None
    return sorted(anns, key=lambda a: a.get("updated_at") or a.get("created_at") or "")[-1]


def parse_annotation(ann):
    regions, page_flags = {}, []
    for r in ann.get("result", []):
        t, fn = r.get("type"), r.get("from_name")
        v = r.get("value", {})
        if t == "choices" and fn == "page_flags":
            page_flags += v.get("choices", [])
            continue
        rid = r.get("id")
        if rid is None:
            continue
        reg = regions.setdefault(rid, {"id": rid, "label": None, "bbox": None, "text": "", "flags": []})
        if t == "rectanglelabels":
            W, H = r["original_width"], r["original_height"]
            reg["label"] = v["rectanglelabels"][0]
            reg["bbox"] = [round(v["x"] / 100 * W, 1), round(v["y"] / 100 * H, 1),
                           round(v["width"] / 100 * W, 1), round(v["height"] / 100 * H, 1)]
            reg["_wh"] = [W, H]
        elif t == "textarea":
            reg["text"] = " ".join(x.strip() for x in v.get("text", []) if x.strip())
        elif t == "choices" and fn == "flags":
            reg["flags"] = v.get("choices", [])
    regs = [r for r in regions.values() if r["label"] and r["bbox"]]
    regs.sort(key=lambda r: (r["bbox"][1], -r["bbox"][0]))     # top to bottom, right to left
    return regs, sorted(set(page_flags))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", default=P.EXPORT_GOLD)
    ap.add_argument("--out", default=P.PROCESSED_DIR)
    ap.add_argument("--doc-root", default=".")
    ap.add_argument("--crops", action="store_true", help="save one image per text_line box")
    args = ap.parse_args()

    with open(args.export, encoding="utf-8") as f:
        tasks = json.load(f)
    os.makedirs(os.path.join(args.out, "pages"), exist_ok=True)
    if args.crops:
        os.makedirs(os.path.join(args.out, "lines"), exist_ok=True)
        from PIL import Image

    warns, excluded, unannotated = [], [], []
    written, line_rows = [], []
    label_count, flag_count = Counter(), Counter()
    field_status = defaultdict(Counter)
    per_split = Counter()

    for task in tasks:
        d = task["data"]
        pid = d["page_id"]
        ann = latest_annotation(task)
        if ann is None:
            unannotated.append(pid)
            continue
        regs, pflags = parse_annotation(ann)
        if EXCLUDE_FLAGS & set(pflags):
            excluded.append((pid, sorted(EXCLUDE_FLAGS & set(pflags))))
            continue

        W, H = (regs[0]["_wh"] if regs else (None, None))
        fields = {}
        for label, fname in FIELD_OF.items():
            hits = [r for r in regs if r["label"] == label]
            if hits:
                r = hits[0]
                fields[fname] = {"region_id": r["id"], "text": r["text"], "bbox": r["bbox"], "flags": r["flags"]}
                field_status[fname]["present"] += 1
                if not r["text"]:
                    warns.append("%s: %s box has no text" % (pid, fname))
                if len(hits) > 1:
                    warns.append("%s: %d boxes labelled %s, using the top-most one" % (pid, len(hits), label))
            else:
                fields[fname] = None
                if ABSENT_FLAG.get(fname) in pflags:
                    field_status[fname]["marked absent"] += 1
                else:
                    field_status[fname]["MISSING (not flagged)"] += 1
                    warns.append("%s: no %s box and the page is not flagged %s" % (pid, fname, ABSENT_FLAG.get(fname, "")))

        lines = [r for r in regs if r["label"] == "text_line"]
        if d.get("pass2") and not lines:
            warns.append("%s: pass 2 page has no text_line boxes" % pid)
        for r in regs:
            label_count[r["label"]] += 1
            for fl in r["flags"]:
                flag_count[(r["label"], fl)] += 1
            if r["label"] in FIELD_OF or r["label"] == "text_line":
                if r["label"] == "text_line" and not r["text"]:
                    warns.append("%s: text_line %s has no text" % (pid, r["id"]))
            x, y, w, h = r["bbox"]
            if w < 5 or h < 5:
                warns.append("%s: tiny %s box (%.0fx%.0f px)" % (pid, r["label"], w, h))
            if W and (x < -1 or y < -1 or x + w > W + 1 or y + h > H + 1):
                warns.append("%s: %s box goes outside the image" % (pid, r["label"]))

        clean = {"page_id": pid, "file": d.get("file"), "image": d.get("local_path"),
                 "width": W, "height": H, "source": d.get("source"), "type": d.get("type"),
                 "split": d.get("split"), "low_res": d.get("low_res"),
                 "page_flags": pflags, "fields": fields,
                 "regions": [{k: v for k, v in r.items() if k != "_wh"} for r in regs]}
        with open(os.path.join(args.out, "pages", pid + ".json"), "w", encoding="utf-8") as f:
            json.dump(clean, f, ensure_ascii=False, indent=1)
        written.append(clean)
        per_split[d.get("split")] += 1

        if args.crops and lines:
            img = Image.open(os.path.join(args.doc_root, d["local_path"])).convert("RGB")
            for n, r in enumerate(sorted(lines, key=lambda r: r["bbox"][1]), 1):
                if not r["text"]:
                    continue                      # never write a crop with an empty label
                x, y, w, h = r["bbox"]
                crop = img.crop((max(0, int(x)), max(0, int(y)), int(x + w), int(y + h)))
                cp = os.path.join("lines", "%s_L%02d.png" % (pid, n))
                crop.save(os.path.join(args.out, cp))
                line_rows.append((cp.replace("\\", "/"), pid, d.get("split"), d.get("type"), r["text"].replace("\t", " ")))

    with open(os.path.join(args.out, "all_pages.jsonl"), "w", encoding="utf-8") as f:
        for p in written:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    if line_rows:
        with open(os.path.join(args.out, "lines.tsv"), "w", encoding="utf-8", newline="") as f:
            f.write("crop\tpage_id\tsplit\ttype\ttext\n")
            for row in line_rows:
                f.write("\t".join(row) + "\n")

    out = ["pages written: %d | by split: %s" % (len(written), dict(per_split)),
           "not annotated yet: %d" % len(unannotated),
           "excluded (personal data / bad image): %d %s" % (len(excluded), excluded[:10]),
           "boxes by label: %s" % dict(label_count),
           "box flags: %s" % {"%s:%s" % k: v for k, v in flag_count.items()},
           "line crops: %d" % len(line_rows), "", "field status:"]
    for fname in ("department", "reference_no", "date", "subject"):
        out.append("  %-13s %s" % (fname, dict(field_status[fname])))
    out += ["", "warnings: %d" % len(warns)] + ["  " + w for w in warns[:200]]
    text = "\n".join(out)
    with open(os.path.join(args.out, "report.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
