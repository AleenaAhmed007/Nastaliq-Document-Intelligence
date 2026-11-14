#!/usr/bin/env python3
"""
triage.py: step 1 + 2 of the Nastaliq project.

Reads every PDF and image under --input (any folder depth) and writes:
  pages/images/<page_id>.png    one image per page (PDFs rendered at --dpi, images copied as PNG)
  pages/manifest.csv            one row per page: source, capture type, resolution, year, split, annotate flag
  pages/review_personal_data.csv  files whose names suggest student data: open them and drop any real slip/result

Rules
  - source:   FBR if the path contains "FBR", else AJK (override with --source-map folder=NAME)
  - type:     digital (PDF with a real Urdu text layer, e.g. Word export), photo (CamScanner, Adobe Scan,
              WhatsApp, screenshots, phone EXIF), scan (everything else); low_res = long side < 1600 px
  - split:    by DOCUMENT, never by page. Near-duplicate documents share a group and stay together.
              FBR -> test_unseen. AJK: newest documents -> test (~--test-pages), next newest -> val
              (~--val-pages), older -> train. Test/val are filled per capture type so each type is in test.
  - annotate: 1 for every test / val / test_unseen page plus a type-balanced sample of train pages,
              up to --annotate pages in total.

Install:  pip install pypdfium2 pypdf pillow
Run:      python triage.py --input DOCS-PDFS --out pages
"""
import argparse
import csv
import os
import random
import re
from collections import Counter, defaultdict
from datetime import datetime

import pypdfium2 as pdfium
from PIL import Image, ImageOps
from pypdf import PdfReader

IMG_EXT = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp")
PHONE_WORDS = ("camscanner", "whatsapp", "screenshot", "img_", "img-", "pxl_", "adobe scan", "intsig", "scanner")
PERSONAL_WORDS = ("rnoslip", "rollnoslip", "slip", "result", "position", "noc", "certificate", "dmc", "marks",
                  "admitcard", "admissionform", "performa")
URDU = re.compile(r"[؀-ۿ]")
YEAR_RE = re.compile(r"(?<!\d)(20[0-3]\d)(?!\d)")


def pdf_info(path):
    """(producer + creator text, creation year or None, number of Urdu characters in the text layer)."""
    try:
        r = PdfReader(path)
        meta = r.metadata or {}
        prod = " ".join(str(meta.get(k, "")) for k in ("/Producer", "/Creator"))
        cdate = str(meta.get("/CreationDate", ""))
        year = int(cdate[2:6]) if cdate.startswith("D:") and cdate[2:6].isdigit() else None
        text = "".join((p.extract_text() or "") for p in r.pages[:2])
        return prod, year, len(URDU.findall(text))
    except Exception:
        return "", None, 0


def exif_info(img):
    """(camera make/model, year) from EXIF if present."""
    try:
        ex = img.getexif()
        make = " ".join(str(ex.get(t, "")) for t in (271, 272)).strip()   # Make, Model
        dt = str(ex.get(306, "") or ex.get(36867, ""))                      # DateTime
        year = int(dt[:4]) if dt[:4].isdigit() else None
        return make, year
    except Exception:
        return "", None


def year_from_name(name):
    ys = [int(y) for y in YEAR_RE.findall(name)]
    ys = [y for y in ys if 2005 <= y <= datetime.now().year + 1]
    if ys:
        return max(ys)
    m = re.search(r"(\d{1,2})[-_.](\d{1,2})[-_.](\d{2})(?!\d)", name)      # e.g. 10-10-16
    if m and 5 <= int(m.group(3)) <= datetime.now().year % 100 + 1:
        return 2000 + int(m.group(3))
    return None


