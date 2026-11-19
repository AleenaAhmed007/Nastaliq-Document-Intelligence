# OCR evaluation

Systems: utrnet_large_w400_val_det, utrnet_large_w800_val_det, tesseract_urd-eng_val, tesseract_eng_val, hybrid_utrnet_w400_tesseract_eng_val, hybrid_utrnet_w800_tesseract_eng_val  
Reference: original gold (data/processed/lines.tsv, NOT human-verified)  
Lines scored: 1432 (crops present in every prediction file, minus 0 with an empty reference, minus 5 with a suspect reference (listed at the end))  
Line accounting: 1437 lines in every prediction file = 1432 scored + 0 empty reference + 5 suspect reference (excluded by heuristic, awaiting human correction)  
CER / WER = total edits (S+D+I) / total reference characters / words over all lines (micro); NED = mean of per-line edit / max(len(ref), len(pred)); can exceed 100% when the OCR inserts text  
Normalisation: full (see eval_ocr.py docstring)

### Overall

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| all | utrnet_large_w400_val_det | 1432 | 23.2 | 20.0 | 72.3 | 0.360 | 4.7 |
| all | utrnet_large_w800_val_det | 1432 | 21.3 | 18.8 | 64.7 | 0.353 | 4.5 |
| all | tesseract_urd-eng_val | 1432 | 70.7 | 73.5 | 95.7 | 0.651 | 9.7 |
| all | tesseract_eng_val | 1432 | 89.5 | 95.3 | 99.7 | 0.771 | 10.7 |
| all | hybrid_utrnet_w400_tesseract_eng_val | 1432 | 22.3 | 19.0 | 71.4 | 0.274 | 14.0 |
| all | hybrid_utrnet_w800_tesseract_eng_val | 1432 | 20.4 | 17.7 | 63.8 | 0.265 | 14.0 |

### By split

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val | utrnet_large_w400_val_det | 1432 | 23.2 | 20.0 | 72.3 | 0.360 | 4.7 |
| val | utrnet_large_w800_val_det | 1432 | 21.3 | 18.8 | 64.7 | 0.353 | 4.5 |
| val | tesseract_urd-eng_val | 1432 | 70.7 | 73.5 | 95.7 | 0.651 | 9.7 |
| val | tesseract_eng_val | 1432 | 89.5 | 95.3 | 99.7 | 0.771 | 10.7 |
| val | hybrid_utrnet_w400_tesseract_eng_val | 1432 | 22.3 | 19.0 | 71.4 | 0.274 | 14.0 |
| val | hybrid_utrnet_w800_tesseract_eng_val | 1432 | 20.4 | 17.7 | 63.8 | 0.265 | 14.0 |

### By split x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / photo | utrnet_large_w400_val_det | 813 | 23.7 | 20.4 | 73.3 | 0.342 | 5.4 |
| val / photo | utrnet_large_w800_val_det | 813 | 21.7 | 19.2 | 65.7 | 0.334 | 5.3 |
| val / photo | tesseract_urd-eng_val | 813 | 69.3 | 72.1 | 95.4 | 0.641 | 10.6 |
| val / photo | tesseract_eng_val | 813 | 88.9 | 94.8 | 99.3 | 0.769 | 11.1 |
| val / photo | hybrid_utrnet_w400_tesseract_eng_val | 813 | 22.8 | 19.3 | 72.4 | 0.261 | 15.0 |
| val / photo | hybrid_utrnet_w800_tesseract_eng_val | 813 | 20.7 | 17.9 | 64.6 | 0.251 | 15.0 |
| val / scan | utrnet_large_w400_val_det | 619 | 22.6 | 19.5 | 70.8 | 0.384 | 3.9 |
| val / scan | utrnet_large_w800_val_det | 619 | 20.8 | 18.4 | 63.5 | 0.378 | 3.6 |
| val / scan | tesseract_urd-eng_val | 619 | 72.7 | 75.3 | 96.0 | 0.665 | 8.6 |
| val / scan | tesseract_eng_val | 619 | 90.3 | 95.9 | 100.3 | 0.774 | 10.2 |
| val / scan | hybrid_utrnet_w400_tesseract_eng_val | 619 | 21.8 | 18.4 | 70.0 | 0.291 | 12.8 |
| val / scan | hybrid_utrnet_w800_tesseract_eng_val | 619 | 19.9 | 17.4 | 62.6 | 0.283 | 12.6 |

### By category

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field | utrnet_large_w400_val_det | 105 | 22.9 | 19.8 | 70.9 | 0.333 | 1.0 |
| val / hw_field | utrnet_large_w800_val_det | 105 | 20.4 | 17.9 | 62.9 | 0.320 | 1.9 |
| val / hw_field | tesseract_urd-eng_val | 105 | 63.9 | 66.8 | 95.3 | 0.621 | 5.7 |
| val / hw_field | tesseract_eng_val | 105 | 86.0 | 91.5 | 99.5 | 0.770 | 6.7 |
| val / hw_field | hybrid_utrnet_w400_tesseract_eng_val | 105 | 22.1 | 18.8 | 70.3 | 0.278 | 7.6 |
| val / hw_field | hybrid_utrnet_w800_tesseract_eng_val | 105 | 19.6 | 16.9 | 62.3 | 0.263 | 8.6 |
| val / num_latin | utrnet_large_w400_val_det | 367 | 77.8 | 78.0 | 107.6 | 0.762 | 0.5 |
| val / num_latin | utrnet_large_w800_val_det | 367 | 78.0 | 78.1 | 108.1 | 0.762 | 0.5 |
| val / num_latin | tesseract_urd-eng_val | 367 | 36.4 | 36.1 | 67.1 | 0.458 | 35.4 |
| val / num_latin | tesseract_eng_val | 367 | 26.7 | 26.0 | 61.3 | 0.375 | 39.8 |
| val / num_latin | hybrid_utrnet_w400_tesseract_eng_val | 367 | 47.7 | 46.6 | 78.8 | 0.441 | 34.9 |
| val / num_latin | hybrid_utrnet_w800_tesseract_eng_val | 367 | 45.4 | 44.4 | 76.7 | 0.434 | 35.4 |
| val / urdu | utrnet_large_w400_val_det | 960 | 21.6 | 18.0 | 71.2 | 0.209 | 6.8 |
| val / urdu | utrnet_large_w800_val_det | 960 | 19.7 | 16.8 | 63.5 | 0.200 | 6.4 |
| val / urdu | tesseract_urd-eng_val | 960 | 72.5 | 75.5 | 96.7 | 0.729 | 0.3 |
| val / urdu | tesseract_eng_val | 960 | 91.8 | 98.1 | 101.1 | 0.923 | 0.0 |
| val / urdu | hybrid_utrnet_w400_tesseract_eng_val | 960 | 21.6 | 18.0 | 71.2 | 0.209 | 6.8 |
| val / urdu | hybrid_utrnet_w800_tesseract_eng_val | 960 | 19.7 | 16.8 | 63.5 | 0.200 | 6.4 |

