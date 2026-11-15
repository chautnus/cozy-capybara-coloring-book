#!/usr/bin/env python3
"""
Regenerate Page 02 and Page 05 with prompts that strictly forbid black signs, black chalkboards,
and black cast-iron utensils, ensuring pure white interiors natively from the model.
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

PROMPT_PAGE_02_CLEAN = (
    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street coffee shop interior. "
    "A cheerful, wholesome fox barista wearing a small bow tie and linen apron, pouring steamed milk to make latte art in a wide ceramic cup. "
    "Behind the counter is a clean white outline vintage coffee machine, a white wooden menu board with simple black lettering 'COFFEE $3', glass jars of coffee beans, stacks of ceramic mugs. "
    "Pure crisp black outlines on a solid pure white background, balanced delicate-to-medium line weight, "
    "strictly ZERO solid black fills, zero black silhouettes, zero black patches, zero black backgrounds, zero black chalkboards, zero black signs, zero shading, zero grayscale. "
    "All signs, menus, appliances, clothing, and walls must have pure white interiors with clean black contour lines. "
    "Spacious, generous open white coloring spaces for markers, square 1:1 aspect ratio."
)

PROMPT_PAGE_05_CLEAN = (
    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street waffle bakery. "
    "A friendly badger chef in a chef hat and apron, smiling beside a clean outline waffle iron on a wooden table with fresh waffles. "
    "On the table are a glass syrup bottle, ceramic bowls of strawberries and blueberries, and a white wooden price sign 'WAFFLES $5'. "
    "Pure crisp black outlines on a solid pure white background, balanced clean contour line weight, "
    "strictly ZERO solid black fills, zero black silhouettes, zero black patches, zero black skillets, zero black pans, zero black signs, zero shading, zero grayscale. "
    "All utensils, pans, appliances, and signs must have pure white interiors with crisp black outlines only. "
    "Spacious, generous open white coloring spaces for markers, square 1:1 aspect ratio."
)

def run():
    token, email = get_best_token(preferred_email="vut08348@gmail.com")
    if not token:
        print("[FAIL] No token found")
        return

    print(f"[INFO] Generating Page 02 pure outline via {email}...")
    img2_bytes = call_generate_image(PROMPT_PAGE_02_CLEAN, token)
    raw2_path = RAW_DIR / "page_02_clean_prompt.png"
    clean2_path = PROCESSED_DIR / "page_02_clean_prompt_clean.png"
    raw2_path.write_bytes(img2_bytes)
    clean_and_threshold_image(raw2_path, clean2_path, threshold=175)

    img2 = cv2.imread(str(clean2_path), cv2.IMREAD_GRAYSCALE)
    density2 = (img2 < 128).mean() * 100
    dist2 = cv2.distanceTransform((img2 < 128).astype(np.uint8), cv2.DIST_L2, 5)
    print(f"Page 02 New Native: density={density2:.2f}%, max radius={dist2.max():.1f}px")

    token, email = get_best_token(preferred_email="dinhthithibwkg58231@gmail.com")
    print(f"[INFO] Generating Page 05 pure outline via {email}...")
    img5_bytes = call_generate_image(PROMPT_PAGE_05_CLEAN, token)
    raw5_path = RAW_DIR / "page_05_clean_prompt.png"
    clean5_path = PROCESSED_DIR / "page_05_clean_prompt_clean.png"
    raw5_path.write_bytes(img5_bytes)
    clean_and_threshold_image(raw5_path, clean5_path, threshold=175)

    img5 = cv2.imread(str(clean5_path), cv2.IMREAD_GRAYSCALE)
    density5 = (img5 < 128).mean() * 100
    dist5 = cv2.distanceTransform((img5 < 128).astype(np.uint8), cv2.DIST_L2, 5)
    print(f"Page 05 New Native: density={density5:.2f}%, max radius={dist5.max():.1f}px")

if __name__ == "__main__":
    run()
