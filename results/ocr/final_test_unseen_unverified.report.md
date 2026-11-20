# OCR evaluation

Systems: utrnet_large_w800_test_unseen_det, tesseract_urd-eng_test_unseen, tesseract_eng_test_unseen, hybrid_final_test_unseen  
Reference: original gold (data/processed/lines.tsv, NOT human-verified)  
Lines scored: 823 (crops present in every prediction file, minus 0 with an empty reference)  
Line accounting: 823 lines in every prediction file = 823 scored + 0 empty reference + 0 suspect reference (excluded by heuristic, awaiting human correction)  
CER / WER = total edits (S+D+I) / total reference characters / words over all lines (micro); NED = mean of per-line edit / max(len(ref), len(pred)); can exceed 100% when the OCR inserts text  
Normalisation: full (see eval_ocr.py docstring)

### Overall

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| all | utrnet_large_w800_test_unseen_det | 823 | 17.7 | 16.0 | 44.2 | 0.169 | 24.5 |
| all | tesseract_urd-eng_test_unseen | 823 | 67.1 | 69.9 | 92.7 | 0.619 | 9.5 |
| all | tesseract_eng_test_unseen | 823 | 88.3 | 94.3 | 98.6 | 0.802 | 9.6 |
| all | hybrid_final_test_unseen | 823 | 16.4 | 14.5 | 43.5 | 0.137 | 26.6 |

### By split

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen | utrnet_large_w800_test_unseen_det | 823 | 17.7 | 16.0 | 44.2 | 0.169 | 24.5 |
| test_unseen | tesseract_urd-eng_test_unseen | 823 | 67.1 | 69.9 | 92.7 | 0.619 | 9.5 |
| test_unseen | tesseract_eng_test_unseen | 823 | 88.3 | 94.3 | 98.6 | 0.802 | 9.6 |
| test_unseen | hybrid_final_test_unseen | 823 | 16.4 | 14.5 | 43.5 | 0.137 | 26.6 |

### By split x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen / digital | utrnet_large_w800_test_unseen_det | 823 | 17.7 | 16.0 | 44.2 | 0.169 | 24.5 |
| test_unseen / digital | tesseract_urd-eng_test_unseen | 823 | 67.1 | 69.9 | 92.7 | 0.619 | 9.5 |
| test_unseen / digital | tesseract_eng_test_unseen | 823 | 88.3 | 94.3 | 98.6 | 0.802 | 9.6 |
| test_unseen / digital | hybrid_final_test_unseen | 823 | 16.4 | 14.5 | 43.5 | 0.137 | 26.6 |

### By category

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen / num_latin | utrnet_large_w800_test_unseen_det | 123 | 72.1 | 70.8 | 81.8 | 0.393 | 50.4 |
| test_unseen / num_latin | tesseract_urd-eng_test_unseen | 123 | 31.5 | 29.4 | 59.7 | 0.217 | 61.0 |
| test_unseen / num_latin | tesseract_eng_test_unseen | 123 | 15.5 | 14.6 | 45.5 | 0.160 | 64.2 |
| test_unseen / num_latin | hybrid_final_test_unseen | 123 | 22.9 | 21.8 | 47.4 | 0.188 | 64.2 |
| test_unseen / urdu | utrnet_large_w800_test_unseen_det | 700 | 16.3 | 14.3 | 43.3 | 0.130 | 20.0 |
| test_unseen / urdu | tesseract_urd-eng_test_unseen | 700 | 68.1 | 71.2 | 93.6 | 0.689 | 0.4 |
| test_unseen / urdu | tesseract_eng_test_unseen | 700 | 90.3 | 96.8 | 99.9 | 0.914 | 0.0 |
| test_unseen / urdu | hybrid_final_test_unseen | 700 | 16.2 | 14.2 | 43.4 | 0.129 | 20.0 |