### By content

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val_det | 295 | 75.8 | 74.8 | 108.8 | 0.778 | 0.7 |
| val / digits_only | utrnet_large_w800_val_det | 295 | 76.0 | 75.1 | 109.1 | 0.781 | 0.7 |
| val / digits_only | tesseract_urd-eng_val | 295 | 43.1 | 41.8 | 79.2 | 0.492 | 33.9 |
| val / digits_only | tesseract_eng_val | 295 | 29.6 | 28.1 | 70.0 | 0.397 | 39.3 |
| val / digits_only | hybrid_utrnet_w400_tesseract_eng_val | 295 | 35.4 | 33.4 | 73.6 | 0.409 | 39.3 |
| val / digits_only | hybrid_utrnet_w800_tesseract_eng_val | 295 | 35.6 | 33.8 | 73.0 | 0.411 | 39.3 |
| val / latin_only | utrnet_large_w400_val_det | 92 | 81.0 | 82.5 | 112.3 | 0.699 | 0.0 |
| val / latin_only | utrnet_large_w800_val_det | 92 | 81.1 | 82.5 | 111.0 | 0.693 | 0.0 |
| val / latin_only | tesseract_urd-eng_val | 92 | 25.5 | 25.8 | 48.4 | 0.329 | 39.1 |
| val / latin_only | tesseract_eng_val | 92 | 21.7 | 21.8 | 48.4 | 0.281 | 40.2 |
| val / latin_only | hybrid_utrnet_w400_tesseract_eng_val | 92 | 68.0 | 68.9 | 96.1 | 0.539 | 20.7 |
| val / latin_only | hybrid_utrnet_w800_tesseract_eng_val | 92 | 62.6 | 63.6 | 89.7 | 0.507 | 22.8 |
| val / other | utrnet_large_w400_val_det | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / other | utrnet_large_w800_val_det | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / other | tesseract_urd-eng_val | 3 | 120.0 | 120.0 | 100.0 | 0.833 | 0.0 |
| val / other | tesseract_eng_val | 3 | 140.0 | 140.0 | 100.0 | 1.000 | 0.0 |
| val / other | hybrid_utrnet_w400_tesseract_eng_val | 3 | 140.0 | 140.0 | 100.0 | 1.000 | 0.0 |
| val / other | hybrid_utrnet_w800_tesseract_eng_val | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / urdu+digits | utrnet_large_w400_val_det | 343 | 22.9 | 18.9 | 75.0 | 0.250 | 0.0 |
| val / urdu+digits | utrnet_large_w800_val_det | 343 | 20.4 | 17.5 | 66.1 | 0.235 | 0.0 |
| val / urdu+digits | tesseract_urd-eng_val | 343 | 71.6 | 74.4 | 97.4 | 0.719 | 0.0 |
| val / urdu+digits | tesseract_eng_val | 343 | 91.0 | 97.1 | 100.3 | 0.901 | 0.0 |
| val / urdu+digits | hybrid_utrnet_w400_tesseract_eng_val | 343 | 22.9 | 18.9 | 75.0 | 0.250 | 0.0 |
| val / urdu+digits | hybrid_utrnet_w800_tesseract_eng_val | 343 | 20.4 | 17.5 | 66.1 | 0.235 | 0.0 |
| val / urdu+latin | utrnet_large_w400_val_det | 122 | 27.2 | 24.4 | 74.2 | 0.281 | 0.0 |
| val / urdu+latin | utrnet_large_w800_val_det | 122 | 24.5 | 22.2 | 65.7 | 0.260 | 0.0 |
| val / urdu+latin | tesseract_urd-eng_val | 122 | 67.6 | 71.0 | 94.1 | 0.679 | 0.0 |
| val / urdu+latin | tesseract_eng_val | 122 | 87.7 | 93.9 | 99.3 | 0.869 | 0.0 |
| val / urdu+latin | hybrid_utrnet_w400_tesseract_eng_val | 122 | 27.2 | 24.4 | 74.2 | 0.281 | 0.0 |
| val / urdu+latin | hybrid_utrnet_w800_tesseract_eng_val | 122 | 24.5 | 22.2 | 65.7 | 0.260 | 0.0 |
| val / urdu_only | utrnet_large_w400_val_det | 577 | 18.1 | 14.5 | 66.3 | 0.171 | 11.4 |
| val / urdu_only | utrnet_large_w800_val_det | 577 | 16.8 | 13.9 | 59.8 | 0.167 | 10.9 |
| val / urdu_only | tesseract_urd-eng_val | 577 | 73.7 | 76.8 | 96.8 | 0.737 | 0.5 |
| val / urdu_only | tesseract_eng_val | 577 | 93.4 | 99.9 | 102.2 | 0.942 | 0.0 |
| val / urdu_only | hybrid_utrnet_w400_tesseract_eng_val | 577 | 18.1 | 14.5 | 66.3 | 0.171 | 11.4 |
| val / urdu_only | hybrid_utrnet_w800_tesseract_eng_val | 577 | 16.8 | 13.9 | 59.8 | 0.167 | 10.9 |

