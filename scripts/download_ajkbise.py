
import os
import re
import csv
import time
import hashlib
import requests

from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

import paths as P

BASE = "https://ajkbise.net"
PAGE = BASE + "/notifications.php"

OUT = P.abspath(os.path.join(P.RAW_DOCS, "azad Kashmir"))
os.makedirs(OUT, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (compatible; UrduOCRResearch/1.0)"
})

ALLOWED_HOSTS = {"ajkbise.net", "www.ajkbise.net"}

records = []
failed = []
seen_urls = set()
seen_hashes = set()

def identify_file(data):
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith(b"%PDF"):
        return ".pdf"
    return None


def main():

    print("Opening notifications page...")

    response = session.get(PAGE, timeout=60)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find notification table
    table = None

    for t in soup.find_all("table"):
        if "View" in t.get_text() and "Download" in t.get_text():
            table = t
            break

    if table is None:
        print("Notification table not found!")
        print(soup.title)
        return

    rows = table.find_all("tr")

    print("Notification rows:", len(rows))

    for row in rows:

        cells = row.find_all(["td", "th"])
        text = [c.get_text(" ", strip=True) for c in cells]

        if len(text) < 2:
            continue

        # Read date and title
        date = text[0]
        title = text[1]

        # Collect ALL links inside this row
        links = row.find_all("a", href=True)

        for link in links:

            url = urljoin(PAGE, link["href"])
            url = url.split("#")[0]

            if url in seen_urls:
                continue

            seen_urls.add(url)

            parsed = urlparse(url)

            if parsed.hostname not in ALLOWED_HOSTS:
                continue

            print("\nChecking:", title)
            print("URL:", url)

            try:
                r = session.get(url, timeout=60)
                r.raise_for_status()

                data = r.content

                if len(data) == 0 or len(data) > 30 * 1024 * 1024:
                    raise ValueError("Empty or oversized file")

                ext = identify_file(data)

                if not ext:
                    print("Not an image/PDF. Skipped.")
                    continue

                sha = hashlib.sha256(data).hexdigest()

                if sha in seen_hashes:
                    print("Duplicate skipped.")
                    continue

                seen_hashes.add(sha)

                original = os.path.basename(
                    unquote(urlparse(r.url).path)
                )

                original = re.sub(
                    r'[^\w.-]', '_', original
                )

                if not original or original == ".":
                    original = "notification"

                if not original.lower().endswith(ext):
                    original += ext

                filename = f"{len(records)+1:04d}_{original}"
                filepath = os.path.join(OUT, filename)

                with open(filepath, "wb") as f:
                    f.write(data)

                # Validate image files
                if ext in (".jpg", ".png"):
                    with Image.open(BytesIO(data)) as img:
                        img.verify()
                    category = "image"
                else:
                    category = "pdf"

                records.append({
                    "file_name": filename,
                    "date": date,
                    "title": title,
                    "format": ext,
                    "category": category,
                    "language": "manual_review",
                    "script": "manual_review",
                    "source_url": r.url,
                    "sha256": sha
                })

                print("SUCCESS:", filename)

            except Exception as e:
                print("FAILED:", str(e))
                failed.append({
                    "url": url,
                    "error": str(e)
                })

            time.sleep(2)

    # Save CSV manifest
    fields = [
        "file_name", "date", "title", "format",
        "category", "language", "script",
        "source_url", "sha256"
    ]

    with open(
        P.abspath(P.AJK_MANIFEST),
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    with open(
        P.abspath(P.SCRAPE_FAILED),
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.DictWriter(
            f, fieldnames=["url", "error"]
        )
        writer.writeheader()
        writer.writerows(failed)

    print("\n========== FINAL REPORT ==========")
    print("Rows:", len(rows))
    print("Downloaded:", len(records))
    print("Images:", sum(x["category"] == "image" for x in records))
    print("PDFs:", sum(x["category"] == "pdf" for x in records))
    print("Failed:", len(failed))
    print("Folder:", OUT)


if __name__ == "__main__":
    main()
