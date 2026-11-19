# OCR evaluation

Systems: utrnet_large_w400_val, utrnet_large_w400_val_pp  
Reference: original gold (data/processed/lines.tsv, NOT human-verified)  
Lines scored: 1432 (crops present in every prediction file, minus 0 with an empty reference, minus 5 with a suspect reference (listed at the end))  
Line accounting: 1437 lines in every prediction file = 1432 scored + 0 empty reference + 5 suspect reference (excluded by heuristic, awaiting human correction)  
CER / WER = total edits (S+D+I) / total reference characters / words over all lines (micro); NED = mean of per-line edit / max(len(ref), len(pred)); can exceed 100% when the OCR inserts text  
Normalisation: full (see eval_ocr.py docstring)

### Overall

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| all | utrnet_large_w400_val | 1432 | 23.2 | 20.0 | 72.4 | 0.361 | 4.7 |
| all | utrnet_large_w400_val_pp | 1432 | 23.0 | 19.7 | 71.9 | 0.302 | 9.3 |

### By split

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val | utrnet_large_w400_val | 1432 | 23.2 | 20.0 | 72.4 | 0.361 | 4.7 |
| val | utrnet_large_w400_val_pp | 1432 | 23.0 | 19.7 | 71.9 | 0.302 | 9.3 |

### By split x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / photo | utrnet_large_w400_val | 813 | 23.7 | 20.4 | 73.3 | 0.342 | 5.3 |
| val / photo | utrnet_large_w400_val_pp | 813 | 23.5 | 20.2 | 73.0 | 0.299 | 8.4 |
| val / scan | utrnet_large_w400_val | 619 | 22.6 | 19.4 | 71.1 | 0.387 | 3.9 |
| val / scan | utrnet_large_w400_val_pp | 619 | 22.2 | 18.9 | 70.5 | 0.305 | 10.5 |

### By category

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field | utrnet_large_w400_val | 105 | 22.9 | 19.8 | 71.1 | 0.334 | 1.0 |
| val / hw_field | utrnet_large_w400_val_pp | 105 | 23.0 | 19.8 | 71.1 | 0.332 | 1.0 |
| val / num_latin | utrnet_large_w400_val | 367 | 78.4 | 77.9 | 107.1 | 0.765 | 0.5 |
| val / num_latin | utrnet_large_w400_val_pp | 367 | 68.6 | 67.8 | 91.9 | 0.535 | 18.5 |
| val / urdu | utrnet_large_w400_val | 960 | 21.6 | 17.9 | 71.3 | 0.209 | 6.7 |
| val / urdu | utrnet_large_w400_val_pp | 960 | 21.6 | 17.9 | 71.3 | 0.209 | 6.7 |

### By content

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val | 295 | 76.2 | 74.9 | 107.5 | 0.782 | 0.7 |
| val / digits_only | utrnet_large_w400_val_pp | 295 | 61.9 | 60.6 | 86.0 | 0.495 | 23.1 |
| val / latin_only | utrnet_large_w400_val | 92 | 81.1 | 81.9 | 112.3 | 0.698 | 0.0 |
| val / latin_only | utrnet_large_w400_val_pp | 92 | 80.8 | 81.5 | 112.3 | 0.697 | 0.0 |
| val / other | utrnet_large_w400_val | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / other | utrnet_large_w400_val_pp | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / urdu+digits | utrnet_large_w400_val | 343 | 22.9 | 18.9 | 75.2 | 0.249 | 0.0 |
| val / urdu+digits | utrnet_large_w400_val_pp | 343 | 22.9 | 18.9 | 75.2 | 0.249 | 0.0 |
| val / urdu+latin | utrnet_large_w400_val | 122 | 27.2 | 24.3 | 74.4 | 0.281 | 0.0 |
| val / urdu+latin | utrnet_large_w400_val_pp | 122 | 27.2 | 24.3 | 74.4 | 0.281 | 0.0 |
| val / urdu_only | utrnet_large_w400_val | 577 | 18.1 | 14.5 | 66.4 | 0.172 | 11.3 |
| val / urdu_only | utrnet_large_w400_val_pp | 577 | 18.1 | 14.5 | 66.4 | 0.172 | 11.3 |