### By aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / 12.5-25 | utrnet_large_w400_val_det | 376 | 21.6 | 18.1 | 71.3 | 0.230 | 0.8 |
| val / 12.5-25 | utrnet_large_w800_val_det | 376 | 19.9 | 17.1 | 63.6 | 0.218 | 0.5 |
| val / 12.5-25 | tesseract_urd-eng_val | 376 | 70.9 | 74.0 | 95.4 | 0.674 | 0.8 |
| val / 12.5-25 | tesseract_eng_val | 376 | 90.3 | 96.6 | 100.4 | 0.874 | 0.8 |
| val / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 376 | 21.5 | 17.9 | 71.2 | 0.225 | 1.1 |
| val / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 376 | 19.6 | 16.8 | 63.4 | 0.206 | 1.1 |
| val / <=12.5 | utrnet_large_w400_val_det | 947 | 30.6 | 28.8 | 75.9 | 0.432 | 6.9 |
| val / <=12.5 | utrnet_large_w800_val_det | 947 | 30.5 | 28.8 | 76.0 | 0.432 | 6.7 |
| val / <=12.5 | tesseract_urd-eng_val | 947 | 75.3 | 77.0 | 97.9 | 0.644 | 14.3 |
| val / <=12.5 | tesseract_eng_val | 947 | 88.3 | 91.7 | 98.4 | 0.717 | 15.7 |
| val / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 947 | 27.7 | 25.4 | 72.9 | 0.304 | 20.8 |
| val / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 947 | 27.6 | 25.4 | 72.9 | 0.303 | 20.7 |
| val / >25 | utrnet_large_w400_val_det | 109 | 17.4 | 12.5 | 69.7 | 0.179 | 0.0 |
| val / >25 | utrnet_large_w800_val_det | 109 | 12.7 | 9.3 | 53.5 | 0.134 | 0.0 |
| val / >25 | tesseract_urd-eng_val | 109 | 64.6 | 67.5 | 93.6 | 0.637 | 0.9 |
| val / >25 | tesseract_eng_val | 109 | 89.4 | 97.0 | 99.9 | 0.886 | 0.9 |
| val / >25 | hybrid_utrnet_w400_tesseract_eng_val | 109 | 17.4 | 12.5 | 69.7 | 0.179 | 0.0 |
| val / >25 | hybrid_utrnet_w800_tesseract_eng_val | 109 | 12.7 | 9.3 | 53.5 | 0.134 | 0.0 |

### By category x aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / 12.5-25 | utrnet_large_w400_val_det | 51 | 20.9 | 17.8 | 68.5 | 0.244 | 0.0 |
| val / hw_field / 12.5-25 | utrnet_large_w800_val_det | 51 | 18.7 | 16.1 | 60.7 | 0.224 | 0.0 |
| val / hw_field / 12.5-25 | tesseract_urd-eng_val | 51 | 65.4 | 68.9 | 94.6 | 0.639 | 0.0 |
| val / hw_field / 12.5-25 | tesseract_eng_val | 51 | 87.6 | 93.5 | 99.2 | 0.848 | 0.0 |
| val / hw_field / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 51 | 20.9 | 17.8 | 68.5 | 0.244 | 0.0 |
| val / hw_field / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 51 | 18.7 | 16.1 | 60.7 | 0.224 | 0.0 |
| val / hw_field / <=12.5 | utrnet_large_w400_val_det | 48 | 35.8 | 34.9 | 80.3 | 0.441 | 2.1 |
| val / hw_field / <=12.5 | utrnet_large_w800_val_det | 48 | 35.5 | 35.0 | 78.3 | 0.442 | 4.2 |
| val / hw_field / <=12.5 | tesseract_urd-eng_val | 48 | 65.4 | 65.6 | 102.0 | 0.612 | 12.5 |
| val / hw_field / <=12.5 | tesseract_eng_val | 48 | 76.2 | 78.4 | 102.0 | 0.676 | 14.6 |
| val / hw_field / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 48 | 29.6 | 27.7 | 75.0 | 0.320 | 16.7 |
| val / hw_field / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 48 | 29.1 | 27.7 | 73.0 | 0.317 | 18.8 |
| val / hw_field / >25 | utrnet_large_w400_val_det | 6 | 21.0 | 14.8 | 75.5 | 0.224 | 0.0 |
| val / hw_field / >25 | utrnet_large_w800_val_det | 6 | 15.3 | 9.7 | 62.2 | 0.164 | 0.0 |
| val / hw_field / >25 | tesseract_urd-eng_val | 6 | 54.3 | 56.4 | 93.4 | 0.542 | 0.0 |
| val / hw_field / >25 | tesseract_eng_val | 6 | 86.9 | 94.3 | 99.5 | 0.867 | 0.0 |
| val / hw_field / >25 | hybrid_utrnet_w400_tesseract_eng_val | 6 | 21.0 | 14.8 | 75.5 | 0.224 | 0.0 |
| val / hw_field / >25 | hybrid_utrnet_w800_tesseract_eng_val | 6 | 15.3 | 9.7 | 62.2 | 0.164 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w400_val_det | 10 | 86.3 | 89.5 | 121.6 | 0.848 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w800_val_det | 10 | 88.5 | 90.9 | 121.6 | 0.872 | 0.0 |
| val / num_latin / 12.5-25 | tesseract_urd-eng_val | 10 | 24.9 | 26.9 | 37.8 | 0.254 | 30.0 |
| val / num_latin / 12.5-25 | tesseract_eng_val | 10 | 9.3 | 9.8 | 37.8 | 0.080 | 30.0 |
| val / num_latin / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 10 | 68.7 | 71.3 | 102.7 | 0.624 | 10.0 |
| val / num_latin / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 10 | 55.3 | 57.0 | 83.8 | 0.456 | 20.0 |
| val / num_latin / <=12.5 | utrnet_large_w400_val_det | 356 | 76.1 | 75.9 | 106.2 | 0.759 | 0.6 |
| val / num_latin / <=12.5 | utrnet_large_w800_val_det | 356 | 75.8 | 75.5 | 106.4 | 0.759 | 0.6 |
| val / num_latin / <=12.5 | tesseract_urd-eng_val | 356 | 39.6 | 38.6 | 71.2 | 0.465 | 35.4 |
| val / num_latin / <=12.5 | tesseract_eng_val | 356 | 30.5 | 29.3 | 64.8 | 0.385 | 39.9 |
| val / num_latin / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 356 | 42.7 | 41.4 | 75.8 | 0.435 | 35.7 |
| val / num_latin / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 356 | 42.2 | 40.9 | 75.1 | 0.433 | 36.0 |
| val / num_latin / >25 | utrnet_large_w400_val_det | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / num_latin / >25 | utrnet_large_w800_val_det | 1 | 90.9 | 97.9 | 125.0 | 0.909 | 0.0 |
| val / num_latin / >25 | tesseract_urd-eng_val | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / num_latin / >25 | tesseract_eng_val | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / num_latin / >25 | hybrid_utrnet_w400_tesseract_eng_val | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / num_latin / >25 | hybrid_utrnet_w800_tesseract_eng_val | 1 | 90.9 | 97.9 | 125.0 | 0.909 | 0.0 |
| val / urdu / 12.5-25 | utrnet_large_w400_val_det | 315 | 21.1 | 17.4 | 71.5 | 0.209 | 1.0 |
| val / urdu / 12.5-25 | utrnet_large_w800_val_det | 315 | 19.4 | 16.5 | 63.7 | 0.196 | 0.6 |
| val / urdu / 12.5-25 | tesseract_urd-eng_val | 315 | 72.1 | 75.3 | 95.8 | 0.693 | 0.0 |
| val / urdu / 12.5-25 | tesseract_eng_val | 315 | 91.4 | 98.0 | 101.0 | 0.903 | 0.0 |
| val / urdu / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 315 | 21.1 | 17.4 | 71.5 | 0.209 | 1.0 |
| val / urdu / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 315 | 19.4 | 16.5 | 63.7 | 0.196 | 0.6 |
| val / urdu / <=12.5 | utrnet_large_w400_val_det | 543 | 26.3 | 23.7 | 72.5 | 0.217 | 11.4 |
| val / urdu / <=12.5 | utrnet_large_w800_val_det | 543 | 26.2 | 23.7 | 72.6 | 0.217 | 10.9 |
| val / urdu / <=12.5 | tesseract_urd-eng_val | 543 | 79.0 | 81.5 | 100.6 | 0.765 | 0.6 |
| val / urdu / <=12.5 | tesseract_eng_val | 543 | 94.0 | 98.9 | 101.9 | 0.939 | 0.0 |
| val / urdu / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 543 | 26.3 | 23.7 | 72.5 | 0.217 | 11.4 |
| val / urdu / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 543 | 26.2 | 23.7 | 72.6 | 0.217 | 10.9 |
| val / urdu / >25 | utrnet_large_w400_val_det | 102 | 16.9 | 12.1 | 69.3 | 0.169 | 0.0 |
| val / urdu / >25 | utrnet_large_w800_val_det | 102 | 12.3 | 9.0 | 52.8 | 0.124 | 0.0 |
| val / urdu / >25 | tesseract_urd-eng_val | 102 | 65.4 | 68.4 | 93.8 | 0.649 | 0.0 |
| val / urdu / >25 | tesseract_eng_val | 102 | 89.9 | 97.5 | 100.2 | 0.896 | 0.0 |
| val / urdu / >25 | hybrid_utrnet_w400_tesseract_eng_val | 102 | 16.9 | 12.1 | 69.3 | 0.169 | 0.0 |
| val / urdu / >25 | hybrid_utrnet_w800_tesseract_eng_val | 102 | 12.3 | 9.0 | 52.8 | 0.124 | 0.0 |