### By content

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen / digits_only | utrnet_large_w800_test_unseen_det | 105 | 62.2 | 60.3 | 59.3 | 0.326 | 59.0 |
| test_unseen / digits_only | tesseract_urd-eng_test_unseen | 105 | 33.1 | 32.1 | 50.8 | 0.209 | 65.7 |
| test_unseen / digits_only | tesseract_eng_test_unseen | 105 | 14.1 | 13.5 | 39.8 | 0.151 | 69.5 |
| test_unseen / digits_only | hybrid_final_test_unseen | 105 | 24.9 | 23.9 | 42.4 | 0.178 | 69.5 |
| test_unseen / latin_only | utrnet_large_w800_test_unseen_det | 17 | 86.0 | 85.8 | 157.1 | 0.803 | 0.0 |
| test_unseen / latin_only | tesseract_urd-eng_test_unseen | 17 | 29.2 | 25.7 | 88.6 | 0.261 | 35.3 |
| test_unseen / latin_only | tesseract_eng_test_unseen | 17 | 17.2 | 16.0 | 62.9 | 0.203 | 35.3 |
| test_unseen / latin_only | hybrid_final_test_unseen | 17 | 19.8 | 18.4 | 62.9 | 0.228 | 35.3 |
| test_unseen / other | utrnet_large_w800_test_unseen_det | 1 | 66.7 | 66.7 | 100.0 | 0.500 | 0.0 |
| test_unseen / other | tesseract_urd-eng_test_unseen | 1 | 33.3 | 33.3 | 100.0 | 0.333 | 0.0 |
| test_unseen / other | tesseract_eng_test_unseen | 1 | 33.3 | 33.3 | 100.0 | 0.333 | 0.0 |
| test_unseen / other | hybrid_final_test_unseen | 1 | 66.7 | 66.7 | 100.0 | 0.500 | 0.0 |
| test_unseen / urdu+digits | utrnet_large_w800_test_unseen_det | 61 | 16.4 | 13.4 | 45.0 | 0.173 | 3.3 |
| test_unseen / urdu+digits | tesseract_urd-eng_test_unseen | 61 | 64.9 | 66.5 | 94.3 | 0.619 | 0.0 |
| test_unseen / urdu+digits | tesseract_eng_test_unseen | 61 | 87.5 | 93.7 | 100.0 | 0.843 | 0.0 |
| test_unseen / urdu+digits | hybrid_final_test_unseen | 61 | 16.2 | 13.1 | 45.0 | 0.162 | 3.3 |
| test_unseen / urdu+latin | utrnet_large_w800_test_unseen_det | 172 | 28.2 | 27.4 | 52.7 | 0.232 | 0.0 |
| test_unseen / urdu+latin | tesseract_urd-eng_test_unseen | 172 | 66.5 | 69.8 | 93.2 | 0.645 | 0.0 |
| test_unseen / urdu+latin | tesseract_eng_test_unseen | 172 | 87.7 | 94.1 | 99.3 | 0.869 | 0.0 |
| test_unseen / urdu+latin | hybrid_final_test_unseen | 172 | 28.1 | 27.3 | 52.9 | 0.231 | 0.0 |
| test_unseen / urdu_only | utrnet_large_w800_test_unseen_det | 467 | 7.4 | 4.7 | 36.3 | 0.087 | 29.6 |
| test_unseen / urdu_only | tesseract_urd-eng_test_unseen | 467 | 70.0 | 73.2 | 93.7 | 0.714 | 0.6 |
| test_unseen / urdu_only | tesseract_eng_test_unseen | 467 | 92.7 | 99.5 | 100.3 | 0.940 | 0.0 |
| test_unseen / urdu_only | hybrid_final_test_unseen | 467 | 7.4 | 4.7 | 36.3 | 0.087 | 29.6 |

### By aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen / 12.5-25 | utrnet_large_w800_test_unseen_det | 146 | 14.5 | 12.8 | 43.2 | 0.154 | 2.7 |
| test_unseen / 12.5-25 | tesseract_urd-eng_test_unseen | 146 | 64.1 | 67.6 | 92.9 | 0.637 | 0.0 |
| test_unseen / 12.5-25 | tesseract_eng_test_unseen | 146 | 86.9 | 94.4 | 99.2 | 0.856 | 0.0 |
| test_unseen / 12.5-25 | hybrid_final_test_unseen | 146 | 14.3 | 12.4 | 43.3 | 0.148 | 2.7 |
| test_unseen / <=12.5 | utrnet_large_w800_test_unseen_det | 667 | 19.7 | 17.8 | 45.4 | 0.171 | 29.7 |
| test_unseen / <=12.5 | tesseract_urd-eng_test_unseen | 667 | 69.6 | 71.8 | 92.9 | 0.615 | 11.7 |
| test_unseen / <=12.5 | tesseract_eng_test_unseen | 667 | 89.9 | 94.8 | 98.2 | 0.791 | 11.8 |
| test_unseen / <=12.5 | hybrid_final_test_unseen | 667 | 17.9 | 15.8 | 44.4 | 0.135 | 32.2 |
| test_unseen / >25 | utrnet_large_w800_test_unseen_det | 10 | 19.4 | 19.7 | 32.7 | 0.250 | 0.0 |
| test_unseen / >25 | tesseract_urd-eng_test_unseen | 10 | 56.8 | 61.4 | 88.8 | 0.558 | 0.0 |
| test_unseen / >25 | tesseract_eng_test_unseen | 10 | 76.0 | 83.3 | 99.0 | 0.681 | 0.0 |
| test_unseen / >25 | hybrid_final_test_unseen | 10 | 13.2 | 13.1 | 28.1 | 0.136 | 0.0 |

