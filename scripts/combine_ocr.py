#!/usr/bin/env python3
"""
combine_ocr.py: route each line to the OCR system that suits its script.

    python scripts/combine_ocr.py results/ocr/utrnet_large_w400_val_det.tsv results/ocr/tesseract_eng_val.tsv \
        --out results/ocr/hybrid_utrnet_w400_tesseract_eng_val.tsv

UTRNet is far better on Nastaliq Urdu, and Tesseract (eng) is far better on digits and English (val, original
gold: Urdu lines 21.6% vs 91.8% CER, numbers/English lines 77.8% vs 26.7%). Rule, decided from the
PREDICTIONS only, never from the gold:

    if the primary (UTRNet) prediction contains no Urdu letter -> use the fallback (Tesseract) prediction
    else                                                        -> keep the primary prediction

On val this routes 301 of 1437 lines and leaves every Urdu-category line's score unchanged. A broader rule
(also route when UTRNet has <= 3 Urdu letters and Tesseract read Latin or digits) scored better on
numbers/English (34.6% vs 47.7%) but slightly changed Urdu lines. It was designed after seeing val results,
so it is not used until it holds on verified text.

The output adds a `source` column (primary / fallback) so the routing can be audited line by line.
"""
import argparse
import os

from eval_ocr import URDU_LETTER, read_tsv


def choose(primary, fallback):
    """-> (prediction, source)"""
    if not URDU_LETTER.search(primary or ""):
        return fallback or "", "fallback"
    return primary, "primary"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("primary", help="UTRNet prediction TSV")
    ap.add_argument("fallback", help="Tesseract (eng) prediction TSV")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    prim = read_tsv(args.primary)
    fb = {r["crop"]: r.get("pred") or "" for r in read_tsv(args.fallback)}
    missing = [r["crop"] for r in prim if r["crop"] not in fb]
    if missing:
        raise SystemExit("%d crops of %s missing from %s, e.g. %s" % (len(missing), args.primary, args.fallback,
                                                                        missing[0]))
    cols = ["crop", "page_id", "split", "type", "pred", "source"]
    n = 0
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(cols) + "\n")
        for r in prim:
            p, src = choose(r.get("pred") or "", fb[r["crop"]])
            n += src == "fallback"
            f.write("\t".join([r["crop"], r["page_id"], r["split"], r["type"], p.replace("\t", " "), src]) + "\n")
    print("%d / %d lines routed to the fallback -> %s" % (n, len(prim), args.out))


if __name__ == "__main__":
    main()
