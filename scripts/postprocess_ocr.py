#!/usr/bin/env python3
"""
postprocess_ocr.py: put dates / reference numbers that UTRNet reads backwards into logical order.

    python scripts/postprocess_ocr.py results/ocr/utrnet_large_w400_val.tsv --out results/ocr/utrnet_large_w400_val_pp.tsv

The raw prediction file is never modified.

Why: UTRNet reads a horizontally flipped crop, i.e. right to left. Inside one digit run it has learned
the left-to-right digit order (1830 stays 1830), but a date printed as 10-12-2021 comes out as
2021-12-10: it reads the digit groups right to left. Under the Unicode bidi algorithm, digit groups
joined by - / . : , form ONE left-to-right run, so the logical text is 10-12-2021. Both the original
gold and the review rules (make_review_sheet.py) agree on that order.

Marks before or after a number are NOT moved. The review rules say a list marker printed as "-5"
(5 on the right) is typed "5-", in right-to-left reading order, which is what UTRNet already emits.
An earlier version of this script (commit b93a362) moved such marks to the front. That matched the
old gold's convention, which the review treats as wrong, so most of its apparent gain would have
turned into a loss against verified text.

Rule, decided from the PREDICTION only (never from the gold):
  if the prediction has no Urdu letters and no Latin letters:
      every group of digit runs joined by single separators (- / . : , ۔) has its parts reversed,
      and a ۔ between two digit runs becomes "-" (an Urdu full stop never sits inside a number)
Lines with Urdu or Latin letters are untouched: on val there was no evidence the rule helps there,
because UTRNet never got a full date inside an Urdu line right in either order.
"""
import argparse
import os
import re

from eval_ocr import LATIN, URDU_LETTER, read_tsv

NUMBER_GROUP = re.compile(r"[0-9۰-۹٠-٩]+(?:[-/.:,۔][0-9۰-۹٠-٩]+)+")
PART = re.compile(r"[0-9۰-۹٠-٩]+|.")


def fix_ltr_line(pred):
    if URDU_LETTER.search(pred) or LATIN.search(pred):
        return pred
    return NUMBER_GROUP.sub(lambda m: "".join(reversed(PART.findall(m.group().replace("۔", "-")))), pred)


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