### By category x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / photo | utrnet_large_w400_val_det | 56 | 21.2 | 17.6 | 70.3 | 0.279 | 0.0 |
| val / hw_field / photo | utrnet_large_w800_val_det | 56 | 18.7 | 15.8 | 60.9 | 0.262 | 0.0 |
| val / hw_field / photo | tesseract_urd-eng_val | 56 | 63.1 | 66.3 | 95.1 | 0.676 | 0.0 |
| val / hw_field / photo | tesseract_eng_val | 56 | 88.3 | 94.3 | 99.9 | 0.866 | 0.0 |
| val / hw_field / photo | hybrid_utrnet_w400_tesseract_eng_val | 56 | 21.2 | 17.6 | 70.3 | 0.279 | 0.0 |
| val / hw_field / photo | hybrid_utrnet_w800_tesseract_eng_val | 56 | 18.7 | 15.8 | 60.9 | 0.262 | 0.0 |
| val / hw_field / scan | utrnet_large_w400_val_det | 49 | 27.3 | 25.2 | 72.6 | 0.395 | 2.0 |
| val / hw_field / scan | utrnet_large_w800_val_det | 49 | 25.0 | 23.1 | 68.7 | 0.387 | 4.1 |
| val / hw_field / scan | tesseract_urd-eng_val | 49 | 65.9 | 68.0 | 95.9 | 0.558 | 12.2 |
| val / hw_field / scan | tesseract_eng_val | 49 | 79.9 | 84.4 | 98.5 | 0.661 | 14.3 |
| val / hw_field / scan | hybrid_utrnet_w400_tesseract_eng_val | 49 | 24.3 | 21.7 | 70.2 | 0.276 | 16.3 |
| val / hw_field / scan | hybrid_utrnet_w800_tesseract_eng_val | 49 | 22.0 | 19.5 | 66.4 | 0.265 | 18.4 |
| val / num_latin / photo | utrnet_large_w400_val_det | 199 | 76.7 | 77.2 | 107.2 | 0.720 | 1.0 |
| val / num_latin / photo | utrnet_large_w800_val_det | 199 | 76.5 | 77.1 | 107.2 | 0.719 | 1.0 |
| val / num_latin / photo | tesseract_urd-eng_val | 199 | 28.4 | 28.0 | 57.0 | 0.375 | 41.7 |
| val / num_latin / photo | tesseract_eng_val | 199 | 21.9 | 21.4 | 52.2 | 0.318 | 45.2 |
| val / num_latin / photo | hybrid_utrnet_w400_tesseract_eng_val | 199 | 45.7 | 44.9 | 74.3 | 0.390 | 40.2 |
| val / num_latin / photo | hybrid_utrnet_w800_tesseract_eng_val | 199 | 41.9 | 41.4 | 71.5 | 0.379 | 40.7 |
| val / num_latin / scan | utrnet_large_w400_val_det | 168 | 79.9 | 79.5 | 108.1 | 0.810 | 0.0 |
| val / num_latin / scan | utrnet_large_w800_val_det | 168 | 80.7 | 79.9 | 109.2 | 0.814 | 0.0 |
| val / num_latin / scan | tesseract_urd-eng_val | 168 | 50.6 | 50.3 | 80.5 | 0.556 | 28.0 |
| val / num_latin / scan | tesseract_eng_val | 168 | 35.0 | 33.9 | 73.5 | 0.443 | 33.3 |
| val / num_latin / scan | hybrid_utrnet_w400_tesseract_eng_val | 168 | 51.1 | 49.6 | 84.9 | 0.502 | 28.6 |
| val / num_latin / scan | hybrid_utrnet_w800_tesseract_eng_val | 168 | 51.5 | 49.6 | 83.8 | 0.501 | 29.2 |
| val / urdu / photo | utrnet_large_w400_val_det | 558 | 22.2 | 18.5 | 72.6 | 0.213 | 7.5 |
| val / urdu / photo | utrnet_large_w800_val_det | 558 | 20.2 | 17.3 | 64.9 | 0.204 | 7.3 |
| val / urdu / photo | tesseract_urd-eng_val | 558 | 71.6 | 74.7 | 96.8 | 0.733 | 0.5 |
| val / urdu / photo | tesseract_eng_val | 558 | 91.3 | 97.8 | 100.9 | 0.920 | 0.0 |
| val / urdu / photo | hybrid_utrnet_w400_tesseract_eng_val | 558 | 22.2 | 18.5 | 72.6 | 0.213 | 7.5 |
| val / urdu / photo | hybrid_utrnet_w800_tesseract_eng_val | 558 | 20.2 | 17.3 | 64.9 | 0.204 | 7.3 |
| val / urdu / scan | utrnet_large_w400_val_det | 402 | 20.9 | 17.3 | 69.5 | 0.204 | 5.7 |
| val / urdu / scan | utrnet_large_w800_val_det | 402 | 19.0 | 16.2 | 61.7 | 0.195 | 5.0 |
| val / urdu / scan | tesseract_urd-eng_val | 402 | 73.7 | 76.5 | 96.5 | 0.724 | 0.0 |
| val / urdu / scan | tesseract_eng_val | 402 | 92.4 | 98.5 | 101.3 | 0.926 | 0.0 |
| val / urdu / scan | hybrid_utrnet_w400_tesseract_eng_val | 402 | 20.9 | 17.3 | 69.5 | 0.204 | 5.7 |
| val / urdu / scan | hybrid_utrnet_w800_tesseract_eng_val | 402 | 19.0 | 16.2 | 61.7 | 0.195 | 5.0 |

