#!/usr/bin/env python3
"""
Generate Version B (Ultra-Clean Minimalist) for Page 02 Agawa Canyon:
Pushing line density even closer to Page 01 (~11-12%), eliminating all texture clutter.
"""

import sys
from pathlib import Path
from PIL import Image
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge

PROMPT_V2 = (
    "Minimalist coloring book page in traditional Vietnamese Dong Ho woodblock print aesthetic, "
    "ultra clean line art, thin-to-medium pure black outlines on pure white paper, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero shaded areas, "
    "zero cross-hatching, zero texture lines, zero halftones, zero grayscale. "
    "Peaceful majestic landscape of Agawa Canyon Scenic Railway in autumn, Northern Ontario. "
    "In the foreground canyon floor, an elegant vintage tour train gently curves along a quiet river, "
    "drawn with clean open white panels, hollow white windows, and simple elegant outlines. "
    "The Agawa river consists of 3 wide flowing smooth woodblock strata bands. "
    "Towering granite canyon walls are rendered as massive smooth geometric planar facets with vast open white spaces. "
    "Atop the cliffs, maple trees are stylized into spacious 3-tier cloud-like woodblock canopy tiers with wide open interiors for color washing. "
    "Extremely spacious coloring compartments, calm meditative composition, sophisticated adult coloring book page. "
    "Square 1:1 aspect ratio, full square canvas composition."
)

def run():
    token, email = get_best_token(preferred_email="ad01.lamlumber@gmail.com")
    if not token:
        print("[FAIL] No valid token.")
        return False
        
    print(f"[INFO] Generating Page 02 Version B using account: {email}...")
    img_bytes = call_generate_image(PROMPT_V2, token)
    
    raw_path = Path("assets/canada/raw/page_02_vB.png")
    clean_path = Path("assets/canada/processed/page_02_vB_clean.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    
    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw -> {raw_path}")
    
    clean_and_threshold_image(raw_path, clean_path, threshold=185)
    
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, "Agawa Canyon Scenic Railway", "Northern Ontario", 2)
        badged.save(clean_path)
    print(f"[OK] Cleaned & badged -> {clean_path}")
    
    with Image.open(clean_path) as img:
        gray = img.convert("L")
        arr = np.array(gray)
        black_pct = (arr < 128).mean() * 100
        print(f"[METRIC] Page 02 Version B Black Density: {black_pct:.2f}% (Page 01: 11.75%)")
        
    return True

if __name__ == "__main__":
    run()