### By category x aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen / num_latin / 12.5-25 | utrnet_large_w800_test_unseen_det | 2 | 84.8 | 84.5 | 100.0 | 0.810 | 0.0 |
| test_unseen / num_latin / 12.5-25 | tesseract_urd-eng_test_unseen | 2 | 80.3 | 69.0 | 140.0 | 0.730 | 0.0 |
| test_unseen / num_latin / 12.5-25 | tesseract_eng_test_unseen | 2 | 27.3 | 22.4 | 70.0 | 0.246 | 0.0 |
| test_unseen / num_latin / 12.5-25 | hybrid_final_test_unseen | 2 | 50.0 | 50.0 | 70.0 | 0.466 | 0.0 |
| test_unseen / num_latin / <=12.5 | utrnet_large_w800_test_unseen_det | 119 | 71.0 | 69.8 | 73.7 | 0.382 | 52.1 |
| test_unseen / num_latin / <=12.5 | tesseract_urd-eng_test_unseen | 119 | 23.4 | 22.5 | 47.4 | 0.204 | 63.0 |
| test_unseen / num_latin / <=12.5 | tesseract_eng_test_unseen | 119 | 15.3 | 14.6 | 40.6 | 0.160 | 66.4 |
| test_unseen / num_latin / <=12.5 | hybrid_final_test_unseen | 119 | 22.5 | 21.1 | 42.9 | 0.185 | 66.4 |
| test_unseen / num_latin / >25 | utrnet_large_w800_test_unseen_det | 2 | 71.3 | 69.7 | 163.6 | 0.657 | 0.0 |
| test_unseen / num_latin / >25 | tesseract_urd-eng_test_unseen | 2 | 50.9 | 51.5 | 136.4 | 0.492 | 0.0 |
| test_unseen / num_latin / >25 | tesseract_eng_test_unseen | 2 | 9.3 | 10.1 | 81.8 | 0.086 | 0.0 |
| test_unseen / num_latin / >25 | hybrid_final_test_unseen | 2 | 9.3 | 10.1 | 81.8 | 0.086 | 0.0 |
| test_unseen / urdu / 12.5-25 | utrnet_large_w800_test_unseen_det | 144 | 14.1 | 12.3 | 43.0 | 0.145 | 2.8 |
| test_unseen / urdu / 12.5-25 | tesseract_urd-eng_test_unseen | 144 | 64.0 | 67.6 | 92.7 | 0.636 | 0.0 |
| test_unseen / urdu / 12.5-25 | tesseract_eng_test_unseen | 144 | 87.2 | 94.8 | 99.4 | 0.865 | 0.0 |
| test_unseen / urdu / 12.5-25 | hybrid_final_test_unseen | 144 | 14.1 | 12.2 | 43.2 | 0.144 | 2.8 |
| test_unseen / urdu / <=12.5 | utrnet_large_w800_test_unseen_det | 548 | 17.8 | 15.6 | 44.4 | 0.126 | 24.8 |
| test_unseen / urdu / <=12.5 | tesseract_urd-eng_test_unseen | 548 | 71.3 | 73.9 | 94.5 | 0.705 | 0.5 |
| test_unseen / urdu / <=12.5 | tesseract_eng_test_unseen | 548 | 92.6 | 98.3 | 100.3 | 0.929 | 0.0 |
| test_unseen / urdu / <=12.5 | hybrid_final_test_unseen | 548 | 17.8 | 15.5 | 44.4 | 0.124 | 24.8 |
| test_unseen / urdu / >25 | utrnet_large_w800_test_unseen_det | 8 | 13.6 | 13.5 | 24.9 | 0.148 | 0.0 |
| test_unseen / urdu / >25 | tesseract_urd-eng_test_unseen | 8 | 57.5 | 62.6 | 85.9 | 0.574 | 0.0 |
| test_unseen / urdu / >25 | tesseract_eng_test_unseen | 8 | 83.4 | 92.4 | 100.0 | 0.830 | 0.0 |
| test_unseen / urdu / >25 | hybrid_final_test_unseen | 8 | 13.6 | 13.5 | 24.9 | 0.148 | 0.0 |

