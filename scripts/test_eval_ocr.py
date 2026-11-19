#!/usr/bin/env python3
"""
test_eval_ocr.py: checks that the OCR metrics are computed the way the report says.

    python scripts/test_eval_ocr.py

No test framework needed. Each check prints PASS or raises with an explanation.
"""
import csv
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eval_ocr import Acc, align, content_type, normalise, suspect_reference   # noqa: E402
from merge_review import kappa                      # noqa: E402
from postprocess_ocr import fix_ltr_line            # noqa: E402
from combine_ocr import choose                      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = []


def check(fn):
    CHECKS.append(fn)
    return fn


def scored(pairs):
    a = Acc()
    for ref, hyp in pairs:
        a.add(normalise(ref), normalise(hyp))
    return dict(zip(["lines", "cer", "cer_nosp", "wer", "ned", "exact"], a.row()))


@check
def same_normalisation_for_gold_and_prediction():
    # Arabic yeh/kaf + Urdu digits in the gold, Urdu letters + ASCII digits in the prediction
    r = scored([("كتاب ي ۲۰۲۶", "کتاب ی 2026")])
    assert r["cer"] == "0.0", r


@check
def cer_is_micro_averaged_not_mean_of_lines():
    # line 1: 2 errors / 2 chars (100%), line 2: 0 / 8 (0%). Mean of lines = 50%, micro = 2/10 = 20%
    r = scored([("ab", ""), ("abcdefgh", "abcdefgh")])
    assert r["cer"] == "20.0", r


@check
def insertions_can_push_cer_above_100():
    r = scored([("1", "123")])                    # 2 insertions / 1 reference char
    assert r["cer"] == "200.0", r


@check
def empty_prediction_is_100_percent():
    r = scored([("abc", "")])
    assert r["cer"] == "100.0" and r["wer"] == "100.0" and r["exact"] == "0.0", r


@check
def wer_counts_word_substitutions_and_deletions():
    r = scored([("a b c d", "a x c")])            # 1 substitution + 1 deletion over 4 words
    assert r["wer"] == "50.0", r


@check
def ned_is_per_line_over_longer_string():
    r = scored([("a", "abcd")])                   # 3 edits / max(1, 4)
    assert r["ned"] == "0.750", r


@check
def substitutions_deletions_insertions_add_up_to_cer():
    a = Acc()
    a.add("abcd", "axd")          # b->x substitution, c deleted
    a.add("12", "1234")           # 2 insertions
    row = dict(zip(["lines", "chars", "avg_ref", "avg_pred", "cer", "s", "d", "i"], a.error_row()))
    assert (row["s"], row["d"], row["i"], row["cer"]) == ("16.7", "16.7", "33.3", "66.7"), row


@check
def content_type_classifies_lines():
    cases = {"کتاب": "urdu_only", "مورخہ 2026": "urdu+digits", "۲۰۲۶ مورخہ": "urdu+digits",
             "Online Account کے": "urdu+latin", "03-08-2022": "digits_only", "CS Scanned": "latin_only",
             "F03-12": "latin_only", "-/:": "other"}
    for text, want in cases.items():
        got = content_type(normalise(text))
        assert got == want, (text, got, want)


@check
def alignment_reports_the_missing_letter():
    d, ops = align("کتاب", "کتب")
    assert d == 1 and ops == [("ا", "∅")], (d, ops)


@check
def suspect_references_are_flagged_and_real_ones_are_not():
    bad = ["からいというかんな", "۔۔۔۔۔۔۔۔۔۔", "中文"]
    good = ["کتاب", "-5", "10-12-2021", "CS Scanned", "()", "☆", "۔۔۔"]   # short odd refs stay scored
    assert all(suspect_reference(normalise(t)) for t in bad), [t for t in bad if not suspect_reference(normalise(t))]
    assert not any(suspect_reference(normalise(t)) for t in good), [t for t in good if suspect_reference(normalise(t))]


