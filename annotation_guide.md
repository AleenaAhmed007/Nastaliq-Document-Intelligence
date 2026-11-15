# Annotation guide (Nastaliq Document Intelligence)

Ye guide poori team ke liye ek hi hai. Rule badalna ho to sab ko batao aur purane pages dobara check karo.

## Setup (ek baar)
```powershell
pip install label-studio
$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED = "true"
$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT = "T:\nastaliq"     # wo folder jis ke andar pages\ hai
label-studio start
```
1. Browser mein project banao, Labeling Setup -> Custom template -> `labelstudio_config.xml` paste karo.
2. `python make_tasks.py` chalao, phir `tasks.json` ko project mein Import karo.
3. Agar images load na hon: Project Settings -> Cloud Storage -> Add Source Storage -> Local Files, absolute path `T:\nastaliq\pages\images`.
4. Data Manager mein `pass2` column se filter karo (1 = line transcription bhi karni hai).

## Pass 1: boxes + fields (sab pages)
Har page par ye boxes lagao. Box ink ke bilkul qareeb ho, bohat khula nahi.

| Label | Kya cover kare | Text likhna? |
|---|---|---|
| header_department | board/department ka naam wali header lines | Haan, naam jaisa likha hai |
| reference_no | sirf number wali string (e.g. `37/8-28`), "نمبر" lafz ke baghair | Haan |
| date | sirf date string, "مورخہ" ke baghair | Haan |
| subject | "موضوع/برائے" wali line. Agar aisi line nahi to notice ka title (e.g. پریس ریلیز) aur flag `implicit_subject` | Haan |
| body | main paragraph(s) | Nahi |
| table | poora table | Nahi |
| stamp_signature | stamp ya signature | Nahi |
| distribution_list | "نقل بالا بخدمت" wali list | Nahi |

**Text ke rules**
- Jo likha hai wahi type karo. Digits convert mat karo (Urdu digit ho to Urdu, Western ho to Western).
- Original ki spelling mistake bhi rakho. Sahi mat karo.
- Handwritten ho to box flag `handwritten`. Stamp ke neeche ho to `stamp_over`. Parh na sako to `unclear` aur text mein jitna parh sako likho.
- Field page par nahi hai to box mat lagao aur page flag lagao: `no_date`, `no_reference_no`, `no_subject`. Bhoolne aur "hai hi nahi" mein farq export report mein dikhega.
- Ek field ke liye ek hi box. Agar do date hain (jaise tareekh issue aur tareekh event), jo header/footer mein document ki date hai wo `date` hai.

**Page flags**
- `contains_personal_data`: student ka naam/roll number/result list wala page. Is par kuch annotate mat karo, bas flag lagao. Ye page dataset se nikal diya jayega.
- `skip_bad_image`: itna kharab ke parha hi na jaye.

## Pass 2: line transcription (sirf `pass2 = 1` pages)
1. Body, header aur list ki har text line par alag `text_line` box lagao (hotkey `t`).
2. Har box ka text type karo, isi tareeqe se jaisa image mein hai. Ek box = ek line.
3. Kisi model ka draft paste karo to **har line khud parho aur theek karo**. Aur private pages kisi external model ko mat bhejo.

## Quality
- 20 pages do logon se annotate karwao (alag projects ya alag copies) aur boxes ka overlap aur field text ka exact match dekho. Match kam ho to guideline theek karo.
- Test pages bhi utni hi tawajjoh se karo jitni train pages. Final numbers inhi se aayenge.
- Har din Export -> JSON (JSON-MIN nahi) karke backup rakho.

## Export
```powershell
python export_to_json.py --export export.json --out dataset --doc-root . --crops
```
`dataset\report.txt` ke warnings zaroor parho: missing field, khali text, bohat chhote boxes.
