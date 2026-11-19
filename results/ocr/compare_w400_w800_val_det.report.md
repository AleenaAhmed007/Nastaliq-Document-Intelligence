# OCR evaluation

Systems: utrnet_large_w400_val_det, utrnet_large_w800_val_det  
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

### By split

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val | utrnet_large_w400_val_det | 1432 | 23.2 | 20.0 | 72.3 | 0.360 | 4.7 |
| val | utrnet_large_w800_val_det | 1432 | 21.3 | 18.8 | 64.7 | 0.353 | 4.5 |

### By split x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / photo | utrnet_large_w400_val_det | 813 | 23.7 | 20.4 | 73.3 | 0.342 | 5.4 |
| val / photo | utrnet_large_w800_val_det | 813 | 21.7 | 19.2 | 65.7 | 0.334 | 5.3 |
| val / scan | utrnet_large_w400_val_det | 619 | 22.6 | 19.5 | 70.8 | 0.384 | 3.9 |
| val / scan | utrnet_large_w800_val_det | 619 | 20.8 | 18.4 | 63.5 | 0.378 | 3.6 |

### By category

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field | utrnet_large_w400_val_det | 105 | 22.9 | 19.8 | 70.9 | 0.333 | 1.0 |
| val / hw_field | utrnet_large_w800_val_det | 105 | 20.4 | 17.9 | 62.9 | 0.320 | 1.9 |
| val / num_latin | utrnet_large_w400_val_det | 367 | 77.8 | 78.0 | 107.6 | 0.762 | 0.5 |
| val / num_latin | utrnet_large_w800_val_det | 367 | 78.0 | 78.1 | 108.1 | 0.762 | 0.5 |
| val / urdu | utrnet_large_w400_val_det | 960 | 21.6 | 18.0 | 71.2 | 0.209 | 6.8 |
| val / urdu | utrnet_large_w800_val_det | 960 | 19.7 | 16.8 | 63.5 | 0.200 | 6.4 |

### By content

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val_det | 295 | 75.8 | 74.8 | 108.8 | 0.778 | 0.7 |
| val / digits_only | utrnet_large_w800_val_det | 295 | 76.0 | 75.1 | 109.1 | 0.781 | 0.7 |
| val / latin_only | utrnet_large_w400_val_det | 92 | 81.0 | 82.5 | 112.3 | 0.699 | 0.0 |
| val / latin_only | utrnet_large_w800_val_det | 92 | 81.1 | 82.5 | 111.0 | 0.693 | 0.0 |
| val / other | utrnet_large_w400_val_det | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / other | utrnet_large_w800_val_det | 3 | 120.0 | 120.0 | 100.0 | 1.000 | 0.0 |
| val / urdu+digits | utrnet_large_w400_val_det | 343 | 22.9 | 18.9 | 75.0 | 0.250 | 0.0 |
| val / urdu+digits | utrnet_large_w800_val_det | 343 | 20.4 | 17.5 | 66.1 | 0.235 | 0.0 |
| val / urdu+latin | utrnet_large_w400_val_det | 122 | 27.2 | 24.4 | 74.2 | 0.281 | 0.0 |
| val / urdu+latin | utrnet_large_w800_val_det | 122 | 24.5 | 22.2 | 65.7 | 0.260 | 0.0 |
| val / urdu_only | utrnet_large_w400_val_det | 577 | 18.1 | 14.5 | 66.3 | 0.171 | 11.4 |
| val / urdu_only | utrnet_large_w800_val_det | 577 | 16.8 | 13.9 | 59.8 | 0.167 | 10.9 |

### By aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / 12.5-25 | utrnet_large_w400_val_det | 376 | 21.6 | 18.1 | 71.3 | 0.230 | 0.8 |
| val / 12.5-25 | utrnet_large_w800_val_det | 376 | 19.9 | 17.1 | 63.6 | 0.218 | 0.5 |
| val / <=12.5 | utrnet_large_w400_val_det | 947 | 30.6 | 28.8 | 75.9 | 0.432 | 6.9 |
| val / <=12.5 | utrnet_large_w800_val_det | 947 | 30.5 | 28.8 | 76.0 | 0.432 | 6.7 |
| val / >25 | utrnet_large_w400_val_det | 109 | 17.4 | 12.5 | 69.7 | 0.179 | 0.0 |
| val / >25 | utrnet_large_w800_val_det | 109 | 12.7 | 9.3 | 53.5 | 0.134 | 0.0 |