### By aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / 12.5-25 | utrnet_large_w400_val | 376 | 21.7 | 18.1 | 71.5 | 0.231 | 0.8 |
| val / 12.5-25 | utrnet_large_w400_val_pp | 376 | 21.7 | 18.1 | 71.5 | 0.230 | 0.8 |
| val / <=12.5 | utrnet_large_w400_val | 947 | 30.6 | 28.8 | 76.1 | 0.434 | 6.8 |
| val / <=12.5 | utrnet_large_w400_val_pp | 947 | 29.7 | 27.8 | 74.5 | 0.344 | 13.7 |
| val / >25 | utrnet_large_w400_val | 109 | 17.3 | 12.4 | 69.6 | 0.178 | 0.0 |
| val / >25 | utrnet_large_w400_val_pp | 109 | 17.3 | 12.4 | 69.6 | 0.178 | 0.0 |

### By category x aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / 12.5-25 | utrnet_large_w400_val | 51 | 21.0 | 17.7 | 68.4 | 0.243 | 0.0 |
| val / hw_field / 12.5-25 | utrnet_large_w400_val_pp | 51 | 21.0 | 17.7 | 68.4 | 0.243 | 0.0 |
| val / hw_field / <=12.5 | utrnet_large_w400_val | 48 | 35.7 | 34.9 | 80.9 | 0.443 | 2.1 |
| val / hw_field / <=12.5 | utrnet_large_w400_val_pp | 48 | 35.9 | 35.2 | 80.9 | 0.439 | 2.1 |
| val / hw_field / >25 | utrnet_large_w400_val | 6 | 21.3 | 15.3 | 77.0 | 0.227 | 0.0 |
| val / hw_field / >25 | utrnet_large_w400_val_pp | 6 | 21.3 | 15.3 | 77.0 | 0.227 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w400_val | 10 | 87.5 | 89.5 | 118.9 | 0.862 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w400_val_pp | 10 | 86.6 | 88.8 | 118.9 | 0.848 | 0.0 |
| val / num_latin / <=12.5 | utrnet_large_w400_val | 356 | 76.6 | 75.7 | 105.9 | 0.762 | 0.6 |
| val / num_latin / <=12.5 | utrnet_large_w400_val_pp | 356 | 64.9 | 63.8 | 88.9 | 0.525 | 19.1 |
| val / num_latin / >25 | utrnet_large_w400_val | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / num_latin / >25 | utrnet_large_w400_val_pp | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / urdu / 12.5-25 | utrnet_large_w400_val | 315 | 21.2 | 17.4 | 71.7 | 0.209 | 1.0 |
| val / urdu / 12.5-25 | utrnet_large_w400_val_pp | 315 | 21.2 | 17.4 | 71.7 | 0.209 | 1.0 |
| val / urdu / <=12.5 | utrnet_large_w400_val | 543 | 26.3 | 23.6 | 72.7 | 0.218 | 11.2 |
| val / urdu / <=12.5 | utrnet_large_w400_val_pp | 543 | 26.3 | 23.6 | 72.7 | 0.218 | 11.2 |
| val / urdu / >25 | utrnet_large_w400_val | 102 | 16.8 | 11.9 | 69.0 | 0.168 | 0.0 |
| val / urdu / >25 | utrnet_large_w400_val_pp | 102 | 16.8 | 11.9 | 69.0 | 0.168 | 0.0 |

