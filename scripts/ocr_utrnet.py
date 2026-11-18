#!/usr/bin/env python3
"""
ocr_utrnet.py: run pretrained UTRNet (HRNet + DBiLSTM + CTC) on the text_line crops.

Runs in its own environment (see README "OCR baseline: UTRNet"), not the main venv:
    .venv-utrnet\\Scripts\\python scripts/ocr_utrnet.py --split val --sample 30
    .venv-utrnet\\Scripts\\python scripts/ocr_utrnet.py --split val test test_unseen

Input : data/processed/lines.tsv + data/processed/lines/*.png  (export_to_json.py --crops)
Output: results/ocr/<name>.tsv   crop, page_id, split, type, pred   (+ a .json run summary)

Preprocessing copies UTRNet's read.py exactly: grayscale, horizontal flip (the model reads
right-to-left text as left-to-right), resize to height imgH keeping aspect ratio with the width
capped at imgW, normalise to [-1, 1], right-pad by repeating the last column.

UTRNet's model.py only needs torch + numpy. Its utils.py / dataset.py are NOT imported: they pull
in matplotlib, lmdb, pytz and torch._utils._accumulate (removed in torch 2.x), none of which
inference needs. CTC greedy decoding is reimplemented below, identical to utils.CTCLabelConverter.

UTRNet code and weights: CC BY-NC-SA 4.0, non-commercial research use only.
"""
import argparse
import csv
import json
import math
import os
import random
import sys
import time
from types import SimpleNamespace

import numpy as np
import torch
from PIL import Image

import paths as P


def load_charset(utrnet_dir):
    with open(os.path.join(utrnet_dir, "UrduGlyphs.txt"), encoding="utf-8") as f:
        chars = "".join(line.strip("\n") for line in f) + " "      # same as read.py
    return ["[CTCblank]"] + list(chars)                             # index 0 = CTC blank


def build_model(utrnet_dir, weights, n_class, device, imgH, imgW):
    sys.path.insert(0, os.path.abspath(utrnet_dir))
    from model import Model                                         # noqa: E402  (UTRNet repo)
    opt = SimpleNamespace(FeatureExtraction="HRNet", SequenceModeling="DBiLSTM", Prediction="CTC",
                          input_channel=1, output_channel=32, hidden_size=256, num_class=n_class,
                          imgH=imgH, imgW=imgW, num_fiducial=20, batch_max_length=100, device=device)
    model = Model(opt).to(device)
    model.load_state_dict(torch.load(weights, map_location=device))
    model.eval()
    return model


def preprocess(path, imgH, imgW):
    img = Image.open(path).convert("L").transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    w, h = img.size
    rw = min(imgW, math.ceil(imgH * w / float(h)))
    img = img.resize((max(1, rw), imgH), Image.Resampling.BICUBIC)
    a = (np.asarray(img, dtype=np.float32) / 255.0 - 0.5) / 0.5    # ToTensor + sub(.5).div(.5)
    out = np.empty((imgH, imgW), dtype=np.float32)
    out[:, :rw] = a
    out[:, rw:] = a[:, rw - 1:rw]                                   # border pad, as NormalizePAD
    return out


