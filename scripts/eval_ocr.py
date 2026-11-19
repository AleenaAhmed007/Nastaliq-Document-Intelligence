#!/usr/bin/env python3
"""
eval_ocr.py: score line-OCR predictions against the gold text_line transcriptions.

    python scripts/eval_ocr.py results/ocr/utrnet_large_w400_val.tsv
    python scripts/eval_ocr.py results/ocr/a.tsv results/ocr/b.tsv     # side-by-side, same lines only

Prediction file: TSV with at least `crop` and `pred` columns (crop = path as written in lines.tsv).
Any OCR system (UTRNet, Tesseract, PaddleOCR, a VLM) is comparable as long as it writes that file.

Metrics (micro-averaged over characters / words unless stated):
  CER        char edit distance / reference chars, after normalisation (below)
  CER_nosp   same with all spaces removed; Urdu word spacing is inconsistent even in the gold
             ("آزادجموں" vs "آزاد جموں"), so this isolates glyph recognition from spacing
  WER        word edit distance / reference words
  NED        mean over lines of edit / max(len(ref), len(pred))   (ICDAR-style, per line)
  exact      share of lines that match exactly

Breakdowns: split, split x capture type, line category, content, aspect-ratio bucket and crosses.
  category  urdu         contains Urdu/Arabic letters, not in a handwritten field
            num_latin    no Urdu letters at all (dates, numbers, English)
            hw_field     >= 50% of the line box lies inside a date / reference_no box flagged
                         `handwritten`. This is a POSITION rule: such a line is often printed text
                         with only the number / date handwritten. It is not a verified writing style.
  content   what characters the (normalised) reference contains:
            urdu_only, urdu+digits, urdu+latin (digits allowed), digits_only (digits + punctuation),
            latin_only (Latin letters, digits allowed), other (punctuation only)
  aspect    w/h <= 12.5 fits UTRNet's 32x400 input; wider lines get squeezed
An error-type table splits each content group's errors into substitutions, deletions and
insertions (each as % of reference characters, so S + D + I = CER).

Suspect references (a heuristic, not proof the reference is wrong; left out of scoring unless
--keep-suspect, and always listed in the report so reviewers can fix them): the reference contains Japanese / Chinese / Korean characters (an annotation-model
hallucination; these documents are Urdu / English only), or has no letter or digit at all while being
5+ characters long (e.g. a row of "۔" given as the text of a full Urdu sentence). Without this, such
lines carry no Urdu letters and land in num_latin, where 10 of them caused 20% of that category's errors.
A reference corrected by a reviewer (--verified) passes the check and is scored normally.

Normalisation (--norm, default on): NFKC; Arabic yeh/kaf/heh/alef-maksura -> Urdu forms;
Urdu / Arabic-Indic digits -> ASCII; drop tatweel, zero-width chars, harakat; collapse spaces.
--no-norm only applies NFC + space collapse.
"""
import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import paths as P

URDU_LETTER = re.compile(r"[ؠ-يٮ-ۓەۺ-ۿ]")
CHAR_MAP = {"ي": "ی", "ى": "ی", "ك": "ک", "ه": "ہ"}
CHAR_MAP.update({chr(0x06F0 + i): str(i) for i in range(10)})
CHAR_MAP.update({chr(0x0660 + i): str(i) for i in range(10)})
DROP = re.compile(r"[ـ​-‏‪-‮⁦-⁩﻿ً-ْٰ]")
SPACES = re.compile(r"\s+")


def normalise(s, full=True):
    if not full:
        return SPACES.sub(" ", unicodedata.normalize("NFC", s)).strip()
    s = unicodedata.normalize("NFKC", s)
    s = "".join(CHAR_MAP.get(c, c) for c in s)
    s = DROP.sub("", s)
    return SPACES.sub(" ", s).strip()


def align(a, b):
    """Levenshtein distance between sequences a, b plus the substitution/ins/del ops."""
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        ai, row, prev = a[i - 1], d[i], d[i - 1]
        for j in range(1, m + 1):
            row[j] = min(prev[j] + 1, row[j - 1] + 1, prev[j - 1] + (ai != b[j - 1]))
    ops, i, j = [], n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            if a[i - 1] != b[j - 1]:
                ops.append((a[i - 1], b[j - 1]))
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i - 1][j] + 1:
            ops.append((a[i - 1], "∅"))
            i -= 1
        else:
            ops.append(("∅", b[j - 1]))
            j -= 1
    return d[n][m], ops


