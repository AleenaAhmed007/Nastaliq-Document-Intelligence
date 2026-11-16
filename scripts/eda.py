"""
EDA — Nastaliq Document Intelligence
Run from repo root:  py -3.14 scripts/eda.py
Outputs:  data/eda/  (PNG plots + eda_summary.txt)
"""

import json, os, sys, collections, textwrap
import pandas as pd
import numpy as np

# ── paths ──────────────────────────────────────────────────────────────────
ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSONL      = os.path.join(ROOT, "data", "processed", "all_pages.jsonl")
MANIFEST   = os.path.join(ROOT, "data", "interim", "manifest.csv")
PRIVACY_REVIEW = os.path.join(ROOT, "data", "interim", "review_personal_data.csv")
OUT_DIR    = os.path.join(ROOT, "data", "eda")
os.makedirs(OUT_DIR, exist_ok=True)

# ── load data ──────────────────────────────────────────────────────────────
pages = [json.loads(l) for l in open(JSONL, encoding="utf-8")]
mf    = pd.read_csv(MANIFEST)
review = pd.read_csv(PRIVACY_REVIEW)
if "file" not in review.columns:
    raise ValueError(f"{PRIVACY_REVIEW} must contain a 'file' column")

total_documents = int(mf["doc_id"].nunique())
flagged_documents = int(review["file"].dropna().astype(str).nunique())
if flagged_documents > total_documents:
    raise ValueError("Personal-data review file count exceeds the manifest document count")
not_flagged_documents = total_documents - flagged_documents

print(f"Loaded {len(pages)} pages from JSONL, {len(mf)} rows from manifest")

# ── try matplotlib; fall back gracefully ──────────────────────────────────
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    HAS_MPL = True
except ImportError:
    HAS_MPL = False
    print("matplotlib not installed — skipping plots, text summary only")

COLORS = {
    "train": "#4C72B0", "val": "#DD8452",
    "test": "#55A868",  "test_unseen": "#C44E52",
}

def savefig(name):
    path = os.path.join(OUT_DIR, name)
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()
    print(f"  saved → {path}")

# ═══════════════════════════════════════════════════════════════════════════
# 1.  PAGES BY SPLIT
# ═══════════════════════════════════════════════════════════════════════════
splits = mf["split"].value_counts().reindex(
    ["train", "val", "test", "test_unseen"], fill_value=0)
print("\n--- 1. Split distribution ---")
for k, v in splits.items():
    print(f"  {k:14s}: {v:4d}  ({v/len(mf)*100:.1f}%)")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(splits.index, splits.values,
                  color=[COLORS[s] for s in splits.index])
    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 4,
                str(int(b.get_height())), ha="center", fontsize=10, fontweight="bold")
    ax.set_title("Pages per Split", fontsize=14)
    ax.set_ylabel("Count"); ax.set_xlabel("Split")
    savefig("01_split_distribution.png")

# ═══════════════════════════════════════════════════════════════════════════
# 2.  CAPTURE TYPE  (scan / photo / digital)
# ═══════════════════════════════════════════════════════════════════════════
types = mf["type"].value_counts()
print("\n--- 2. Capture type ---")
for k, v in types.items():
    print(f"  {k:10s}: {v:4d}  ({v/len(mf)*100:.1f}%)")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.bar(types.index, types.values, color=["#4C72B0","#DD8452","#55A868"])
    for i, v in enumerate(types.values):
        ax.text(i, v + 2, str(v), ha="center", fontsize=10, fontweight="bold")
    ax.set_title("Pages by Capture Type", fontsize=14)
    ax.set_ylabel("Count"); ax.set_xlabel("Type")
    savefig("02_capture_type.png")

# ═══════════════════════════════════════════════════════════════════════════
# 3.  SOURCE  (AJK / FBR)
# ═══════════════════════════════════════════════════════════════════════════
srcs = mf["source"].value_counts()
print("\n--- 3. Source ---")
for k, v in srcs.items():
    print(f"  {k:10s}: {v:4d}  ({v/len(mf)*100:.1f}%)")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.pie(srcs.values, labels=srcs.index, autopct="%1.1f%%",
           colors=["#4C72B0","#DD8452"], startangle=90)
    ax.set_title("Source Distribution", fontsize=14)
    savefig("03_source_distribution.png")

# ═══════════════════════════════════════════════════════════════════════════
# 4.  LOW-RES  FLAG
# ═══════════════════════════════════════════════════════════════════════════
lr = mf["low_res"].value_counts().reindex([0, 1], fill_value=0)
print(f"\n--- 4. Low-res pages ---")
print(f"  Normal  : {lr[0]:4d}")
print(f"  Low-res : {lr[1]:4d}  ({lr[1]/len(mf)*100:.1f}%)")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie([lr[0], lr[1]], labels=["Normal", "Low-res"],
           autopct="%1.1f%%", colors=["#55A868","#C44E52"])
    ax.set_title("Low-Resolution Pages", fontsize=14)
    savefig("04_low_res.png")

