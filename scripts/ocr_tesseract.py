#!/usr/bin/env python3
"""
ocr_tesseract.py: run Tesseract 5 on the text_line crops, as a second OCR system next to UTRNet.

    python scripts/ocr_tesseract.py --split val --lang urd+eng
    python scripts/ocr_tesseract.py --split val --lang eng          # English / digits only

Input : data/processed/lines.tsv + data/processed/lines/*.png  (export_to_json.py --crops)
Output: results/ocr/tesseract_<lang>_<splits>.tsv   crop, page_id, split, type, pred   (+ a .json run summary)
        Same format as ocr_utrnet.py, so eval_ocr.py scores both side by side on the same lines.

Each crop is one text line, so Tesseract runs with --psm 7 (single text line) and the LSTM engine (--oem 1).
Tesseract is deterministic: the same crop, version and traineddata always give the same text, so --resume
is safe. Needs the tesseract executable (Windows: winget install UB-Mannheim.TesseractOCR) with urd.traineddata
and eng.traineddata in its tessdata folder; --tessdata points elsewhere (e.g. tessdata_best files).
"""
import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import time

import paths as P

DEFAULT_EXE = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def find_exe(given):
    for c in (given, shutil.which("tesseract"), DEFAULT_EXE):
        if c and os.path.exists(c):
            return c
    sys.exit("tesseract not found; install it or pass --exe")


def run(exe, path, lang, psm, tessdata):
    cmd = [exe, path, "stdout", "-l", lang, "--psm", str(psm), "--oem", "1"]
    if tessdata:
        cmd += ["--tessdata-dir", tessdata]
    r = subprocess.run(cmd, capture_output=True, env=dict(os.environ, OMP_THREAD_LIMIT="1"))   # one core per line
    if r.returncode != 0:
        raise RuntimeError("tesseract failed on %s: %s" % (path, r.stderr.decode("utf-8", "replace")[-300:]))
    return " ".join(r.stdout.decode("utf-8", "replace").split())     # one line, collapsed whitespace


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", default=os.path.join(P.PROCESSED_DIR, "lines.tsv"))
    ap.add_argument("--crop-root", default=P.PROCESSED_DIR)
    ap.add_argument("--split", nargs="+", default=["val"])
    ap.add_argument("--lang", default="urd+eng")
    ap.add_argument("--psm", type=int, default=7, help="7 = single text line")
    ap.add_argument("--exe", default=None)
    ap.add_argument("--tessdata", default=None, help="folder with *.traineddata (default: the install's)")
    ap.add_argument("--name", default=None, help="default tesseract_<lang>_<splits>")
    ap.add_argument("--out-dir", default=os.path.join("results", "ocr"))
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    exe = find_exe(args.exe)
    version = subprocess.run([exe, "--version"], capture_output=True).stdout.decode("utf-8", "replace").split("\n")[0]
    with open(args.lines, encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE) if r["split"] in args.split]
    name = args.name or "tesseract_%s_%s" % (args.lang.replace("+", "-"), "+".join(args.split))
    os.makedirs(args.out_dir, exist_ok=True)
    out_tsv = os.path.join(args.out_dir, name + ".tsv")
    done = set()
    if os.path.exists(out_tsv):
        if not args.resume:
            sys.exit("%s exists; pass --resume to continue it, or delete it to start over" % out_tsv)
        with open(out_tsv, encoding="utf-8", newline="") as f:
            done = {r["crop"] for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}
    todo = [r for r in rows if r["crop"] not in done]
    print("%s | lang %s | %d lines (%d already done) -> %s" % (version, args.lang, len(rows), len(done), out_tsv),
          flush=True)

    t0 = time.time()
    with open(out_tsv, "a", encoding="utf-8", newline="") as f:
        if not done:
            f.write("crop\tpage_id\tsplit\ttype\tpred\n")
        for i, r in enumerate(todo, 1):
            p = run(exe, os.path.join(args.crop_root, r["crop"]), args.lang, args.psm, args.tessdata)
            f.write("\t".join([r["crop"], r["page_id"], r["split"], r["type"], p.replace("\t", " ")]) + "\n")
            f.flush()
            if i % 100 == 0 or i == len(todo):
                print("  %d / %d  (%.0f s)" % (i, len(todo), time.time() - t0), flush=True)
    secs = time.time() - t0
    summary = {"engine": version, "lang": args.lang, "psm": args.psm, "oem": 1, "tessdata": args.tessdata,
               "splits": args.split, "lines": len(rows), "lines_this_run": len(todo),
               "seconds_this_run": round(secs, 1), "ms_per_line": round(1000 * secs / max(len(todo), 1), 1)}
    with open(os.path.join(args.out_dir, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1)
    print("DONE wrote %s  (%.1f s)" % (out_tsv, secs), flush=True)


if __name__ == "__main__":
    main()