### By category x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / photo | utrnet_large_w400_val | 56 | 21.5 | 17.8 | 70.3 | 0.283 | 0.0 |
| val / hw_field / photo | utrnet_large_w400_val_pp | 56 | 21.5 | 17.8 | 70.3 | 0.283 | 0.0 |
| val / hw_field / scan | utrnet_large_w400_val | 49 | 26.8 | 24.6 | 73.5 | 0.392 | 2.0 |
| val / hw_field / scan | utrnet_large_w400_val_pp | 49 | 26.9 | 24.8 | 73.5 | 0.388 | 2.0 |
| val / num_latin / photo | utrnet_large_w400_val | 199 | 76.7 | 76.5 | 106.8 | 0.717 | 1.0 |
| val / num_latin / photo | utrnet_large_w400_val_pp | 199 | 70.8 | 70.4 | 96.8 | 0.544 | 13.6 |
| val / num_latin / scan | utrnet_large_w400_val | 168 | 81.6 | 80.4 | 107.6 | 0.822 | 0.0 |
| val / num_latin / scan | utrnet_large_w400_val_pp | 168 | 64.7 | 63.4 | 85.4 | 0.524 | 24.4 |
| val / urdu / photo | utrnet_large_w400_val | 558 | 22.2 | 18.5 | 72.6 | 0.213 | 7.3 |
| val / urdu / photo | utrnet_large_w400_val_pp | 558 | 22.2 | 18.5 | 72.6 | 0.213 | 7.3 |
| val / urdu / scan | utrnet_large_w400_val | 402 | 20.8 | 17.2 | 69.8 | 0.204 | 5.7 |
| val / urdu / scan | utrnet_large_w400_val_pp | 402 | 20.8 | 17.2 | 69.8 | 0.204 | 5.7 |

### Error types by content

S / D / I = substitutions / deletions / insertions as % of reference characters (they add up to CER).

| group | system | lines | ref chars | avg ref len | avg pred len | CER % | S % | D % | I % |
|---|---|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val | 295 | 1444 | 4.9 | 4.1 | 76.2 | 53.2 | 19.3 | 3.8 |
| val / digits_only | utrnet_large_w400_val_pp | 295 | 1444 | 4.9 | 4.1 | 61.9 | 41.6 | 17.9 | 2.4 |
| val / latin_only | utrnet_large_w400_val | 92 | 962 | 10.5 | 7.7 | 81.1 | 52.8 | 27.5 | 0.7 |
| val / latin_only | utrnet_large_w400_val_pp | 92 | 962 | 10.5 | 7.7 | 80.8 | 52.7 | 27.4 | 0.6 |
| val / other | utrnet_large_w400_val | 3 | 5 | 1.7 | 1.7 | 120.0 | 80.0 | 20.0 | 20.0 |
| val / other | utrnet_large_w400_val_pp | 3 | 5 | 1.7 | 1.7 | 120.0 | 80.0 | 20.0 | 20.0 |
| val / urdu+digits | utrnet_large_w400_val | 343 | 29793 | 86.9 | 81.2 | 22.9 | 10.7 | 9.3 | 2.8 |
| val / urdu+digits | utrnet_large_w400_val_pp | 343 | 29793 | 86.9 | 81.2 | 22.9 | 10.7 | 9.3 | 2.8 |
| val / urdu+latin | utrnet_large_w400_val | 122 | 13318 | 109.2 | 102.7 | 27.2 | 15.1 | 9.0 | 3.1 |
| val / urdu+latin | utrnet_large_w400_val_pp | 122 | 13318 | 109.2 | 102.7 | 27.2 | 15.1 | 9.0 | 3.1 |
| val / urdu_only | utrnet_large_w400_val | 577 | 34080 | 59.1 | 56.0 | 18.1 | 8.0 | 7.7 | 2.5 |
| val / urdu_only | utrnet_large_w400_val_pp | 577 | 34080 | 59.1 | 56.0 | 18.1 | 8.0 | 7.7 | 2.5 |

### Top character confusions on Urdu lines: utrnet_large_w400_val

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3227 |
| ∅ |   | 527 |
| ا | ∅ | 285 |
| م | ∅ | 225 |
| ر | ∅ | 221 |
| ی | ∅ | 195 |
| و | د | 181 |
| ن | ∅ | 147 |
| ل | ∅ | 144 |
| د | ∅ | 120 |
| ∅ | ی | 118 |
| / | ا | 117 |
| ی | پ | 116 |
| ب | پ | 114 |
| ک | ∅ | 114 |
| و | ∅ | 113 |
| ہ | ∅ | 104 |
| - | ۔ | 104 |
| ∅ | ا | 99 |
|   | ر | 92 |