@check
def ltr_postprocessing_only_touches_digit_punctuation_lines():
    cases = {"2021-12-10": "10-12-2021", "2021/4/16": "16/4/2021", "25۔03": "03-25",   # date groups reversed
             "5۔": "5۔", "1-": "1-",        # list markers stay in RTL reading order (review rule: -5 is typed 5-)
             "1830": "1830", "(12) 3": "(12) 3",   # a single digit run and text around numbers keep their order
             "مورخہ 2021-12-10": "مورخہ 2021-12-10",   # Urdu line: untouched
             "(7ز)": "(7ز)", "CS 5": "CS 5"}   # Urdu or Latin letters present: untouched
    for pred, want in cases.items():
        got = fix_ltr_line(pred)
        assert got == want, (pred, got, want)


@check
def hybrid_routes_only_lines_without_urdu_letters():
    assert choose("5۔", "-5") == ("-5", "fallback")
    assert choose("(77)", "(vi)") == ("(vi)", "fallback")
    assert choose("", "12") == ("12", "fallback")
    assert choose("مورخہ 10-12-2021", "garbage 10-12-2021") == ("مورخہ 10-12-2021", "primary")


@check
def kappa_matches_hand_computation():
    # po = 3/4; reviewer A keeps 3/4, B keeps 2/4 -> pe = (3*2 + 1*2) / 16 = 0.5 -> kappa = 0.5
    assert kappa([(True, True), (True, False), (False, False), (True, True)]) == 0.5
    assert kappa([(True, True), (True, True)]) is None          # no variation: undefined, not 1.0


@check
def report_uses_only_common_lines_and_skips_empty_references():
    with tempfile.TemporaryDirectory() as d:
        def tsv(name, cols, rows):
            p = os.path.join(d, name)
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write("\t".join(cols) + "\n")
                for r in rows:
                    f.write("\t".join(r) + "\n")
            return p
        cols = ["crop", "page_id", "split", "type", "region_id", "bbox", "text"]
        lines = tsv("lines.tsv", cols, [
            ["lines/A_L01.png", "A", "val", "scan", "r1", "0,0,100,20", "کتاب"],
            ["lines/A_L02.png", "A", "val", "scan", "r2", "0,30,100,20", "ـ"],        # tatweel only -> empty
            ["lines/A_L03.png", "A", "val", "photo", "r3", "0,60,100,20", "قلم"]])
        pages = os.path.join(d, "pages.jsonl")
        with open(pages, "w", encoding="utf-8") as f:
            f.write(json.dumps({"page_id": "A", "regions": []}) + "\n")
        p1 = tsv("sys1.tsv", ["crop", "pred"], [["lines/A_L01.png", "کتاب"], ["lines/A_L02.png", "x"],
                                                ["lines/A_L03.png", "قلم"]])
        p2 = tsv("sys2.tsv", ["crop", "pred"], [["lines/A_L01.png", "کتب"], ["lines/A_L02.png", "x"]])  # no L03
        ver = tsv("verified.tsv", ["crop", "status", "verified_text"], [
            ["lines/A_L01.png", "corrected", "کتاب"], ["lines/A_L02.png", "gold_ok", "ـ"],
            ["lines/A_L03.png", "exclude", ""]])
        out = os.path.join(d, "r.md")
        subprocess.run([sys.executable, os.path.join(HERE, "eval_ocr.py"), p1, p2, "--lines", lines,
                        "--pages", pages, "--verified", ver, "--out", out],
                       check=True, capture_output=True)
        text = open(out, encoding="utf-8").read()
        # L03 is excluded by review and missing from sys2; L02 is empty after normalisation
        assert "Lines scored: 1 (" in text and "minus 1 with an empty reference" in text, text[:600]
        assert "Skipped 1 line(s) whose reference is empty" in text, text[:900]
        overall = text.split("### Overall")[1].split("###")[0]
        assert "| all | sys1 | 1 | 0.0 |" in overall, overall           # same single line for both systems
        assert "| all | sys2 | 1 | 25.0 |" in overall, overall
        assert "| all | original_gold | 1 | 0.0 |" in overall, overall   # Evaluation A row present
        assert "| val | 3 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 |" in text, text  # coverage table row


if __name__ == "__main__":
    failed = 0
    for fn in CHECKS:
        try:
            fn()
            print("PASS  " + fn.__name__)
        except AssertionError as e:
            failed += 1
            print("FAIL  %s: %s" % (fn.__name__, e))
    print("\n%d / %d checks passed" % (len(CHECKS) - failed, len(CHECKS)))
    sys.exit(1 if failed else 0)