### Error types by content

S / D / I = substitutions / deletions / insertions as % of reference characters (they add up to CER).

| group | system | lines | ref chars | avg ref len | avg pred len | CER % | S % | D % | I % |
|---|---|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val_det | 295 | 1444 | 4.9 | 4.2 | 75.8 | 53.7 | 18.1 | 3.9 |
| val / digits_only | utrnet_large_w800_val_det | 295 | 1444 | 4.9 | 4.2 | 76.0 | 53.4 | 18.6 | 3.9 |
| val / digits_only | tesseract_urd-eng_val | 295 | 1444 | 4.9 | 4.5 | 43.1 | 28.0 | 11.2 | 3.9 |
| val / digits_only | tesseract_eng_val | 295 | 1444 | 4.9 | 4.5 | 29.6 | 16.9 | 10.2 | 2.5 |
| val / digits_only | hybrid_utrnet_w400_tesseract_eng_val | 295 | 1444 | 4.9 | 4.7 | 35.4 | 23.7 | 8.0 | 3.7 |
| val / digits_only | hybrid_utrnet_w800_tesseract_eng_val | 295 | 1444 | 4.9 | 4.6 | 35.6 | 22.9 | 8.9 | 3.7 |
| val / latin_only | utrnet_large_w400_val_det | 92 | 962 | 10.5 | 7.7 | 81.0 | 53.3 | 27.0 | 0.6 |
| val / latin_only | utrnet_large_w800_val_det | 92 | 962 | 10.5 | 7.5 | 81.1 | 50.8 | 29.4 | 0.8 |
| val / latin_only | tesseract_urd-eng_val | 92 | 962 | 10.5 | 9.1 | 25.5 | 10.3 | 13.9 | 1.2 |
| val / latin_only | tesseract_eng_val | 92 | 962 | 10.5 | 9.2 | 21.7 | 8.2 | 12.8 | 0.7 |
| val / latin_only | hybrid_utrnet_w400_tesseract_eng_val | 92 | 962 | 10.5 | 8.2 | 68.0 | 44.9 | 22.1 | 0.9 |
| val / latin_only | hybrid_utrnet_w800_tesseract_eng_val | 92 | 962 | 10.5 | 8.4 | 62.6 | 40.6 | 20.8 | 1.1 |
| val / other | utrnet_large_w400_val_det | 3 | 5 | 1.7 | 1.7 | 120.0 | 80.0 | 20.0 | 20.0 |
| val / other | utrnet_large_w800_val_det | 3 | 5 | 1.7 | 1.7 | 120.0 | 80.0 | 20.0 | 20.0 |
| val / other | tesseract_urd-eng_val | 3 | 5 | 1.7 | 2.0 | 120.0 | 60.0 | 20.0 | 40.0 |
| val / other | tesseract_eng_val | 3 | 5 | 1.7 | 1.7 | 140.0 | 60.0 | 40.0 | 40.0 |
| val / other | hybrid_utrnet_w400_tesseract_eng_val | 3 | 5 | 1.7 | 1.7 | 140.0 | 60.0 | 40.0 | 40.0 |
| val / other | hybrid_utrnet_w800_tesseract_eng_val | 3 | 5 | 1.7 | 1.3 | 120.0 | 60.0 | 40.0 | 20.0 |
| val / urdu+digits | utrnet_large_w400_val_det | 343 | 29793 | 86.9 | 81.2 | 22.9 | 10.8 | 9.3 | 2.8 |
| val / urdu+digits | utrnet_large_w800_val_det | 343 | 29793 | 86.9 | 82.6 | 20.4 | 10.0 | 7.7 | 2.7 |
| val / urdu+digits | tesseract_urd-eng_val | 343 | 29793 | 86.9 | 44.4 | 71.6 | 20.7 | 49.9 | 1.0 |
| val / urdu+digits | tesseract_eng_val | 343 | 29793 | 86.9 | 30.3 | 91.0 | 25.4 | 65.4 | 0.2 |
| val / urdu+digits | hybrid_utrnet_w400_tesseract_eng_val | 343 | 29793 | 86.9 | 81.2 | 22.9 | 10.8 | 9.3 | 2.8 |
| val / urdu+digits | hybrid_utrnet_w800_tesseract_eng_val | 343 | 29793 | 86.9 | 82.6 | 20.4 | 10.0 | 7.7 | 2.7 |
| val / urdu+latin | utrnet_large_w400_val_det | 122 | 13318 | 109.2 | 102.6 | 27.2 | 15.1 | 9.1 | 3.0 |
| val / urdu+latin | utrnet_large_w800_val_det | 122 | 13318 | 109.2 | 103.3 | 24.5 | 13.4 | 8.2 | 2.8 |
| val / urdu+latin | tesseract_urd-eng_val | 122 | 13318 | 109.2 | 66.4 | 67.6 | 24.4 | 41.2 | 2.0 |
| val / urdu+latin | tesseract_eng_val | 122 | 13318 | 109.2 | 45.3 | 87.7 | 28.9 | 58.6 | 0.2 |
| val / urdu+latin | hybrid_utrnet_w400_tesseract_eng_val | 122 | 13318 | 109.2 | 102.6 | 27.2 | 15.1 | 9.1 | 3.0 |
| val / urdu+latin | hybrid_utrnet_w800_tesseract_eng_val | 122 | 13318 | 109.2 | 103.3 | 24.5 | 13.4 | 8.2 | 2.8 |
| val / urdu_only | utrnet_large_w400_val_det | 577 | 34080 | 59.1 | 56.0 | 18.1 | 7.9 | 7.7 | 2.5 |
| val / urdu_only | utrnet_large_w800_val_det | 577 | 34080 | 59.1 | 56.9 | 16.8 | 7.6 | 6.4 | 2.8 |
| val / urdu_only | tesseract_urd-eng_val | 577 | 34080 | 59.1 | 27.8 | 73.7 | 18.9 | 53.9 | 0.9 |
| val / urdu_only | tesseract_eng_val | 577 | 34080 | 59.1 | 18.3 | 93.4 | 23.9 | 69.2 | 0.2 |
| val / urdu_only | hybrid_utrnet_w400_tesseract_eng_val | 577 | 34080 | 59.1 | 56.0 | 18.1 | 7.9 | 7.7 | 2.5 |
| val / urdu_only | hybrid_utrnet_w800_tesseract_eng_val | 577 | 34080 | 59.1 | 56.9 | 16.8 | 7.6 | 6.4 | 2.8 |

