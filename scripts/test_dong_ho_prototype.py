#!/usr/bin/env python3
"""
Generate and evaluate a Dong Ho Woodblock Layered Prototype for Canada Coloring Book.
Core Principles:
- Inspired by Vietnamese Dong Ho folk woodblock prints (Tranh khac go Dan gian Dong Ho)
- Multi-layer colorable planes (van mau xep tang): 3-4 rhythmic contour tiers per object
- Foliage stylized into layered woodblock tiers (tán cây phân tầng) for sequential color washing
- Water divided into elegant rhythmic strata bands (sóng nước xếp lớp mộc bản)
- Mature, sophisticated folk art aesthetic — strictly NOT childish, NOT cartoonish blobs
- Spacious colorable compartments for multi-layer marker blending (quét nhiều lớp màu)
"""

import sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge

PROMPT = (
    "Coloring book page inspired by traditional woodblock printmaking and Vietnamese Dong Ho folk art aesthetic, "
    "clean bold graphic woodcut line art, crisp black outlines, pure white background, zero shading, "
    "black and white only, no grayscale, no halftones. "
    "Artistic adult landscape of Algonquin Provincial Park in autumn, Canada. "
    "In the foreground, a graceful cedar canoe rests on the quiet lake shore with an elegant paddle. "
    "The autumn maple trees are stylized into elegant rhythmic multi-tiered woodblock canopy layers, "
    "creating distinct nested planes for multi-layer color washing and blending. "
    "The calm lake water is composed of flowing rhythmic woodcut strata bands. "
    "In the background, majestic rolling granite hills with clean chiseled woodcut facets. "
    "Sophisticated graphic heritage line art, mature and poetic, zero childish cartoon shapes, "
    "generous open colorable compartments designed for smooth marker layering, adult coloring page."
)


def run_prototype():
    token, email = get_best_token(preferred_email="ad01.lamlumber@gmail.com")
    if not token:
        print("[FAIL] No valid token found.")
        return False

    print(f"[INFO] Generating Dong Ho Layered Prototype using account: {email}...")
    img_bytes = call_generate_image(PROMPT, token)

    raw_path = Path("assets/canada/raw/prototype_dong_ho_page_01.png")
    clean_path = Path("assets/canada/processed/prototype_dong_ho_page_01.png")
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
        # Count black pixels
        bw = gray.point(lambda p: 255 if p > 128 else 0)
        black_cnt = sum(1 for px in bw.getdata() if px == 0)
        pct = (black_cnt / (w * h)) * 100
        print(f"[METRIC] Density: {pct:.2f}% ({w}x{h})")

    return True


if __name__ == "__main__":
    run_prototype()
