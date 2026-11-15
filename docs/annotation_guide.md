# Annotation Guide (Nastaliq Document Intelligence)

This guide applies to the whole team. If a rule needs to change, tell everyone and review the pages annotated under the old rule.

## Setup (once)
```powershell
pip install label-studio
$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED = "true"
$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT = "T:\\nastaliq"     # The folder that contains pages\
label-studio start
```
1. Create a project in your browser. Go to **Labeling Setup -> Custom template** and paste in `labelstudio_config.xml`.
2. Run `python make_tasks.py`, then import `tasks.json` into the project.
3. If the images do not load, go to **Project Settings -> Cloud Storage -> Add Source Storage -> Local Files** and enter the absolute path `T:\\nastaliq\\pages\\images`.
4. In **Data Manager**, filter by the `pass2` column (`1` means line transcription is also required).

## Pass 1: Boxes and fields (all pages)
Add the following boxes to every page. Keep each box close to the ink; do not make it unnecessarily large.

| Label | What to cover | Enter text? |
|---|---|---|
| `header_department` | Header lines containing the board or department name | Yes, exactly as written |
| `reference_no` | Only the reference number string (e.g. `37/8-28`), without the word “نمبر” | Yes |
| `date` | Only the date string, without the word “مورخہ” | Yes |
| `subject` | The line labeled “موضوع/برائے”. If there is no such line, use the notice title (e.g. “پریس ریلیز”) and set the `implicit_subject` flag | Yes |
| `body` | The main paragraph(s) | No |
| `table` | The entire table | No |
| `stamp_signature` | A stamp or signature | No |
| `distribution_list` | The list labeled “نقل بالا بخدمت” | No |

**Text rules**
- Type exactly what is written. Do not convert digits: use Urdu digits if the image has Urdu digits, and Western digits if it has Western digits.
- Preserve spelling mistakes from the original. Do not correct them.
- If text is handwritten, set the `handwritten` box flag. If it is under a stamp, set `stamp_over`. If you cannot read it, set `unclear` and type as much as you can read.
- If a field is absent from the page, do not add a box; set the corresponding page flag: `no_date`, `no_reference_no`, or `no_subject`. The export report distinguishes a forgotten field from one that is genuinely absent.
- Use only one box for each field. If there are two dates (for example, an issue date and an event date), label the document date in the header or footer as `date`.

**Page flags**
- `contains_personal_data`: Use for a page containing a student's name, roll number, or results list. Do not annotate that page; just set the flag. It will be excluded from the dataset.
- `skip_bad_image`: Use when the image is so poor that it cannot be read.

## Pass 2: Line transcription (only pages where `pass2 = 1`)
1. Add a separate `text_line` box to every text line in the body, header, and list (hotkey `t`).
2. Type the text for each box exactly as it appears in the image. One box = one line.
3. If you paste a model's draft, read and correct every line yourself. Do not send private pages to an external model.

## Quality
- Have two people annotate the same 20 pages (in separate projects or copies). Compare box overlap and exact field-text matches. If agreement is low, revise the guidelines.
- Give test pages as much attention as training pages. The final metrics will be calculated from the test pages.
- Export to JSON (**Export -> JSON**, not **JSON-MIN**) every day and keep a backup.

## Export
```powershell
python export_to_json.py --export export.json --out dataset --doc-root . --crops
```
Be sure to read the warnings in `dataset\\report.txt`: they include missing fields, empty text, and boxes that are too small.