def ctc_greedy(indices, charset):
    out, prev = [], 0
    for i in indices:
        if i != 0 and i != prev:
            out.append(charset[i])
        prev = i
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", default=os.path.join(P.PROCESSED_DIR, "lines.tsv"))
    ap.add_argument("--crop-root", default=P.PROCESSED_DIR)
    ap.add_argument("--utrnet", default=os.path.join("third_party", "UTRNet"))
    ap.add_argument("--weights", default=os.path.join("third_party", "UTRNet", "saved_models",
                                                      "UTRNet-Large", "best_norm_ED.pth"))
    ap.add_argument("--split", nargs="+", default=["val"], help="splits to run (train val test test_unseen)")
    ap.add_argument("--sample", type=int, default=0, help="random N lines (stratified by capture type); 0 = all")
    ap.add_argument("--imgH", type=int, default=32)
    ap.add_argument("--imgW", type=int, default=400, help="UTRNet was trained at 400; try 800 for long lines")
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--seed", type=int, default=0, help="UTRNet averages 5 random temporal-dropout passes at eval")
    ap.add_argument("--name", default=None, help="output name; default utrnet_large_w<imgW>_<splits>")
    ap.add_argument("--out-dir", default=os.path.join("results", "ocr"))
    ap.add_argument("--resume", action="store_true", help="continue an interrupted run, skipping crops already written")
    args = ap.parse_args()

    with open(args.lines, encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE) if r["split"] in args.split]
    if args.sample and args.sample < len(rows):
        rng = random.Random(args.seed)
        by_type = {}
        for r in rows:
            by_type.setdefault(r["type"], []).append(r)
        picked = []
        for t, rs in sorted(by_type.items()):                      # proportional per capture type
            k = max(1, round(args.sample * len(rs) / len(rows)))
            picked += rng.sample(rs, min(k, len(rs)))
        rows = picked[:args.sample]
    if not rows:
        sys.exit("no lines for splits %s in %s" % (args.split, args.lines))

    name = args.name or "utrnet_large_w%d_%s%s" % (args.imgW, "+".join(args.split),
                                                   "_n%d" % args.sample if args.sample else "")
    os.makedirs(args.out_dir, exist_ok=True)
    out_tsv = os.path.join(args.out_dir, name + ".tsv")
    done = set()
    if os.path.exists(out_tsv):
        if not args.resume:
            sys.exit("%s exists; pass --resume to continue it, or delete it to start over" % out_tsv)
        with open(out_tsv, encoding="utf-8", newline="") as f:
            done = {r["crop"] for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}
    todo = [r for r in rows if r["crop"] not in done]

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    charset = load_charset(args.utrnet)
    model = build_model(args.utrnet, args.weights, len(charset), device, args.imgH, args.imgW)
    print("device %s | %d lines (%d already done) | splits %s | imgW %d -> %s"
          % (device, len(rows), len(rows) - len(todo), args.split, args.imgW, out_tsv), flush=True)

    t0 = time.time()
    with open(out_tsv, "a", encoding="utf-8", newline="") as f, torch.no_grad():
        if not done:
            f.write("crop\tpage_id\tsplit\ttype\tpred\n")
        for b in range(0, len(todo), args.batch):                 # written per batch: a killed run can --resume
            chunk = todo[b:b + args.batch]
            x = np.stack([preprocess(os.path.join(args.crop_root, r["crop"]), args.imgH, args.imgW) for r in chunk])
            logits = model(torch.from_numpy(x).unsqueeze(1).to(device))   # [b, T, n_class]
            for r, idx in zip(chunk, logits.argmax(2).cpu().numpy()):
                p = ctc_greedy(idx.tolist(), charset)
                f.write("\t".join([r["crop"], r["page_id"], r["split"], r["type"], p.replace("\t", " ")]) + "\n")
            f.flush()
            print("  %d / %d  (%.0f s)" % (min(b + args.batch, len(todo)), len(todo), time.time() - t0), flush=True)
    secs = time.time() - t0

    summary = {"model": "UTRNet-Large", "weights": args.weights, "imgH": args.imgH, "imgW": args.imgW,
               "splits": args.split, "sample": args.sample, "seed": args.seed, "lines": len(rows),
               "lines_this_run": len(todo), "device": str(device), "seconds_this_run": round(secs, 1),
               "ms_per_line": round(1000 * secs / max(len(todo), 1), 1), "batch": args.batch,
               "torch": torch.__version__,
               "note": "a resumed run only times its own lines; seed reproducibility holds within one run"}
    with open(os.path.join(args.out_dir, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1)
    print("DONE wrote %s  (%.1f s, %.0f ms/line)" % (out_tsv, secs, 1000 * secs / max(len(todo), 1)), flush=True)


if __name__ == "__main__":
    main()
