#!/usr/bin/env python3
"""
Finalize Batch 2 (Pages 06 to 10) with verified clean assets:
- Page 06: The Milkcart Dairy Cow (Density 10.61%, Max Radius 3.0px)
- Page 07: The Pancake Squirrel (Density 11.99%, Max Radius 3.0px)
- Page 08: The Juice Porcupine (Density 10.80%, Max Radius 3.0px)
- Page 09: The Owl's Bookstore (Density 14.12%, Max Radius 3.0px)
- Page 10: The Florist Deer (Density 14.80%, Max Radius 2.2px)
Rebuilds the master approval sheet and synchronizes all artifact directories.
"""

import sys
import shutil
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.produce_main_street_batch_2 import build_batch_approval_sheet

PROCESSED_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "processed"
PUBLIC_DIR = WORKSPACE_ROOT / "public" / "assets" / "main_street"
ARTIFACT_DIR = Path(r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d")

# Replace page 06 with v2 clean
src_06 = PROCESSED_DIR / "page_06_v2_clean.png"
if src_06.exists():
    shutil.copy2(src_06, PROCESSED_DIR / "page_06_clean.png")
    shutil.copy2(src_06, PUBLIC_DIR / "page_06_clean.png")
    shutil.copy2(src_06, ARTIFACT_DIR / "page_06_clean.png")
    print("Updated page 06 clean images everywhere.")

metrics = [
    {
        "page": 6,
        "title": "The Milkcart Dairy Cow",
        "subtitle": "Cỗ Xe Sữa Thủy Tinh Ban Mai",
        "clean_path": PROCESSED_DIR / "page_06_clean.png",
        "density": 10.61,
        "max_rad": 3.0
    },
    {
        "page": 7,
        "title": "The Pancake Squirrel",
        "subtitle": "Căn Bếp Bánh Kếch Sóc Nâu",
        "clean_path": PROCESSED_DIR / "page_07_clean.png",
        "density": 11.99,
        "max_rad": 3.0
    },
    {
        "page": 8,
        "title": "The Juice Porcupine",
        "subtitle": "Quầy Nước Ép Bé Nhím",
        "clean_path": PROCESSED_DIR / "page_08_clean.png",
        "density": 10.80,
        "max_rad": 3.0
    },
    {
        "page": 9,
        "title": "The Owl's Bookstore",
        "subtitle": "Hiệu Sách Cũ Của Thầy Cú Mèo",
        "clean_path": PROCESSED_DIR / "page_09_clean.png",
        "density": 14.12,
        "max_rad": 3.0
    },
    {
        "page": 10,
        "title": "The Florist Deer",
        "subtitle": "Cửa Hàng Hoa Nàng Hươu Sao",
        "clean_path": PROCESSED_DIR / "page_10_clean.png",
        "density": 14.80,
        "max_rad": 2.2
    }
]

# Ensure public and artifact have all clean pages 06 to 10
for m in metrics:
    p_num = m["page"]
    clean_file = PROCESSED_DIR / f"page_{p_num:02d}_clean.png"
    shutil.copy2(clean_file, PUBLIC_DIR / f"page_{p_num:02d}_clean.png")
    shutil.copy2(clean_file, ARTIFACT_DIR / f"page_{p_num:02d}_clean.png")

build_batch_approval_sheet(metrics)
print("[OK] Rebuilt Batch 2 Approval Sheet and staged to Artifact Directory.")
