# OCR evaluation

Systems: utrnet_large_w400_val_det, utrnet_large_w800_val_det, tesseract_urd-eng_val, tesseract_eng_val, hybrid_utrnet_w400_tesseract_eng_val, hybrid_utrnet_w800_tesseract_eng_val, hybrid_final_val, original_gold  
Reference: human-verified text (data/annotations/verified_lines.tsv): 1067 usable lines, 27 excluded/illegible  
Lines scored: 1067 (crops present in every prediction file, minus 0 with an empty reference)  
Line accounting: 1067 lines in every prediction file = 1067 scored + 0 empty reference + 0 suspect reference (excluded by heuristic, awaiting human correction)  
CER / WER = total edits (S+D+I) / total reference characters / words over all lines (micro); NED = mean of per-line edit / max(len(ref), len(pred)); can exceed 100% when the OCR inserts text  
Normalisation: full (see eval_ocr.py docstring)

### Review coverage (every line of the split is accounted for)

| split | lines | gold_ok | utrnet_ok | corrected | exclude | illegible | conflict | unreviewed | scored here |
|---|---|---|---|---|---|---|---|---|---|
| val | 1437 | 172 | 74 | 821 | 7 | 5 | 15 | 343 | 1067 |

`original_gold` row = the original annotation scored against the verified text (annotation error rate, Evaluation A). Other rows = OCR error rate (Evaluation B).

### Overall

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| all | utrnet_large_w400_val_det | 1067 | 17.7 | 13.5 | 64.5 | 0.242 | 13.7 |
| all | utrnet_large_w800_val_det | 1067 | 15.2 | 11.8 | 54.5 | 0.233 | 13.6 |
| all | tesseract_urd-eng_val | 1067 | 70.6 | 73.3 | 95.6 | 0.665 | 7.8 |
| all | tesseract_eng_val | 1067 | 89.9 | 95.6 | 100.0 | 0.805 | 8.0 |
| all | hybrid_utrnet_w400_tesseract_eng_val | 1067 | 17.3 | 12.9 | 64.1 | 0.246 | 17.4 |
| all | hybrid_utrnet_w800_tesseract_eng_val | 1067 | 14.8 | 11.3 | 54.1 | 0.235 | 17.4 |
| all | hybrid_final_val | 1067 | 14.5 | 11.0 | 53.8 | 0.230 | 18.1 |
| all | original_gold | 1067 | 16.2 | 14.0 | 52.4 | 0.245 | 19.6 |

### By split

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val | utrnet_large_w400_val_det | 1067 | 17.7 | 13.5 | 64.5 | 0.242 | 13.7 |
| val | utrnet_large_w800_val_det | 1067 | 15.2 | 11.8 | 54.5 | 0.233 | 13.6 |
| val | tesseract_urd-eng_val | 1067 | 70.6 | 73.3 | 95.6 | 0.665 | 7.8 |
| val | tesseract_eng_val | 1067 | 89.9 | 95.6 | 100.0 | 0.805 | 8.0 |
| val | hybrid_utrnet_w400_tesseract_eng_val | 1067 | 17.3 | 12.9 | 64.1 | 0.246 | 17.4 |
| val | hybrid_utrnet_w800_tesseract_eng_val | 1067 | 14.8 | 11.3 | 54.1 | 0.235 | 17.4 |
| val | hybrid_final_val | 1067 | 14.5 | 11.0 | 53.8 | 0.230 | 18.1 |
| val | original_gold | 1067 | 16.2 | 14.0 | 52.4 | 0.245 | 19.6 |

### By split x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / photo | utrnet_large_w400_val_det | 711 | 17.5 | 13.0 | 65.8 | 0.229 | 14.5 |
| val / photo | utrnet_large_w800_val_det | 711 | 14.8 | 11.2 | 55.2 | 0.219 | 14.6 |
| val / photo | tesseract_urd-eng_val | 711 | 69.5 | 72.3 | 95.2 | 0.652 | 9.6 |
| val / photo | tesseract_eng_val | 711 | 89.6 | 95.4 | 99.6 | 0.794 | 9.6 |
| val / photo | hybrid_utrnet_w400_tesseract_eng_val | 711 | 17.1 | 12.5 | 65.3 | 0.222 | 19.8 |
| val / photo | hybrid_utrnet_w800_tesseract_eng_val | 711 | 14.3 | 10.6 | 54.7 | 0.210 | 20.0 |
| val / photo | hybrid_final_val | 711 | 14.0 | 10.3 | 54.5 | 0.204 | 20.5 |
| val / photo | original_gold | 711 | 15.9 | 13.6 | 51.7 | 0.224 | 21.4 |
| val / scan | utrnet_large_w400_val_det | 356 | 18.2 | 14.5 | 61.5 | 0.268 | 12.1 |
| val / scan | utrnet_large_w800_val_det | 356 | 16.1 | 13.3 | 52.7 | 0.262 | 11.5 |
| val / scan | tesseract_urd-eng_val | 356 | 73.0 | 75.4 | 96.7 | 0.693 | 4.2 |
| val / scan | tesseract_eng_val | 356 | 90.7 | 96.1 | 100.8 | 0.828 | 4.8 |
| val / scan | hybrid_utrnet_w400_tesseract_eng_val | 356 | 17.7 | 14.0 | 61.5 | 0.294 | 12.6 |
| val / scan | hybrid_utrnet_w800_tesseract_eng_val | 356 | 15.7 | 12.8 | 52.6 | 0.286 | 12.4 |
| val / scan | hybrid_final_val | 356 | 15.6 | 12.6 | 52.4 | 0.281 | 13.2 |
| val / scan | original_gold | 356 | 17.0 | 14.7 | 54.1 | 0.288 | 16.0 |

### By category

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field | utrnet_large_w400_val_det | 67 | 18.6 | 15.0 | 64.0 | 0.260 | 6.0 |
| val / hw_field | utrnet_large_w800_val_det | 67 | 16.2 | 13.3 | 53.2 | 0.246 | 6.0 |
| val / hw_field | tesseract_urd-eng_val | 67 | 60.8 | 63.2 | 93.7 | 0.621 | 3.0 |
| val / hw_field | tesseract_eng_val | 67 | 86.1 | 91.6 | 99.2 | 0.812 | 4.5 |
| val / hw_field | hybrid_utrnet_w400_tesseract_eng_val | 67 | 18.2 | 14.6 | 63.8 | 0.249 | 9.0 |
| val / hw_field | hybrid_utrnet_w800_tesseract_eng_val | 67 | 15.7 | 12.8 | 53.0 | 0.234 | 9.0 |
| val / hw_field | hybrid_final_val | 67 | 15.7 | 12.8 | 53.0 | 0.234 | 9.0 |
| val / hw_field | original_gold | 67 | 11.8 | 10.4 | 39.8 | 0.156 | 16.4 |
| val / num_latin | utrnet_large_w400_val_det | 260 | 66.0 | 65.4 | 98.3 | 0.501 | 12.3 |
| val / num_latin | utrnet_large_w800_val_det | 260 | 66.0 | 65.4 | 97.6 | 0.500 | 12.3 |
| val / num_latin | tesseract_urd-eng_val | 260 | 38.4 | 38.5 | 68.8 | 0.502 | 29.6 |
| val / num_latin | tesseract_eng_val | 260 | 32.4 | 32.0 | 68.1 | 0.480 | 31.5 |
| val / num_latin | hybrid_utrnet_w400_tesseract_eng_val | 260 | 51.2 | 49.8 | 86.1 | 0.524 | 26.9 |
| val / num_latin | hybrid_utrnet_w800_tesseract_eng_val | 260 | 49.4 | 48.2 | 83.7 | 0.518 | 27.3 |
| val / num_latin | hybrid_final_val | 260 | 39.4 | 38.6 | 73.6 | 0.495 | 30.4 |
| val / num_latin | original_gold | 260 | 22.1 | 22.1 | 49.7 | 0.448 | 48.5 |
| val / urdu | utrnet_large_w400_val_det | 740 | 16.4 | 11.8 | 63.5 | 0.150 | 14.9 |
| val / urdu | utrnet_large_w800_val_det | 740 | 13.8 | 10.1 | 53.3 | 0.138 | 14.7 |
| val / urdu | tesseract_urd-eng_val | 740 | 72.4 | 75.3 | 96.6 | 0.727 | 0.5 |
| val / urdu | tesseract_eng_val | 740 | 91.7 | 98.0 | 101.0 | 0.919 | 0.0 |
| val / urdu | hybrid_utrnet_w400_tesseract_eng_val | 740 | 16.3 | 11.7 | 63.5 | 0.148 | 14.9 |
| val / urdu | hybrid_utrnet_w800_tesseract_eng_val | 740 | 13.8 | 10.0 | 53.3 | 0.136 | 14.7 |
| val / urdu | hybrid_final_val | 740 | 13.7 | 10.0 | 53.3 | 0.136 | 14.6 |
| val / urdu | original_gold | 740 | 16.5 | 14.1 | 53.8 | 0.182 | 9.7 |