def ahash(img):
    g = ImageOps.grayscale(img).resize((16, 16))
    px = list(g.getdata())
    mean = sum(px) / len(px)
    return "".join("1" if p > mean else "0" for p in px)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", default="pages")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--test-pages", type=int, default=50)
    ap.add_argument("--val-pages", type=int, default=30)
    ap.add_argument("--annotate", type=int, default=250, help="total pages to mark for annotation")
    ap.add_argument("--max-pages", type=int, default=10, help="pages kept per PDF")
    ap.add_argument("--seed", type=int, default=13)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    img_dir = os.path.join(args.out, "images")
    os.makedirs(img_dir, exist_ok=True)
    files = []
    for root, _, fs in os.walk(args.input):
        for f in sorted(fs):
            if f.lower().endswith((".pdf",) + IMG_EXT):
                files.append(os.path.join(root, f))
    print("files found:", len(files))

    rows, review = [], []
    for k, path in enumerate(files, 1):
        rel = os.path.relpath(path, args.input)
        name = os.path.basename(path)
        low = (rel + " ").lower()
        source = "FBR" if "fbr" in low else "AJK"
        doc_id = "%s_%04d" % (source, k)
        if any(w in low.replace(" ", "") for w in PERSONAL_WORDS):
            review.append({"file": rel, "reason": "file name suggests student data; open and drop real slips/results"})
        try:
            if name.lower().endswith(".pdf"):
                prod, pyear, n_urdu = pdf_info(path)
                pdf = pdfium.PdfDocument(path)
                pages = [pdf[i].render(scale=args.dpi / 72).to_pil() for i in range(min(len(pdf), args.max_pages))]
                kind_hint = (prod + " " + name).lower()
                digital = n_urdu > 50 and not any(w in kind_hint for w in PHONE_WORDS)
                year = year_from_name(name) or pyear
            else:
                img = Image.open(path)
                make, eyear = exif_info(img)
                img = ImageOps.exif_transpose(img)
                pages = [img]
                prod, digital = make, False
                kind_hint = (make + " " + name).lower()
                if make:
                    kind_hint += " camera"
                year = year_from_name(name) or eyear
        except Exception as e:
            print("skip", rel, e)
            continue
        for i, im in enumerate(pages, 1):
            im = im.convert("RGB")
            page_id = "%s_p%02d" % (doc_id, i)
            out = os.path.join(img_dir, page_id + ".png")
            im.save(out)
            if digital:
                ctype = "digital"
            elif any(w in kind_hint for w in PHONE_WORDS + ("camera",)):
                ctype = "photo"
            else:
                ctype = "scan"
            rows.append({"page_id": page_id, "image": out, "file": rel, "page": i, "doc_id": doc_id,
                         "source": source, "type": ctype, "low_res": int(max(im.size) < 1600),
                         "width": im.width, "height": im.height, "year": year or "",
                         "producer": prod.strip()[:60], "hash": ahash(im)})
        if k % 50 == 0:
            print("  %d/%d files, %d pages" % (k, len(files), len(rows)))

    # group near-duplicate documents (same notice saved twice) so they always share a split
    first = {}
    for r in rows:
        if r["page"] == 1:
            first[r["doc_id"]] = r["hash"]
    group, reps = {}, []
    for d, h in first.items():
        for rd, rh in reps:
            if sum(a != b for a, b in zip(h, rh)) <= 12:
                group[d] = group[rd]
                break
        else:
            reps.append((d, h))
            group[d] = d
    for r in rows:
        r["group"] = group.get(r["doc_id"], r["doc_id"])

    # document-level split
    docs = defaultdict(list)
    for r in rows:
        docs[r["group"]].append(r)
    split = {}
    ajk = [g for g, rs in docs.items() if rs[0]["source"] == "AJK"]
    for g, rs in docs.items():
        if rs[0]["source"] != "AJK":
            split[g] = "test_unseen"
    by_type = defaultdict(list)
    for g in ajk:
        by_type[docs[g][0]["type"]].append(g)
    n_ajk = sum(len(docs[g]) for g in ajk) or 1
    for t, gs in by_type.items():
        rng.shuffle(gs)
        gs.sort(key=lambda g: -(docs[g][0]["year"] or 0))           # newest first, unknown years last
        share = sum(len(docs[g]) for g in gs) / n_ajk
        t_target, v_target = args.test_pages * share, args.val_pages * share
        t = v = 0
        for g in gs:
            n = len(docs[g])
            if t < t_target:
                split[g] = "test"; t += n
            elif v < v_target:
                split[g] = "val"; v += n
            else:
                split[g] = "train"
    for r in rows:
        r["split"] = split[r["group"]]

    # annotation sample: all evaluation pages + type-balanced train pages
    for r in rows:
        r["annotate"] = int(r["split"] != "train")
    left = args.annotate - sum(r["annotate"] for r in rows)
    train_by_type = defaultdict(list)
    for r in rows:
        if r["split"] == "train":
            train_by_type[r["type"]].append(r)
    while left > 0 and any(train_by_type.values()):
        for t in list(train_by_type):
            if train_by_type[t] and left > 0:
                r = train_by_type[t].pop(rng.randrange(len(train_by_type[t])))
                r["annotate"] = 1
                left -= 1

    cols = ["page_id", "image", "file", "page", "doc_id", "group", "source", "type", "low_res", "width", "height",
            "year", "split", "annotate", "producer"]
    with open(os.path.join(args.out, "manifest.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(args.out, "review_personal_data.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "reason"])
        w.writeheader()
        w.writerows(review)

    print("\npages:", len(rows), "| documents:", len(first), "| duplicate groups merged:", len(first) - len(set(group.values())))
    print("by source:", dict(Counter(r["source"] for r in rows)))
    print("by type:", dict(Counter(r["type"] for r in rows)), "| low_res:", sum(r["low_res"] for r in rows))
    print("unknown year:", sum(1 for r in rows if not r["year"]))
    tab = Counter((r["split"], r["type"]) for r in rows)
    for s in ("train", "val", "test", "test_unseen"):
        print("  %-12s" % s, {t: tab[(s, t)] for t in ("scan", "photo", "digital") if tab[(s, t)]},
              "| years", sorted({r["year"] for r in rows if r["split"] == s and r["year"]})[:1],
              "-", sorted({r["year"] for r in rows if r["split"] == s and r["year"]})[-1:])
    print("marked for annotation:", sum(r["annotate"] for r in rows))
    print("files to check for personal data:", len(review), "->", os.path.join(args.out, "review_personal_data.csv"))


if __name__ == "__main__":
    main()