def edit(a, b):
    return align(a, b)[0]


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def handwritten_lines(pages_jsonl):
    """region ids of text_lines that sit inside a handwritten date / reference_no box."""
    hw = set()
    with open(pages_jsonl, encoding="utf-8") as f:
        for line in f:
            p = json.loads(line)
            boxes = [r["bbox"] for r in p["regions"]
                     if r["label"] in ("date", "reference_no") and "handwritten" in r["flags"]]
            if not boxes:
                continue
            for r in p["regions"]:
                if r["label"] != "text_line":
                    continue
                x, y, w, h = r["bbox"]
                for bx, by, bw, bh in boxes:
                    iw = min(x + w, bx + bw) - max(x, bx)
                    ih = min(y + h, by + bh) - max(y, by)
                    if iw > 0 and ih > 0 and iw * ih >= 0.5 * w * h:
                        hw.add((p["page_id"], r["id"]))
                        break
    return hw


DIGIT = re.compile(r"[0-9]")            # Urdu / Arabic-Indic digits are already mapped to ASCII
LATIN = re.compile(r"[A-Za-z]")


FOREIGN_SCRIPT = re.compile(r"[぀-ヿ㐀-䶿一-鿿가-힯ｦ-ﾟ]")
LETTER_OR_DIGIT = re.compile(r"[^\W_]")


def suspect_reference(ref):
    """Reason string if the (normalised) reference cannot be a transcription of this corpus, else ''."""
    if FOREIGN_SCRIPT.search(ref):
        return "CJK / kana characters"
    if len(ref) >= 5 and not LETTER_OR_DIGIT.search(ref):
        return "no letters or digits"
    return ""


def content_type(ref):
    u, d, l = bool(URDU_LETTER.search(ref)), bool(DIGIT.search(ref)), bool(LATIN.search(ref))
    if u:
        return "urdu+latin" if l else ("urdu+digits" if d else "urdu_only")
    if l:
        return "latin_only"
    return "digits_only" if d else "other"


def aspect_bucket(bbox):
    w, h = (float(v) for v in bbox.split(",")[2:4])
    r = w / max(h, 1e-6)
    return "<=12.5" if r <= 12.5 else ("12.5-25" if r <= 25 else ">25")


class Acc:
    def __init__(self):
        self.n = self.ce = self.cn = self.se = self.sn = self.we = self.wn = self.exact = 0
        self.ned = 0.0
        self.sub = self.dele = self.ins = self.hn = 0

    def add(self, ref, hyp):
        ce, ops = align(ref, hyp)
        for a, b in ops:
            if a == "∅":
                self.ins += 1
            elif b == "∅":
                self.dele += 1
            else:
                self.sub += 1
        self.hn += len(hyp)
        self.n += 1
        self.ce += ce
        self.cn += len(ref)
        self.se += edit(ref.replace(" ", ""), hyp.replace(" ", ""))
        self.sn += len(ref.replace(" ", ""))
        self.we += edit(ref.split(), hyp.split())
        self.wn += len(ref.split())
        self.ned += ce / max(len(ref), len(hyp), 1)
        self.exact += ref == hyp

    def row(self):
        pct = lambda a, b: "%.1f" % (100.0 * a / b) if b else "-"
        return [str(self.n), pct(self.ce, self.cn), pct(self.se, self.sn), pct(self.we, self.wn),
                "%.3f" % (self.ned / self.n) if self.n else "-", pct(self.exact, self.n)]


    def error_row(self):
        pct = lambda a: "%.1f" % (100.0 * a / self.cn) if self.cn else "-"
        return [str(self.n), str(self.cn), "%.1f" % (self.cn / self.n) if self.n else "-",
                "%.1f" % (self.hn / self.n) if self.n else "-",
                pct(self.ce), pct(self.sub), pct(self.dele), pct(self.ins)]


HEAD = ["lines", "CER %", "CER_nosp %", "WER %", "NED", "exact %"]
ERR_HEAD = ["lines", "ref chars", "avg ref len", "avg pred len", "CER %", "S %", "D %", "I %"]
BREAKDOWNS = ("split", "split x type", "category", "content", "aspect", "category x aspect", "category x type")


def error_table(title, groups, systems):
    out = ["### " + title, "", "S / D / I = substitutions / deletions / insertions as % of reference characters "
           "(they add up to CER).", ""]
    multi = len(systems) > 1
    cols = (["group", "system"] if multi else ["group"]) + ERR_HEAD
    out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for g in sorted(groups):
        for s in systems:
            if s in groups[g]:
                out.append("| " + " | ".join(([g, s] if multi else [g]) + groups[g][s].error_row()) + " |")
    return out + [""]


