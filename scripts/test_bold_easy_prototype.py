#!/usr/bin/env python3
"""
Generate and evaluate a Bold & Easy prototype for Canada Coloring Book.
Focuses on:
- Chunky, large open coloring spaces
- Cloud-like tree canopies (zero individual leaves)
- Broad ribbon waves (zero ripples)
- Bold thick outlines (3-4px)
- Ultra-low complexity, ideal for alcohol markers (Ohuhu/Copic)
"""

import sys
import json
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge

PROMPT = (
    "Coloring book page in Coco Wyo bold and easy style, ultra simple minimalist line art, "
    "very thick bold black outlines, pure white background, zero shading, black and white only, "
    "no grayscale, no halftones. Giant chunky open coloring spaces, extremely easy to color with alcohol markers. "
    "A peaceful autumn scene at Algonquin Park in Canada: a simple smooth chunky wooden canoe resting gently "
    "on a grassy bank with one large paddle. The lake water consists of only 3 to 4 wide smooth flowing ribbon waves. "
    "In the background, three large fluffy cloud-like rounded tree silhouettes with zero individual leaves, "
    "a big clean round autumn sun, and simple smooth rolling hills. "
    "Extremely simplified, clean bold 4px outlines, zero tiny details, zero texture lines, cozy relaxing coloring page."
)


def run_prototype():
    token, email = get_best_token(preferred_email="ad01.lamlumber@gmail.com")
    if not token:
        print("[FAIL] No valid token found.")
        return False

    print(f"[INFO] Generating Bold & Easy prototype using account: {email}...")
    img_bytes = call_generate_image(PROMPT, token)

    raw_path = Path("assets/canada/raw/prototype_bold_easy_page_01.png")
    clean_path = Path("assets/canada/processed/prototype_bold_easy_page_01.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)

    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw -> {raw_path}")

    # Clean and threshold to 300 DPI
    clean_and_threshold_image(raw_path, clean_path, threshold=185)

    # Inscribe Typography Badge
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, "Algonquin Provincial Park", "Ontario, Canada", 1)
        badged.save(clean_path)
    print(f"[OK] Inscribed typography badge -> {clean_path}")

    # Calculate density
    with Image.open(clean_path) as img:
        gray = img.convert("L")
        w, h = gray.size
        pixels = list(gray.getdata())
        black_cnt = sum(1 for px in pixels if px < 128)
        pct = (black_cnt / (w * h)) * 100
        print(f"[METRIC] Density: {pct:.2f}% ({w}x{h})")

    return True


if __name__ == "__main__":
    run_prototype()
