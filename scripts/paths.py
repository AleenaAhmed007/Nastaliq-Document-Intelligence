"""
Single source of truth for the project's directory layout.

All paths are relative to the repository root. Run the scripts from the repo root
(e.g. `python scripts/triage.py`) so that the relative image paths stored inside the
data files (manifest.csv, tasks.json, exports, page records) keep resolving.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# configs / docs
LABELSTUDIO_CONFIG = os.path.join("configs", "labelstudio_config.xml")

# data/raw: immutable source documents, never edited by hand
RAW_DIR          = os.path.join("data", "raw")
RAW_DOCS         = os.path.join(RAW_DIR, "documents")          # FBR/, azad Kashmir/
AJK_MANIFEST     = os.path.join(RAW_DIR, "ajkbise_manifest.csv")
SCRAPE_FAILED    = os.path.join(RAW_DIR, "scrape_failed.csv")

# data/interim: triage output (rendered pages + page manifest)
INTERIM_DIR      = os.path.join("data", "interim")
PAGE_IMAGES      = os.path.join(INTERIM_DIR, "images")
PAGE_MANIFEST    = os.path.join(INTERIM_DIR, "manifest.csv")
PRIVACY_REVIEW   = os.path.join(INTERIM_DIR, "review_personal_data.csv")

# data/annotations: Label Studio tasks + exports
ANN_DIR          = os.path.join("data", "annotations")
TASKS_JSON       = os.path.join(ANN_DIR, "tasks.json")
EXPORT_GOLD      = os.path.join(ANN_DIR, "export.json")         # 239 human-verified pages
EXPORT_FULL      = os.path.join(ANN_DIR, "export_full.json")    # gold + auto-heuristic (789 pages)
AUTO_DIR         = os.path.join(ANN_DIR, "auto")
REMAINING_PAGES  = os.path.join(AUTO_DIR, "remaining_pages.json")
REMAINING_ANNS   = os.path.join(AUTO_DIR, "remaining_annotations.json")

# data/processed: clean, model-ready dataset
PROCESSED_DIR    = os.path.join("data", "processed")
ALL_PAGES_FULL   = os.path.join(PROCESSED_DIR, "all_pages_full.jsonl")

# data/previews: annotation overlays for visual QA
PREVIEWS_DIR     = os.path.join("data", "previews")


def abspath(rel):
    """Resolve a repo-relative path to an absolute one."""
    return os.path.join(ROOT, rel)