### By category x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test_unseen / num_latin / digital | utrnet_large_w800_test_unseen_det | 123 | 72.1 | 70.8 | 81.8 | 0.393 | 50.4 |
| test_unseen / num_latin / digital | tesseract_urd-eng_test_unseen | 123 | 31.5 | 29.4 | 59.7 | 0.217 | 61.0 |
| test_unseen / num_latin / digital | tesseract_eng_test_unseen | 123 | 15.5 | 14.6 | 45.5 | 0.160 | 64.2 |
| test_unseen / num_latin / digital | hybrid_final_test_unseen | 123 | 22.9 | 21.8 | 47.4 | 0.188 | 64.2 |
| test_unseen / urdu / digital | utrnet_large_w800_test_unseen_det | 700 | 16.3 | 14.3 | 43.3 | 0.130 | 20.0 |
| test_unseen / urdu / digital | tesseract_urd-eng_test_unseen | 700 | 68.1 | 71.2 | 93.6 | 0.689 | 0.4 |
| test_unseen / urdu / digital | tesseract_eng_test_unseen | 700 | 90.3 | 96.8 | 99.9 | 0.914 | 0.0 |
| test_unseen / urdu / digital | hybrid_final_test_unseen | 700 | 16.2 | 14.2 | 43.4 | 0.129 | 20.0 |

### Error types by content

S / D / I = substitutions / deletions / insertions as % of reference characters (they add up to CER).

| group | system | lines | ref chars | avg ref len | avg pred len | CER % | S % | D % | I % |
|---|---|---|---|---|---|---|---|---|---|
| test_unseen / digits_only | utrnet_large_w800_test_unseen_det | 105 | 481 | 4.6 | 4.5 | 62.2 | 46.8 | 8.1 | 7.3 |
| test_unseen / digits_only | tesseract_urd-eng_test_unseen | 105 | 481 | 4.6 | 4.5 | 33.1 | 19.3 | 7.9 | 5.8 |
| test_unseen / digits_only | tesseract_eng_test_unseen | 105 | 481 | 4.6 | 4.4 | 14.1 | 6.0 | 5.6 | 2.5 |
| test_unseen / digits_only | hybrid_final_test_unseen | 105 | 481 | 4.6 | 4.6 | 24.9 | 16.4 | 4.4 | 4.2 |
| test_unseen / latin_only | utrnet_large_w800_test_unseen_det | 17 | 349 | 20.5 | 18.2 | 86.0 | 69.3 | 14.0 | 2.6 |
| test_unseen / latin_only | tesseract_urd-eng_test_unseen | 17 | 349 | 20.5 | 19.8 | 29.2 | 13.2 | 9.7 | 6.3 |
| test_unseen / latin_only | tesseract_eng_test_unseen | 17 | 349 | 20.5 | 19.4 | 17.2 | 4.0 | 9.5 | 3.7 |
| test_unseen / latin_only | hybrid_final_test_unseen | 17 | 349 | 20.5 | 19.7 | 19.8 | 8.3 | 7.7 | 3.7 |
| test_unseen / other | utrnet_large_w800_test_unseen_det | 1 | 3 | 3.0 | 4.0 | 66.7 | 33.3 | 0.0 | 33.3 |
| test_unseen / other | tesseract_urd-eng_test_unseen | 1 | 3 | 3.0 | 3.0 | 33.3 | 33.3 | 0.0 | 0.0 |
| test_unseen / other | tesseract_eng_test_unseen | 1 | 3 | 3.0 | 3.0 | 33.3 | 33.3 | 0.0 | 0.0 |
| test_unseen / other | hybrid_final_test_unseen | 1 | 3 | 3.0 | 4.0 | 66.7 | 33.3 | 0.0 | 33.3 |
| test_unseen / urdu+digits | utrnet_large_w800_test_unseen_det | 61 | 3239 | 53.1 | 49.3 | 16.4 | 5.2 | 9.2 | 2.0 |
| test_unseen / urdu+digits | tesseract_urd-eng_test_unseen | 61 | 3239 | 53.1 | 31.7 | 64.9 | 20.3 | 42.5 | 2.2 |
| test_unseen / urdu+digits | tesseract_eng_test_unseen | 61 | 3239 | 53.1 | 22.7 | 87.5 | 29.5 | 57.6 | 0.4 |
| test_unseen / urdu+digits | hybrid_final_test_unseen | 61 | 3239 | 53.1 | 49.3 | 16.2 | 5.0 | 9.2 | 2.0 |
| test_unseen / urdu+latin | utrnet_large_w800_test_unseen_det | 172 | 11857 | 68.9 | 57.8 | 28.2 | 10.0 | 17.1 | 1.0 |
| test_unseen / urdu+latin | tesseract_urd-eng_test_unseen | 172 | 11857 | 68.9 | 39.7 | 66.5 | 21.2 | 43.8 | 1.4 |
| test_unseen / urdu+latin | tesseract_eng_test_unseen | 172 | 11857 | 68.9 | 29.5 | 87.7 | 29.9 | 57.5 | 0.3 |
| test_unseen / urdu+latin | hybrid_final_test_unseen | 172 | 11857 | 68.9 | 57.8 | 28.1 | 9.9 | 17.2 | 1.0 |
| test_unseen / urdu_only | utrnet_large_w800_test_unseen_det | 467 | 15866 | 34.0 | 32.8 | 7.4 | 2.2 | 4.3 | 0.9 |
| test_unseen / urdu_only | tesseract_urd-eng_test_unseen | 467 | 15866 | 34.0 | 17.3 | 70.0 | 18.7 | 50.3 | 1.1 |
| test_unseen / urdu_only | tesseract_eng_test_unseen | 467 | 15866 | 34.0 | 10.6 | 92.7 | 24.0 | 68.7 | 0.0 |
| test_unseen / urdu_only | hybrid_final_test_unseen | 467 | 15866 | 34.0 | 32.8 | 7.4 | 2.2 | 4.3 | 0.9 |

### Top character confusions on Urdu lines: utrnet_large_w800_test_unseen_det

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 1073 |
| ی | ∅ | 205 |
| ا | ∅ | 200 |
| ∅ |   | 163 |
| ن | ∅ | 129 |
| ر | ∅ | 90 |
| I | ∅ | 81 |
| ک | ∅ | 71 |
| س | ∅ | 68 |
| و | ∅ | 66 |
| ( | ∅ | 57 |
| ، | ∅ | 53 |
| ٹ | ∅ | 50 |
| I | 0 | 47 |
| د | ∅ | 47 |
| ل | ∅ | 47 |
| م | ∅ | 39 |
| ) | ∅ | 39 |
| ی | پ | 37 |
| 1 | 0 | 35 |

### Top confusions on digit / Latin characters: utrnet_large_w800_test_unseen_det

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| I | ∅ | 81 |
| I | 0 | 47 |
| 1 | 0 | 41 |
| 2 | ∅ | 38 |
| 1 | ∅ | 28 |
| R | ∅ | 26 |
| I | 1 | 25 |
| 9 | 0 | 24 |
| 0 | ∅ | 22 |
| 1 | . | 19 |
| 3 | ∅ | 19 |
| 6 | 9 | 18 |
| 4 | ∅ | 18 |
| 9 | 6 | 17 |
| 5 | 4 | 17 |
| 0 | . | 16 |
| P | ∅ | 16 |
| A | 4 | 16 |
| 9 | ∅ | 15 |
| 0 |   | 15 |

### Worst 15 lines: utrnet_large_w800_test_unseen_det