### Top confusions on digit / Latin characters: utrnet_large_w400_val

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 131 |
| 0 | 2 | 122 |
| 2 | ∅ | 76 |
| 1 | ∅ | 71 |
| 0 |   | 50 |
| 2 | 0 | 44 |
| 1 | 2 | 42 |
| 2 | 1 | 41 |
| i | ∅ | 38 |
| 5 | ∅ | 33 |
| 0 | 1 | 32 |
| 0 | 8 | 30 |
| 1 |   | 28 |
| 2 |   | 28 |
| 1 | ۔ | 26 |
| 9 | ∅ | 25 |
| a | ∅ | 24 |
| 7 | ∅ | 23 |
| 3 | ∅ | 22 |
| 2 | 9 | 21 |

### Worst 15 lines: utrnet_large_w400_val

| CER | crop | gold | pred |
|---|---|---|---|
| 2.50 | lines/AJK_0429_p01_L26.png | 31 | مورعع |
| 2.00 | lines/AJK_0484_p01_L26.png | ☆ | 77 |
| 2.00 | lines/AJK_0475_p01_L43.png | W | 44 |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | 99 |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | 4۔ |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | 4۔ |
| 2.00 | lines/AJK_0056_p01_L27.png | 3 | 4۔ |
| 1.54 | lines/AJK_0139_p02_L70.png | وسر ک انفار میشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔ | ڈسٹرکٹ انفاریشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔اسٹیشن ڈائریکٹرصاحب انیوزایڈیٹرصاحب آزادکشمیرریڈیومیرپوررتر اڑکھل مظفرآباد |
| 1.50 | lines/AJK_0448_p01_L24.png | _4 | 7ے۔ |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.30 | lines/AJK_0079_p01_L17.png | ا فار اللہ اللہ اللہ اللہ اللہ اللہ اللہ الل | 4۔ ڈسٹرکٹ انفاریشن آفیسرصاحب میرپور برائے اشاعت بطورخبردرقومی اخبارات۔ |
| 1.14 | lines/AJK_0023_p01_L25.png | 01-10-26 2026/ | 22216 مورخہ 26 -ے 8ر |
| 1.13 | lines/AJK_0148_p01_L07.png | 26-03-2025 3111 | امورخہ ک4ےو۔ر -گ6 |
| 1.07 | lines/AJK_0416_p01_L19.png | 05/01/2022 315 | مورخہ 2212/"ہ/ کھ |
| 1.00 | lines/AJK_0521_p01_L27.png | رپیل شاف، در رپرائیدین نیکر فری ہمراہ جناب بیکر فری با نیرا بع - ن.پرائیدین بیکر فری ہمراہ جناب بیکر فری المینی کوشنجناب چیئر شن 10 زاد جمول و کشمیر بورد آف اظرمیذیت و میکنداری تعلقی بورد چیر پورمسلم احسام مرکادی تبعی | ے |

### Top character confusions on Urdu lines: utrnet_large_w400_val_pp

ref → pred (∅ = missing / extra)

| ref | pred | count |
|---|---|---|
|   | ∅ | 3227 |
| ∅ |   | 527 |
| ا | ∅ | 285 |
| م | ∅ | 225 |
| ر | ∅ | 221 |
| ی | ∅ | 195 |
| و | د | 181 |
| ن | ∅ | 147 |
| ل | ∅ | 144 |
| د | ∅ | 120 |
| ∅ | ی | 118 |
| / | ا | 117 |
| ی | پ | 116 |
| ب | پ | 114 |
| ک | ∅ | 114 |
| و | ∅ | 113 |
| ہ | ∅ | 104 |
| - | ۔ | 104 |
| ∅ | ا | 99 |
|   | ر | 92 |

### Top confusions on digit / Latin characters: utrnet_large_w400_val_pp

reference digit or Latin letter → pred, plus insertions on digit-only / Latin-only lines

