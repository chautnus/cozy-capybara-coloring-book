#!/usr/bin/env python3
"""
Regenerate Page 02 (Agawa Canyon) strictly adhering to Page 01 Dong Ho Rules:
- Line density target: 10% - 13% (matching Page 01's 11.75%)
- Strictly NO solid black fills, NO black silhouettes, NO filled windows, NO dark shading
- Spacious open colorable compartments for multi-layer marker color washing (3-tier canopy, smooth rock facets)
- Vintage train simplified into elegant hollow woodblock line contours (all panels and windows hollow white)
"""

import sys
from pathlib import Path
from PIL import Image
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge

PAGE_02_PROMPT = (
    "Coloring book page inspired by Vietnamese Dong Ho folk woodblock print aesthetic, "
    "pure clean outline line art, crisp consistent black contour lines on pure white paper, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero filled windows, "
    "zero shading, zero gradients, zero halftones, zero cross-hatching. "
    "Mature sophisticated adult landscape of Agawa Canyon Scenic Railway in autumn, Northern Ontario, Canada. "
    "In the center, an elegant vintage passenger train curves along the canyon floor, drawn with clean hollow white panels "
    "and hollow white windows with crisp black outlines, perfectly colorable. "
    "Beside the train, the serene Agawa river is stylized into 3-4 wide flowing rhythmic woodblock strata bands. "
    "On both sides, towering granite canyon cliffs are composed of large, smooth chiseled planar facets without clutter. "
    "Autumn maple and birch canopies atop the cliffs are stylized into distinct rhythmic 3-tiered woodblock canopy planes "
    "for smooth multi-layer color washing and blending. "
    "Spacious, generous open white coloring compartments, elegant folk art composition, adult coloring book page. "
    "Square 1:1 aspect ratio, full square canvas composition."
)

def run():
    token, email = get_best_token(preferred_email="ad01.lamlumber@gmail.com")
    if not token:
        print("[FAIL] No valid token.")
        return False
        
    print(f"[INFO] Generating Page 02 redesign using account: {email}...")
    img_bytes = call_generate_image(PAGE_02_PROMPT, token)
    
    raw_path = Path("assets/canada/raw/page_02_redesign.png")
    clean_path = Path("assets/canada/processed/page_02_redesign_clean.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    
    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw -> {raw_path}")
    
    clean_and_threshold_image(raw_path, clean_path, threshold=185)
    
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, "Agawa Canyon Scenic Railway", "Northern Ontario", 2)
        badged.save(clean_path)
    print(f"[OK] Cleaned & badged -> {clean_path}")
    
    # Analyze density
    with Image.open(clean_path) as img:
        gray = img.convert("L")
        arr = np.array(gray)
        black_pct = (arr < 128).mean() * 100
        print(f"[METRIC] Page 02 Redesign Black Density: {black_pct:.2f}% (Target: 10-14%, Page 01 was 11.75%)")
        
    return True

if __name__ == "__main__":
    run()