### By content

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val_det | 218 | 59.9 | 58.7 | 95.0 | 0.473 | 15.1 |
| val / digits_only | utrnet_large_w800_val_det | 218 | 59.9 | 58.8 | 94.5 | 0.474 | 15.1 |
| val / digits_only | tesseract_urd-eng_val | 218 | 44.0 | 43.3 | 79.1 | 0.549 | 26.1 |
| val / digits_only | tesseract_eng_val | 218 | 37.5 | 36.2 | 77.7 | 0.530 | 28.4 |
| val / digits_only | hybrid_utrnet_w400_tesseract_eng_val | 218 | 40.0 | 38.2 | 83.2 | 0.529 | 28.4 |
| val / digits_only | hybrid_utrnet_w800_tesseract_eng_val | 218 | 40.0 | 38.4 | 81.8 | 0.530 | 28.4 |
| val / digits_only | hybrid_final_val | 218 | 40.0 | 38.4 | 81.8 | 0.530 | 28.4 |
| val / digits_only | original_gold | 218 | 30.6 | 30.0 | 63.2 | 0.539 | 39.4 |
| val / latin_only | utrnet_large_w400_val_det | 51 | 80.6 | 81.6 | 111.4 | 0.645 | 0.0 |
| val / latin_only | utrnet_large_w800_val_det | 51 | 80.6 | 81.6 | 111.4 | 0.634 | 0.0 |
| val / latin_only | tesseract_urd-eng_val | 51 | 28.2 | 29.5 | 44.3 | 0.317 | 43.1 |
| val / latin_only | tesseract_eng_val | 51 | 22.9 | 23.6 | 44.3 | 0.263 | 45.1 |
| val / latin_only | hybrid_utrnet_w400_tesseract_eng_val | 51 | 75.3 | 75.9 | 97.5 | 0.511 | 21.6 |
| val / latin_only | hybrid_utrnet_w800_tesseract_eng_val | 51 | 70.1 | 70.9 | 93.7 | 0.475 | 23.5 |
| val / latin_only | hybrid_final_val | 51 | 42.3 | 43.1 | 57.0 | 0.355 | 39.2 |
| val / latin_only | original_gold | 51 | 2.5 | 2.4 | 7.6 | 0.020 | 92.2 |
| val / other | utrnet_large_w400_val_det | 1 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| val / other | utrnet_large_w800_val_det | 1 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| val / other | tesseract_urd-eng_val | 1 | 50.0 | 50.0 | 100.0 | 0.500 | 0.0 |
| val / other | tesseract_eng_val | 1 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| val / other | hybrid_utrnet_w400_tesseract_eng_val | 1 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| val / other | hybrid_utrnet_w800_tesseract_eng_val | 1 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| val / other | hybrid_final_val | 1 | 100.0 | 100.0 | 100.0 | 1.000 | 0.0 |
| val / other | original_gold | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / urdu+digits | utrnet_large_w400_val_det | 267 | 17.5 | 12.8 | 65.9 | 0.203 | 2.2 |
| val / urdu+digits | utrnet_large_w800_val_det | 267 | 14.7 | 11.2 | 54.6 | 0.187 | 2.2 |
| val / urdu+digits | tesseract_urd-eng_val | 267 | 69.6 | 72.2 | 96.7 | 0.700 | 0.0 |
| val / urdu+digits | tesseract_eng_val | 267 | 90.1 | 96.2 | 100.2 | 0.876 | 0.0 |
| val / urdu+digits | hybrid_utrnet_w400_tesseract_eng_val | 267 | 17.3 | 12.6 | 65.9 | 0.197 | 2.2 |
| val / urdu+digits | hybrid_utrnet_w800_tesseract_eng_val | 267 | 14.5 | 10.9 | 54.6 | 0.180 | 2.2 |
| val / urdu+digits | hybrid_final_val | 267 | 14.4 | 10.8 | 54.6 | 0.177 | 2.2 |
| val / urdu+digits | original_gold | 267 | 17.2 | 15.0 | 55.7 | 0.209 | 1.5 |
| val / urdu+latin | utrnet_large_w400_val_det | 100 | 23.2 | 19.2 | 69.9 | 0.221 | 0.0 |
| val / urdu+latin | utrnet_large_w800_val_det | 100 | 19.7 | 16.4 | 58.7 | 0.192 | 0.0 |
| val / urdu+latin | tesseract_urd-eng_val | 100 | 67.4 | 70.7 | 94.0 | 0.671 | 0.0 |
| val / urdu+latin | tesseract_eng_val | 100 | 88.9 | 95.0 | 99.3 | 0.883 | 0.0 |
| val / urdu+latin | hybrid_utrnet_w400_tesseract_eng_val | 100 | 23.2 | 19.2 | 69.9 | 0.221 | 0.0 |
| val / urdu+latin | hybrid_utrnet_w800_tesseract_eng_val | 100 | 19.7 | 16.4 | 58.7 | 0.192 | 0.0 |
| val / urdu+latin | hybrid_final_val | 100 | 19.7 | 16.4 | 58.7 | 0.192 | 0.0 |
| val / urdu+latin | original_gold | 100 | 15.2 | 13.1 | 46.3 | 0.161 | 2.0 |
| val / urdu_only | utrnet_large_w400_val_det | 430 | 12.3 | 7.7 | 58.1 | 0.105 | 24.9 |
| val / urdu_only | utrnet_large_w800_val_det | 430 | 10.4 | 6.5 | 49.2 | 0.099 | 24.7 |
| val / urdu_only | tesseract_urd-eng_val | 430 | 74.9 | 77.9 | 97.2 | 0.743 | 0.9 |
| val / urdu_only | tesseract_eng_val | 430 | 93.7 | 99.9 | 102.2 | 0.947 | 0.0 |
| val / urdu_only | hybrid_utrnet_w400_tesseract_eng_val | 430 | 12.3 | 7.7 | 58.1 | 0.105 | 24.9 |
| val / urdu_only | hybrid_utrnet_w800_tesseract_eng_val | 430 | 10.4 | 6.5 | 49.2 | 0.099 | 24.7 |
| val / urdu_only | hybrid_final_val | 430 | 10.4 | 6.5 | 49.2 | 0.102 | 24.4 |
| val / urdu_only | original_gold | 430 | 15.6 | 13.0 | 52.8 | 0.165 | 16.0 |

### By aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / 12.5-25 | utrnet_large_w400_val_det | 276 | 16.2 | 11.4 | 65.4 | 0.169 | 0.4 |
| val / 12.5-25 | utrnet_large_w800_val_det | 276 | 13.7 | 10.0 | 53.6 | 0.149 | 0.7 |
| val / 12.5-25 | tesseract_urd-eng_val | 276 | 71.5 | 74.4 | 95.6 | 0.689 | 0.4 |
| val / 12.5-25 | tesseract_eng_val | 276 | 90.7 | 96.9 | 100.3 | 0.888 | 0.4 |
| val / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 276 | 16.2 | 11.3 | 65.4 | 0.167 | 0.4 |
| val / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 276 | 13.6 | 9.8 | 53.6 | 0.144 | 0.7 |
| val / 12.5-25 | hybrid_final_val | 276 | 13.4 | 9.7 | 53.4 | 0.141 | 0.7 |
| val / 12.5-25 | original_gold | 276 | 15.6 | 13.2 | 52.2 | 0.158 | 3.6 |
| val / <=12.5 | utrnet_large_w400_val_det | 712 | 21.6 | 19.3 | 57.8 | 0.279 | 20.4 |
| val / <=12.5 | utrnet_large_w800_val_det | 712 | 21.4 | 19.3 | 57.7 | 0.278 | 20.1 |
| val / <=12.5 | tesseract_urd-eng_val | 712 | 75.0 | 76.8 | 98.0 | 0.662 | 11.4 |
| val / <=12.5 | tesseract_eng_val | 712 | 89.2 | 92.7 | 99.5 | 0.765 | 11.7 |
| val / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 712 | 20.1 | 17.6 | 56.6 | 0.285 | 26.0 |
| val / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 712 | 19.9 | 17.5 | 56.3 | 0.283 | 25.8 |
| val / <=12.5 | hybrid_final_val | 712 | 19.6 | 17.1 | 56.0 | 0.277 | 26.7 |
| val / <=12.5 | original_gold | 712 | 23.0 | 20.5 | 65.6 | 0.296 | 27.7 |
| val / >25 | utrnet_large_w400_val_det | 79 | 16.3 | 10.5 | 70.3 | 0.172 | 0.0 |
| val / >25 | utrnet_large_w800_val_det | 79 | 10.9 | 6.3 | 52.5 | 0.119 | 0.0 |
| val / >25 | tesseract_urd-eng_val | 79 | 62.9 | 65.7 | 92.9 | 0.617 | 1.3 |
| val / >25 | tesseract_eng_val | 79 | 89.1 | 96.7 | 99.7 | 0.881 | 1.3 |
| val / >25 | hybrid_utrnet_w400_tesseract_eng_val | 79 | 16.3 | 10.5 | 70.3 | 0.172 | 0.0 |
| val / >25 | hybrid_utrnet_w800_tesseract_eng_val | 79 | 10.9 | 6.3 | 52.5 | 0.119 | 0.0 |
| val / >25 | hybrid_final_val | 79 | 10.5 | 5.8 | 52.1 | 0.107 | 1.3 |
| val / >25 | original_gold | 79 | 9.1 | 6.9 | 37.7 | 0.090 | 2.5 |

