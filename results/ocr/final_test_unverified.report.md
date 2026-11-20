# OCR evaluation

Systems: utrnet_large_w800_test_det, tesseract_urd-eng_test, tesseract_eng_test, hybrid_final_test  
Reference: original gold (data/processed/lines.tsv, NOT human-verified)  
Lines scored: 2541 (crops present in every prediction file, minus 0 with an empty reference, minus 5 with a suspect reference (listed at the end))  
Line accounting: 2546 lines in every prediction file = 2541 scored + 0 empty reference + 5 suspect reference (excluded by heuristic, awaiting human correction)  
CER / WER = total edits (S+D+I) / total reference characters / words over all lines (micro); NED = mean of per-line edit / max(len(ref), len(pred)); can exceed 100% when the OCR inserts text  
Normalisation: full (see eval_ocr.py docstring)

### Overall

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| all | utrnet_large_w800_test_det | 2541 | 25.6 | 23.8 | 70.6 | 0.343 | 7.9 |
| all | tesseract_urd-eng_test | 2541 | 70.0 | 72.8 | 96.2 | 0.620 | 12.5 |
| all | tesseract_eng_test | 2541 | 87.8 | 93.3 | 98.5 | 0.748 | 13.5 |
| all | hybrid_final_test | 2541 | 23.1 | 21.0 | 68.3 | 0.239 | 19.2 |

### By split

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test | utrnet_large_w800_test_det | 2541 | 25.6 | 23.8 | 70.6 | 0.343 | 7.9 |
| test | tesseract_urd-eng_test | 2541 | 70.0 | 72.8 | 96.2 | 0.620 | 12.5 |
| test | tesseract_eng_test | 2541 | 87.8 | 93.3 | 98.5 | 0.748 | 13.5 |
| test | hybrid_final_test | 2541 | 23.1 | 21.0 | 68.3 | 0.239 | 19.2 |

### By split x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test / photo | utrnet_large_w800_test_det | 1112 | 22.1 | 19.8 | 68.0 | 0.326 | 5.8 |
| test / photo | tesseract_urd-eng_test | 1112 | 70.1 | 73.1 | 97.1 | 0.645 | 8.2 |
| test / photo | tesseract_eng_test | 1112 | 88.3 | 93.8 | 99.9 | 0.773 | 9.7 |
| test / photo | hybrid_final_test | 1112 | 20.3 | 17.8 | 67.0 | 0.245 | 14.1 |
| test / scan | utrnet_large_w800_test_det | 1429 | 28.3 | 26.9 | 72.6 | 0.356 | 9.5 |
| test / scan | tesseract_urd-eng_test | 1429 | 69.9 | 72.5 | 95.4 | 0.601 | 15.9 |
| test / scan | tesseract_eng_test | 1429 | 87.5 | 92.9 | 97.4 | 0.728 | 16.4 |
| test / scan | hybrid_final_test | 1429 | 25.3 | 23.5 | 69.3 | 0.235 | 23.2 |

### By category

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test / hw_field | utrnet_large_w800_test_det | 160 | 19.7 | 17.4 | 62.2 | 0.270 | 6.2 |
| test / hw_field | tesseract_urd-eng_test | 160 | 66.1 | 69.6 | 95.0 | 0.616 | 10.0 |
| test / hw_field | tesseract_eng_test | 160 | 87.1 | 93.1 | 98.7 | 0.758 | 11.2 |
| test / hw_field | hybrid_final_test | 160 | 18.2 | 15.7 | 60.8 | 0.220 | 11.9 |
| test / num_latin | utrnet_large_w800_test_det | 641 | 79.3 | 79.9 | 104.7 | 0.702 | 6.7 |
| test / num_latin | tesseract_urd-eng_test | 641 | 26.4 | 26.4 | 53.6 | 0.336 | 46.2 |
| test / num_latin | tesseract_eng_test | 641 | 19.0 | 19.0 | 49.1 | 0.283 | 50.5 |
| test / num_latin | hybrid_final_test | 641 | 24.5 | 24.6 | 51.6 | 0.304 | 50.2 |
| test / urdu | utrnet_large_w800_test_det | 1740 | 23.6 | 21.4 | 69.9 | 0.217 | 8.5 |
| test / urdu | tesseract_urd-eng_test | 1740 | 72.5 | 75.6 | 98.3 | 0.726 | 0.3 |
| test / urdu | tesseract_eng_test | 1740 | 91.3 | 97.4 | 100.8 | 0.918 | 0.0 |
| test / urdu | hybrid_final_test | 1740 | 23.6 | 21.4 | 69.9 | 0.217 | 8.5 |