### Top character confusions on Urdu lines: utrnet_large_w400_val_det

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3219 |
| ∅ |   | 512 |
| ا | ∅ | 284 |
| م | ∅ | 218 |
| ر | ∅ | 211 |
| ی | ∅ | 203 |
| و | د | 177 |
| ن | ∅ | 149 |
| ل | ∅ | 147 |
| د | ∅ | 125 |
| و | ∅ | 118 |
| ی | پ | 118 |
| / | ا | 118 |
| ∅ | ی | 113 |
| ب | پ | 111 |
| ک | ∅ | 111 |
| - | ۔ | 110 |
| ہ | ∅ | 104 |
|   | ر | 94 |
| ∅ | ا | 94 |

### Top confusions on digit / Latin characters: utrnet_large_w400_val_det

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 118 |
| 0 | ∅ | 118 |
| 1 | ∅ | 81 |
| 2 | ∅ | 70 |
| 2 | 0 | 58 |
| 0 |   | 53 |
| i | ∅ | 42 |
| 2 | 1 | 39 |
| 1 | 2 | 38 |
| 5 | ∅ | 36 |
| 0 | 1 | 31 |
| a | ∅ | 27 |
| 2 |   | 26 |
| 3 | ∅ | 24 |
| 1 | ۔ | 24 |
| 1 | 0 | 23 |
| 9 | ∅ | 23 |
| 0 | 8 | 23 |
| 7 | ∅ | 22 |
| 1 |   | 21 |

### Worst 15 lines: utrnet_large_w400_val_det

| CER | crop | gold | pred |
|---|---|---|---|
| 2.50 | lines/AJK_0429_p01_L26.png | 31 | مورعع |
| 2.00 | lines/AJK_0484_p01_L26.png | ☆ | 77 |
| 2.00 | lines/AJK_0475_p01_L43.png | W | 44 |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | 99 |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | 4۔ |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | 4۔ |
| 2.00 | lines/AJK_0056_p01_L27.png | 3 | 4۔ |
| 1.56 | lines/AJK_0139_p02_L70.png | وسر ک انفار میشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔ | ڈسٹرکٹ انفاریشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔اسٹیشن ڈائریکٹرصاحب انیوزایڈیٹرصاحب آزادکشمیرریڈیومیرپوررتر اڑکھل مظفرآبا د |
| 1.50 | lines/AJK_0448_p01_L24.png | _4 | 7ے۔ |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.30 | lines/AJK_0079_p01_L17.png | ا فار اللہ اللہ اللہ اللہ اللہ اللہ اللہ الل | 4۔ ڈسٹرکٹ انفاریشن آفیسرصاحب میرپور برائے اشاعت بطورخبردرقومی اخبارات۔ |
| 1.14 | lines/AJK_0056_p01_L18.png | 05827-960005-6 | ملہاری00096277.7 1 |
| 1.14 | lines/AJK_0023_p01_L25.png | 01-10-26 2026/ | 22216 مورخہ 26 -ے 2ر |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدد191 1111 |
| 1.07 | lines/AJK_0416_p01_L19.png | 05/01/2022 315 | مورخہ 2212/"ہ/ کھ |

### Top character confusions on Urdu lines: utrnet_large_w800_val_det

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2526 |
| ∅ |   | 603 |
| ا | ∅ | 284 |
| ر | ∅ | 190 |
| ی | ∅ | 182 |
| م | ∅ | 173 |
| ل | ∅ | 136 |
| ن | ∅ | 135 |
| ی | پ | 122 |
| ب | پ | 115 |
| ∅ | ی | 113 |
| د | ∅ | 112 |
| - | ۔ | 109 |
| و | ∅ | 106 |
| و | د | 101 |
| ک | ∅ | 97 |
| د | ڈ | 95 |
| ∅ | م | 95 |
| / | ا | 88 |
| ∅ | س | 86 |

### Top confusions on digit / Latin characters: utrnet_large_w800_val_det

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 122 |
| 0 | ∅ | 118 |
| 2 | ∅ | 83 |
| 1 | ∅ | 71 |
| 2 | 0 | 55 |
| i | ∅ | 51 |
| 2 | 1 | 48 |
| 0 |   | 47 |
| 1 | 2 | 40 |
| 5 | ∅ | 34 |
| 0 | 1 | 31 |
| 0 | 9 | 29 |
| n | ∅ | 26 |
| a | ∅ | 26 |
| 4 | ∅ | 25 |
| 7 | ∅ | 25 |
| e | ∅ | 25 |
| 1 | ۔ | 24 |
| 3 | ∅ | 23 |
| 0 | 8 | 23 |

### Worst 15 lines: utrnet_large_w800_val_det