### By category x aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / 12.5-25 | utrnet_large_w400_val_det | 38 | 16.4 | 12.8 | 59.9 | 0.173 | 0.0 |
| val / hw_field / 12.5-25 | utrnet_large_w800_val_det | 38 | 14.6 | 11.5 | 50.9 | 0.155 | 0.0 |
| val / hw_field / 12.5-25 | tesseract_urd-eng_val | 38 | 62.5 | 65.1 | 93.4 | 0.620 | 0.0 |
| val / hw_field / 12.5-25 | tesseract_eng_val | 38 | 87.4 | 93.0 | 99.1 | 0.868 | 0.0 |
| val / hw_field / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 38 | 16.4 | 12.8 | 59.9 | 0.173 | 0.0 |
| val / hw_field / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 38 | 14.6 | 11.5 | 50.9 | 0.155 | 0.0 |
| val / hw_field / 12.5-25 | hybrid_final_val | 38 | 14.6 | 11.5 | 50.9 | 0.155 | 0.0 |
| val / hw_field / 12.5-25 | original_gold | 38 | 10.9 | 9.4 | 38.7 | 0.118 | 2.6 |
| val / hw_field / <=12.5 | utrnet_large_w400_val_det | 24 | 39.7 | 38.1 | 91.8 | 0.413 | 16.7 |
| val / hw_field / <=12.5 | utrnet_large_w800_val_det | 24 | 40.2 | 39.1 | 91.8 | 0.415 | 16.7 |
| val / hw_field / <=12.5 | tesseract_urd-eng_val | 24 | 64.8 | 65.5 | 103.3 | 0.647 | 8.3 |
| val / hw_field / <=12.5 | tesseract_eng_val | 24 | 73.5 | 74.9 | 101.6 | 0.714 | 12.5 |
| val / hw_field / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 24 | 34.5 | 32.6 | 88.5 | 0.383 | 25.0 |
| val / hw_field / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 24 | 34.8 | 33.4 | 88.5 | 0.381 | 25.0 |
| val / hw_field / <=12.5 | hybrid_final_val | 24 | 34.8 | 33.4 | 88.5 | 0.381 | 25.0 |
| val / hw_field / <=12.5 | original_gold | 24 | 25.3 | 22.5 | 75.4 | 0.228 | 41.7 |
| val / hw_field / >25 | utrnet_large_w400_val_det | 5 | 18.8 | 13.0 | 73.1 | 0.188 | 0.0 |
| val / hw_field / >25 | utrnet_large_w800_val_det | 5 | 11.9 | 7.5 | 50.3 | 0.122 | 0.0 |
| val / hw_field / >25 | tesseract_urd-eng_val | 5 | 50.9 | 53.0 | 91.8 | 0.500 | 0.0 |
| val / hw_field / >25 | tesseract_eng_val | 5 | 86.2 | 93.8 | 98.8 | 0.863 | 0.0 |
| val / hw_field / >25 | hybrid_utrnet_w400_tesseract_eng_val | 5 | 18.8 | 13.0 | 73.1 | 0.188 | 0.0 |
| val / hw_field / >25 | hybrid_utrnet_w800_tesseract_eng_val | 5 | 11.9 | 7.5 | 50.3 | 0.122 | 0.0 |
| val / hw_field / >25 | hybrid_final_val | 5 | 11.9 | 7.5 | 50.3 | 0.122 | 0.0 |
| val / hw_field / >25 | original_gold | 5 | 9.5 | 8.9 | 32.2 | 0.101 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w400_val_det | 4 | 91.0 | 93.5 | 147.1 | 0.913 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w800_val_det | 4 | 91.6 | 93.5 | 135.3 | 0.922 | 0.0 |
| val / num_latin / 12.5-25 | tesseract_urd-eng_val | 4 | 21.7 | 23.5 | 35.3 | 0.192 | 25.0 |
| val / num_latin / 12.5-25 | tesseract_eng_val | 4 | 12.7 | 13.1 | 41.2 | 0.125 | 25.0 |
| val / num_latin / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 4 | 91.0 | 93.5 | 147.1 | 0.913 | 0.0 |
| val / num_latin / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 4 | 77.7 | 79.7 | 123.5 | 0.692 | 0.0 |
| val / num_latin / 12.5-25 | hybrid_final_val | 4 | 48.8 | 50.3 | 76.5 | 0.474 | 0.0 |
| val / num_latin / 12.5-25 | original_gold | 4 | 4.2 | 4.6 | 11.8 | 0.040 | 75.0 |
| val / num_latin / <=12.5 | utrnet_large_w400_val_det | 255 | 61.3 | 60.5 | 94.7 | 0.493 | 12.5 |
| val / num_latin / <=12.5 | utrnet_large_w800_val_det | 255 | 61.0 | 60.1 | 94.3 | 0.492 | 12.5 |
| val / num_latin / <=12.5 | tesseract_urd-eng_val | 255 | 42.7 | 42.2 | 73.0 | 0.509 | 29.4 |
| val / num_latin / <=12.5 | tesseract_eng_val | 255 | 36.9 | 36.0 | 71.9 | 0.488 | 31.4 |
| val / num_latin / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 255 | 43.6 | 42.1 | 81.4 | 0.516 | 27.5 |
| val / num_latin / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 255 | 43.3 | 41.8 | 79.8 | 0.514 | 27.8 |
| val / num_latin / <=12.5 | hybrid_final_val | 255 | 40.0 | 38.6 | 75.7 | 0.497 | 30.6 |
| val / num_latin / <=12.5 | original_gold | 255 | 25.8 | 25.4 | 53.6 | 0.456 | 47.8 |
| val / num_latin / >25 | utrnet_large_w400_val_det | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / num_latin / >25 | utrnet_large_w800_val_det | 1 | 90.9 | 97.9 | 125.0 | 0.909 | 0.0 |
| val / num_latin / >25 | tesseract_urd-eng_val | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / num_latin / >25 | tesseract_eng_val | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / num_latin / >25 | hybrid_utrnet_w400_tesseract_eng_val | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / num_latin / >25 | hybrid_utrnet_w800_tesseract_eng_val | 1 | 90.9 | 97.9 | 125.0 | 0.909 | 0.0 |
| val / num_latin / >25 | hybrid_final_val | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / num_latin / >25 | original_gold | 1 | 0.0 | 0.0 | 0.0 | 0.000 | 100.0 |
| val / urdu / 12.5-25 | utrnet_large_w400_val_det | 234 | 15.7 | 10.6 | 66.0 | 0.155 | 0.4 |
| val / urdu / 12.5-25 | utrnet_large_w800_val_det | 234 | 13.1 | 9.1 | 53.8 | 0.135 | 0.9 |
| val / urdu / 12.5-25 | tesseract_urd-eng_val | 234 | 73.3 | 76.3 | 96.2 | 0.709 | 0.0 |
| val / urdu / 12.5-25 | tesseract_eng_val | 234 | 91.7 | 98.1 | 100.8 | 0.904 | 0.0 |
| val / urdu / 12.5-25 | hybrid_utrnet_w400_tesseract_eng_val | 234 | 15.6 | 10.5 | 66.0 | 0.153 | 0.4 |
| val / urdu / 12.5-25 | hybrid_utrnet_w800_tesseract_eng_val | 234 | 13.0 | 9.1 | 53.8 | 0.133 | 0.9 |
| val / urdu / 12.5-25 | hybrid_final_val | 234 | 13.0 | 9.1 | 53.8 | 0.133 | 0.9 |
| val / urdu / 12.5-25 | original_gold | 234 | 16.5 | 13.9 | 54.6 | 0.167 | 2.6 |
| val / urdu / <=12.5 | utrnet_large_w400_val_det | 433 | 18.1 | 15.2 | 53.4 | 0.145 | 25.2 |
| val / urdu / <=12.5 | utrnet_large_w800_val_det | 433 | 17.9 | 15.1 | 53.3 | 0.144 | 24.7 |
| val / urdu / <=12.5 | tesseract_urd-eng_val | 433 | 77.7 | 80.1 | 100.4 | 0.752 | 0.9 |
| val / urdu / <=12.5 | tesseract_eng_val | 433 | 93.5 | 98.2 | 102.2 | 0.931 | 0.0 |
| val / urdu / <=12.5 | hybrid_utrnet_w400_tesseract_eng_val | 433 | 17.9 | 15.0 | 53.4 | 0.143 | 25.2 |
| val / urdu / <=12.5 | hybrid_utrnet_w800_tesseract_eng_val | 433 | 17.8 | 14.9 | 53.2 | 0.142 | 24.7 |
| val / urdu / <=12.5 | hybrid_final_val | 433 | 17.7 | 14.8 | 53.4 | 0.142 | 24.5 |
| val / urdu / <=12.5 | original_gold | 433 | 22.7 | 20.0 | 66.5 | 0.205 | 15.0 |
| val / urdu / >25 | utrnet_large_w400_val_det | 73 | 15.8 | 9.9 | 70.0 | 0.161 | 0.0 |
| val / urdu / >25 | utrnet_large_w800_val_det | 73 | 10.4 | 5.7 | 52.4 | 0.108 | 0.0 |
| val / urdu / >25 | tesseract_urd-eng_val | 73 | 64.0 | 66.9 | 93.3 | 0.633 | 0.0 |
| val / urdu / >25 | tesseract_eng_val | 73 | 89.7 | 97.3 | 100.1 | 0.894 | 0.0 |
| val / urdu / >25 | hybrid_utrnet_w400_tesseract_eng_val | 73 | 15.8 | 9.9 | 70.0 | 0.161 | 0.0 |
| val / urdu / >25 | hybrid_utrnet_w800_tesseract_eng_val | 73 | 10.4 | 5.7 | 52.4 | 0.108 | 0.0 |
| val / urdu / >25 | hybrid_final_val | 73 | 10.4 | 5.7 | 52.4 | 0.108 | 0.0 |
| val / urdu / >25 | original_gold | 73 | 9.1 | 6.8 | 38.2 | 0.090 | 1.4 |