### By content

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test / digits_only | utrnet_large_w800_test_det | 517 | 70.0 | 68.7 | 99.5 | 0.667 | 10.1 |
| test / digits_only | tesseract_urd-eng_test | 517 | 29.2 | 28.3 | 63.8 | 0.337 | 48.9 |
| test / digits_only | tesseract_eng_test | 517 | 20.8 | 20.3 | 57.0 | 0.284 | 53.2 |
| test / digits_only | hybrid_final_test | 517 | 24.0 | 23.3 | 58.6 | 0.296 | 53.2 |
| test / latin_only | utrnet_large_w800_test_det | 149 | 89.0 | 92.4 | 112.0 | 0.783 | 0.0 |
| test / latin_only | tesseract_urd-eng_test | 149 | 24.5 | 25.1 | 42.7 | 0.315 | 39.6 |
| test / latin_only | tesseract_eng_test | 149 | 17.4 | 17.7 | 39.1 | 0.241 | 45.0 |
| test / latin_only | hybrid_final_test | 149 | 26.0 | 26.9 | 43.4 | 0.303 | 43.6 |
| test / other | utrnet_large_w800_test_det | 6 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| test / other | tesseract_urd-eng_test | 6 | 112.5 | 112.5 | 100.0 | 1.000 | 0.0 |
| test / other | tesseract_eng_test | 6 | 125.0 | 125.0 | 100.0 | 1.000 | 0.0 |
| test / other | hybrid_final_test | 6 | 125.0 | 125.0 | 100.0 | 1.000 | 0.0 |
| test / urdu+digits | utrnet_large_w800_test_det | 685 | 23.9 | 21.4 | 73.9 | 0.264 | 0.0 |
| test / urdu+digits | tesseract_urd-eng_test | 685 | 70.9 | 74.0 | 98.9 | 0.705 | 0.0 |
| test / urdu+digits | tesseract_eng_test | 685 | 90.4 | 96.8 | 100.5 | 0.888 | 0.0 |
| test / urdu+digits | hybrid_final_test | 685 | 23.9 | 21.4 | 73.9 | 0.262 | 0.0 |
| test / urdu+latin | utrnet_large_w800_test_det | 287 | 29.2 | 27.7 | 73.2 | 0.299 | 0.0 |
| test / urdu+latin | tesseract_urd-eng_test | 287 | 72.3 | 75.9 | 96.6 | 0.713 | 0.0 |
| test / urdu+latin | tesseract_eng_test | 287 | 88.4 | 94.1 | 99.2 | 0.874 | 0.0 |
| test / urdu+latin | hybrid_final_test | 287 | 29.2 | 27.7 | 73.2 | 0.300 | 0.0 |
| test / urdu_only | utrnet_large_w800_test_det | 897 | 17.9 | 15.5 | 60.9 | 0.153 | 16.6 |
| test / urdu_only | tesseract_urd-eng_test | 897 | 73.1 | 76.1 | 98.1 | 0.738 | 0.7 |
| test / urdu_only | tesseract_eng_test | 897 | 93.5 | 99.9 | 102.0 | 0.951 | 0.0 |
| test / urdu_only | hybrid_final_test | 897 | 17.9 | 15.5 | 60.9 | 0.154 | 16.6 |

### By aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test / 12.5-25 | utrnet_large_w800_test_det | 641 | 23.6 | 21.5 | 69.4 | 0.269 | 0.3 |
| test / 12.5-25 | tesseract_urd-eng_test | 641 | 70.8 | 74.0 | 96.0 | 0.661 | 1.9 |
| test / 12.5-25 | tesseract_eng_test | 641 | 89.2 | 95.3 | 99.7 | 0.840 | 2.7 |
| test / 12.5-25 | hybrid_final_test | 641 | 22.2 | 19.9 | 68.3 | 0.218 | 2.8 |
| test / <=12.5 | utrnet_large_w800_test_det | 1726 | 30.8 | 29.3 | 76.3 | 0.380 | 11.5 |
| test / <=12.5 | tesseract_urd-eng_test | 1726 | 73.4 | 74.9 | 98.4 | 0.607 | 17.3 |
| test / <=12.5 | tesseract_eng_test | 1726 | 87.1 | 90.3 | 97.4 | 0.706 | 18.4 |
| test / <=12.5 | hybrid_final_test | 1726 | 27.1 | 25.0 | 72.5 | 0.252 | 26.9 |
| test / >25 | utrnet_large_w800_test_det | 174 | 22.1 | 20.5 | 64.8 | 0.248 | 0.0 |
| test / >25 | tesseract_urd-eng_test | 174 | 62.8 | 66.3 | 93.1 | 0.602 | 4.0 |
| test / >25 | tesseract_eng_test | 174 | 85.7 | 93.4 | 97.1 | 0.823 | 4.0 |
| test / >25 | hybrid_final_test | 174 | 19.4 | 17.4 | 61.9 | 0.189 | 4.0 |