| CER | crop | gold | pred |
|---|---|---|---|
| 2.50 | lines/AJK_0429_p01_L26.png | 31 | مورعع |
| 2.00 | lines/AJK_0484_p01_L26.png | ☆ | ک7 |
| 2.00 | lines/AJK_0475_p01_L43.png | W | 44 |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | 99 |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | 4۔ |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | 4۔ |
| 2.00 | lines/AJK_0056_p01_L27.png | 3 | 4۔ |
| 1.62 | lines/AJK_0139_p02_L70.png | وسر ک انفار میشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔ | ڈسٹرکٹ انفارمیشن آفیسر صاحب میرپوربغرض اشاعت بطورخبر اسٹیشن ڈائریکٹر صاحب انیوز ایڈیٹر صاحب آزادکشمیرریڈیومیرپوررتر اڑکھلرمظفرآباد۔ |
| 1.50 | lines/AJK_0448_p01_L24.png | _4 | 7ے۔ |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.32 | lines/AJK_0079_p01_L17.png | ا فار اللہ اللہ اللہ اللہ اللہ اللہ اللہ الل | 4۔ ڈسٹرکٹ انفاریشن آفیسرصاحب میر پور برائے اشاعت بطورخبردرقومی اخبارات۔ |
| 1.21 | lines/AJK_0023_p01_L25.png | 01-10-26 2026/ | 22216 مورخہ 26 -ے- 8ر |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدہد191 111 |
| 1.07 | lines/AJK_0416_p01_L19.png | 05/01/2022 315 | مورخہ 2212/"ہ/ کھ |
| 1.00 | lines/AJK_0521_p01_L27.png | رپیل شاف، در رپرائیدین نیکر فری ہمراہ جناب بیکر فری با نیرا بع - ن.پرائیدین بیکر فری ہمراہ جناب بیکر فری المینی کوشنجناب چیئر شن 10 زاد جمول و کشمیر بورد آف اظرمیذیت و میکنداری تعلقی بورد چیر پورمسلم احسام مرکادی تبعی | ے |

### Top character confusions on Urdu lines: tesseract_urd-eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 4921 |
| ا | ∅ | 3578 |
| ی | ∅ | 2900 |
| ر | ∅ | 2679 |
| م | ∅ | 1893 |
| و | ∅ | 1738 |
| ک | ∅ | 1584 |
| ن | ∅ | 1562 |
| ل | ∅ | 1318 |
| ب | ∅ | 1285 |
| د | ∅ | 974 |
| ت | ∅ | 960 |
| ہ | ∅ | 936 |
| س | ∅ | 903 |
| ج | ∅ | 768 |
| ے | ∅ | 604 |
| ئ | ∅ | 457 |
| ف | ∅ | 438 |
| ع | ∅ | 430 |
| ش | ∅ | 417 |

### Top confusions on digit / Latin characters: tesseract_urd-eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 162 |
| 2 | ∅ | 161 |
| 1 | ∅ | 153 |
| 5 | ∅ | 57 |
| 3 | ∅ | 51 |
| i | ∅ | 48 |
| 9 | ∅ | 37 |
| 7 | ∅ | 37 |
| 8 | ∅ | 28 |
| a | ∅ | 27 |
| 6 | ∅ | 24 |
| 4 | ∅ | 24 |
| 1 | 4 | 22 |
| 2 | 0 | 21 |
| 0 |   | 20 |
| e | ∅ | 18 |
| n | ∅ | 18 |
| o | ∅ | 18 |
| 2 |   | 17 |
| P | ∅ | 16 |

### Worst 15 lines: tesseract_urd-eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 3.00 | lines/AJK_0484_p01_L26.png | ☆ | pid |
| 3.00 | lines/AJK_0351_p01_L16.png | 3 | ایس |
| 2.00 | lines/AJK_0475_p01_L43.png | W | ر1 |
| 2.00 | lines/AJK_0448_p01_L37.png | -11 | I / od |
| 2.00 | lines/AJK_0383_p02_L53.png | -7 | Ny J |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | _f |
| 2.00 | lines/AJK_0102_p01_L41.png | -7 | =r J |
| 2.00 | lines/AJK_0056_p01_L27.png | 3 | بے |
| 1.50 | lines/AJK_0478_p01_L22.png | _4 | 0.1 |
| 1.50 | lines/AJK_0478_p01_L20.png | _3 | 1۔_ |
| 1.50 | lines/AJK_0383_p02_L47.png | -4 | =f] |
| 1.50 | lines/AJK_0383_p01_L25.png | _1 | i / |
| 1.50 | lines/AJK_0139_p02_L57.png | -1 | 1۔- |
| 1.50 | lines/AJK_0139_p02_L31.png | -6 | I 6] |
| 1.50 | lines/AJK_0116_p01_L27.png | وب | [—y |

### Top character confusions on Urdu lines: tesseract_eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 6016 |
| ا | ∅ | 5357 |
| ر | ∅ | 3726 |
| ی | ∅ | 3670 |
| م | ∅ | 2465 |
| و | ∅ | 2451 |
| ک | ∅ | 2076 |
| ن | ∅ | 2024 |
| ب | ∅ | 1665 |
| ل | ∅ | 1621 |
| د | ∅ | 1255 |
| ت | ∅ | 1170 |
| س | ∅ | 1161 |
| ہ | ∅ | 1064 |
| ج | ∅ | 998 |
| ے | ∅ | 770 |
| ف | ∅ | 572 |
| ش | ∅ | 547 |
| ح | ∅ | 544 |
| ع | ∅ | 514 |

### Top confusions on digit / Latin characters: tesseract_eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 248 |
| 1 | ∅ | 206 |
| 2 | ∅ | 206 |
| 5 | ∅ | 79 |
| 3 | ∅ | 73 |
| 9 | ∅ | 55 |
| 7 | ∅ | 52 |
| i | ∅ | 52 |
| 4 | ∅ | 45 |
| 6 | ∅ | 37 |
| 8 | ∅ | 33 |
| a | ∅ | 29 |
| n | ∅ | 29 |
| e | ∅ | 27 |
| P | ∅ | 23 |
| t | ∅ | 21 |
| l | ∅ | 20 |
| s | ∅ | 17 |
| o | ∅ | 17 |
| c | ∅ | 15 |

### Worst 15 lines: tesseract_eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 3.00 | lines/AJK_0484_p01_L26.png | ☆ | pid |
| 2.00 | lines/AJK_0484_p01_L19.png | نوت: | : od Gud |
| 2.00 | lines/AJK_0475_p01_L43.png | W | Dy |
| 2.00 | lines/AJK_0448_p01_L37.png | -11 | I / od |
| 2.00 | lines/AJK_0383_p02_L53.png | -7 | Ny J |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | HO |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | lH |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | _f |
| 2.00 | lines/AJK_0102_p01_L41.png | -7 | =r J |
| 1.56 | lines/AJK_0475_p01_L02.png | نوٹیفکیشن | Cutie betnd nd |
| 1.50 | lines/AJK_0383_p02_L47.png | -4 | =f] |
| 1.50 | lines/AJK_0383_p01_L25.png | _1 | i / |
| 1.50 | lines/AJK_0139_p02_L31.png | -6 | I 6] |
| 1.50 | lines/AJK_0116_p01_L27.png | وب | [—y |
| 1.50 | lines/AJK_0106_p01_L11.png | 62 | i 4 |

### Top character confusions on Urdu lines: hybrid_utrnet_w400_tesseract_eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3219 |
| ∅ |   | 512 |
| ا | ∅ | 284 |
| م | ∅ | 218 |
| ر | ∅ | 211 |
| ی | ∅ | 202 |
| و | د | 177 |
| ن | ∅ | 149 |
| ل | ∅ | 147 |
| د | ∅ | 125 |
| و | ∅ | 118 |
| ی | پ | 118 |
| / | ا | 118 |
| ∅ | ی | 113 |
| ب | پ | 111 |
| ک | ∅ | 111 |
| - | ۔ | 110 |
| ہ | ∅ | 104 |
|   | ر | 94 |
| ∅ | ا | 94 |

### Top confusions on digit / Latin characters: hybrid_utrnet_w400_tesseract_eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 93 |
| 0 | ∅ | 75 |
| 1 | ∅ | 63 |
| 2 | ∅ | 55 |
| 0 |   | 50 |
| 2 | 0 | 46 |
| i | ∅ | 36 |
| 2 | 1 | 29 |
| 2 |   | 24 |
| a | ∅ | 24 |
| 1 |   | 22 |
| 1 | 2 | 22 |
| 1 | 0 | 21 |
| 0 | 1 | 20 |
| 0 | - | 18 |
| 3 | ∅ | 18 |
| 5 | ∅ | 18 |
| 7 | ∅ | 17 |
| 5 | 0 | 17 |
| 0 | 6 | 16 |

### Worst 15 lines: hybrid_utrnet_w400_tesseract_eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 3.00 | lines/AJK_0484_p01_L26.png | ☆ | pid |
| 2.50 | lines/AJK_0429_p01_L26.png | 31 | مورعع |
| 2.00 | lines/AJK_0475_p01_L43.png | W | Dy |
| 2.00 | lines/AJK_0448_p01_L37.png | -11 | I / od |
| 2.00 | lines/AJK_0383_p02_L53.png | -7 | Ny J |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | HO |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | lH |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | _f |
| 2.00 | lines/AJK_0102_p01_L41.png | -7 | =r J |
| 1.56 | lines/AJK_0139_p02_L70.png | وسر ک انفار میشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔ | ڈسٹرکٹ انفاریشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔اسٹیشن ڈائریکٹرصاحب انیوزایڈیٹرصاحب آزادکشمیرریڈیومیرپوررتر اڑکھل مظفرآبا د |
| 1.50 | lines/AJK_0448_p01_L24.png | _4 | 7ے۔ |
| 1.50 | lines/AJK_0383_p02_L47.png | -4 | =f] |
| 1.50 | lines/AJK_0383_p01_L25.png | _1 | i / |
| 1.50 | lines/AJK_0139_p02_L31.png | -6 | I 6] |
| 1.50 | lines/AJK_0106_p01_L11.png | 62 | i 4 |