| ref | pred | count |
|---|---|---|
| 0 | ∅ | 129 |
| 0 | 2 | 123 |
| 2 | ∅ | 76 |
| 1 | ∅ | 72 |
| 0 |   | 52 |
| 2 | 0 | 43 |
| 1 | 2 | 39 |
| 2 | 1 | 37 |
| i | ∅ | 37 |
| 5 | ∅ | 33 |
| 0 | 1 | 32 |
| 1 |   | 28 |
| 0 | 8 | 28 |
| 3 | ∅ | 25 |
| 9 | ∅ | 24 |
| 2 |   | 24 |
| a | ∅ | 24 |
| 7 | ∅ | 23 |
| 2 | 9 | 20 |
| 0 | 9 | 20 |

### Worst 15 lines: utrnet_large_w400_val_pp

| CER | crop | gold | pred |
|---|---|---|---|
| 2.50 | lines/AJK_0429_p01_L26.png | 31 | مورعع |
| 2.00 | lines/AJK_0484_p01_L26.png | ☆ | 77 |
| 2.00 | lines/AJK_0475_p01_L43.png | W | 44 |
| 2.00 | lines/AJK_0352_p01_L08.png | 4 | 99 |
| 2.00 | lines/AJK_0351_p01_L16.png | 3 | -4 |
| 2.00 | lines/AJK_0106_p01_L15.png | 7 | -4 |
| 2.00 | lines/AJK_0056_p01_L27.png | 3 | -4 |
| 1.54 | lines/AJK_0139_p02_L70.png | وسر ک انفار میشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔ | ڈسٹرکٹ انفاریشن آفیسرصاحب میرپوربغرض اشاعت بطورخبر۔اسٹیشن ڈائریکٹرصاحب انیوزایڈیٹرصاحب آزادکشمیرریڈیومیرپوررتر اڑکھل مظفرآباد |
| 1.50 | lines/AJK_0448_p01_L24.png | _4 | 7ے۔ |
| 1.33 | lines/AJK_0475_p01_L74.png | iii | ققلا |
| 1.30 | lines/AJK_0079_p01_L17.png | ا فار اللہ اللہ اللہ اللہ اللہ اللہ اللہ الل | 4۔ ڈسٹرکٹ انفاریشن آفیسرصاحب میرپور برائے اشاعت بطورخبردرقومی اخبارات۔ |
| 1.14 | lines/AJK_0023_p01_L25.png | 01-10-26 2026/ | 22216 مورخہ 26 -ے 8ر |
| 1.13 | lines/AJK_0148_p01_L07.png | 26-03-2025 3111 | امورخہ ک4ےو۔ر -گ6 |
| 1.07 | lines/AJK_0416_p01_L19.png | 05/01/2022 315 | مورخہ 2212/"ہ/ کھ |
| 1.00 | lines/AJK_0521_p01_L27.png | رپیل شاف، در رپرائیدین نیکر فری ہمراہ جناب بیکر فری با نیرا بع - ن.پرائیدین بیکر فری ہمراہ جناب بیکر فری المینی کوشنجناب چیئر شن 10 زاد جمول و کشمیر بورد آف اظرمیذیت و میکنداری تعلقی بورد چیر پورمسلم احسام مرکادی تبعی | ے |

### Suspect references (not scored; awaiting human correction)

Flagged by a heuristic (see eval_ocr.py docstring), not proof that each reference is wrong. Each line is scored again once a reviewer confirms or corrects it (--verified), or always with --keep-suspect.

| crop | reason | reference |
|---|---|---|
| lines/AJK_0102_p01_L08.png | CJK / kana characters | でいっというというというには しいかいかんとしないのとはいいい |
| lines/AJK_0102_p01_L51.png | CJK / kana characters | いるからいというなとないいいととないしんなきというというないといいのアフリスタアといると |
| lines/AJK_0429_p01_L08.png | CJK / kana characters | からいというかんな |
| lines/AJK_0429_p01_L09.png | CJK / kana characters | もならうでもかってもっと |
| lines/AJK_0475_p01_L69.png | no letters or digits | ۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔ |
