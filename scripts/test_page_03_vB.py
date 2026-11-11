#!/usr/bin/env python3
"""
Generate Version B (Ultra-Clean Minimalist) for Page 03 Niagara Falls:
Aiming for 10-13% line density, wide open water strata, completely hollow white compartments.
"""

import os
import sys
import shutil
import urllib.error
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge

PROMPT_V3_B = (
    "Minimalist coloring book page in traditional Vietnamese Dong Ho woodblock print aesthetic, "
    "ultra clean line art, thin-to-medium pure black outlines on pure white paper, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero shaded areas, "
    "zero cross-hatching, zero texture lines, zero halftones, zero grayscale. "
    "Peaceful majestic panoramic view of Niagara Horseshoe Falls in autumn, Ontario, Canada. "
    "The grand curved waterfall is stylized into 4 to 5 wide, smooth sweeping curved water strata bands, "
    "with soft stylized rolling cloud-like mist at the bottom, all completely open and hollow white. "
    "In the foreground, a peaceful historic curved stone promenade railing drawn with clean hollow white rectangular panels. "
    "Framing the autumn sky, maple branches are stylized into spacious 3-tier cloud-like woodblock canopy tiers with vast open white interiors. "
    "Extremely spacious coloring compartments, calm meditative composition, sophisticated adult coloring book page. "
    "Square 1:1 aspect ratio, full square canvas composition."
)

ACCOUNTS = [
    "loch7444@gmail.com",
    "lynnphan2017@gmail.com",
    "chautnus@gmail.com",
    "vut08348@gmail.com",
    "ad01.lamlumber@gmail.com"
]

def run():
    img_bytes = None
    for email in ACCOUNTS:
        token, used_email = get_best_token(preferred_email=email)
        if not token:
            continue
        print(f"[INFO] Generating Page 03 Version B using: {used_email}...")
        try:
            img_bytes = call_generate_image(PROMPT_V3_B, token)
            print(f"[OK] Succeeded with {used_email}!")
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[WARN] 429 Quota exhausted on {used_email}, trying next...")
            else:
                print(f"[ERROR] HTTP {e.code} on {used_email}")
        except Exception as e:
            print(f"[ERROR] {e} on {used_email}")
            
    if not img_bytes:
        print("[FAIL] Failed to generate Page 03 Version B.")
        return False
        
    raw_path = Path("assets/canada/raw/page_03_vB.png")
    clean_path = Path("assets/canada/processed/page_03_vB_clean.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    
    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw -> {raw_path}")
    
    clean_and_threshold_image(raw_path, clean_path, threshold=185)
    
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, "Niagara Horseshoe Falls", "Ontario", 3)
        badged.save(clean_path)
    print(f"[OK] Cleaned & badged -> {clean_path}")
    
    with Image.open(clean_path) as img:
        gray = img.convert("L")
        arr = np.array(gray)
        black_pct_b = (arr < 128).mean() * 100
        print(f"[METRIC] Page 03 Version B Black Density: {black_pct_b:.2f}% (Page 01: 11.78%)")
        
    # Get Version A density
    with Image.open("assets/canada/processed/page_03_redesign_clean.png") as img:
        gray = img.convert("L")
        arr = np.array(gray)
        black_pct_a = (arr < 128).mean() * 100

    # Build 4-panel comparison sheet
    w, h = 1200, 1200
    pad = 40
    header_h = 100
    total_w = w * 2 + pad * 3
    total_h = h * 2 + pad * 3 + header_h

    canvas = Image.new("RGB", (total_w, total_h), (245, 245, 247))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("arial.ttf", 38)
        font_label = ImageFont.truetype("arialbd.ttf", 32)
        font_sub = ImageFont.truetype("arial.ttf", 24)
    except:
        font_title = font_label = font_sub = ImageFont.load_default()

    draw.text((pad, 30), "NGHIỆM THU REDESIGN PAGE 03: NIAGARA HORSESHOE FALLS (ONTARIO)", fill=(20, 20, 20), font=font_title)

    panels = [
        {
            "title": "1. PAGE 01 (CHUẨN ĐÃ DUYỆT)",
            "sub": "Mật độ nét: 11.78% | Vùng tô lớn, không mảng đen, chuẩn Đông Hồ",
            "path": "assets/canada/processed/page_01_clean.png",
            "pos": (pad, header_h + pad),
            "border_color": (46, 125, 50)
        },
        {
            "title": "2. PAGE 03 CŨ (LỖI BỊ BÁC BỎ)",
            "sub": "Mật độ nét: 29.68% | LỖI: Vách đá đen đặc, thác nước sọc li ti",
            "path": "assets/canada/processed/page_03_clean.png",
            "pos": (pad * 2 + w, header_h + pad),
            "border_color": (198, 40, 40)
        },
        {
            "title": "3. PAGE 03 REDESIGN - BẢN A",
            "sub": f"Mật độ nét: {black_pct_a:.2f}% | Dòng thác mộc bản, triệt tiêu mảng đen đặc",
            "path": "assets/canada/processed/page_03_redesign_clean.png",
            "pos": (pad, header_h + pad * 2 + h),
            "border_color": (30, 136, 229)
        },
        {
            "title": "4. PAGE 03 REDESIGN - BẢN B (TỐI GIẢN)",
            "sub": f"Mật độ nét: {black_pct_b:.2f}% | Siêu thoáng, dải thác mở rộng, mây cuộn lớn",
            "path": str(clean_path),
            "pos": (pad * 2 + w, header_h + pad * 2 + h),
            "border_color": (156, 39, 176)
        }
    ]

    card_header = 70
    for p in panels:
        x, y = p["pos"]
        img = Image.open(p["path"]).resize((w, h - card_header), Image.Resampling.LANCZOS)
        draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=p["border_color"], width=4)
        draw.rectangle([x, y, x + w, y + card_header], fill=p["border_color"])
        draw.text((x + 15, y + 8), p["title"], fill=(255, 255, 255), font=font_label)
        draw.text((x + 15, y + 42), p["sub"], fill=(235, 235, 235), font=font_sub)
        canvas.paste(img, (x, y + card_header))

    out_sheet = "assets/canada/page_03_approval_sheet.jpg"
    canvas.save(out_sheet, quality=92)
    print(f"[OK] Saved comparison sheet -> {out_sheet}")

    brain_dir = r"C:/Users/Chau/.gemini/antigravity/brain/674909f7-e452-4364-a9b3-88ff0fbdeb5d"
    shutil.copy2(out_sheet, os.path.join(brain_dir, "page_03_approval_sheet.jpg"))
    shutil.copy2("assets/canada/processed/page_03_redesign_clean.png", os.path.join(brain_dir, "page_03_variant_a.png"))
    shutil.copy2(str(clean_path), os.path.join(brain_dir, "page_03_variant_b.png"))
    print("[OK] Copied all assets to brain artifacts.")

    return True

if __name__ == "__main__":
    run()