# ═══════════════════════════════════════════════════════════════════════════
# 5.  LOW-RES  BY SPLIT  (stretch-goal relevant)
# ═══════════════════════════════════════════════════════════════════════════
print("\n--- 5. Low-res per split ---")
lr_split = mf.groupby("split")["low_res"].agg(["sum","count"])
lr_split["pct"] = lr_split["sum"] / lr_split["count"] * 100
for s, row in lr_split.iterrows():
    print(f"  {s:14s}: {int(row['sum']):3d}/{int(row['count']):3d}  ({row['pct']:.1f}%)")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(6, 4))
    sp_order = ["train","val","test","test_unseen"]
    vals = [lr_split.loc[s,"pct"] if s in lr_split.index else 0 for s in sp_order]
    ax.bar(sp_order, vals, color=[COLORS[s] for s in sp_order])
    ax.set_title("% Low-res Pages per Split", fontsize=14)
    ax.set_ylabel("Percent low-res"); ax.set_ylim(0, 100)
    savefig("05_lowres_per_split.png")

# ═══════════════════════════════════════════════════════════════════════════
# 6.  FIELD PRESENCE  (date / department / subject / ref_no)
# ═══════════════════════════════════════════════════════════════════════════
FIELDS = ["date", "department", "subject", "reference_no"]
field_pres = {f: 0 for f in FIELDS}
field_pres_by_split = {s: {f: 0 for f in FIELDS} for s in ["train","val","test","test_unseen"]}
split_counts = collections.Counter()

for p in pages:
    sp = p.get("split", "train")
    split_counts[sp] += 1
    flds = p.get("fields", {})
    for f in FIELDS:
        v = flds.get(f, "")
        if v and str(v).strip():
            field_pres[f] += 1
            if sp in field_pres_by_split:
                field_pres_by_split[sp][f] += 1

print("\n--- 6. Field presence (overall) ---")
for f in FIELDS:
    pct = field_pres[f] / len(pages) * 100
    print(f"  {f:15s}: {field_pres[f]:4d}/{len(pages)}  ({pct:.1f}%)")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(7, 4))
    vals = [field_pres[f]/len(pages)*100 for f in FIELDS]
    bars = ax.bar(FIELDS, vals, color=["#4C72B0","#DD8452","#55A868","#C44E52"])
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width()/2, v + 1,
                f"{v:.1f}%", ha="center", fontsize=10, fontweight="bold")
    ax.set_title("Field Presence Rate (all 789 pages)", fontsize=14)
    ax.set_ylabel("% pages with field"); ax.set_ylim(0, 110)
    savefig("06_field_presence.png")

# ═══════════════════════════════════════════════════════════════════════════
# 7.  FIELD PRESENCE  BY SPLIT  (grouped bar)
# ═══════════════════════════════════════════════════════════════════════════
print("\n--- 7. Field presence per split ---")
sp_order = ["train","val","test","test_unseen"]
print(f"  {'split':14s} " + "  ".join(f"{f[:8]:>8}" for f in FIELDS))
for sp in sp_order:
    n = split_counts[sp] or 1
    row = "  ".join(f"{field_pres_by_split[sp].get(f,0)/n*100:7.1f}%" for f in FIELDS)
    print(f"  {sp:14s} {row}")

if HAS_MPL:
    x = np.arange(len(FIELDS))
    width = 0.2
    fig, ax = plt.subplots(figsize=(9, 5))
    for i, sp in enumerate(sp_order):
        n = split_counts[sp] or 1
        vals = [field_pres_by_split[sp].get(f,0)/n*100 for f in FIELDS]
        ax.bar(x + i*width, vals, width, label=sp, color=COLORS[sp])
    ax.set_xticks(x + width*1.5); ax.set_xticklabels(FIELDS)
    ax.set_title("Field Presence % per Split", fontsize=14)
    ax.set_ylabel("% pages with field"); ax.set_ylim(0, 115)
    ax.legend(); savefig("07_field_presence_by_split.png")

# ═══════════════════════════════════════════════════════════════════════════
# 8.  REGION  (box) LABEL DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════════
label_counts = collections.Counter()
box_per_page = []
for p in pages:
    regs = p.get("regions", [])
    box_per_page.append(len(regs))
    for r in regs:
        lbl = r.get("label", "unknown")
        label_counts[lbl] += 1

total_boxes = sum(label_counts.values())
print(f"\n--- 8. Region label distribution (total boxes: {total_boxes}) ---")
for lbl, cnt in label_counts.most_common():
    print(f"  {lbl:20s}: {cnt:5d}  ({cnt/total_boxes*100:.1f}%)")