def table(title, groups, systems):
    out = ["### " + title, ""]
    multi = len(systems) > 1
    cols = (["group", "system"] if multi else ["group"]) + HEAD
    out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for g in sorted(groups):
        for s in systems:
            if g in groups and s in groups[g]:
                out.append("| " + " | ".join(([g, s] if multi else [g]) + groups[g][s].row()) + " |")
    return out + [""]


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # Windows consoles default to cp1252
    except AttributeError:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("pred", nargs="+", help="prediction TSV(s) with crop + pred columns")
    ap.add_argument("--lines", default=os.path.join(P.PROCESSED_DIR, "lines.tsv"))
    ap.add_argument("--pages", default=os.path.join(P.PROCESSED_DIR, "all_pages.jsonl"))
    ap.add_argument("--verified", default=None,
                    help="data/annotations/verified_lines.tsv from merge_review.py: score only human-verified "
                         "lines against their verified text (exclude / illegible lines are dropped)")
    ap.add_argument("--keep-suspect", action="store_true",
                    help="score suspect references too (see docstring) instead of listing them separately")
    ap.add_argument("--no-norm", action="store_true")
    ap.add_argument("--out", default=None, help="markdown report; default <first pred>.report.md")
    ap.add_argument("--worst", type=int, default=15, help="list the N worst lines per system")
    args = ap.parse_args()

    gold = {r["crop"]: r for r in read_tsv(args.lines)}
    all_lines = dict(gold)
    reference = "original gold (data/processed/lines.tsv, NOT human-verified)"
    ver = {}
    if args.verified:
        ver = {r["crop"]: r for r in read_tsv(args.verified)}
        usable = {c: r for c, r in ver.items() if r["status"] in ("gold_ok", "utrnet_ok", "corrected")}
        for c, r in usable.items():
            gold[c] = dict(gold[c], text=r["verified_text"])
        gold = {c: g for c, g in gold.items() if c in usable}
        reference = "human-verified text (%s): %d usable lines, %d excluded/illegible" % (
            args.verified, len(usable), len(ver) - len(usable))
    hw = handwritten_lines(args.pages)
    preds = {}
    for path in args.pred:
        name = os.path.splitext(os.path.basename(path))[0]
        preds[name] = {r["crop"]: r.get("pred") or "" for r in read_tsv(path)}
    pred_splits = sorted({all_lines[c]["split"] for p in preds.values() for c in p if c in all_lines})
    if args.verified:
        # Evaluation A: how wrong was the original annotation? (scored like an OCR system)
        preds["original_gold"] = {c: all_lines[c]["text"] for c in all_lines}
    common = set(gold)
    for p in preds.values():
        common &= set(p)
    if not common:
        raise SystemExit("no crops in common between the prediction files and %s" % args.lines)
    systems = list(preds)

    by = {k: defaultdict(lambda: defaultdict(Acc)) for k in BREAKDOWNS}
    overall = defaultdict(Acc)
    confusions = {s: Counter() for s in systems}
    confusions_nl = {s: Counter() for s in systems}       # on digit / Latin characters, any line
    per_line = {s: [] for s in systems}
    empty_ref, suspect = [], []
    for crop in sorted(common):
        g = gold[crop]
        ref = normalise(g["text"], not args.no_norm)
        if not ref:                       # nothing left to score against (e.g. only tatweel / diacritics)
            empty_ref.append(crop)
            continue
        why = suspect_reference(ref)
        if why and not args.keep_suspect:
            suspect.append((crop, why, ref))
            continue
        if (g["page_id"], g["region_id"]) in hw:
            cat = "hw_field"
        elif URDU_LETTER.search(ref):
            cat = "urdu"
        else:
            cat = "num_latin"
        asp = aspect_bucket(g["bbox"])
        keys = {"split": g["split"], "split x type": "%s / %s" % (g["split"], g["type"]),
                "category": "%s / %s" % (g["split"], cat), "aspect": "%s / %s" % (g["split"], asp),
                "content": "%s / %s" % (g["split"], content_type(ref)),
                "category x aspect": "%s / %s / %s" % (g["split"], cat, asp),
                "category x type": "%s / %s / %s" % (g["split"], cat, g["type"])}
        for s in systems:
            hyp = normalise(preds[s][crop], not args.no_norm)
            overall[s].add(ref, hyp)
            for k, v in keys.items():
                by[k][v][s].add(ref, hyp)
            ed, ops = align(ref, hyp)
            if cat == "urdu":
                confusions[s].update(ops)
            confusions_nl[s].update(o for o in ops
                                    if DIGIT.match(o[0]) or LATIN.match(o[0]) or (o[0] == "∅" and content_type(ref) in ("digits_only", "latin_only")))
            per_line[s].append((ed / max(len(ref), 1), crop, ref, hyp))

    out = ["# OCR evaluation", "",
           "Systems: %s  " % ", ".join(systems),
           "Reference: %s  " % reference,
           "Lines scored: %d (crops present in every prediction file, minus %d with an empty reference"
           "%s)  " % (len(common) - len(empty_ref) - len(suspect), len(empty_ref),
                      ", minus %d with a suspect reference (listed at the end)" % len(suspect) if suspect else ""),
           "Line accounting: %d lines in every prediction file = %d scored + %d empty reference + %d suspect "
           "reference (excluded by heuristic, awaiting human correction)  "
           % (len(common), len(common) - len(empty_ref) - len(suspect), len(empty_ref), len(suspect)),
           "CER / WER = total edits (S+D+I) / total reference characters / words over all lines (micro); "
           "NED = mean of per-line edit / max(len(ref), len(pred)); can exceed 100% when the OCR inserts text  ",
           "Normalisation: %s" % ("NFC + spaces only" if args.no_norm else "full (see eval_ocr.py docstring)"), ""]
    if args.verified:
        st_cols = ["gold_ok", "utrnet_ok", "corrected", "exclude", "illegible", "conflict"]
        out += ["### Review coverage (every line of the split is accounted for)", "",
                "| split | lines | " + " | ".join(st_cols) + " | unreviewed | scored here |",
                "|" + "---|" * (len(st_cols) + 4)]
        for sp in pred_splits:
            crops = [c for c, g in all_lines.items() if g["split"] == sp]
            st = Counter(ver[c]["status"] for c in crops if c in ver)
            out.append("| %s | %d | %s | %d | %d |" % (
                sp, len(crops), " | ".join(str(st[s]) for s in st_cols),
                sum(c not in ver for c in crops), sum(c in common for c in crops)))
        out += ["", "`original_gold` row = the original annotation scored against the verified text "
                "(annotation error rate, Evaluation A). Other rows = OCR error rate (Evaluation B).", ""]
    out += table("Overall", {"all": overall}, systems)
    if empty_ref:
        out += ["Skipped %d line(s) whose reference is empty after normalisation: %s" % (
            len(empty_ref), ", ".join(empty_ref[:10])), ""]
    for k in BREAKDOWNS:
        out += table("By " + k, by[k], systems)
    out += error_table("Error types by content", by["content"], systems)
    for s in systems:
        out += ["### Top character confusions on Urdu lines: %s" % s, "",
                "ref → pred (∅ = missing / extra)", "", "| ref | pred | count |", "|---|---|---|"]
        out += ["| %s | %s | %d |" % (a, b, n) for (a, b), n in confusions[s].most_common(20)] + [""]
        out += ["### Top confusions on digit / Latin characters: %s" % s, "",
                "reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines", "",
                "| ref | pred | count |", "|---|---|---|"]
        out += ["| %s | %s | %d |" % (a, b, n) for (a, b), n in confusions_nl[s].most_common(20)] + [""]
        out += ["### Worst %d lines: %s" % (args.worst, s), "", "| CER | crop | gold | pred |", "|---|---|---|---|"]
        for c, crop, ref, hyp in sorted(per_line[s], reverse=True)[:args.worst]:
            out.append("| %.2f | %s | %s | %s |" % (c, crop, ref.replace("|", "/"), hyp.replace("|", "/")))
        out.append("")
    if suspect:
        out += ["### Suspect references (not scored; awaiting human correction)", "",
                "Flagged by a heuristic (see eval_ocr.py docstring), not proof that each reference is wrong. "
                "Each line is scored again once a reviewer confirms or corrects it (--verified), "
                "or always with --keep-suspect.", "",
                "| crop | reason | reference |", "|---|---|---|"]
        out += ["| %s | %s | %s |" % (c, why, ref.replace("|", "/")) for c, why, ref in suspect] + [""]
    text = "\n".join(out)
    dest = args.out or os.path.splitext(args.pred[0])[0] + ".report.md"
    with open(dest, "w", encoding="utf-8") as f:
        f.write(text)
    print(text.split("### By split x type")[0])
    print("full report: %s" % dest)


if __name__ == "__main__":
    main()