### By category x aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test / hw_field / 12.5-25 | utrnet_large_w800_test_det | 71 | 16.1 | 13.5 | 57.6 | 0.176 | 0.0 |
| test / hw_field / 12.5-25 | tesseract_urd-eng_test | 71 | 67.2 | 71.2 | 95.4 | 0.663 | 0.0 |
| test / hw_field / 12.5-25 | tesseract_eng_test | 71 | 89.4 | 96.2 | 99.8 | 0.887 | 0.0 |
| test / hw_field / 12.5-25 | hybrid_final_test | 71 | 16.1 | 13.5 | 57.6 | 0.176 | 0.0 |
| test / hw_field / <=12.5 | utrnet_large_w800_test_det | 73 | 33.1 | 31.1 | 75.7 | 0.361 | 13.7 |
| test / hw_field / <=12.5 | tesseract_urd-eng_test | 73 | 71.0 | 71.8 | 100.3 | 0.589 | 19.2 |
| test / hw_field / <=12.5 | tesseract_eng_test | 73 | 82.9 | 84.6 | 97.9 | 0.631 | 21.9 |
| test / hw_field / <=12.5 | hybrid_final_test | 73 | 29.1 | 26.8 | 72.2 | 0.276 | 23.3 |
| test / hw_field / >25 | utrnet_large_w800_test_det | 16 | 21.8 | 19.5 | 67.8 | 0.268 | 0.0 |
| test / hw_field / >25 | tesseract_urd-eng_test | 16 | 58.4 | 62.3 | 89.5 | 0.535 | 12.5 |
| test / hw_field / >25 | tesseract_eng_test | 16 | 82.2 | 89.1 | 95.5 | 0.760 | 12.5 |
| test / hw_field / >25 | hybrid_final_test | 16 | 16.9 | 13.9 | 63.0 | 0.162 | 12.5 |
| test / num_latin / 12.5-25 | utrnet_large_w800_test_det | 47 | 88.8 | 92.1 | 115.8 | 0.873 | 0.0 |
| test / num_latin / 12.5-25 | tesseract_urd-eng_test | 47 | 21.6 | 22.1 | 50.8 | 0.215 | 23.4 |
| test / num_latin / 12.5-25 | tesseract_eng_test | 47 | 9.3 | 9.8 | 41.5 | 0.088 | 36.2 |
| test / num_latin / 12.5-25 | hybrid_final_test | 47 | 18.6 | 20.0 | 45.9 | 0.175 | 34.0 |
| test / num_latin / <=12.5 | utrnet_large_w800_test_det | 584 | 74.2 | 73.0 | 101.5 | 0.686 | 7.4 |
| test / num_latin / <=12.5 | tesseract_urd-eng_test | 584 | 33.7 | 32.7 | 63.1 | 0.351 | 47.9 |
| test / num_latin / <=12.5 | tesseract_eng_test | 584 | 26.7 | 25.7 | 59.2 | 0.303 | 51.7 |
| test / num_latin / <=12.5 | hybrid_final_test | 584 | 31.9 | 30.6 | 61.6 | 0.319 | 51.5 |
| test / num_latin / >25 | utrnet_large_w800_test_det | 10 | 85.5 | 92.4 | 105.7 | 0.857 | 0.0 |
| test / num_latin / >25 | tesseract_urd-eng_test | 10 | 1.2 | 1.5 | 5.7 | 0.012 | 50.0 |
| test / num_latin / >25 | tesseract_eng_test | 10 | 1.2 | 1.5 | 5.7 | 0.012 | 50.0 |
| test / num_latin / >25 | hybrid_final_test | 10 | 1.2 | 1.5 | 5.7 | 0.012 | 50.0 |
| test / urdu / 12.5-25 | utrnet_large_w800_test_det | 523 | 23.1 | 20.8 | 70.3 | 0.227 | 0.4 |
| test / urdu / 12.5-25 | tesseract_urd-eng_test | 523 | 72.5 | 75.8 | 96.9 | 0.700 | 0.2 |
| test / urdu / 12.5-25 | tesseract_eng_test | 523 | 91.1 | 97.5 | 100.8 | 0.901 | 0.0 |
| test / urdu / 12.5-25 | hybrid_final_test | 523 | 23.1 | 20.8 | 70.3 | 0.227 | 0.4 |
| test / urdu / <=12.5 | utrnet_large_w800_test_det | 1069 | 26.5 | 24.4 | 73.7 | 0.214 | 13.7 |
| test / urdu / <=12.5 | tesseract_urd-eng_test | 1069 | 77.3 | 79.7 | 102.0 | 0.748 | 0.5 |
| test / urdu / <=12.5 | tesseract_eng_test | 1069 | 93.1 | 97.7 | 101.4 | 0.931 | 0.0 |
| test / urdu / <=12.5 | hybrid_final_test | 1069 | 26.5 | 24.3 | 73.7 | 0.214 | 13.7 |
| test / urdu / >25 | utrnet_large_w800_test_det | 148 | 20.2 | 18.2 | 63.3 | 0.204 | 0.0 |
| test / urdu / >25 | tesseract_urd-eng_test | 148 | 65.2 | 68.8 | 95.8 | 0.649 | 0.0 |
| test / urdu / >25 | tesseract_eng_test | 148 | 88.7 | 96.8 | 99.8 | 0.884 | 0.0 |
| test / urdu / >25 | hybrid_final_test | 148 | 20.2 | 18.2 | 63.3 | 0.204 | 0.0 |