if HAS_MPL:
    lbls, cnts = zip(*label_counts.most_common()) if label_counts else ([], [])
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.barh(list(reversed(lbls)), list(reversed(cnts)), color="#4C72B0")
    ax.set_title("Box Count per Label Class", fontsize=14)
    ax.set_xlabel("Number of boxes")
    savefig("08_label_distribution.png")

# ═══════════════════════════════════════════════════════════════════════════
# 9.  BOXES PER PAGE  distribution
# ═══════════════════════════════════════════════════════════════════════════
bpp = np.array(box_per_page)
print(f"\n--- 9. Boxes per page ---")
print(f"  min={bpp.min()}  max={bpp.max()}  mean={bpp.mean():.1f}  median={np.median(bpp):.0f}")
print(f"  Pages with 0 boxes : {(bpp==0).sum()}")
print(f"  Pages with 1-3     : {((bpp>=1)&(bpp<=3)).sum()}")
print(f"  Pages with 4-9     : {((bpp>=4)&(bpp<=9)).sum()}")
print(f"  Pages with 10+     : {(bpp>=10).sum()}")

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(bpp, bins=range(0, bpp.max()+2), color="#4C72B0", edgecolor="white")
    ax.set_title("Distribution of Boxes per Page", fontsize=14)
    ax.set_xlabel("Boxes per page"); ax.set_ylabel("Number of pages")
    savefig("09_boxes_per_page.png")

# ═══════════════════════════════════════════════════════════════════════════
# 10. BOX SIZE  (w × h as % of page)  per label
# ═══════════════════════════════════════════════════════════════════════════
box_areas = collections.defaultdict(list)
for p in pages:
    pw, ph = p.get("width", 1), p.get("height", 1)
    for r in p.get("regions", []):
        lbl = r.get("label", "unknown")
        bbox = r.get("bbox")          # format: [x, y, w, h]  absolute pixels
        if not bbox or len(bbox) < 4:
            continue
        bx, by, bw, bh = bbox
        if bw <= 0 or bh <= 0 or pw <= 0 or ph <= 0:
            continue
        area_pct = (bw * bh) / (pw * ph) * 100   # area as % of page
        box_areas[lbl].append(area_pct)

print("\n--- 10. Median box area (% of page area) per label ---")
for lbl, areas in sorted(box_areas.items(), key=lambda x: -np.median(x[1])):
    print(f"  {lbl:20s}: median={np.median(areas):6.3f}%  n={len(areas)}")

if HAS_MPL:
    lbls_sorted = sorted(box_areas.keys(), key=lambda l: -np.median(box_areas[l]))
    data_sorted = [box_areas[l] for l in lbls_sorted]
    fig, ax = plt.subplots(figsize=(10, 5))
    bp = ax.boxplot(data_sorted, patch_artist=True, vert=True)
    for patch in bp["boxes"]:
        patch.set_facecolor("#4C72B0"); patch.set_alpha(0.7)
    ax.set_xticks(range(1, len(lbls_sorted)+1))
    ax.set_xticklabels(lbls_sorted, rotation=30, ha="right")
    ax.set_title("Box Area Distribution per Label (% of page area)", fontsize=14)
    ax.set_ylabel("Box area (% of page)")
    savefig("10_box_area_per_label.png")

# ═══════════════════════════════════════════════════════════════════════════
# 11. YEAR  DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════════
years = mf["year"].dropna().astype(int).value_counts().sort_index()
print("\n--- 11. Year distribution ---")
for y, cnt in years.items():
    print(f"  {y}: {cnt}")

if HAS_MPL and len(years):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(years.index.astype(str), years.values, color="#4C72B0")
    ax.set_title("Documents by Year", fontsize=14)
    ax.set_xlabel("Year"); ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    savefig("11_year_distribution.png")

# ═══════════════════════════════════════════════════════════════════════════
# 12. IMAGE RESOLUTION  distribution
# ═══════════════════════════════════════════════════════════════════════════
widths  = mf["width"].dropna().astype(int)
heights = mf["height"].dropna().astype(int)
print(f"\n--- 12. Resolution stats ---")
print(f"  Width : min={widths.min()}  max={widths.max()}  mean={widths.mean():.0f}")
print(f"  Height: min={heights.min()}  max={heights.max()}  mean={heights.mean():.0f}")

if HAS_MPL:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].hist(widths,  bins=30, color="#4C72B0", edgecolor="white")
    axes[0].set_title("Image Width Distribution"); axes[0].set_xlabel("px")
    axes[1].hist(heights, bins=30, color="#DD8452", edgecolor="white")
    axes[1].set_title("Image Height Distribution"); axes[1].set_xlabel("px")
    savefig("12_resolution.png")

# ═══════════════════════════════════════════════════════════════════════════
# 13. ANNOTATION SOURCE  (gold vs auto_heuristic vs gemini)
# ═══════════════════════════════════════════════════════════════════════════
ann_src = collections.Counter()
# triage.py ne annotate=1 set kiya → gold (Label Studio human)
# annotate=0                        → Gemini Vision ne annotate kiya
gold_ids = set(mf[mf["annotate"] == 1]["page_id"].tolist())

for p in pages:
    pid = p.get("page_id", "")
    if pid in gold_ids:
        ann_src["human_gold (Label Studio)"] += 1
    else:
        ann_src["gemini_vision"] += 1

print("\n--- 13. Annotation source ---")
for k, v in ann_src.most_common():
    print(f"  {k:30s}: {v:4d}  ({v/len(pages)*100:.1f}%)")

if HAS_MPL and ann_src:
    fig, ax = plt.subplots(figsize=(6, 5))
    colors = ["#55A868", "#4C72B0", "#DD8452"]
    wedges, texts, autotexts = ax.pie(
        ann_src.values(), labels=ann_src.keys(), autopct="%1.1f%%",
        colors=colors[:len(ann_src)], startangle=90)
    for t in autotexts:
        t.set_fontsize(11); t.set_fontweight("bold")
    ax.set_title("Annotation Source\n(Who annotated each page?)", fontsize=13)
    savefig("13_annotation_source.png")

# ═══════════════════════════════════════════════════════════════════════════
# 14.  FILES FLAGGED FOR PERSONAL-DATA REVIEW
# ═══════════════════════════════════════════════════════════════════════════
print("\n--- 14. Personal-data review candidates ---")
print(f"  flagged by filename: {flagged_documents}/{total_documents}")
print(f"  not flagged by filename: {not_flagged_documents}/{total_documents}")

if HAS_MPL and total_documents:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(
        [flagged_documents, not_flagged_documents],
        labels=[
            f"Flagged for review\n({flagged_documents})",
            f"Not filename-flagged\n({not_flagged_documents})",
        ],
        autopct="%1.1f%%",
        colors=["#C44E52", "#55A868"],
        startangle=90,
    )
    ax.set_title(
        "Files Flagged for Personal-Data Review\n(filename screening; not confirmed PII)",
        fontsize=12,
    )
    savefig("14_personal_data_review.png")

# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY  TEXT FILE
# ═══════════════════════════════════════════════════════════════════════════
summary_path = os.path.join(OUT_DIR, "eda_summary.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write("=== EDA Summary — Nastaliq Document Intelligence ===\n\n")
    f.write(f"Total pages        : {len(pages)}\n")
    f.write(f"Total documents    : {total_documents}\n")
    f.write(f"Total boxes        : {total_boxes}\n\n")

    f.write("--- Split ---\n")
    for k, v in splits.items():
        f.write(f"  {k:14s}: {v}\n")

    f.write("\n--- Capture type ---\n")
    for k, v in types.items():
        f.write(f"  {k:10s}: {v}\n")

    f.write("\n--- Source ---\n")
    for k, v in srcs.items():
        f.write(f"  {k:10s}: {v}\n")

    f.write(f"\n--- Low-res pages : {lr[1]} ({lr[1]/len(mf)*100:.1f}%) ---\n")

    f.write("\n--- Field presence ---\n")
    for fi in FIELDS:
        pct = field_pres[fi]/len(pages)*100
        f.write(f"  {fi:15s}: {field_pres[fi]:4d}/{len(pages)} ({pct:.1f}%)\n")

    f.write("\n--- Region labels ---\n")
    for lbl, cnt in label_counts.most_common():
        f.write(f"  {lbl:20s}: {cnt}\n")

    f.write("\n--- Boxes per page ---\n")
    f.write(f"  min={bpp.min()}  max={bpp.max()}  mean={bpp.mean():.1f}  median={np.median(bpp):.0f}\n")

    f.write("\n--- Annotation source ---\n")
    for k, v in ann_src.most_common():
        f.write(f"  {k:20s}: {v}\n")

    f.write("\n--- Personal-data review candidates (filename screening) ---\n")
    f.write(f"  flagged for review: {flagged_documents}/{total_documents}\n")
    f.write(f"  not filename-flagged: {not_flagged_documents}/{total_documents}\n")
    f.write("  note: filename screening does not confirm whether files contain personal data.\n")

print(f"\n✅ EDA complete!  Outputs in: {OUT_DIR}")
print(f"   Summary      → {summary_path}")
if HAS_MPL:
    plots = sorted(f for f in os.listdir(OUT_DIR) if f.endswith(".png"))
    print(f"   Plots ({len(plots)})   → {OUT_DIR}/")
