#!/usr/bin/env python3
"""
postprocess_ocr.py: fix the reading order UTRNet emits on lines that contain only digits / punctuation.

    python scripts/postprocess_ocr.py results/ocr/utrnet_large_w400_val.tsv
    # -> results/ocr/utrnet_large_w400_val_pp.tsv   (raw file is never modified)

Why: UTRNet reads a horizontally flipped crop, i.e. right to left. Inside a digit run it has learned
the logical (left-to-right) digit order, but the runs and the punctuation between them come out in
right-to-left order. On an Urdu line that is the correct logical order. On a line with no Urdu at
all (a list marker "-5", a date "10-12-2021", a page number) it is backwards: the crop "-5" is read
as "5۔". The Urdu full stop "۔" is also how it spells a hyphen there.

Rule, decided from the PREDICTION only (never from the gold), so it is a legitimate part of the OCR
system and applies the same way to unseen data:
  if the prediction has no Urdu letters and no Latin letters:
      "۔" -> "-"  and  reverse the order of the [digit run | single other character] tokens
Lines with Urdu letters are untouched. Lines with Latin letters are untouched too: reversing them
made Latin-only lines slightly worse on val, because those predictions are mostly misrecognised.
"""
import argparse
import os
import re

from eval_ocr import LATIN, URDU_LETTER, read_tsv

TOKEN = re.compile(r"[0-9۰-۹٠-٩]+|.", re.S)
MIRROR = str.maketrans("()[]{}<>", ")(][}{><")      # Unicode bidi mirroring: reversing order flips brackets


def fix_ltr_line(pred):
    if URDU_LETTER.search(pred) or LATIN.search(pred):
        return pred
    return "".join(reversed(TOKEN.findall(pred.replace("۔", "-")))).translate(MIRROR)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pred", help="prediction TSV with crop + pred columns")
    ap.add_argument("--out", default=None, help="default <pred>_pp.tsv")
    args = ap.parse_args()
    rows = read_tsv(args.pred)
    changed = 0
    for r in rows:
        new = fix_ltr_line(r.get("pred") or "")
        changed += new != (r.get("pred") or "")
        r["pred"] = new
    dest = args.out or os.path.splitext(args.pred)[0] + "_pp.tsv"
    cols = list(rows[0])
    with open(dest, "w", encoding="utf-8", newline="") as f:       # same plain format as ocr_utrnet.py
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join((r.get(c) or "").replace("\t", " ") for c in cols) + "\n")
    print("%d / %d predictions changed -> %s" % (changed, len(rows), dest))


if __name__ == "__main__":
    main()