### By category x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / photo | utrnet_large_w400_val_det | 51 | 17.4 | 13.4 | 63.6 | 0.216 | 2.0 |
| val / hw_field / photo | utrnet_large_w800_val_det | 51 | 14.8 | 11.7 | 52.1 | 0.199 | 2.0 |
| val / hw_field / photo | tesseract_urd-eng_val | 51 | 61.6 | 64.3 | 93.7 | 0.654 | 0.0 |
| val / hw_field / photo | tesseract_eng_val | 51 | 87.6 | 93.4 | 99.5 | 0.868 | 0.0 |
| val / hw_field / photo | hybrid_utrnet_w400_tesseract_eng_val | 51 | 17.4 | 13.5 | 63.7 | 0.236 | 0.0 |
| val / hw_field / photo | hybrid_utrnet_w800_tesseract_eng_val | 51 | 14.8 | 11.7 | 52.2 | 0.219 | 0.0 |
| val / hw_field / photo | hybrid_final_val | 51 | 14.8 | 11.7 | 52.2 | 0.219 | 0.0 |
| val / hw_field / photo | original_gold | 51 | 11.5 | 10.2 | 39.2 | 0.147 | 9.8 |
| val / hw_field / scan | utrnet_large_w400_val_det | 16 | 29.5 | 28.0 | 68.1 | 0.400 | 18.8 |
| val / hw_field / scan | utrnet_large_w800_val_det | 16 | 27.9 | 26.2 | 63.8 | 0.395 | 18.8 |
| val / hw_field / scan | tesseract_urd-eng_val | 16 | 54.0 | 54.8 | 93.6 | 0.516 | 12.5 |
| val / hw_field / scan | tesseract_eng_val | 16 | 73.5 | 77.1 | 96.8 | 0.635 | 18.8 |
| val / hw_field / scan | hybrid_utrnet_w400_tesseract_eng_val | 16 | 25.2 | 23.3 | 64.9 | 0.292 | 37.5 |
| val / hw_field / scan | hybrid_utrnet_w800_tesseract_eng_val | 16 | 23.4 | 21.2 | 60.6 | 0.281 | 37.5 |
| val / hw_field / scan | hybrid_final_val | 16 | 23.4 | 21.2 | 60.6 | 0.281 | 37.5 |
| val / hw_field / scan | original_gold | 16 | 14.2 | 12.0 | 45.7 | 0.184 | 37.5 |
| val / num_latin / photo | utrnet_large_w400_val_det | 172 | 66.4 | 66.1 | 98.4 | 0.486 | 12.2 |
| val / num_latin / photo | utrnet_large_w800_val_det | 172 | 66.4 | 66.1 | 97.4 | 0.486 | 12.2 |
| val / num_latin / photo | tesseract_urd-eng_val | 172 | 32.8 | 33.1 | 61.5 | 0.427 | 37.2 |
| val / num_latin / photo | tesseract_eng_val | 172 | 27.7 | 27.6 | 59.4 | 0.411 | 39.5 |
| val / num_latin / photo | hybrid_utrnet_w400_tesseract_eng_val | 172 | 49.0 | 47.8 | 78.6 | 0.452 | 34.9 |
| val / num_latin / photo | hybrid_utrnet_w800_tesseract_eng_val | 172 | 46.5 | 45.6 | 76.6 | 0.446 | 34.9 |
| val / num_latin / photo | hybrid_final_val | 172 | 35.3 | 34.8 | 65.1 | 0.422 | 37.8 |
| val / num_latin / photo | original_gold | 172 | 16.5 | 16.4 | 41.7 | 0.380 | 56.4 |
| val / num_latin / scan | utrnet_large_w400_val_det | 88 | 65.1 | 63.5 | 97.9 | 0.530 | 12.5 |
| val / num_latin / scan | utrnet_large_w800_val_det | 88 | 65.1 | 63.5 | 97.9 | 0.530 | 12.5 |
| val / num_latin / scan | tesseract_urd-eng_val | 88 | 52.5 | 52.3 | 83.3 | 0.647 | 14.8 |
| val / num_latin / scan | tesseract_eng_val | 88 | 44.4 | 43.2 | 85.4 | 0.615 | 15.9 |
| val / num_latin / scan | hybrid_utrnet_w400_tesseract_eng_val | 88 | 57.0 | 55.0 | 101.0 | 0.664 | 11.4 |
| val / num_latin / scan | hybrid_utrnet_w800_tesseract_eng_val | 88 | 57.0 | 55.0 | 97.9 | 0.660 | 12.5 |
| val / num_latin / scan | hybrid_final_val | 88 | 49.9 | 48.3 | 90.6 | 0.637 | 15.9 |
| val / num_latin / scan | original_gold | 88 | 36.5 | 36.5 | 65.6 | 0.581 | 33.0 |
| val / urdu / photo | utrnet_large_w400_val_det | 488 | 16.2 | 11.3 | 65.2 | 0.140 | 16.6 |
| val / urdu / photo | utrnet_large_w800_val_det | 488 | 13.4 | 9.4 | 54.4 | 0.127 | 16.8 |
| val / urdu / photo | tesseract_urd-eng_val | 488 | 71.6 | 74.6 | 96.4 | 0.731 | 0.8 |
| val / urdu / photo | tesseract_eng_val | 488 | 91.5 | 97.9 | 100.8 | 0.921 | 0.0 |
| val / urdu / photo | hybrid_utrnet_w400_tesseract_eng_val | 488 | 16.2 | 11.2 | 65.2 | 0.139 | 16.6 |
| val / urdu / photo | hybrid_utrnet_w800_tesseract_eng_val | 488 | 13.4 | 9.4 | 54.4 | 0.125 | 16.8 |
| val / urdu / photo | hybrid_final_val | 488 | 13.3 | 9.3 | 54.5 | 0.125 | 16.6 |
| val / urdu / photo | original_gold | 488 | 16.5 | 14.0 | 53.8 | 0.176 | 10.2 |
| val / urdu / scan | utrnet_large_w400_val_det | 252 | 16.8 | 12.8 | 60.2 | 0.169 | 11.5 |
| val / urdu / scan | utrnet_large_w800_val_det | 252 | 14.7 | 11.5 | 51.1 | 0.160 | 10.7 |
| val / urdu / scan | tesseract_urd-eng_val | 252 | 74.1 | 76.7 | 97.1 | 0.720 | 0.0 |
| val / urdu / scan | tesseract_eng_val | 252 | 92.2 | 98.1 | 101.3 | 0.915 | 0.0 |
| val / urdu / scan | hybrid_utrnet_w400_tesseract_eng_val | 252 | 16.7 | 12.6 | 60.2 | 0.165 | 11.5 |
| val / urdu / scan | hybrid_utrnet_w800_tesseract_eng_val | 252 | 14.6 | 11.4 | 51.1 | 0.156 | 10.7 |
| val / urdu / scan | hybrid_final_val | 252 | 14.6 | 11.4 | 51.1 | 0.156 | 10.7 |
| val / urdu / scan | original_gold | 252 | 16.7 | 14.3 | 54.0 | 0.192 | 8.7 |