| CER | crop | gold | pred |
|---|---|---|---|
| 1.09 | lines/FBR_0676_p07_L22.png | (∠1701.9990 | 4999. 1771 کے) |
| 1.08 | lines/FBR_0676_p10_L17.png | √(∠2106.9070 | 2790.6010 کے)۔ |
| 1.08 | lines/FBR_0676_p08_L03.png | _(∠1806.2020 | 12000 6000 کے)۔ |
| 1.03 | lines/FBR_0683_p03_L16.png | Taxpayers Unit(I) / 100 26 25 24 | 24، 25، 26، 30 اور ()ندل ecoco87اور |
| 1.00 | lines/FBR_0683_p10_L34.png | ایڈیشنل ڈائریکٹر-II، انٹیلی ایڈیشنل کمشنر(ان لینڈ دفعہ 21A، 22، 23، (I) ایسے تمام افراد یا افراد کے جنس اینڈ انویسٹی گیشن(IR)، ریونیو) 45، 24، 25، 26، 30، اور طبقات جو ریجنل ٹیکس آفس فیصل آباد کیاں آباد دور میں کاروبار کر |  |
| 1.00 | lines/FBR_0683_p10_L26.png | 45(1) | (445 |
| 1.00 | lines/FBR_0683_p09_L26.png | 45(1) | (445 |
| 1.00 | lines/FBR_0683_p09_L02.png | 45(1) | (4445 |
| 1.00 | lines/FBR_0683_p07_L29.png | 45(1) | (4450 |
| 1.00 | lines/FBR_0683_p06_L29.png | ایڈیشنل ڈائر کیٹر – III، انٹیل ایڈیشنل کمشنر (ان لینڈ دفعہ 21A، 22، 23، ڈائر کیٹر انٹیلی جنس اینڈ انویسٹی جنس اینڈ انویسٹی جنس اینڈ انویسٹی اسلام آباد کی طرف سے جنس اینڈ انویسٹی گیسٹن (IR) ریونیو) 45، 24، 25، 26، 30، اور |  |
| 1.00 | lines/FBR_0683_p06_L22.png | 45(1) | (4450 |
| 1.00 | lines/FBR_0683_p06_L06.png | 45(1) | (4442 |
| 1.00 | lines/FBR_0683_p05_L23.png | 45(1) | (4452 |
| 1.00 | lines/FBR_0683_p04_L18.png | 45(1) | (4452 |
| 1.00 | lines/FBR_0683_p03_L33.png | 45(1) | (4440 |

### Top character confusions on Urdu lines: tesseract_urd-eng_test_unseen

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2094 |
| ی | ∅ | 1546 |
| ا | ∅ | 1210 |
| ن | ∅ | 704 |
| ر | ∅ | 693 |
| ک | ∅ | 691 |
| و | ∅ | 642 |
| م | ∅ | 501 |
| ہ | ∅ | 390 |
| ل | ∅ | 389 |
| س | ∅ | 376 |
| د | ∅ | 335 |
| ت | ∅ | 327 |
| ے | ∅ | 310 |
| ، | ∅ | 275 |
| ب | ∅ | 270 |
| ش | ∅ | 255 |
| ٹ | ∅ | 255 |
| گ | ∅ | 221 |
| ( | ∅ | 192 |

### Top confusions on digit / Latin characters: tesseract_urd-eng_test_unseen

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| I | ∅ | 107 |
| 2 | ∅ | 104 |
| 1 | ∅ | 66 |
| 0 | ∅ | 42 |
| R | ∅ | 36 |
| I | 1 | 34 |
| 9 | ∅ | 21 |
| 3 | ∅ | 20 |
| i | ∅ | 20 |
| 5 | ∅ | 19 |
| 6 | ∅ | 16 |
| A | ∅ | 16 |
| 4 | ∅ | 12 |
| S | ∅ | 11 |
| P | ∅ | 11 |
| O | 0 | 11 |
| v | ∅ | 9 |
| 8 | ∅ | 8 |
| C | ∅ | 8 |
| 9 | 0 | 8 |

### Worst 15 lines: tesseract_urd-eng_test_unseen

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/FBR_0683_p02_L42.png | 2 | ر27 |
| 1.50 | lines/FBR_0683_p09_L22.png | 22 | by) |
| 1.33 | lines/FBR_0683_p02_L22.png | (2) | )وو( |
| 1.00 | lines/FBR_0684_p01_L16.png | زاہربیگ | yy |
| 1.00 | lines/FBR_0684_p01_L14.png | کے اندر فروخت کے لیے تیار نہیں کیے گئے" |  |
| 1.00 | lines/FBR_0684_p01_L12.png | "شرط بیہ ہے کہ بورڈ پاکستان سے باہر بر آمد کیے جانے والے سگریٹ کے پیکٹس پر کوڈ شائع کرنے کی شرط کو ان کیسز میں ہٹا سکتا ہے اگر درآمد کنندہ |  |
| 1.00 | lines/FBR_0684_p01_L09.png | خوشی محسوس کر تاہے، لینی:- |  |
| 1.00 | lines/FBR_0684_p01_L05.png | نو شفکیش |  |
| 1.00 | lines/FBR_0683_p10_L34.png | ایڈیشنل ڈائریکٹر-II، انٹیلی ایڈیشنل کمشنر(ان لینڈ دفعہ 21A، 22، 23، (I) ایسے تمام افراد یا افراد کے جنس اینڈ انویسٹی گیشن(IR)، ریونیو) 45، 24، 25، 26، 30، اور طبقات جو ریجنل ٹیکس آفس فیصل آباد کیاں آباد دور میں کاروبار کر |  |
| 1.00 | lines/FBR_0683_p10_L32.png | رہے ہیں جن کی تخصیص (I) میں | NOS |
| 1.00 | lines/FBR_0683_p10_L28.png | رہے ہول۔ | “Uy |
| 1.00 | lines/FBR_0683_p10_L27.png | آباد | aT |
| 1.00 | lines/FBR_0683_p10_L18.png | لاہور | vl |
| 1.00 | lines/FBR_0683_p10_L04.png | لاہور | vl |
| 1.00 | lines/FBR_0683_p09_L33.png | 9 | 0 |

### Top character confusions on Urdu lines: tesseract_eng_test_unseen

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2658 |
| ا | ∅ | 1977 |
| ی | ∅ | 1867 |
| و | ∅ | 1065 |
| ر | ∅ | 1049 |
| ک | ∅ | 989 |
| ن | ∅ | 884 |
| م | ∅ | 700 |
| ل | ∅ | 543 |
| ہ | ∅ | 526 |
| د | ∅ | 461 |
| ت | ∅ | 456 |
| س | ∅ | 445 |
| ے | ∅ | 403 |
| ب | ∅ | 344 |
| ش | ∅ | 316 |
| ف | ∅ | 304 |
| گ | ∅ | 285 |
| ٹ | ∅ | 284 |
| ج | ∅ | 278 |

### Top confusions on digit / Latin characters: tesseract_eng_test_unseen

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 2 | ∅ | 148 |
| I | ∅ | 108 |
| 0 | ∅ | 61 |
| 1 | ∅ | 56 |
| R | ∅ | 37 |
| 3 | ∅ | 35 |
| i | ∅ | 33 |
| 9 | ∅ | 22 |
| 6 | ∅ | 22 |
| 4 | ∅ | 22 |
| 5 | ∅ | 20 |
| S | ∅ | 18 |
| 8 | ∅ | 16 |
| I | S | 15 |
| 0 |   | 14 |
| O | ∅ | 12 |
| P | ∅ | 11 |
| A | ∅ | 11 |
| a | ∅ | 9 |
| 1 |   | 8 |

### Worst 15 lines: tesseract_eng_test_unseen

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/FBR_0683_p02_L05.png | 2 | b) |
| 1.50 | lines/FBR_0683_p09_L22.png | 22 | by) |
| 1.00 | lines/FBR_0684_p01_L16.png | زاہربیگ | yy |
| 1.00 | lines/FBR_0684_p01_L14.png | کے اندر فروخت کے لیے تیار نہیں کیے گئے" |  |
| 1.00 | lines/FBR_0684_p01_L12.png | "شرط بیہ ہے کہ بورڈ پاکستان سے باہر بر آمد کیے جانے والے سگریٹ کے پیکٹس پر کوڈ شائع کرنے کی شرط کو ان کیسز میں ہٹا سکتا ہے اگر درآمد کنندہ |  |
| 1.00 | lines/FBR_0684_p01_L09.png | خوشی محسوس کر تاہے، لینی:- |  |
| 1.00 | lines/FBR_0684_p01_L05.png | نو شفکیش |  |
| 1.00 | lines/FBR_0684_p01_L01.png | حکومت بإکستان | Iles? |
| 1.00 | lines/FBR_0683_p10_L34.png | ایڈیشنل ڈائریکٹر-II، انٹیلی ایڈیشنل کمشنر(ان لینڈ دفعہ 21A، 22، 23، (I) ایسے تمام افراد یا افراد کے جنس اینڈ انویسٹی گیشن(IR)، ریونیو) 45، 24، 25، 26، 30، اور طبقات جو ریجنل ٹیکس آفس فیصل آباد کیاں آباد دور میں کاروبار کر |  |
| 1.00 | lines/FBR_0683_p10_L33.png | ا کی گئی ہے۔ | JY |
| 1.00 | lines/FBR_0683_p10_L32.png | رہے ہیں جن کی تخصیص (I) میں | NOS |
| 1.00 | lines/FBR_0683_p10_L28.png | رہے ہول۔ | “Uy |
| 1.00 | lines/FBR_0683_p10_L27.png | آباد | aT |
| 1.00 | lines/FBR_0683_p10_L18.png | لاہور | vl |
| 1.00 | lines/FBR_0683_p10_L11.png | کی گئی ہے۔ | 5S |

### Top character confusions on Urdu lines: hybrid_final_test_unseen

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 1075 |
| ی | ∅ | 205 |
| ا | ∅ | 200 |
| ∅ |   | 166 |
| ن | ∅ | 129 |
| ر | ∅ | 90 |
| I | ∅ | 82 |
| ک | ∅ | 71 |
| س | ∅ | 68 |
| و | ∅ | 67 |
| ، | ∅ | 58 |
| ( | ∅ | 57 |
| ٹ | ∅ | 50 |
| I | 0 | 47 |
| د | ∅ | 47 |
| ل | ∅ | 46 |
| م | ∅ | 39 |
| ) | ∅ | 39 |
| ی | پ | 37 |
| 2 | ∅ | 36 |

### Top confusions on digit / Latin characters: hybrid_final_test_unseen

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| I | ∅ | 82 |
| I | 0 | 47 |
| 1 | 0 | 37 |
| 2 | ∅ | 36 |
| I | 1 | 27 |
| R | ∅ | 26 |
| 1 | ∅ | 25 |
| 9 | 0 | 21 |
| 1 | . | 19 |
| 3 | ∅ | 18 |
| 6 | 9 | 17 |
| 9 | 6 | 17 |
| 0 | ∅ | 17 |
| A | 4 | 16 |
| P | ∅ | 15 |
| 0 |   | 15 |
| 9 | ∅ | 14 |
| 0 | . | 13 |
| S | ∅ | 13 |
| i | ن | 13 |

### Worst 15 lines: hybrid_final_test_unseen

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/FBR_0683_p02_L05.png | 2 | b) |
| 1.50 | lines/FBR_0683_p09_L22.png | 22 | by) |
| 1.09 | lines/FBR_0676_p07_L22.png | (∠1701.9990 | 4999. 1771 کے) |
| 1.08 | lines/FBR_0676_p10_L17.png | √(∠2106.9070 | 2790.6010 کے)۔ |
| 1.08 | lines/FBR_0676_p08_L03.png | _(∠1806.2020 | 12000 6000 کے)۔ |
| 1.00 | lines/FBR_0683_p10_L34.png | ایڈیشنل ڈائریکٹر-II، انٹیلی ایڈیشنل کمشنر(ان لینڈ دفعہ 21A، 22، 23، (I) ایسے تمام افراد یا افراد کے جنس اینڈ انویسٹی گیشن(IR)، ریونیو) 45، 24، 25، 26، 30، اور طبقات جو ریجنل ٹیکس آفس فیصل آباد کیاں آباد دور میں کاروبار کر |  |
| 1.00 | lines/FBR_0683_p09_L33.png | 9 | O |
| 1.00 | lines/FBR_0683_p08_L35.png | 8 | Q |
| 1.00 | lines/FBR_0683_p06_L29.png | ایڈیشنل ڈائر کیٹر – III، انٹیل ایڈیشنل کمشنر (ان لینڈ دفعہ 21A، 22، 23، ڈائر کیٹر انٹیلی جنس اینڈ انویسٹی جنس اینڈ انویسٹی جنس اینڈ انویسٹی اسلام آباد کی طرف سے جنس اینڈ انویسٹی گیسٹن (IR) ریونیو) 45، 24، 25، 26، 30، اور |  |
| 1.00 | lines/FBR_0683_p05_L19.png | 9 | Q |
| 1.00 | lines/FBR_0683_p05_L06.png | 8 | Q |
| 1.00 | lines/FBR_0683_p02_L32.png | 2 | J |
| 1.00 | lines/FBR_0676_p09_L29.png | -5% | ہو۔ |
| 0.91 | lines/FBR_0683_p04_L29.png | عنات جو پشاور اور ایبٹ آباد کے ریخان میں 30 ، 26 ، 25 ، 26 اور ریبٹ آباد کے ریخان ٹیکس آفسز کی حدود میں کاروبار کررہے ہوں۔ | ل تلن اھری صودیں |
| 0.90 | lines/FBR_0683_p05_L30.png | ایڈ بیشنل ڈائر کیٹر – ہیڈ کوارٹرز، ایڈ بیشنل کمشنر(ان لینڈ دفعہ 21A، 22، 23، ڈائر کیٹر جزل انٹیلی جنس اینڈ انٹیلی جنس اینڈ انویسٹی گیسٹن (IR) اسلام آباد انٹیلی جنس اینڈ انویسٹی گیسٹن (IR) اسلام آباد طرف سے پاکستان کی علاق | وبل اررا کورارووچ مرد ید ک |