### By category x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| test / hw_field / photo | utrnet_large_w800_test_det | 95 | 17.3 | 14.6 | 61.2 | 0.212 | 9.5 |
| test / hw_field / photo | tesseract_urd-eng_test | 95 | 67.5 | 71.3 | 95.3 | 0.647 | 6.3 |
| test / hw_field / photo | tesseract_eng_test | 95 | 88.7 | 95.1 | 99.3 | 0.792 | 8.4 |
| test / hw_field / photo | hybrid_final_test | 95 | 17.1 | 14.3 | 61.1 | 0.211 | 8.4 |
| test / hw_field / scan | utrnet_large_w800_test_det | 65 | 24.1 | 22.4 | 64.2 | 0.354 | 1.5 |
| test / hw_field / scan | tesseract_urd-eng_test | 65 | 63.6 | 66.7 | 94.5 | 0.572 | 15.4 |
| test / hw_field / scan | tesseract_eng_test | 65 | 84.1 | 89.5 | 97.5 | 0.707 | 15.4 |
| test / hw_field / scan | hybrid_final_test | 65 | 20.2 | 18.0 | 60.1 | 0.234 | 16.9 |
| test / num_latin / photo | utrnet_large_w800_test_det | 241 | 78.9 | 78.6 | 108.0 | 0.744 | 2.1 |
| test / num_latin / photo | tesseract_urd-eng_test | 241 | 38.7 | 37.9 | 79.7 | 0.416 | 34.4 |
| test / num_latin / photo | tesseract_eng_test | 241 | 26.9 | 26.3 | 72.9 | 0.336 | 41.5 |
| test / num_latin / photo | hybrid_final_test | 241 | 33.9 | 33.1 | 77.7 | 0.373 | 40.7 |
| test / num_latin / scan | utrnet_large_w800_test_det | 400 | 79.6 | 80.7 | 102.9 | 0.677 | 9.5 |
| test / num_latin / scan | tesseract_urd-eng_test | 400 | 18.3 | 18.8 | 38.8 | 0.288 | 53.2 |
| test / num_latin / scan | tesseract_eng_test | 400 | 13.9 | 14.2 | 35.7 | 0.251 | 56.0 |
| test / num_latin / scan | hybrid_final_test | 400 | 18.4 | 19.0 | 36.8 | 0.262 | 56.0 |
| test / urdu / photo | utrnet_large_w800_test_det | 776 | 20.3 | 17.6 | 67.6 | 0.211 | 6.6 |
| test / urdu / photo | tesseract_urd-eng_test | 776 | 72.0 | 75.2 | 98.1 | 0.716 | 0.3 |
| test / urdu / photo | tesseract_eng_test | 776 | 91.0 | 97.2 | 101.0 | 0.906 | 0.0 |
| test / urdu / photo | hybrid_final_test | 776 | 20.2 | 17.6 | 67.6 | 0.209 | 6.6 |
| test / urdu / scan | utrnet_large_w800_test_det | 964 | 26.0 | 24.2 | 71.6 | 0.222 | 10.1 |
| test / urdu / scan | tesseract_urd-eng_test | 964 | 72.9 | 75.9 | 98.4 | 0.733 | 0.4 |
| test / urdu / scan | tesseract_eng_test | 964 | 91.4 | 97.6 | 100.6 | 0.928 | 0.0 |
| test / urdu / scan | hybrid_final_test | 964 | 26.0 | 24.2 | 71.5 | 0.224 | 10.1 |