### Error types by content

S / D / I = substitutions / deletions / insertions as % of reference characters (they add up to CER).

| group | system | lines | ref chars | avg ref len | avg pred len | CER % | S % | D % | I % |
|---|---|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val_det | 218 | 949 | 4.4 | 3.8 | 59.9 | 41.8 | 15.9 | 2.1 |
| val / digits_only | utrnet_large_w800_val_det | 218 | 949 | 4.4 | 3.7 | 59.9 | 41.8 | 16.2 | 1.8 |
| val / digits_only | tesseract_urd-eng_val | 218 | 949 | 4.4 | 4.0 | 44.0 | 26.2 | 13.3 | 4.5 |
| val / digits_only | tesseract_eng_val | 218 | 949 | 4.4 | 4.0 | 37.5 | 21.5 | 12.0 | 4.0 |
| val / digits_only | hybrid_utrnet_w400_tesseract_eng_val | 218 | 949 | 4.4 | 4.1 | 40.0 | 25.8 | 9.5 | 4.7 |
| val / digits_only | hybrid_utrnet_w800_tesseract_eng_val | 218 | 949 | 4.4 | 4.1 | 40.0 | 25.4 | 10.4 | 4.2 |
| val / digits_only | hybrid_final_val | 218 | 949 | 4.4 | 4.1 | 40.0 | 25.4 | 10.4 | 4.2 |
| val / digits_only | original_gold | 218 | 949 | 4.4 | 4.4 | 30.6 | 23.1 | 2.8 | 4.6 |
| val / latin_only | utrnet_large_w400_val_det | 51 | 485 | 9.5 | 7.0 | 80.6 | 54.2 | 26.2 | 0.2 |
| val / latin_only | utrnet_large_w800_val_det | 51 | 485 | 9.5 | 7.0 | 80.6 | 54.0 | 26.4 | 0.2 |
| val / latin_only | tesseract_urd-eng_val | 51 | 485 | 9.5 | 8.2 | 28.2 | 10.5 | 15.9 | 1.9 |
| val / latin_only | tesseract_eng_val | 51 | 485 | 9.5 | 8.2 | 22.9 | 7.8 | 14.2 | 0.8 |
| val / latin_only | hybrid_utrnet_w400_tesseract_eng_val | 51 | 485 | 9.5 | 7.3 | 75.3 | 50.5 | 24.1 | 0.6 |
| val / latin_only | hybrid_utrnet_w800_tesseract_eng_val | 51 | 485 | 9.5 | 7.4 | 70.1 | 47.0 | 22.5 | 0.6 |
| val / latin_only | hybrid_final_val | 51 | 485 | 9.5 | 7.9 | 42.3 | 23.9 | 17.7 | 0.6 |
| val / latin_only | original_gold | 51 | 485 | 9.5 | 9.6 | 2.5 | 1.4 | 0.0 | 1.0 |
| val / other | utrnet_large_w400_val_det | 1 | 2 | 2.0 | 1.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| val / other | utrnet_large_w800_val_det | 1 | 2 | 2.0 | 1.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| val / other | tesseract_urd-eng_val | 1 | 2 | 2.0 | 2.0 | 50.0 | 50.0 | 0.0 | 0.0 |
| val / other | tesseract_eng_val | 1 | 2 | 2.0 | 1.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| val / other | hybrid_utrnet_w400_tesseract_eng_val | 1 | 2 | 2.0 | 1.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| val / other | hybrid_utrnet_w800_tesseract_eng_val | 1 | 2 | 2.0 | 1.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| val / other | hybrid_final_val | 1 | 2 | 2.0 | 1.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| val / other | original_gold | 1 | 2 | 2.0 | 2.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| val / urdu+digits | utrnet_large_w400_val_det | 267 | 22347 | 83.7 | 77.3 | 17.5 | 7.4 | 8.9 | 1.2 |
| val / urdu+digits | utrnet_large_w800_val_det | 267 | 22347 | 83.7 | 78.4 | 14.7 | 6.3 | 7.3 | 1.0 |
| val / urdu+digits | tesseract_urd-eng_val | 267 | 22347 | 83.7 | 43.7 | 69.6 | 20.1 | 48.6 | 0.8 |
| val / urdu+digits | tesseract_eng_val | 267 | 22347 | 83.7 | 29.9 | 90.1 | 25.4 | 64.4 | 0.2 |
| val / urdu+digits | hybrid_utrnet_w400_tesseract_eng_val | 267 | 22347 | 83.7 | 77.3 | 17.3 | 7.2 | 8.8 | 1.2 |
| val / urdu+digits | hybrid_utrnet_w800_tesseract_eng_val | 267 | 22347 | 83.7 | 78.5 | 14.5 | 6.2 | 7.2 | 1.0 |
| val / urdu+digits | hybrid_final_val | 267 | 22347 | 83.7 | 78.5 | 14.4 | 6.2 | 7.2 | 1.0 |
| val / urdu+digits | original_gold | 267 | 22347 | 83.7 | 81.1 | 17.2 | 8.2 | 6.1 | 3.0 |
| val / urdu+latin | utrnet_large_w400_val_det | 100 | 11953 | 119.5 | 108.1 | 23.2 | 11.3 | 10.7 | 1.2 |
| val / urdu+latin | utrnet_large_w800_val_det | 100 | 11953 | 119.5 | 109.1 | 19.7 | 9.1 | 9.7 | 1.0 |
| val / urdu+latin | tesseract_urd-eng_val | 100 | 11953 | 119.5 | 69.0 | 67.4 | 22.1 | 43.8 | 1.5 |
| val / urdu+latin | tesseract_eng_val | 100 | 11953 | 119.5 | 46.2 | 88.9 | 27.1 | 61.5 | 0.2 |
| val / urdu+latin | hybrid_utrnet_w400_tesseract_eng_val | 100 | 11953 | 119.5 | 108.1 | 23.2 | 11.3 | 10.7 | 1.2 |
| val / urdu+latin | hybrid_utrnet_w800_tesseract_eng_val | 100 | 11953 | 119.5 | 109.1 | 19.7 | 9.1 | 9.7 | 1.0 |
| val / urdu+latin | hybrid_final_val | 100 | 11953 | 119.5 | 109.1 | 19.7 | 9.1 | 9.7 | 1.0 |
| val / urdu+latin | original_gold | 100 | 11953 | 119.5 | 115.7 | 15.2 | 7.2 | 5.6 | 2.4 |
| val / urdu_only | utrnet_large_w400_val_det | 430 | 24306 | 56.5 | 52.7 | 12.3 | 3.6 | 7.7 | 1.0 |
| val / urdu_only | utrnet_large_w800_val_det | 430 | 24306 | 56.5 | 53.6 | 10.4 | 3.1 | 6.3 | 1.0 |
| val / urdu_only | tesseract_urd-eng_val | 430 | 24306 | 56.5 | 25.1 | 74.9 | 18.2 | 56.1 | 0.6 |
| val / urdu_only | tesseract_eng_val | 430 | 24306 | 56.5 | 16.8 | 93.7 | 23.0 | 70.4 | 0.2 |
| val / urdu_only | hybrid_utrnet_w400_tesseract_eng_val | 430 | 24306 | 56.5 | 52.7 | 12.3 | 3.7 | 7.7 | 1.0 |
| val / urdu_only | hybrid_utrnet_w800_tesseract_eng_val | 430 | 24306 | 56.5 | 53.6 | 10.4 | 3.1 | 6.3 | 1.0 |
| val / urdu_only | hybrid_final_val | 430 | 24306 | 56.5 | 53.6 | 10.4 | 3.1 | 6.3 | 1.0 |
| val / urdu_only | original_gold | 430 | 24306 | 56.5 | 54.8 | 15.6 | 7.9 | 5.4 | 2.3 |

### Top character confusions on Urdu lines: utrnet_large_w400_val_det

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2634 |
| ∅ |   | 270 |
|   | ا | 167 |
| / |   | 163 |
| ی | ∅ | 161 |
| / | ∅ | 140 |
| ر | ∅ | 138 |
| م | ∅ | 130 |
| و | د | 124 |
| س | ∅ | 111 |
| / | ا | 105 |
| ہ | ∅ | 104 |
| ا | ∅ | 101 |
| و | ∅ | 75 |
| ک | ∅ | 69 |
| ن | ∅ | 66 |
| - | ∅ | 65 |
| 0 | ∅ | 61 |
| - | ۔ | 58 |
| ۔ | ∅ | 58 |