### Top character confusions on Urdu lines: hybrid_utrnet_w800_tesseract_eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2526 |
| ∅ |   | 603 |
| ا | ∅ | 284 |
| ر | ∅ | 190 |
| ی | ∅ | 181 |
| م | ∅ | 173 |
| ل | ∅ | 136 |
| ن | ∅ | 135 |
| ی | پ | 122 |
| ب | پ | 115 |
| ∅ | ی | 113 |
| د | ∅ | 112 |
| - | ۔ | 109 |
| و | ∅ | 106 |
| و | د | 101 |
| ک | ∅ | 97 |
| د | ڈ | 95 |
| ∅ | م | 95 |
| / | ا | 88 |
| ∅ | س | 86 |

### Top confusions on digit / Latin characters: hybrid_utrnet_w800_tesseract_eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 91 |
| 0 | ∅ | 76 |
| 2 | ∅ | 65 |
| 1 | ∅ | 57 |
| 2 | 0 | 47 |
| 0 |   | 44 |
| i | ∅ | 41 |
| 2 | 1 | 37 |
| 1 | 2 | 25 |
| 0 | 1 | 22 |
| e | ∅ | 21 |
| n | ∅ | 21 |
| a | ∅ | 20 |
| 7 | ∅ | 19 |
| 5 | ∅ | 18 |
| 0 | - | 18 |
| w | ∅ | 18 |
| i | ز | 17 |
| 3 | ∅ | 16 |
| 2 |   | 16 |

### Worst 15 lines: hybrid_utrnet_w800_tesseract_eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.50 | lines/AJK_0429_p01_L26.png | 31 | مورعع |
| 2.00 | lines/AJK_0484_p01_L26.png | ☆ | ک7 |
| 2.00 | lines/AJK_0475_p01_L43.png | W | Dy |
| 2.00 | lines/AJK_0448_p01_L37.png | -11 | I / od |
| 2.00 | lines/AJK_0383_p02_L53.png | -7 | Ny J |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | HO |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | lH |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | _f |
| 2.00 | lines/AJK_0102_p01_L41.png | -7 | =r J |
| 1.62 | lines/AJK_0139_p02_L70.png | وسر ک انفار میشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔ | ڈسٹرکٹ انفارمیشن آفیسر صاحب میرپوربغرض اشاعت بطورخبر اسٹیشن ڈائریکٹر صاحب انیوز ایڈیٹر صاحب آزادکشمیرریڈیومیرپوررتر اڑکھلرمظفرآباد۔ |
| 1.50 | lines/AJK_0448_p01_L24.png | _4 | 7ے۔ |
| 1.50 | lines/AJK_0383_p02_L47.png | -4 | =f] |
| 1.50 | lines/AJK_0383_p01_L25.png | _1 | i / |
| 1.50 | lines/AJK_0139_p02_L31.png | -6 | I 6] |
| 1.50 | lines/AJK_0106_p01_L11.png | 62 | i 4 |

### Suspect references (not scored; awaiting human correction)

Flagged by a heuristic (see eval_ocr.py docstring), not proof that each reference is wrong. Each line is scored again once a reviewer confirms or corrects it (--verified), or always with --keep-suspect.

| crop | reason | reference |
|---|---|---|
| lines/AJK_0102_p01_L08.png | CJK / kana characters | でいっというというというには しいかいかんとしないのとはいいい |
| lines/AJK_0102_p01_L51.png | CJK / kana characters | いるからいというなとないいいととないしんなきというというないといいのアフリスタアといると |
| lines/AJK_0429_p01_L08.png | CJK / kana characters | からいというかんな |
| lines/AJK_0429_p01_L09.png | CJK / kana characters | もならうでもかってもっと |
| lines/AJK_0475_p01_L69.png | no letters or digits | ۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔ |
