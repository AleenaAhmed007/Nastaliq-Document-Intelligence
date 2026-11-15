"""
Draw annotation boxes on page images and save as visual previews.
Reads export.json (Label Studio format) and draws colored bounding boxes
with labels on each page image. Output goes to data/previews/.

Usage (from repo root):  python scripts/draw_annotations.py
"""

import json, os, re
from PIL import Image, ImageDraw, ImageFont

import paths as P

EXPORT   = P.abspath(P.EXPORT_GOLD)
IMG_DIR  = P.abspath(P.PAGE_IMAGES)
OUT_DIR  = P.abspath(P.PREVIEWS_DIR)

# Color map for each label type (R, G, B)
COLORS = {
    "header_department":  (0,   120, 215),   # blue
    "reference_no":       (220, 50,  50),    # red
    "date":               (50,  180, 50),    # green
    "subject":            (200, 120, 0),     # orange
    "body":               (128, 128, 128),   # gray
    "table":              (160, 32,  240),   # purple
    "stamp_signature":    (0,   180, 180),   # teal
    "distribution_list":  (180, 100, 160),   # mauve
    "text_line":          (100, 100, 200),   # light blue
}

# Short display labels for readability
SHORT = {
    "header_department": "DEPT",
    "reference_no":      "REF#",
    "date":              "DATE",
    "subject":           "SUBJ",
    "body":              "BODY",
    "table":             "TABLE",
    "stamp_signature":   "STAMP",
    "distribution_list": "DIST",
    "text_line":         "LINE",
}

def get_font(size):
    """Try to load a decent font, fall back to default."""
    for name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except (IOError, OSError):
            pass
    return ImageFont.load_default()


def draw_task(task, img_dir, out_dir):
    """Draw all annotation boxes on one page image."""
    # Extract page_id from image path
    img_path_raw = task["data"].get("image", "")
    match = re.search(r"([\w]+)\.png", img_path_raw)
    if not match:
        return None
    page_id = match.group(1)
    img_path = os.path.join(img_dir, page_id + ".png")
    if not os.path.exists(img_path):
        return None

    img = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size

    # Collect rectangles and their texts
    annotations = task.get("annotations", [])
    if not annotations:
        return None

    results = annotations[0].get("result", [])

    # Build id -> text mapping
    text_map = {}
    for r in results:
        if r["type"] == "textarea":
            rid = r["id"]
            texts = r["value"].get("text", [])
            if texts:
                text_map[rid] = texts[0]

    # Font sizes based on image size
    label_font = get_font(max(20, int(h * 0.012)))
    text_font  = get_font(max(16, int(h * 0.009)))

    # Draw rectangles
    box_count = 0
    for r in results:
        if r["type"] != "rectanglelabels":
            continue
        val = r["value"]
        labels = val.get("rectanglelabels", [])
        if not labels:
            continue
        label = labels[0]

        # Convert percentage to pixels
        x1 = val["x"] / 100.0 * w
        y1 = val["y"] / 100.0 * h
        bw = val["width"] / 100.0 * w
        bh = val["height"] / 100.0 * h
        x2 = x1 + bw
        y2 = y1 + bh

        color = COLORS.get(label, (200, 200, 200))
        line_width = 3 if label != "text_line" else 2

        # Draw rectangle
        draw.rectangle([x1, y1, x2, y2], outline=color, width=line_width)

        # Draw label tag
        short = SHORT.get(label, label.upper())
        # For field labels (not text_line), draw a filled tag
        if label != "text_line":
            bbox = label_font.getbbox(short)
            tw = bbox[2] - bbox[0] + 8
            th = bbox[3] - bbox[1] + 6
            tag_y = max(0, y1 - th - 2)
            draw.rectangle([x1, tag_y, x1 + tw, tag_y + th], fill=color)
            draw.text((x1 + 4, tag_y + 2), short, fill="white", font=label_font)

            # If there's associated text, draw it below the tag
            rid = r["id"]
            if rid in text_map:
                txt = text_map[rid]
                if len(txt) > 80:
                    txt = txt[:77] + "..."
                draw.text((x1 + 4, y1 + 4), txt, fill=color, font=text_font)

        box_count += 1

    out_path = os.path.join(out_dir, page_id + "_annotated.png")
    img.save(out_path, "PNG")
    return box_count


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    with open(EXPORT, encoding="utf-8") as f:
        data = json.load(f)

    total = 0
    done = 0
    for task in data:
        total += 1
        count = draw_task(task, IMG_DIR, OUT_DIR)
        if count is not None:
            done += 1
            if done % 50 == 0:
                print(f"  ... {done} pages drawn")

    print(f"\nDone! {done}/{total} annotated images saved to {OUT_DIR}/")
    print(f"Total images: {done}")


if __name__ == "__main__":
    main()