### Top confusions on digit / Latin characters: utrnet_large_w400_val_det

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 99 |
| 0 | 2 | 85 |
| 2 | ∅ | 51 |
| 1 | ∅ | 49 |
| 2 | 0 | 44 |
| 2 | 1 | 38 |
| 5 | ∅ | 38 |
| 0 |   | 36 |
| i | ∅ | 31 |
| 1 | 2 | 26 |
| 0 | 8 | 23 |
| 3 | ∅ | 21 |
| 0 | 1 | 20 |
| 2 |   | 19 |
| 1 | 3 | 19 |
| 0 | 9 | 19 |
| 2 | 6 | 18 |
| a | ∅ | 17 |
| 2 | 3 | 16 |
| 0 | 5 | 16 |

### Worst 15 lines: utrnet_large_w400_val_det

| CER | crop | gold | pred |
|---|---|---|---|
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.20 | lines/AJK_0478_p01_L06.png | 14-02-2021 | 2211- lc - سعتع |
| 1.14 | lines/AJK_0056_p01_L18.png | 05827-960005-6 | ملہاری00096277.7 1 |
| 1.12 | lines/AJK_0144_p01_L10.png | 21/04/25 | "رم 59/ اح |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدد191 1111 |
| 1.00 | lines/AJK_0521_p01_L27.png | پرنسپل سٹاف آفیسر/ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ہائیر ایجوکیشن۔ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ایلیمنٹری اینڈ سیکنڈری ایجوکیشن۔ جناب چیئرمین آزاد جموں وکشمیر بورڈ آف انٹرمیڈیٹ وسیکنڈری ایجوکیشن میرپور۔ سسٹم آفیسر، محکمہ سروسز اینڈ جنرل ایڈمنسٹریشن آزاد حکومت ریاست جموں وکشمیر مظفرآباد بغرض اشاعت سرکاری جریدہ۔ دفتر کاپی۔ | ے |
| 1.00 | lines/AJK_0475_p01_L70.png | i |  |
| 1.00 | lines/AJK_0475_p01_L59.png | 6- | 5۔ |
| 1.00 | lines/AJK_0475_p01_L52.png | (iv) | 1ا |
| 1.00 | lines/AJK_0475_p01_L31.png | () | 1 |
| 1.00 | lines/AJK_0475_p01_L14.png | (ج) | ت |
| 1.00 | lines/AJK_0448_p01_L06.png | 09-09-2021 | .211 -.9-39 ہ |
| 1.00 | lines/AJK_0383_p02_L34.png | (ساجد عزیز نور) سیکریٹری |  |
| 1.00 | lines/AJK_0383_p02_L07.png | ation |  |
| 1.00 | lines/AJK_0383_p02_L04.png | 9th | 6 |

### Top character confusions on Urdu lines: utrnet_large_w800_val_det

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2080 |
| ∅ |   | 313 |
| ی | ∅ | 146 |
|   | ا | 130 |
| / |   | 130 |
| / | ∅ | 126 |
| ر | ∅ | 118 |
| / | ا | 98 |
| م | ∅ | 93 |
| س | ∅ | 91 |
| ا | ∅ | 91 |
| ہ | ∅ | 66 |
| و | ∅ | 64 |
| - | ∅ | 64 |
| - | ۔ | 61 |
| ک | ∅ | 61 |
| و | د | 59 |
| ن | ∅ | 57 |
| 0 | 2 | 53 |
| 0 | ∅ | 52 |

### Top confusions on digit / Latin characters: utrnet_large_w800_val_det

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 94 |
| 0 | 2 | 81 |
| 2 | ∅ | 61 |
| 2 | 1 | 48 |
| 1 | ∅ | 46 |
| i | ∅ | 38 |
| 2 | 0 | 33 |
| 5 | ∅ | 33 |
| 0 |   | 31 |
| 1 | 2 | 26 |
| 0 | - | 25 |
| 0 | 1 | 23 |
| w | ∅ | 21 |
| 2 | - | 20 |
| n | ∅ | 20 |
| 0 | 9 | 20 |
| 5 | 3 | 19 |
| e | ∅ | 19 |
| 2 | 3 | 18 |
| 3 | ∅ | 18 |

### Worst 15 lines: utrnet_large_w800_val_det

| CER | crop | gold | pred |
|---|---|---|---|
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.30 | lines/AJK_0478_p01_L06.png | 14-02-2021 | 221- lc ۔ سعتم |
| 1.12 | lines/AJK_0144_p01_L10.png | 21/04/25 | ارم 59/ اح |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدہد191 111 |
| 1.10 | lines/AJK_0448_p01_L06.png | 09-09-2021 | 2.211 -.9-و9 ہ |
| 1.00 | lines/AJK_0521_p01_L27.png | پرنسپل سٹاف آفیسر/ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ہائیر ایجوکیشن۔ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ایلیمنٹری اینڈ سیکنڈری ایجوکیشن۔ جناب چیئرمین آزاد جموں وکشمیر بورڈ آف انٹرمیڈیٹ وسیکنڈری ایجوکیشن میرپور۔ سسٹم آفیسر، محکمہ سروسز اینڈ جنرل ایڈمنسٹریشن آزاد حکومت ریاست جموں وکشمیر مظفرآباد بغرض اشاعت سرکاری جریدہ۔ دفتر کاپی۔ | ے |
| 1.00 | lines/AJK_0475_p01_L70.png | i |  |
| 1.00 | lines/AJK_0475_p01_L59.png | 6- | 5۔ |
| 1.00 | lines/AJK_0475_p01_L52.png | (iv) | 1ا |
| 1.00 | lines/AJK_0475_p01_L31.png | () | 1 |
| 1.00 | lines/AJK_0475_p01_L14.png | (ج) | ت |
| 1.00 | lines/AJK_0383_p02_L34.png | (ساجد عزیز نور) سیکریٹری |  |
| 1.00 | lines/AJK_0383_p02_L07.png | ation |  |
| 1.00 | lines/AJK_0383_p02_L04.png | 9th | 6 |
| 1.00 | lines/AJK_0351_p01_L12.png | 1- | ا۔ |

### Top character confusions on Urdu lines: tesseract_urd-eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3811 |
| ا | ∅ | 2470 |
| ی | ∅ | 2220 |
| ر | ∅ | 2014 |
| م | ∅ | 1409 |
| و | ∅ | 1260 |
| ک | ∅ | 1175 |
| ن | ∅ | 1136 |
| ل | ∅ | 876 |
| ب | ∅ | 860 |
| س | ∅ | 852 |
| ہ | ∅ | 827 |
| ت | ∅ | 686 |
| ج | ∅ | 578 |
| د | ∅ | 577 |
| پ | ∅ | 492 |
| ٹ | ∅ | 446 |
| ے | ∅ | 433 |
| ئ | ∅ | 379 |
| ف | ∅ | 362 |

### Top confusions on digit / Latin characters: tesseract_urd-eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 145 |
| 1 | ∅ | 130 |
| 2 | ∅ | 114 |
| 5 | ∅ | 46 |
| i | ∅ | 41 |
| 3 | ∅ | 39 |
| 9 | ∅ | 27 |
| a | ∅ | 24 |
| 7 | ∅ | 22 |
| n | ∅ | 19 |
| e | ∅ | 18 |
| o | ∅ | 16 |
| 1 | 4 | 15 |
| 6 | ∅ | 15 |
| 4 | ∅ | 15 |
| w | ∅ | 14 |
| 0 |   | 13 |
| l | ∅ | 12 |
| 2 | 0 | 12 |
| P | ∅ | 12 |

### Worst 15 lines: tesseract_urd-eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/AJK_0383_p02_L53.png | 7- | Ny J |
| 2.00 | lines/AJK_0102_p01_L41.png | 7۔ | =r J |
| 1.50 | lines/AJK_0478_p01_L22.png | 4۔ | 0.1 |
| 1.50 | lines/AJK_0383_p02_L47.png | 4- | =f] |
| 1.50 | lines/AJK_0351_p01_L16.png | 4- | ایس |
| 1.50 | lines/AJK_0139_p02_L31.png | 6- | I 6] |
| 1.50 | lines/AJK_0102_p01_L01.png | 43 | رین |
| 1.50 | lines/AJK_0056_p01_L33.png | 7- | oii |
| 1.50 | lines/AJK_0054_p01_L34.png | 7۔ | odd |
| 1.29 | lines/AJK_0351_p01_L07.png | 4648-53 | چک> ۔614) |
| 1.20 | lines/AJK_0116_p01_L34.png | داخلہ | راغ )ڑل |
| 1.00 | lines/AJK_0521_p01_L27.png | پرنسپل سٹاف آفیسر/ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ہائیر ایجوکیشن۔ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ایلیمنٹری اینڈ سیکنڈری ایجوکیشن۔ جناب چیئرمین آزاد جموں وکشمیر بورڈ آف انٹرمیڈیٹ وسیکنڈری ایجوکیشن میرپور۔ سسٹم آفیسر، محکمہ سروسز اینڈ جنرل ایڈمنسٹریشن آزاد حکومت ریاست جموں وکشمیر مظفرآباد بغرض اشاعت سرکاری جریدہ۔ دفتر کاپی۔ |  |
| 1.00 | lines/AJK_0521_p01_L19.png | (کبیر زادہ خان) سیکشن آفیسر ہائیر ایجوکیشن 07/5/2020 |  |
| 1.00 | lines/AJK_0521_p01_L06.png | نوٹیفکیشن:۔ |  |
| 1.00 | lines/AJK_0521_p01_L04.png | ’’مظفرآباد‘‘ | “Take |

