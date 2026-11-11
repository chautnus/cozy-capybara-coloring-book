#!/usr/bin/env python3
"""
Regenerate Page 03 (Niagara Horseshoe Falls) strictly adhering to Dong Ho Woodblock Rules:
- Line density target: 11% - 15% (matching Page 01: 11.78% & Page 02 Bản A: 15.40%)
- Strictly NO solid black fills, NO black silhouettes, NO black patches, NO shaded areas
- Flowing rhythmic water strata bands with wide open white channels for tiered color washing
- Foreground historic stone promenade railing with clean chiseled planar facets (hollow white)
- Framing autumn maple tree canopy stylized into 3-tiered woodblock canopy layers
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

PAGE_03_PROMPT = (
    "Coloring book page inspired by Vietnamese Dong Ho folk woodblock print aesthetic, "
    "pure clean outline line art, crisp consistent black contour lines on pure white paper, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero dark shaded areas, "
    "zero black water, zero filled rocks, zero shading, zero gradients, zero halftones, zero cross-hatching. "
    "Mature sophisticated adult landscape of Niagara Horseshoe Falls in autumn, Ontario, Canada. "
    "The grand curved waterfall cascades down in wide flowing rhythmic water strata bands with stylized smooth curved mist crests, "
    "rendered with clean open white channels for easy tiered color washing. "
    "In the foreground, an elegant curved historic stone promenade railing with smooth chiseled planar facets "
    "and wide open hollow white colorable compartments. "
    "Framing the upper vista, autumn maple branches are stylized into spacious rhythmic 3-tiered cloud-like woodblock canopy planes "
    "with hollow white interiors for smooth color blending. "
    "Spacious, generous open white coloring compartments, calm meditative composition, adult coloring book page. "
    "Square 1:1 aspect ratio, full square canvas composition."
)

ACCOUNTS = [
    "vut08348@gmail.com",
    "loch7444@gmail.com",
    "lynnphan2017@gmail.com",
    "chautnus@gmail.com",
    "ad01.lamlumber@gmail.com"
]

def run():
    img_bytes = None
    for email in ACCOUNTS:
        token, used_email = get_best_token(preferred_email=email)
        if not token:
            continue
        print(f"[INFO] Attempting Page 03 generation with: {used_email}...")
        try:
            img_bytes = call_generate_image(PAGE_03_PROMPT, token)
            print(f"[OK] Generation succeeded with {used_email}!")
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[WARN] 429 Quota exhausted on {used_email}, trying next account...")
            else:
                print(f"[ERROR] HTTP {e.code} on {used_email}: {e.reason}")
        except Exception as e:
            print(f"[ERROR] {e} on {used_email}")

    if not img_bytes:
        print("[FAIL] All accounts failed to generate image.")
        return False
        
    raw_path = Path("assets/canada/raw/page_03_redesign.png")
    clean_path = Path("assets/canada/processed/page_03_redesign_clean.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    
    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw -> {raw_path}")
    
    clean_and_threshold_image(raw_path, clean_path, threshold=185)
    
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, "Niagara Horseshoe Falls", "Ontario", 3)
        badged.save(clean_path)
    print(f"[OK] Cleaned & badged -> {clean_path}")
    
    # Calculate density
    with Image.open(clean_path) as img:
        gray = img.convert("L")
        arr = np.array(gray)
        black_pct = (arr < 128).mean() * 100
        print(f"[METRIC] Page 03 Redesign Black Density: {black_pct:.2f}% (Target: 11-15%, Page 01: 11.78%)")
        
    # Generate 3-panel comparison sheet: Page 01 (Standard), Page 03 Old (Faulty), Page 03 Redesign
    w, h = 1000, 1000
    pad = 30
    header_h = 90
    total_w = w * 3 + pad * 4
    total_h = h + pad * 2 + header_h
    
    canvas = Image.new("RGB", (total_w, total_h), (245, 245, 247))
    draw = ImageDraw.Draw(canvas)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 36)
        font_label = ImageFont.truetype("arialbd.ttf", 28)
        font_sub = ImageFont.truetype("arial.ttf", 20)
    except:
        font_title = font_label = font_sub = ImageFont.load_default()
        
    draw.text((pad, 25), "ĐỐI CHIẾU NGHIỆM THU PAGE 03: NIAGARA HORSESHOE FALLS (ONTARIO)", fill=(20, 20, 20), font=font_title)
    
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
            "sub": "Mật độ nét: 29.68% | Mảng đen đặc ở vách đá, thác & lan can",
            "path": "assets/canada/processed/page_03_clean.png",
            "pos": (pad * 2 + w, header_h + pad),
            "border_color": (198, 40, 40)
        },
        {
            "title": "3. PAGE 03 REDESIGN (ĐỀ XUẤT DUYỆT)",
            "sub": f"Mật độ nét: {black_pct:.2f}% | Dòng thác mộc bản, ô mở, rỗng hoàn toàn",
            "path": str(clean_path),
            "pos": (pad * 3 + w * 2, header_h + pad),
            "border_color": (30, 136, 229)
        }
    ]
    
    card_header = 65
    for p in panels:
        x, y = p["pos"]
        img = Image.open(p["path"]).resize((w, h - card_header), Image.Resampling.LANCZOS)
        draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=p["border_color"], width=4)
        draw.rectangle([x, y, x + w, y + card_header], fill=p["border_color"])
        draw.text((x + 15, y + 8), p["title"], fill=(255, 255, 255), font=font_label)
        draw.text((x + 15, y + 38), p["sub"], fill=(235, 235, 235), font=font_sub)
        canvas.paste(img, (x, y + card_header))
        
    out_sheet = "assets/canada/page_03_approval_sheet.jpg"
    canvas.save(out_sheet, quality=92)
    print(f"[OK] Saved comparison sheet -> {out_sheet}")
    
    brain_dir = r"C:/Users/Chau/.gemini/antigravity/brain/674909f7-e452-4364-a9b3-88ff0fbdeb5d"
    shutil.copy2(out_sheet, os.path.join(brain_dir, "page_03_approval_sheet.jpg"))
    shutil.copy2(str(clean_path), os.path.join(brain_dir, "page_03_redesign_clean.png"))
    print("[OK] Copied to brain artifacts.")
    
    return True

if __name__ == "__main__":
    run()
