#!/usr/bin/env python3
"""
combine_ocr.py: route each line to the OCR system that suits its script.

    python scripts/combine_ocr.py results/ocr/utrnet_large_w800_val_det.tsv results/ocr/tesseract_eng_val.tsv \
        --out results/ocr/hybrid_utrnet_w800_tesseract_eng_val.tsv

UTRNet is far better on Nastaliq Urdu; Tesseract (eng) is far better on digits and English. The rule is decided
from the PREDICTIONS only, never from the reference text:

    use the fallback (Tesseract eng) prediction if
        the primary (UTRNet) prediction contains no Urdu letter                         (rule A)
     or Tesseract's mean word confidence >= --min-conf (70) and its text has a Latin letter or digit   (rule B)
    else keep the primary prediction

FROZEN (2026-11-20) after tuning on the human-verified val lines only (1067 lines). Test and test_unseen were not
looked at. Val CER, UTRNet w800 -> rule A -> A+B: overall 15.2 -> 14.8 -> 14.5, Urdu-reference lines 14.0 -> 13.9
-> 13.9, latin_only 80.6 -> 70.1 -> 42.3, digits_only 59.9 -> 40.0 -> 40.0. Rule A alone missed English list
markers such as "(iii)", which UTRNet reads as "(تتن)". Tesseract reads them with high confidence and Urdu lines
as low-confidence gibberish. Thresholds 60-80 scored within 0.1 point of each other overall; 70 is the middle of
that plateau. Rejected on val: routing on Tesseract urd+eng's script (it reads 90 of 430 Urdu-only lines with no
Urdu letter; Urdu-only CER 10.4 -> 17.3) and capping UTRNet's Urdu-letter count (lost the long English lines).

The output adds `source` (primary / fallback) and `why` (A / B / -) columns so the routing can be audited.
"""
import argparse
import re

from eval_ocr import URDU_LETTER, read_tsv

ALNUM = re.compile(r"[A-Za-z0-9]")
MIN_CONF = 70.0


def choose(primary, fallback, fb_conf, min_conf=MIN_CONF):
    """-> (prediction, source, why)"""
    if not URDU_LETTER.search(primary or ""):
        return fallback or "", "fallback", "A"
    if fb_conf >= min_conf and ALNUM.search(fallback or ""):
        return fallback, "fallback", "B"
    return primary, "primary", "-"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("primary", help="UTRNet prediction TSV")
    ap.add_argument("fallback", help="Tesseract (eng) prediction TSV with a conf column (ocr_tesseract.py)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-conf", type=float, default=MIN_CONF, help="frozen at 70; change only for val analysis")
    args = ap.parse_args()
    prim = read_tsv(args.primary)
    fb_rows = read_tsv(args.fallback)
    if fb_rows and "conf" not in fb_rows[0]:
        raise SystemExit("%s has no conf column; rerun scripts/ocr_tesseract.py" % args.fallback)
    fb = {r["crop"]: (r.get("pred") or "", float(r["conf"])) for r in fb_rows}
    missing = [r["crop"] for r in prim if r["crop"] not in fb]
    if missing:
        raise SystemExit("%d crops of %s missing from %s, e.g. %s" % (len(missing), args.primary, args.fallback,
                                                                        missing[0]))
    cols = ["crop", "page_id", "split", "type", "pred", "source", "why"]
    n = {"A": 0, "B": 0, "-": 0}
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(cols) + "\n")
        for r in prim:
            p, src, why = choose(r.get("pred") or "", *fb[r["crop"]], min_conf=args.min_conf)
            n[why] += 1
            f.write("\t".join([r["crop"], r["page_id"], r["split"], r["type"], p.replace("\t", " "), src, why]) + "\n")
    print("%d / %d lines routed to the fallback (A no Urdu letter: %d, B confident Latin/digits: %d) -> %s"
          % (n["A"] + n["B"], len(prim), n["A"], n["B"], args.out))


if __name__ == "__main__":
    main()