### Top character confusions on Urdu lines: tesseract_eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 4699 |
| ا | ∅ | 3814 |
| ر | ∅ | 2764 |
| ی | ∅ | 2745 |
| م | ∅ | 1854 |
| و | ∅ | 1754 |
| ک | ∅ | 1550 |
| ن | ∅ | 1489 |
| ب | ∅ | 1109 |
| ل | ∅ | 1099 |
| س | ∅ | 1044 |
| ہ | ∅ | 957 |
| ت | ∅ | 839 |
| د | ∅ | 786 |
| ج | ∅ | 743 |
| پ | ∅ | 588 |
| ٹ | ∅ | 579 |
| ے | ∅ | 545 |
| ف | ∅ | 487 |
| ئ | ∅ | 423 |

### Top confusions on digit / Latin characters: tesseract_eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 204 |
| 2 | ∅ | 154 |
| 1 | ∅ | 139 |
| 5 | ∅ | 71 |
| 3 | ∅ | 57 |
| i | ∅ | 42 |
| 7 | ∅ | 33 |
| 9 | ∅ | 29 |
| 6 | ∅ | 28 |
| 4 | ∅ | 27 |
| n | ∅ | 25 |
| a | ∅ | 24 |
| e | ∅ | 20 |
| 8 | ∅ | 19 |
| l | ∅ | 17 |
| w | ∅ | 17 |
| c | ∅ | 14 |
| s | ∅ | 14 |
| O | ∅ | 14 |
| t | ∅ | 13 |

### Worst 15 lines: tesseract_eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/AJK_0484_p01_L19.png | نوٹ: | : od Gud |
| 2.00 | lines/AJK_0383_p02_L53.png | 7- | Ny J |
| 2.00 | lines/AJK_0102_p01_L41.png | 7۔ | =r J |
| 1.56 | lines/AJK_0475_p01_L02.png | نوٹیفکیشن | Cutie betnd nd |
| 1.50 | lines/AJK_0383_p02_L47.png | 4- | =f] |
| 1.50 | lines/AJK_0139_p02_L31.png | 6- | I 6] |
| 1.50 | lines/AJK_0106_p01_L11.png | 2۔ | i 4 |
| 1.50 | lines/AJK_0056_p01_L33.png | 7- | oii |
| 1.50 | lines/AJK_0056_p01_L30.png | 6- | re. |
| 1.50 | lines/AJK_0054_p01_L34.png | 7۔ | odd |
| 1.41 | lines/AJK_0139_p02_L36.png | مضامین/گروپ کی تبدیلی۔ | «(gui cuts] (gum wid sm / ind WED |
| 1.33 | lines/AJK_0102_p01_L55.png | 14۔ | BRT} |
| 1.25 | lines/AJK_0351_p01_L06.png | رجسٹریشن | . 2 plus 8 |
| 1.20 | lines/AJK_0139_p02_L30.png | ادارہ سے ادارہ مائیگریشن۔ | «utinl yetel a0 © 310] mi 0 300) |
| 1.12 | lines/AJK_0383_p02_L25.png | ادارہ سے ادارہ مائیگریشن۔ | Cound uted a) 0 3lal mi © 318) |

### Top character confusions on Urdu lines: hybrid_utrnet_w400_tesseract_eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2637 |
| ∅ |   | 270 |
|   | ا | 167 |
| / |   | 163 |
| ی | ∅ | 160 |
| / | ∅ | 140 |
| ر | ∅ | 137 |
| م | ∅ | 130 |
| و | د | 124 |
| س | ∅ | 111 |
| / | ا | 105 |
| ہ | ∅ | 104 |
| ا | ∅ | 103 |
| و | ∅ | 75 |
| ک | ∅ | 69 |
| ن | ∅ | 66 |
| - | ∅ | 60 |
| - | ۔ | 58 |
| ۔ | ∅ | 58 |
| پ | ی | 57 |

### Top confusions on digit / Latin characters: hybrid_utrnet_w400_tesseract_eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 65 |
| 0 | ∅ | 64 |
| 2 | ∅ | 41 |
| 1 | ∅ | 40 |
| 0 |   | 35 |
| 2 | 0 | 34 |
| 2 | 1 | 31 |
| i | ∅ | 25 |
| 1 | 2 | 24 |
| 5 | ∅ | 24 |
| 2 |   | 18 |
| 2 | 6 | 17 |
| a | ∅ | 17 |
| 3 | ∅ | 17 |
| n | ∅ | 15 |
| w | ∅ | 15 |
| 0 | 1 | 15 |
| 0 | 5 | 14 |
| 9 | ∅ | 14 |
| 1 | 0 | 14 |

### Worst 15 lines: hybrid_utrnet_w400_tesseract_eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/AJK_0383_p02_L53.png | 7- | Ny J |
| 2.00 | lines/AJK_0102_p01_L41.png | 7۔ | =r J |
| 1.50 | lines/AJK_0383_p02_L47.png | 4- | =f] |
| 1.50 | lines/AJK_0139_p02_L31.png | 6- | I 6] |
| 1.50 | lines/AJK_0106_p01_L11.png | 2۔ | i 4 |
| 1.50 | lines/AJK_0056_p01_L33.png | 7- | oii |
| 1.50 | lines/AJK_0056_p01_L30.png | 6- | re. |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.33 | lines/AJK_0102_p01_L55.png | 14۔ | BRT} |
| 1.20 | lines/AJK_0478_p01_L06.png | 14-02-2021 | 2211- lc - سعتع |
| 1.14 | lines/AJK_0056_p01_L18.png | 05827-960005-6 | ملہاری00096277.7 1 |
| 1.12 | lines/AJK_0144_p01_L10.png | 21/04/25 | "رم 59/ اح |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدد191 1111 |
| 1.00 | lines/AJK_0521_p01_L27.png | پرنسپل سٹاف آفیسر/ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ہائیر ایجوکیشن۔ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ایلیمنٹری اینڈ سیکنڈری ایجوکیشن۔ جناب چیئرمین آزاد جموں وکشمیر بورڈ آف انٹرمیڈیٹ وسیکنڈری ایجوکیشن میرپور۔ سسٹم آفیسر، محکمہ سروسز اینڈ جنرل ایڈمنسٹریشن آزاد حکومت ریاست جموں وکشمیر مظفرآباد بغرض اشاعت سرکاری جریدہ۔ دفتر کاپی۔ | ے |
| 1.00 | lines/AJK_0484_p01_L47.png | 9- | _9 |

### Top character confusions on Urdu lines: hybrid_utrnet_w800_tesseract_eng_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2081 |
| ∅ |   | 313 |
| ی | ∅ | 145 |
|   | ا | 130 |
| / |   | 130 |
| / | ∅ | 126 |
| ر | ∅ | 117 |
| / | ا | 98 |
| م | ∅ | 93 |
| ا | ∅ | 93 |
| س | ∅ | 91 |
| ہ | ∅ | 66 |
| و | ∅ | 64 |
| - | ∅ | 61 |
| - | ۔ | 61 |
| ک | ∅ | 60 |
| و | د | 59 |
| ن | ∅ | 57 |
| ٹ | ∅ | 51 |
| ب | ∅ | 50 |

### Top confusions on digit / Latin characters: hybrid_utrnet_w800_tesseract_eng_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | 2 | 58 |
| 0 | ∅ | 57 |
| 2 | ∅ | 49 |
| 2 | 1 | 39 |
| 1 | ∅ | 39 |
| i | ∅ | 31 |
| 0 |   | 28 |
| 2 | 0 | 26 |
| 0 | - | 24 |
| 5 | ∅ | 22 |
| 1 | 2 | 22 |
| w | ∅ | 21 |
| n | ∅ | 20 |
| 2 | - | 19 |
| 0 | 1 | 19 |
| e | ∅ | 17 |
| a | ∅ | 17 |
| c | ∅ | 14 |
| 3 | ∅ | 14 |
| O | ∅ | 14 |

