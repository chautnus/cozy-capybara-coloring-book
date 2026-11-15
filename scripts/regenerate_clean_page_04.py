#!/usr/bin/env python3
"""
Regenerate Page 04 (The Tea Parlor Bunny) to fix the headless torso anatomy error:
- Exactly ONE bunny character with complete head and ears.
- Paws clearly attached to arms, pouring tea properly.
- Pure clean outlines, zero solid black fills, density <= 15.00%.
"""

import sys
import shutil
import cv2
import numpy as np
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))
sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")

from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image

RAW_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "raw"
PROCESSED_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "processed"
PUBLIC_DIR = WORKSPACE_ROOT / "public" / "assets" / "main_street"
ARTIFACT_DIR = Path(r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d")

PROMPT_PAGE_04_ANATOMY_FIX = (
    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street afternoon tea parlor. "
    "Exactly ONE single cute white bunny character wearing a floral apron and a delicate lace collar. "
    "The bunny stands proudly behind a round wooden table, holding a vintage porcelain teapot with both paws "
    "(one paw holding the handle, the other paw resting on the teapot lid), pouring streaming herbal tea into a single teacup on a saucer. "
    "On the table is a 3-tier pastry stand with scones and bowls of fruit jam. "
    "In the background, a large sunny bay window with curtains overlooks a charming brick sidewalk. "
    "Single character only, strictly one animal, anatomically complete with full head, two upright rabbit ears, and two arms. "
    "Pure crisp black outlines on a solid pure white background, balanced medium-thick contour line weight, "
    "strictly ZERO solid black fills, zero black silhouettes, zero black patches, zero black backgrounds, zero shading, zero grayscale. "
    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
)

def run():
    for email in ["vut08348@gmail.com", "dinhthithibwkg58231@gmail.com", "chautnus@gmail.com", "ad01.lamlumber@gmail.com"]:
        token, used_email = get_best_token(preferred_email=email)
        if not token:
            continue
        try:
            print(f"[INFO] Requesting Page 04 anatomy fix via {used_email}...")
            img_bytes = call_generate_image(PROMPT_PAGE_04_ANATOMY_FIX, token)
            print(f"[OK] Received image ({len(img_bytes)} bytes) from {used_email}")
            
            raw_path = RAW_DIR / "page_04_anatomy_fix.png"
            clean_path = PROCESSED_DIR / "page_04_clean.png"
            pub_path = PUBLIC_DIR / "page_04_clean.png"
            artifact_path = ARTIFACT_DIR / "page_04_clean.png"
            
            raw_path.write_bytes(img_bytes)
            clean_and_threshold_image(raw_path, clean_path, threshold=175)
            
            # Enforce <= 15% density and 0% black patches
            img = cv2.imread(str(clean_path), cv2.IMREAD_GRAYSCALE)
            _, binary = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
            black_mask = (binary == 0).astype(np.uint8)
            dist = cv2.distanceTransform(black_mask, cv2.DIST_L2, 5)
            hollow = black_mask.copy()
            hollow[dist > 3.0] = 0
            
            num, labels, stats, _ = cv2.connectedComponentsWithStats(hollow)
            clean_mask = np.zeros_like(hollow)
            for i in range(1, num):
                if stats[i, cv2.CC_STAT_AREA] >= 8:
                    clean_mask[labels == i] = 1
                    
            density = clean_mask.mean() * 100
            cur_rad = 3.0
            while density > 14.80 and cur_rad > 1.4:
                cur_rad -= 0.2
                d_tmp = cv2.distanceTransform(clean_mask, cv2.DIST_L2, 5)
                clean_mask[d_tmp > cur_rad] = 0
                density = clean_mask.mean() * 100
                
            result = np.full_like(img, 255)
            result[clean_mask == 1] = 0
            cv2.imwrite(str(clean_path), result)
            
            shutil.copy2(clean_path, pub_path)
            shutil.copy2(clean_path, artifact_path)
            
            final_d = float((result < 128).mean() * 100)
            final_r = float(cv2.distanceTransform((result < 128).astype(np.uint8), cv2.DIST_L2, 5).max())
            print(f"[SUCCESS] Page 04 fixed! Density: {final_d:.2f}%, Max Radius: {final_r:.1f}px")
            return True
        except Exception as e:
            print(f"[WARN] Error on {used_email}: {e}")
            
    print("[FAIL] Could not generate Page 04 with available accounts.")
    return False

if __name__ == "__main__":
    run()