### Error types by content

S / D / I = substitutions / deletions / insertions as % of reference characters (they add up to CER).

| group | system | lines | ref chars | avg ref len | avg pred len | CER % | S % | D % | I % |
|---|---|---|---|---|---|---|---|---|---|
| test / digits_only | utrnet_large_w800_test_det | 517 | 2846 | 5.5 | 4.8 | 70.0 | 51.4 | 15.6 | 3.0 |
| test / digits_only | tesseract_urd-eng_test | 517 | 2846 | 5.5 | 5.1 | 29.2 | 15.7 | 10.6 | 2.8 |
| test / digits_only | tesseract_eng_test | 517 | 2846 | 5.5 | 5.1 | 20.8 | 10.4 | 8.5 | 1.9 |
| test / digits_only | hybrid_final_test | 517 | 2846 | 5.5 | 5.2 | 24.0 | 14.1 | 7.3 | 2.6 |
| test / latin_only | utrnet_large_w800_test_det | 149 | 2991 | 20.1 | 14.1 | 89.0 | 53.4 | 32.8 | 2.9 |
| test / latin_only | tesseract_urd-eng_test | 149 | 2991 | 20.1 | 17.9 | 24.5 | 10.6 | 12.3 | 1.5 |
| test / latin_only | tesseract_eng_test | 149 | 2991 | 20.1 | 17.9 | 17.4 | 5.1 | 11.5 | 0.8 |
| test / latin_only | hybrid_final_test | 149 | 2991 | 20.1 | 18.4 | 26.0 | 11.9 | 11.3 | 2.8 |
| test / other | utrnet_large_w800_test_det | 6 | 8 | 1.3 | 1.3 | 100.0 | 100.0 | 0.0 | 0.0 |
| test / other | tesseract_urd-eng_test | 6 | 8 | 1.3 | 1.3 | 112.5 | 87.5 | 12.5 | 12.5 |
| test / other | tesseract_eng_test | 6 | 8 | 1.3 | 1.7 | 125.0 | 100.0 | 0.0 | 25.0 |
| test / other | hybrid_final_test | 6 | 8 | 1.3 | 1.7 | 125.0 | 100.0 | 0.0 | 25.0 |
| test / urdu+digits | utrnet_large_w800_test_det | 685 | 50279 | 73.4 | 72.5 | 23.9 | 13.0 | 6.1 | 4.8 |
| test / urdu+digits | tesseract_urd-eng_test | 685 | 50279 | 73.4 | 40.4 | 70.9 | 23.0 | 46.5 | 1.5 |
| test / urdu+digits | tesseract_eng_test | 685 | 50279 | 73.4 | 27.5 | 90.4 | 27.1 | 63.0 | 0.4 |
| test / urdu+digits | hybrid_final_test | 685 | 50279 | 73.4 | 72.5 | 23.9 | 13.0 | 6.1 | 4.8 |
| test / urdu+latin | utrnet_large_w800_test_det | 287 | 30211 | 105.3 | 100.1 | 29.2 | 17.1 | 8.5 | 3.6 |
| test / urdu+latin | tesseract_urd-eng_test | 287 | 30211 | 105.3 | 57.5 | 72.3 | 24.6 | 46.5 | 1.2 |
| test / urdu+latin | tesseract_eng_test | 287 | 30211 | 105.3 | 41.0 | 88.4 | 26.8 | 61.3 | 0.3 |
| test / urdu+latin | hybrid_final_test | 287 | 30211 | 105.3 | 100.1 | 29.2 | 17.1 | 8.5 | 3.6 |
| test / urdu_only | utrnet_large_w800_test_det | 897 | 44396 | 49.5 | 48.5 | 17.9 | 8.7 | 5.6 | 3.6 |
| test / urdu_only | tesseract_urd-eng_test | 897 | 44396 | 49.5 | 24.2 | 73.1 | 20.3 | 51.9 | 0.9 |
| test / urdu_only | tesseract_eng_test | 897 | 44396 | 49.5 | 15.6 | 93.5 | 24.8 | 68.6 | 0.1 |
| test / urdu_only | hybrid_final_test | 897 | 44396 | 49.5 | 48.5 | 17.9 | 8.7 | 5.6 | 3.6 |