### By category x aspect

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / 12.5-25 | utrnet_large_w400_val_det | 51 | 20.9 | 17.8 | 68.5 | 0.244 | 0.0 |
| val / hw_field / 12.5-25 | utrnet_large_w800_val_det | 51 | 18.7 | 16.1 | 60.7 | 0.224 | 0.0 |
| val / hw_field / <=12.5 | utrnet_large_w400_val_det | 48 | 35.8 | 34.9 | 80.3 | 0.441 | 2.1 |
| val / hw_field / <=12.5 | utrnet_large_w800_val_det | 48 | 35.5 | 35.0 | 78.3 | 0.442 | 4.2 |
| val / hw_field / >25 | utrnet_large_w400_val_det | 6 | 21.0 | 14.8 | 75.5 | 0.224 | 0.0 |
| val / hw_field / >25 | utrnet_large_w800_val_det | 6 | 15.3 | 9.7 | 62.2 | 0.164 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w400_val_det | 10 | 86.3 | 89.5 | 121.6 | 0.848 | 0.0 |
| val / num_latin / 12.5-25 | utrnet_large_w800_val_det | 10 | 88.5 | 90.9 | 121.6 | 0.872 | 0.0 |
| val / num_latin / <=12.5 | utrnet_large_w400_val_det | 356 | 76.1 | 75.9 | 106.2 | 0.759 | 0.6 |
| val / num_latin / <=12.5 | utrnet_large_w800_val_det | 356 | 75.8 | 75.5 | 106.4 | 0.759 | 0.6 |
| val / num_latin / >25 | utrnet_large_w400_val_det | 1 | 87.3 | 89.6 | 112.5 | 0.873 | 0.0 |
| val / num_latin / >25 | utrnet_large_w800_val_det | 1 | 90.9 | 97.9 | 125.0 | 0.909 | 0.0 |
| val / urdu / 12.5-25 | utrnet_large_w400_val_det | 315 | 21.1 | 17.4 | 71.5 | 0.209 | 1.0 |
| val / urdu / 12.5-25 | utrnet_large_w800_val_det | 315 | 19.4 | 16.5 | 63.7 | 0.196 | 0.6 |
| val / urdu / <=12.5 | utrnet_large_w400_val_det | 543 | 26.3 | 23.7 | 72.5 | 0.217 | 11.4 |
| val / urdu / <=12.5 | utrnet_large_w800_val_det | 543 | 26.2 | 23.7 | 72.6 | 0.217 | 10.9 |
| val / urdu / >25 | utrnet_large_w400_val_det | 102 | 16.9 | 12.1 | 69.3 | 0.169 | 0.0 |
| val / urdu / >25 | utrnet_large_w800_val_det | 102 | 12.3 | 9.0 | 52.8 | 0.124 | 0.0 |

### By category x type

| group | system | lines | CER % | CER_nosp % | WER % | NED | exact % |
|---|---|---|---|---|---|---|---|
| val / hw_field / photo | utrnet_large_w400_val_det | 56 | 21.2 | 17.6 | 70.3 | 0.279 | 0.0 |
| val / hw_field / photo | utrnet_large_w800_val_det | 56 | 18.7 | 15.8 | 60.9 | 0.262 | 0.0 |
| val / hw_field / scan | utrnet_large_w400_val_det | 49 | 27.3 | 25.2 | 72.6 | 0.395 | 2.0 |
| val / hw_field / scan | utrnet_large_w800_val_det | 49 | 25.0 | 23.1 | 68.7 | 0.387 | 4.1 |
| val / num_latin / photo | utrnet_large_w400_val_det | 199 | 76.7 | 77.2 | 107.2 | 0.720 | 1.0 |
| val / num_latin / photo | utrnet_large_w800_val_det | 199 | 76.5 | 77.1 | 107.2 | 0.719 | 1.0 |
| val / num_latin / scan | utrnet_large_w400_val_det | 168 | 79.9 | 79.5 | 108.1 | 0.810 | 0.0 |
| val / num_latin / scan | utrnet_large_w800_val_det | 168 | 80.7 | 79.9 | 109.2 | 0.814 | 0.0 |
| val / urdu / photo | utrnet_large_w400_val_det | 558 | 22.2 | 18.5 | 72.6 | 0.213 | 7.5 |
| val / urdu / photo | utrnet_large_w800_val_det | 558 | 20.2 | 17.3 | 64.9 | 0.204 | 7.3 |
| val / urdu / scan | utrnet_large_w400_val_det | 402 | 20.9 | 17.3 | 69.5 | 0.204 | 5.7 |
| val / urdu / scan | utrnet_large_w800_val_det | 402 | 19.0 | 16.2 | 61.7 | 0.195 | 5.0 |