### Worst 15 lines: hybrid_utrnet_w800_tesseract_eng_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/AJK_0383_p02_L53.png | 7- | Ny J |
| 2.00 | lines/AJK_0102_p01_L41.png | 7۔ | =r J |
| 1.50 | lines/AJK_0383_p02_L47.png | 4- | =f] |
| 1.50 | lines/AJK_0139_p02_L31.png | 6- | I 6] |
| 1.50 | lines/AJK_0106_p01_L11.png | 2۔ | i 4 |
| 1.50 | lines/AJK_0056_p01_L33.png | 7- | oii |
| 1.50 | lines/AJK_0056_p01_L30.png | 6- | re. |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.33 | lines/AJK_0102_p01_L55.png | 14۔ | BRT} |
| 1.30 | lines/AJK_0478_p01_L06.png | 14-02-2021 | 221- lc ۔ سعتم |
| 1.12 | lines/AJK_0144_p01_L10.png | 21/04/25 | ارم 59/ اح |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدہد191 111 |
| 1.10 | lines/AJK_0448_p01_L06.png | 09-09-2021 | 2.211 -.9-و9 ہ |
| 1.00 | lines/AJK_0521_p01_L27.png | پرنسپل سٹاف آفیسر/ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ہائیر ایجوکیشن۔ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ایلیمنٹری اینڈ سیکنڈری ایجوکیشن۔ جناب چیئرمین آزاد جموں وکشمیر بورڈ آف انٹرمیڈیٹ وسیکنڈری ایجوکیشن میرپور۔ سسٹم آفیسر، محکمہ سروسز اینڈ جنرل ایڈمنسٹریشن آزاد حکومت ریاست جموں وکشمیر مظفرآباد بغرض اشاعت سرکاری جریدہ۔ دفتر کاپی۔ | ے |
| 1.00 | lines/AJK_0484_p01_L47.png | 9- | _9 |

### Top character confusions on Urdu lines: hybrid_final_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 2084 |
| ∅ |   | 313 |
| ی | ∅ | 145 |
|   | ا | 130 |
| / |   | 130 |
| / | ∅ | 126 |
| ر | ∅ | 117 |
| / | ا | 98 |
| ا | ∅ | 96 |
| م | ∅ | 93 |
| س | ∅ | 91 |
| ہ | ∅ | 66 |
| و | ∅ | 64 |
| - | ۔ | 61 |
| ک | ∅ | 60 |
| و | د | 59 |
| - | ∅ | 58 |
| ن | ∅ | 57 |
| ٹ | ∅ | 51 |
| ب | ∅ | 50 |

### Top confusions on digit / Latin characters: hybrid_final_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 55 |
| 0 | 2 | 54 |
| 2 | ∅ | 44 |
| 2 | 1 | 38 |
| 1 | ∅ | 37 |
| i | ∅ | 29 |
| 0 |   | 28 |
| 2 | 0 | 26 |
| 0 | - | 22 |
| 1 | 2 | 22 |
| w | ∅ | 21 |
| 5 | ∅ | 20 |
| 2 | - | 19 |
| 0 | 1 | 19 |
| n | ∅ | 19 |
| e | ∅ | 15 |
| a | ∅ | 15 |
| c | ∅ | 14 |
| 3 | ∅ | 14 |
| O | ∅ | 14 |

### Worst 15 lines: hybrid_final_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.00 | lines/AJK_0383_p02_L53.png | 7- | Ny J |
| 2.00 | lines/AJK_0102_p01_L41.png | 7۔ | =r J |
| 1.50 | lines/AJK_0383_p02_L47.png | 4- | =f] |
| 1.50 | lines/AJK_0139_p02_L31.png | 6- | I 6] |
| 1.50 | lines/AJK_0106_p01_L11.png | 2۔ | i 4 |
| 1.50 | lines/AJK_0056_p01_L33.png | 7- | oii |
| 1.50 | lines/AJK_0056_p01_L30.png | 6- | re. |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.33 | lines/AJK_0102_p01_L55.png | 14۔ | BRT} |
| 1.30 | lines/AJK_0478_p01_L06.png | 14-02-2021 | 221- lc ۔ سعتم |
| 1.12 | lines/AJK_0144_p01_L10.png | 21/04/25 | ارم 59/ اح |
| 1.11 | lines/AJK_0102_p01_L26.png | 19/9/2025 | کدہد191 111 |
| 1.10 | lines/AJK_0448_p01_L06.png | 09-09-2021 | 2.211 -.9-و9 ہ |
| 1.00 | lines/AJK_0521_p01_L27.png | پرنسپل سٹاف آفیسر/ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ہائیر ایجوکیشن۔ پرائیویٹ سیکرٹری ہمراہ جناب سیکرٹری ایلیمنٹری اینڈ سیکنڈری ایجوکیشن۔ جناب چیئرمین آزاد جموں وکشمیر بورڈ آف انٹرمیڈیٹ وسیکنڈری ایجوکیشن میرپور۔ سسٹم آفیسر، محکمہ سروسز اینڈ جنرل ایڈمنسٹریشن آزاد حکومت ریاست جموں وکشمیر مظفرآباد بغرض اشاعت سرکاری جریدہ۔ دفتر کاپی۔ | ے |
| 1.00 | lines/AJK_0484_p01_L47.png | 9- | _9 |

### Top character confusions on Urdu lines: original_gold

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 1157 |
| ∅ |   | 738 |
| ی | ∅ | 171 |
|   | ا | 123 |
| ن | ∅ | 120 |
| م | ∅ | 117 |
| ر | ∅ | 114 |
| / |   | 114 |
| پ | ی | 106 |
| س | ∅ | 105 |
| ہ | ∅ | 103 |
| ا | ∅ | 101 |
| ∅ | ا | 93 |
| ک | ∅ | 93 |
| پ | ب | 92 |
| ٹ | ∅ | 82 |
| ڈ | د | 79 |
| ۔ | ∅ | 79 |
| و | ∅ | 70 |
| / | ∅ | 65 |

### Top confusions on digit / Latin characters: original_gold

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 2 | ∅ | 34 |
| 0 | ∅ | 21 |
| ∅ | - | 16 |
| 1 | ∅ | 15 |
| 2 | - | 14 |
| 6 | - | 12 |
| 1 | _ | 11 |
| 1 | 2 | 11 |
| w | ∅ | 10 |
| 4 | ∅ | 10 |
| 1 | - | 10 |
| 5 | ∅ | 10 |
| 2 | 1 | 9 |
| 1 | 0 | 8 |
| 5 | - | 8 |
| 8 | - | 8 |
| e | ∅ | 7 |
| 0 | 1 | 7 |
| 3 | - | 7 |
| 3 | ∅ | 7 |

### Worst 15 lines: original_gold

| CER | crop | gold | pred |
|---|---|---|---|
| 1.56 | lines/AJK_0116_p02_L26.png | (محمد مسعود چوہدری) 13-8-25 | الا . کا الا الم الا الم الم الم الم الم الم ال |
| 1.27 | lines/AJK_0063_p01_L19.png | (وقاص احمد) | رار کرد میرارد(وقاص احمد) |
| 1.18 | lines/AJK_0106_p01_L02.png | نمبر بورڈ/ انٹر/ 9393-9418 /مورخہ 17-09-2025 | الم بورد الراکا 17-09-2025 مورد 2025 مورد 2025 مورد المراکا 17-09 |
| 1.03 | lines/AJK_0116_p02_L03.png | 11 تبدیلی مرکز فیس-/3000 روپے، تبدیلی گروپ فیس-/3000 روپے اور تبدیلی مضمون-/1500 روپے فی مضمون مقرر ہے۔ تبدیلی گروپ/ مضامین کا پروسیس Online ہوگا اور داخلہ فیس جمع | عبونا ن ارتید پر میرون سرہ میرون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کارون کا |
| 1.00 | lines/AJK_0484_p01_L47.png | 9- | _9 |
| 1.00 | lines/AJK_0484_p01_L45.png | 8- | -8 |
| 1.00 | lines/AJK_0484_p01_L43.png | 7- | -7 |
| 1.00 | lines/AJK_0484_p01_L41.png | 6- | -6 |
| 1.00 | lines/AJK_0484_p01_L39.png | 5- | _5 |
| 1.00 | lines/AJK_0484_p01_L37.png | 4- | _4 |
| 1.00 | lines/AJK_0484_p01_L35.png | 3- | _3 |
| 1.00 | lines/AJK_0484_p01_L33.png | 2- | _2 |
| 1.00 | lines/AJK_0484_p01_L29.png | مورخہ /2021 | 2021مورفتہ |
| 1.00 | lines/AJK_0484_p01_L23.png | 2- | _2 |
| 1.00 | lines/AJK_0484_p01_L21.png | 1- | _1 |