### Top character confusions on Urdu lines: utrnet_large_w800_test_det

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3439 |
| ∅ |   | 1256 |
| ا | ∅ | 432 |
| م | ∅ | 379 |
| - | ۔ | 314 |
| و | د | 312 |
| ی | پ | 277 |
| ل | ∅ | 268 |
| ∅ | ی | 257 |
| ∅ | س | 257 |
| ∅ | ن | 253 |
| / | ا | 251 |
| ∅ | ہ | 247 |
| ∅ | م | 241 |
| ث | ٹ | 238 |
| ب | ہ | 230 |
| ب | پ | 226 |
| ر | ∅ | 192 |
| _ | ۔ | 189 |
| د | ڈ | 188 |

### Top confusions on digit / Latin characters: utrnet_large_w800_test_det

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 239 |
| 0 | 2 | 206 |
| 2 | ∅ | 158 |
| a | ∅ | 109 |
| 2 | 1 | 109 |
| 1 | ∅ | 109 |
| 1 | 2 | 105 |
| e | ∅ | 92 |
| 0 |   | 89 |
| 2 | 0 | 81 |
| n | ∅ | 81 |
| i | ∅ | 78 |
| 0 | 1 | 67 |
| 5 | ∅ | 63 |
| S | ∅ | 62 |
| s | ∅ | 59 |
| C | ∅ | 59 |
| r | ∅ | 54 |
| 6 | ∅ | 54 |
| 0 | 3 | 52 |

### Worst 15 lines: utrnet_large_w800_test_det

| CER | crop | gold | pred |
|---|---|---|---|
| 4.91 | lines/AJK_0187_p01_L15.png | 2_دو گنافیر | 2 دوگنافیس 2214- 11- 31 تا421-وں-3 (ریگوکراپرائیویٹ امیدواران) |
| 2.43 | lines/AJK_0274_p01_L90.png | Scanned with CamScanner | (چاری پرسوفبری ے۔چادنےتعدارعرف 55اسیدوارمان ول نےبععوں ےکو |
| 2.00 | lines/AJK_0134_p01_L13.png | 5 | نہ |
| 2.00 | lines/AJK_0028_p01_L21.png | 2 | ہا |
| 1.50 | lines/AJK_0323_p01_L15.png | -6 | گا۔ |
| 1.44 | lines/AJK_0066_p01_L16.png | 16/26(26) | د 25 وقاص احم |
| 1.38 | lines/AJK_0038_p01_L17.png | 31.08.2026 تک | 22200 216 تا2220..1.16 تک |
| 1.23 | lines/AJK_0189_p01_L07.png | 12-07-2024 81 | تاریخ ہادھ ر۔72-7 |
| 1.21 | lines/AJK_0028_p01_L24.png | W 05827-960004 | پار 10 0094- NA6 87 م |
| 1.18 | lines/AJK_0247_p02_L21.png | 15-11-2023 13686-13776 | رڈکرتاتوی ت71تا221 222 -اا 1/ |
| 1.12 | lines/AJK_0005_p01_L45.png | 30 IN 26 | 26 مورجہ 30 |
| 1.11 | lines/AJK_0274_p01_L84.png | - Joe 2001- 2000 ve 20001- 20001- 20001- 2000 | میں تہدیلی گردپ لیس میلغ30000 روپے کل فیس میلغ۔ا9000ددپے ہوگی۔ |
| 1.10 | lines/AJK_0013_p01_L02.png | 13/10/2026 me 2026/2000 TRAPIE | نمبربورڈااتزا 277 2ہ 2211 مورحہ 440 32 |
| 1.00 | lines/AJK_0401_p02_L34.png | Copy to: | :50 267) |
| 1.00 | lines/AJK_0401_p02_L30.png | Office: | ھ880 |

### Top character confusions on Urdu lines: tesseract_urd-eng_test

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 7253 |
| ا | ∅ | 5575 |
| ی | ∅ | 4564 |
| ر | ∅ | 4100 |
| م | ∅ | 3178 |
| و | ∅ | 2660 |
| ن | ∅ | 2243 |
| ک | ∅ | 2239 |
| ب | ∅ | 2110 |
| ل | ∅ | 1975 |
| د | ∅ | 1537 |
| س | ∅ | 1414 |
| ت | ∅ | 1408 |
| ہ | ∅ | 1201 |
| ج | ∅ | 938 |
| ف | ∅ | 874 |
| ے | ∅ | 745 |
| ع | ∅ | 741 |
| پ | ∅ | 661 |
| ش | ∅ | 633 |

### Top confusions on digit / Latin characters: tesseract_urd-eng_test

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 1 | ∅ | 298 |
| 0 | ∅ | 294 |
| 2 | ∅ | 292 |
| 5 | ∅ | 114 |
| 6 | ∅ | 98 |
| e | ∅ | 92 |
| 3 | ∅ | 85 |
| i | ∅ | 77 |
| a | ∅ | 75 |
| n | ∅ | 68 |
| s | ∅ | 66 |
| 9 | ∅ | 61 |
| 7 | ∅ | 59 |
| 4 | ∅ | 58 |
| 8 | ∅ | 52 |
| t | ∅ | 49 |
| l | ∅ | 48 |
| r | ∅ | 48 |
| O | ∅ | 44 |
| 1 | 4 | 41 |

### Worst 15 lines: tesseract_urd-eng_test

| CER | crop | gold | pred |
|---|---|---|---|
| 4.55 | lines/AJK_0187_p01_L15.png | 2_دو گنافیر | 03-09-2024t31-08-2024 S22) (ر یوار ابرائیو یٹ امیدواران) |
| 3.00 | lines/AJK_0028_p01_L21.png | 2 | / 4 |
| 2.33 | lines/AJK_0075_p01_L28.png | روپ | بلاسیںے |
| 2.25 | lines/AJK_0330_p01_L14.png | 146- | ۔- ئل 17 / |
| 2.00 | lines/AJK_0330_p01_L42.png | £ | Vd |
| 2.00 | lines/AJK_0329_p01_L22.png | _4 | a. / |
| 2.00 | lines/AJK_0075_p01_L109.png | 0 | ©) |
| 2.00 | lines/AJK_0070_p01_L01.png | 1 | جم |
| 2.00 | lines/AJK_0049_p01_L07.png | 0 | جم |
| 2.00 | lines/AJK_0002_p01_L25.png | 3 | تہ |
| 1.67 | lines/AJK_0075_p01_L67.png | روپ | ارؤمیں |
| 1.57 | lines/AJK_0049_p02_L54.png | سیدریری | سنئنل ئل © ( |
| 1.50 | lines/AJK_0330_p01_L19.png | -1 | = / |
| 1.50 | lines/AJK_0329_p01_L28.png | -7 | 2۔- |
| 1.50 | lines/AJK_0323_p01_L43.png | -9 | 9۔_ |

### Top character confusions on Urdu lines: tesseract_eng_test

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 9288 |
| ا | ∅ | 8463 |
| ر | ∅ | 5752 |
| ی | ∅ | 5698 |
| م | ∅ | 4062 |
| و | ∅ | 3793 |
| ک | ∅ | 3186 |
| ن | ∅ | 3043 |
| ب | ∅ | 2692 |
| ل | ∅ | 2582 |
| د | ∅ | 2037 |
| س | ∅ | 1755 |
| ت | ∅ | 1732 |
| ہ | ∅ | 1413 |
| ج | ∅ | 1302 |
| ف | ∅ | 1155 |
| ے | ∅ | 954 |
| ش | ∅ | 883 |
| ع | ∅ | 877 |
| پ | ∅ | 804 |

### Top confusions on digit / Latin characters: tesseract_eng_test

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 390 |
| 2 | ∅ | 380 |
| 1 | ∅ | 360 |
| 5 | ∅ | 158 |
| 3 | ∅ | 145 |
| 6 | ∅ | 137 |
| e | ∅ | 124 |
| i | ∅ | 99 |
| 7 | ∅ | 99 |
| 4 | ∅ | 94 |
| 9 | ∅ | 84 |
| 8 | ∅ | 83 |
| n | ∅ | 80 |
| a | ∅ | 76 |
| s | ∅ | 74 |
| l | ∅ | 66 |
| t | ∅ | 62 |
| r | ∅ | 52 |
| P | ∅ | 47 |
| o | ∅ | 47 |

### Worst 15 lines: tesseract_eng_test

| CER | crop | gold | pred |
|---|---|---|---|
| 4.00 | lines/AJK_0003_p01_L01.png | 2 | py A |
| 3.55 | lines/AJK_0187_p01_L15.png | 2_دو گنافیر | (tsar fiyl A) 03-09-2024t31-08-2024 S22) |
| 3.00 | lines/AJK_0075_p01_L01.png | 0 | Fos |
| 3.00 | lines/AJK_0072_p01_L19.png | 3 | ied |
| 3.00 | lines/AJK_0013_p01_L21.png | 3 | i 1 |
| 2.00 | lines/AJK_0330_p01_L42.png | £ | Vd |
| 2.00 | lines/AJK_0329_p01_L22.png | _4 | a. / |
| 2.00 | lines/AJK_0247_p01_L66.png | روپ | rt 3.1 |
| 2.00 | lines/AJK_0133_p01_L12.png | Φ | [© |
| 2.00 | lines/AJK_0075_p01_L109.png | 0 | ©) |
| 2.00 | lines/AJK_0070_p01_L01.png | 1 | (r |
| 2.00 | lines/AJK_0049_p02_L54.png | سیدریری | ( © id wiadill |
| 2.00 | lines/AJK_0002_p01_L25.png | 3 | ~N |
| 1.67 | lines/AJK_0049_p02_L75.png | -11 | ~ § / |
| 1.50 | lines/AJK_0330_p01_L19.png | -1 | = / |

### Top character confusions on Urdu lines: hybrid_final_test

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3445 |
| ∅ |   | 1257 |
| ا | ∅ | 435 |
| م | ∅ | 379 |
| - | ۔ | 314 |
| و | د | 312 |
| ی | پ | 277 |
| ل | ∅ | 268 |
| ∅ | ی | 257 |
| ∅ | س | 256 |
| ∅ | ن | 253 |
| / | ا | 251 |
| ∅ | ہ | 246 |
| ∅ | م | 241 |
| ث | ٹ | 238 |
| ب | ہ | 230 |
| ب | پ | 226 |
| ر | ∅ | 192 |
| _ | ۔ | 188 |
| د | ڈ | 188 |

### Top confusions on digit / Latin characters: hybrid_final_test

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 166 |
| 0 | ∅ | 144 |
| 2 | ∅ | 105 |
| 1 | ∅ | 77 |
| 2 | 1 | 72 |
| 0 |   | 66 |
| e | ∅ | 60 |
| a | ∅ | 52 |
| 1 | 2 | 51 |
| 2 | 0 | 48 |
| s | ∅ | 47 |
| n | ∅ | 45 |
| i | ∅ | 44 |
| r | ∅ | 42 |
| O | ∅ | 41 |
| 0 | 1 | 39 |
| 6 | ∅ | 36 |
| 5 | ∅ | 36 |
| 0 | - | 36 |
| 1 | 6 | 35 |

### Worst 15 lines: hybrid_final_test

| CER | crop | gold | pred |
|---|---|---|---|
| 4.91 | lines/AJK_0187_p01_L15.png | 2_دو گنافیر | 2 دوگنافیس 2214- 11- 31 تا421-وں-3 (ریگوکراپرائیویٹ امیدواران) |
| 4.00 | lines/AJK_0003_p01_L01.png | 2 | py A |
| 3.00 | lines/AJK_0072_p01_L19.png | 3 | ied |
| 3.00 | lines/AJK_0013_p01_L21.png | 3 | i 1 |
| 2.43 | lines/AJK_0274_p01_L90.png | Scanned with CamScanner | (چاری پرسوفبری ے۔چادنےتعدارعرف 55اسیدوارمان ول نےبععوں ےکو |
| 2.00 | lines/AJK_0330_p01_L42.png | £ | Vd |
| 2.00 | lines/AJK_0329_p01_L22.png | _4 | a. / |
| 2.00 | lines/AJK_0134_p01_L13.png | 5 | نہ |
| 2.00 | lines/AJK_0133_p01_L12.png | Φ | [© |
| 2.00 | lines/AJK_0075_p01_L109.png | 0 | ©) |
| 2.00 | lines/AJK_0070_p01_L01.png | 1 | (r |
| 2.00 | lines/AJK_0028_p01_L21.png | 2 | ہا |
| 2.00 | lines/AJK_0002_p01_L25.png | 3 | ~N |
| 1.67 | lines/AJK_0049_p02_L75.png | -11 | ~ § / |
| 1.50 | lines/AJK_0330_p01_L19.png | -1 | = / |

### Suspect references (not scored; awaiting human correction)

Flagged by a heuristic (see eval_ocr.py docstring), not proof that each reference is wrong. Each line is scored again once a reviewer confirms or corrects it (--verified), or always with --keep-suspect.

| crop | reason | reference |
|---|---|---|
| lines/AJK_0030_p01_L11.png | CJK / kana characters | そんないでもしいできない |
| lines/AJK_0187_p01_L09.png | CJK / kana characters | そっせいさて |
| lines/AJK_0274_p01_L09.png | CJK / kana characters | なんしょうでとしょう |
| lines/AJK_0274_p01_L10.png | CJK / kana characters | からんとしてかんなん |
| lines/AJK_0322_p01_L06.png | CJK / kana characters | もた |
