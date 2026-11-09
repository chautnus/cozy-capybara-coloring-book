#!/usr/bin/env python3
"""
Batch processor for Canada coloring book images:
1. Copies raw AI output
2. Thresholds and cleans to pure 300 DPI vector line art
3. Adds colorable typography signboard badge
4. Copies to public web assets
5. Validates line coverage and zone density
"""

import shutil
import cv2
import sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge

def process_batch(items):
    pub_dir = Path("public/assets/canada")
    pub_dir.mkdir(parents=True, exist_ok=True)
    
    for item in items:
        page_num = item["page"]
        src = Path(item["src"])
        raw = Path(item["raw"])
        clean = Path(item["clean"])
        title = item["title"]
        province = item["province"]
        
        # 1. Copy raw
        raw.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, raw)
        
        # 2. Preprocess to 300 DPI binary
        clean.parent.mkdir(parents=True, exist_ok=True)
        clean_and_threshold_image(raw, clean, threshold=185)
        
        # 3. Add typography badge
        with Image.open(clean) as img:
            badged = add_landmark_badge(img, title, province, page_num)
            badged.save(clean)
            
            # 4. Copy to public web assets
            pub_path = pub_dir / clean.name
            badged.save(pub_path)
            
        # 5. Measure stats
        arr = cv2.imread(str(clean), cv2.IMREAD_GRAYSCALE)
        cov = (arr < 128).mean() * 100
        _, _, stats, _ = cv2.connectedComponentsWithStats((arr > 127).astype("uint8"))
        zones = len(stats) - 1
        tiny = (stats[1:, 4] < 100).sum()
        
        print(f"[PAGE {page_num:02d}] {title} ({province}): coverage={cov:.2f}%, zones={zones}, tiny={tiny}")

if __name__ == "__main__":
    batch1 = [
        {
            "page": 2,
            "src": r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d\canada_page_02_agawa_canyon_1794211584267.jpg",
            "raw": "assets/canada/raw/page_02.png",
            "clean": "assets/canada/processed/page_02_clean.png",
            "title": "Agawa Canyon Scenic Railway",
            "province": "Northern Ontario"
        },
        {
            "page": 3,
            "src": r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d\canada_page_03_niagara_falls_1794211602433.jpg",
            "raw": "assets/canada/raw/page_03.png",
            "clean": "assets/canada/processed/page_03_clean.png",
            "title": "Niagara Horseshoe Falls",
            "province": "Ontario"
        },
        {
            "page": 4,
            "src": r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d\canada_page_04_rideau_canal_1794211632185.jpg",
            "raw": "assets/canada/raw/page_04.png",
            "clean": "assets/canada/processed/page_04_clean.png",
            "title": "Rideau Canal & Parliament",
            "province": "Ottawa, Ontario"
        },
        {
            "page": 5,
            "src": r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d\canada_page_05_chateau_frontenac_1794211649157.jpg",
            "raw": "assets/canada/raw/page_05.png",
            "clean": "assets/canada/processed/page_05_clean.png",
            "title": "Château Frontenac & Old Quebec",
            "province": "Quebec"
        }
    ]
    process_batch(batch1)
