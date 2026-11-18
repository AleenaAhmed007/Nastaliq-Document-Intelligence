#!/usr/bin/env python3
"""
merge_review.py: collect filled review sheets into one verified transcription file.

    python scripts/merge_review.py                       # all data/review/*.xlsx
    python scripts/merge_review.py data/review/val_review_b1.xlsx

Writes (default data/annotations/):
  verified_lines.tsv      one row per reviewed line: status, verified_text, original_text, changed,
                          reviewed_by, n_reviews, agreement, notes, sheets, sheet_modified, merged_at,
                          lines_sha256 (dataset version of lines.tsv the review refers to)
  review_conflicts.tsv    double-reviewed lines where reviewers disagree (need adjudication)
  review_agreement.json   inter-reviewer agreement on the double-reviewed lines

Only crop_id + the reviewer columns (status, verified_text, reviewer, notes) are read from the sheets.
original_text always comes from data/processed/lines.tsv, so edits to the sheet's original columns
cannot leak in. Rows without a status are pending and not written.

  gold_ok    -> verified_text = original gold
  utrnet_ok  -> verified_text = the utrnet_pred shown in the sheet
  corrected  -> verified_text = what the reviewer typed (required)
  exclude / illegible -> kept with empty verified_text; eval_ocr.py --verified leaves them out

Double-reviewed lines: reviewers agree when both keep the line with the same text (after the
eval_ocr.py normalisation) or both drop it (exclude / illegible). Disagreements get status
`conflict` and are left out of evaluation until adjudicated. Adjudication: build a sheet with
    python scripts/make_review_sheet.py --pred <pred.tsv> --only data/annotations/review_conflicts.tsv --name val_adjudication --batches 1
and fill it; any sheet whose file name contains "adjudication" overrides the other reviews.
"""
import argparse
import datetime
import glob
import json
import os
import sys
from collections import Counter, defaultdict

from openpyxl import load_workbook

import paths as P
from eval_ocr import edit, normalise, read_tsv
from make_review_sheet import STATUSES, sha256

USABLE = ("gold_ok", "utrnet_ok", "corrected")
OUT_COLS = ["crop", "page_id", "split", "status", "verified_text", "original_text", "changed", "reviewed_by",
            "review_date", "n_reviews", "agreement", "notes", "sheets", "sheet_modified", "merged_at", "lines_sha256"]


def cell(v):
    return "" if v is None else str(v).strip().replace("\t", " ").replace("\r", " ").replace("\n", " ")


def read_sheet(path, gold, warns):
    """-> (list of review dicts, rows in sheet)"""
    sheet = os.path.basename(path)
    modified = datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat(timespec="seconds")
    ws = load_workbook(path, read_only=True)["review"]
    it = ws.iter_rows(values_only=True)
    head = [cell(h) for h in next(it)]
    ix = {h: head.index(h) for h in ("crop_id", "utrnet_pred", "status", "verified_text", "reviewer", "notes")}
    ix_date = head.index("review_date") if "review_date" in head else None
    reviews, total = [], 0
    for row in it:
        cid = cell(row[ix["crop_id"]])
        if not cid:
            continue
        total += 1
        if cid not in gold:
            warns.append("%s: unknown crop_id %s" % (sheet, cid))
            continue
        status = cell(row[ix["status"]]).lower()
        typed = cell(row[ix["verified_text"]])
        if not status and not typed:
            continue                                             # pending
        if not status:
            status = "corrected"
            warns.append("%s: %s has verified_text but no status, treated as corrected" % (sheet, cid))
        if status not in STATUSES:
            warns.append("%s: %s has unknown status '%s', skipped" % (sheet, cid, status))
            continue
        if status == "gold_ok":
            text = gold[cid]["text"]
        elif status == "utrnet_ok":
            text = cell(row[ix["utrnet_pred"]])
        elif status == "corrected":
            text = typed
            if not text:
                warns.append("%s: %s is 'corrected' but verified_text is empty, skipped" % (sheet, cid))
                continue
        else:
            text = ""
        if typed and status in ("gold_ok", "utrnet_ok") and typed != text:
            warns.append("%s: %s is %s but has different verified_text; using the typed text" % (sheet, cid, status))
            text, status = typed, "corrected"
        reviewer = cell(row[ix["reviewer"]])
        if not reviewer:
            warns.append("%s: %s has no reviewer name" % (sheet, cid))
        date = row[ix_date] if ix_date is not None else None
        date = date.date().isoformat() if hasattr(date, "date") else cell(date)   # Excel may store a datetime
        reviews.append({"cid": cid, "status": status, "text": text, "reviewer": reviewer or "?",
                        "review_date": date, "notes": cell(row[ix["notes"]]), "sheet": sheet, "modified": modified,
                        "adjudication": "adjudication" in sheet.lower()})
    return reviews, total


def same(a, b):
    ua, ub = a["status"] in USABLE, b["status"] in USABLE
    if ua != ub:
        return False
    return (not ua) or normalise(a["text"]) == normalise(b["text"])


def kappa(pairs):
    """Cohen's kappa for a list of (label_a, label_b)."""
    n = len(pairs)
    if not n:
        return None
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return None if pe == 1 else round((po - pe) / (1 - pe), 3)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("sheets", nargs="*", help="default: data/review/*.xlsx")
    ap.add_argument("--lines", default=os.path.join(P.PROCESSED_DIR, "lines.tsv"))
    ap.add_argument("--out-dir", default=os.path.join("data", "annotations"))
    args = ap.parse_args()
    sheets = args.sheets or sorted(glob.glob(os.path.join("data", "review", "*.xlsx")))
    sheets = [s for s in sheets if not os.path.basename(s).startswith("~$")]   # Excel lock files
    if not sheets:
        raise SystemExit("no review sheets found")

    gold = {os.path.splitext(os.path.basename(r["crop"]))[0]: r for r in read_tsv(args.lines)}
    lines_sha = sha256(args.lines)
    overlap_crops = set()
    for d in sorted({os.path.dirname(os.path.abspath(s)) for s in sheets}):
        for mp in glob.glob(os.path.join(d, "*_manifest.json")):
            with open(mp, encoding="utf-8") as f:
                m = json.load(f)
            overlap_crops |= {os.path.splitext(os.path.basename(c))[0] for c in m.get("overlap", [])}
            if m.get("lines_tsv_sha256") != lines_sha:
                print("WARNING: %s was built from a different lines.tsv (sha %s...) than %s (sha %s...). "
                      "Crops may not match the text the reviewers saw." % (os.path.basename(mp),
                      str(m.get("lines_tsv_sha256"))[:12], args.lines, lines_sha[:12]))
    merged_at = datetime.datetime.now().isoformat(timespec="seconds")
    warns, per_sheet = [], []
    by_crop = defaultdict(list)
    for path in sheets:
        reviews, total = read_sheet(path, gold, warns)
        per_sheet.append((os.path.basename(path), len(reviews), total))
        for rv in reviews:
            by_crop[rv["cid"]].append(rv)

    out, conflicts, pairs_keep, pair_cer = {}, [], [], [0, 0]
    agree_n = double_n = 0
    for cid, rvs in by_crop.items():
        g = gold[cid]
        adj = [r for r in rvs if r["adjudication"]]
        normal = [r for r in rvs if not r["adjudication"]]
        if len(normal) >= 2:                                      # agreement stats ignore adjudication
            a, b = normal[0], normal[1]
            double_n += 1
            agree_n += same(a, b)
            pairs_keep.append((a["status"] in USABLE, b["status"] in USABLE))
            if a["status"] in USABLE and b["status"] in USABLE:
                ta, tb = normalise(a["text"]), normalise(b["text"])
                pair_cer[0] += edit(ta, tb)
                pair_cer[1] += max(len(ta), len(tb))
        if adj:
            final, agreement = adj[-1], "adjudicated"
        elif len(normal) == 1:
            final, agreement = normal[0], "single"
        elif all(same(normal[0], r) for r in normal[1:]):
            final, agreement = normal[0], "agree"
        else:
            final, agreement = None, "conflict"
            conflicts.append({"crop": g["crop"], "page_id": g["page_id"], "split": g["split"],
                              "original_text": g["text"],
                              "reviews": " || ".join("%s [%s]: %s" % (r["reviewer"], r["status"], r["text"]) for r in normal)})
        status = final["status"] if final else "conflict"
        text = final["text"] if final else ""
        out[cid] = {"crop": g["crop"], "page_id": g["page_id"], "split": g["split"], "status": status,
                    "verified_text": text, "original_text": g["text"],
                    "changed": "1" if status in USABLE and text != g["text"] else "0",
                    "reviewed_by": "; ".join(dict.fromkeys(r["reviewer"] for r in rvs)),
                    "review_date": "; ".join(r["review_date"] or "?" for r in rvs),
                    "n_reviews": str(len(rvs)), "agreement": agreement,
                    "notes": " | ".join(r["notes"] for r in rvs if r["notes"]),
                    "sheets": "; ".join(dict.fromkeys(r["sheet"] for r in rvs)),
                    "sheet_modified": max(r["modified"] for r in rvs), "merged_at": merged_at,
                    "lines_sha256": lines_sha}

    os.makedirs(args.out_dir, exist_ok=True)
    with open(os.path.join(args.out_dir, "verified_lines.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(OUT_COLS) + "\n")
        for cid in sorted(out):
            f.write("\t".join(out[cid][c] for c in OUT_COLS) + "\n")
    with open(os.path.join(args.out_dir, "review_conflicts.tsv"), "w", encoding="utf-8", newline="") as f:
        cols = ["crop", "page_id", "split", "original_text", "reviews"]
        f.write("\t".join(cols) + "\n")
        for c in conflicts:
            f.write("\t".join(c[k].replace("\t", " ") for k in cols) + "\n")
    n_normal = {c: sum(not r["adjudication"] for r in by_crop.get(c, [])) for c in overlap_crops}
    k = kappa(pairs_keep)
    agreement = {"merged_at": merged_at, "lines_sha256": lines_sha,
                 "overlap_lines_planned": len(overlap_crops),
                 "overlap_awaiting_second_review": sum(v == 1 for v in n_normal.values()),
                 "overlap_not_reviewed": sum(v == 0 for v in n_normal.values()),
                 "double_reviewed_lines": double_n,
                 "agreement_rate": round(agree_n / double_n, 3) if double_n else None,
                 "keep_vs_drop_kappa": k,
                 "keep_vs_drop_kappa_note": None if k is not None else
                     "undefined: no double-reviewed lines, or both reviewers made the same keep/drop choice on every line",
                 "inter_reviewer_cer_pct": round(100.0 * pair_cer[0] / pair_cer[1], 2) if pair_cer[1] else None,
                 "conflicts_open": len(conflicts),
                 "definitions": {
                     "double_reviewed_lines": "lines with a decision from two non-adjudication reviewers; lines "
                                              "with one or no decision are counted separately, never as agreement",
                     "agreement_rate": "both keep the line with identical normalised text, or both drop it",
                     "keep_vs_drop_kappa": "Cohen's kappa on the two reviewers' keep (gold_ok/utrnet_ok/corrected) "
                                           "vs drop (exclude/illegible) decisions",
                     "inter_reviewer_cer_pct": "total edit distance / total max(len) between the two reviewers' "
                                               "normalised texts, on lines both kept"}}
    with open(os.path.join(args.out_dir, "review_agreement.json"), "w", encoding="utf-8") as f:
        json.dump(agreement, f, indent=1)

    print("review progress:")
    for name, done, total in per_sheet:
        print("  %-30s %4d / %4d reviewed (%.0f%%)" % (name, done, total, 100.0 * done / max(total, 1)))
    print("lines with a final status: %d   statuses: %s" % (len(out), dict(Counter(r["status"] for r in out.values()))))
    usable = [r for r in out.values() if r["status"] in USABLE]
    print("original gold changed on %d of %d usable lines" % (sum(r["changed"] == "1" for r in usable), len(usable)))
    if overlap_crops:
        print("overlap: %d planned, %d awaiting 2nd review, %d not reviewed"
              % (len(overlap_crops), agreement["overlap_awaiting_second_review"], agreement["overlap_not_reviewed"]))
    if double_n:
        print("double-reviewed: %d  agreement %.1f%%  keep/drop kappa %s  inter-reviewer CER %s%%  open conflicts %d"
              % (double_n, 100.0 * agree_n / double_n, k if k is not None else "undefined",
                 agreement["inter_reviewer_cer_pct"], len(conflicts)))
    missing_dates = sum(1 for rvs in by_crop.values() for r in rvs if not r["review_date"])
    if missing_dates:
        print("reviews without a review_date: %d" % missing_dates)
    print("wrote %s/{verified_lines.tsv, review_conflicts.tsv, review_agreement.json}" % args.out_dir)
    if warns:
        print("\nwarnings: %d" % len(warns))
        for w in warns[:50]:
            print("  " + w)


if __name__ == "__main__":
    main()
