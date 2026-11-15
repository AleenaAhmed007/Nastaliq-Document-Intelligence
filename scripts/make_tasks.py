#!/usr/bin/env python3
"""
make_tasks.py: manifest.csv -> Label Studio import file (tasks.json)

Takes the pages marked annotate=1 by triage.py and builds one task per page.
Order is: test, test_unseen, val, then train, so the evaluation pages are done first.
Pages from files listed in review_personal_data.csv are left out unless you pass
--include-flagged (do that only after you opened those files and checked them).

Run from the repo root (the same folder you ran triage.py from):
    python scripts/make_tasks.py
"""
import argparse
import csv
import json
import os
import random
from collections import Counter, defaultdict

import paths as P


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default=P.PAGE_MANIFEST)
    ap.add_argument("--review", default=P.PRIVACY_REVIEW)
    ap.add_argument("--doc-root", default=".",
                    help="folder you give to Label Studio as LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT")
    ap.add_argument("--out", default=P.TASKS_JSON)
    ap.add_argument("--all", action="store_true", help="ignore the annotate flag, use every page")
    ap.add_argument("--include-flagged", action="store_true")
    ap.add_argument("--pass2", type=int, default=120,
                    help="pages to mark for line transcription: all test/val/test_unseen plus balanced train up to this total")
    ap.add_argument("--seed", type=int, default=13)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    rows = read_csv(args.manifest)
    flagged = set()
    if os.path.exists(args.review):
        flagged = {r["file"] for r in read_csv(args.review)}

    chosen, dropped = [], Counter()
    for r in rows:
        if not args.all and r.get("annotate") != "1":
            continue
        if r["file"] in flagged and not args.include_flagged:
            dropped["flagged_file"] += 1
            continue
        chosen.append(r)

    # pass 2 = all evaluation pages + type balanced train pages
    eval_splits = ("test", "test_unseen", "val")
    pass2 = {r["page_id"] for r in chosen if r["split"] in eval_splits}
    left = args.pass2 - len(pass2)
    train_by_type = defaultdict(list)
    for r in chosen:
        if r["split"] == "train":
            train_by_type[r["type"]].append(r)
    while left > 0 and any(train_by_type.values()):
        for t in list(train_by_type):
            if train_by_type[t] and left > 0:
                pass2.add(train_by_type[t].pop(rng.randrange(len(train_by_type[t])))["page_id"])
                left -= 1

    order = {"test": 0, "test_unseen": 1, "val": 2, "train": 3}
    rng.shuffle(chosen)
    chosen.sort(key=lambda r: order.get(r["split"], 9))

    tasks = []
    for r in chosen:
        rel = os.path.relpath(r["image"], args.doc_root).replace("\\", "/")
        tasks.append({"data": {
            "image": "/data/local-files/?d=" + rel,
            "local_path": rel,
            "page_id": r["page_id"],
            "file": r["file"],
            "source": r["source"],
            "type": r["type"],
            "split": r["split"],
            "low_res": int(r.get("low_res") or 0),
            "pass2": int(r["page_id"] in pass2),
        }})

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=1)

    print("tasks written:", len(tasks), "->", args.out)
    print("by split:", dict(Counter(t["data"]["split"] for t in tasks)))
    print("by type :", dict(Counter(t["data"]["type"] for t in tasks)))
    print("pass 2 (line transcription):", sum(t["data"]["pass2"] for t in tasks))
    if dropped:
        print("left out because their file is in the personal data review list:", dict(dropped))
        print("  (open those files, delete the real slips/results, then re-run with --include-flagged)")


if __name__ == "__main__":
    main()