### Error types by content

S / D / I = substitutions / deletions / insertions as % of reference characters (they add up to CER).

| group | system | lines | ref chars | avg ref len | avg pred len | CER % | S % | D % | I % |
|---|---|---|---|---|---|---|---|---|---|
| val / digits_only | utrnet_large_w400_val_det | 295 | 1444 | 4.9 | 4.2 | 75.8 | 53.7 | 18.1 | 3.9 |
| val / digits_only | utrnet_large_w800_val_det | 295 | 1444 | 4.9 | 4.2 | 76.0 | 53.4 | 18.6 | 3.9 |
| val / latin_only | utrnet_large_w400_val_det | 92 | 962 | 10.5 | 7.7 | 81.0 | 53.3 | 27.0 | 0.6 |
| val / latin_only | utrnet_large_w800_val_det | 92 | 962 | 10.5 | 7.5 | 81.1 | 50.8 | 29.4 | 0.8 |
| val / other | utrnet_large_w400_val_det | 3 | 5 | 1.7 | 1.7 | 120.0 | 80.0 | 20.0 | 20.0 |
| val / other | utrnet_large_w800_val_det | 3 | 5 | 1.7 | 1.7 | 120.0 | 80.0 | 20.0 | 20.0 |
| val / urdu+digits | utrnet_large_w400_val_det | 343 | 29793 | 86.9 | 81.2 | 22.9 | 10.8 | 9.3 | 2.8 |
| val / urdu+digits | utrnet_large_w800_val_det | 343 | 29793 | 86.9 | 82.6 | 20.4 | 10.0 | 7.7 | 2.7 |
| val / urdu+latin | utrnet_large_w400_val_det | 122 | 13318 | 109.2 | 102.6 | 27.2 | 15.1 | 9.1 | 3.0 |
| val / urdu+latin | utrnet_large_w800_val_det | 122 | 13318 | 109.2 | 103.3 | 24.5 | 13.4 | 8.2 | 2.8 |
| val / urdu_only | utrnet_large_w400_val_det | 577 | 34080 | 59.1 | 56.0 | 18.1 | 7.9 | 7.7 | 2.5 |
| val / urdu_only | utrnet_large_w800_val_det | 577 | 34080 | 59.1 | 56.9 | 16.8 | 7.6 | 6.4 | 2.8 |

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

### Suspect references (not scored; awaiting human correction)

Flagged by a heuristic (see eval_ocr.py docstring), not proof that each reference is wrong. Each line is scored again once a reviewer confirms or corrects it (--verified), or always with --keep-suspect.

| crop | reason | reference |
|---|---|---|
| lines/AJK_0102_p01_L08.png | CJK / kana characters | でいっというというというには しいかいかんとしないのとはいいい |
| lines/AJK_0102_p01_L51.png | CJK / kana characters | いるからいというなとないいいととないしんなきというというないといいのアフリスタアといると |
| lines/AJK_0429_p01_L08.png | CJK / kana characters | からいというかんな |
| lines/AJK_0429_p01_L09.png | CJK / kana characters | もならうでもかってもっと |
| lines/AJK_0475_p01_L69.png | no letters or digits | ۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔۔ |
