#!/usr/bin/env python3
"""
Refine Page 03 Bản A (Niagara Horseshoe Falls) targeting ~15.0% black density:
- Preserve the dynamic multi-layered waterfall composition of Version A
- Thin-to-medium delicate outlines, spacious open water strata, hollow promenade railing
- Calibrate threshold to achieve exactly 14.5% - 15.5% black density
"""

import os
import sys
import shutil
import urllib.error
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import TARGET_WIDTH_PX, TARGET_HEIGHT_PX, TARGET_DPI
from scripts.add_landmark_typography import add_landmark_badge

PAGE_03_PROMPT_A_REFINED = (
    "Coloring book page inspired by Vietnamese Dong Ho folk woodblock print aesthetic, "
    "clean delicate outline line art, thin-to-medium crisp black contour lines on pure white paper, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero dark shaded areas, "
    "zero cross-hatching, zero texture lines, zero halftones, zero grayscale. "
    "Mature sophisticated adult landscape of Niagara Horseshoe Falls in autumn, Ontario, Canada. "
    "The iconic curved waterfall cascades in 5 to 6 wide flowing rhythmic water strata bands with smooth rounded mist clouds at the bottom, "
    "each band having generous open white space for sequential color washing. "
    "In the foreground, an elegant curved historic stone promenade railing rendered with clean hollow white rectangular facets and minimal lines. "
    "Framing the vista above, autumn maple tree branches stylized into spacious 3-tiered cloud-like woodblock canopy planes with hollow white interiors. "
    "Open airy composition, large colorable compartments, calm meditative mood, adult coloring book page. "
    "Square 1:1 aspect ratio, full square canvas composition."
)

ACCOUNTS = [
    "vut08348@gmail.com",
    "loch7444@gmail.com",
    "lynnphan2017@gmail.com",
    "chautnus@gmail.com",
    "ad01.lamlumber@gmail.com"
]

def clean_with_target_density(raw_path: Path, clean_path: Path, target_pct: float = 15.0):
    with Image.open(raw_path) as img:
        gray = img.convert("L")
        autocontrast = ImageOps.autocontrast(gray, cutoff=1)
        
        # Test thresholds to hit closest to target_pct
        best_t = 160
        best_diff = 999
        best_binary = None
        
        for t in range(120, 210, 5):
            table = [0 if i < t else 255 for i in range(256)]
            binary = autocontrast.point(table, mode="1")
            clean_l = binary.convert("L")
            w, h = clean_l.size
            scale = min(TARGET_WIDTH_PX / w, TARGET_HEIGHT_PX / h)
            new_w = int(w * scale)
            new_h = int(h * scale)
            resized = clean_l.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
            canvas = Image.new("L", (TARGET_WIDTH_PX, TARGET_HEIGHT_PX), color=255)
            paste_x = (TARGET_WIDTH_PX - new_w) // 2
            paste_y = (TARGET_HEIGHT_PX - new_h) // 2
            canvas.paste(resized, (paste_x, paste_y))
            
            arr = np.array(canvas)
            pct = (arr < 128).mean() * 100
            diff = abs(pct - target_pct)
            if diff < best_diff:
                best_diff = diff
                best_t = t
                best_binary = canvas
                
        print(f"[TUNING] Best threshold for ~{target_pct}%: t={best_t} -> Density: {(np.array(best_binary) < 128).mean() * 100:.2f}%")
        best_binary.save(clean_path, dpi=(TARGET_DPI, TARGET_DPI))

def run():
    img_bytes = None
    for email in ACCOUNTS:
        token, used_email = get_best_token(preferred_email=email)
        if not token:
            continue
        print(f"[INFO] Generating Page 03 Refined Bản A with: {used_email}...")
        try:
            img_bytes = call_generate_image(PAGE_03_PROMPT_A_REFINED, token)
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
        print("[FAIL] Failed to generate image.")
        return False
        
    raw_path = Path("assets/canada/raw/page_03_A_refined.png")
    clean_path = Path("assets/canada/processed/page_03_A_refined_clean.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    
    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw -> {raw_path}")
    
    # Process with calibrated threshold for ~15.0%
    clean_with_target_density(raw_path, clean_path, target_pct=15.0)
    
    # Add landmark badge
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, "Niagara Horseshoe Falls", "Ontario", 3)
        badged.save(clean_path)
        
    with Image.open(clean_path) as img:
        gray = img.convert("L")
        arr = np.array(gray)
        final_pct = (arr < 128).mean() * 100
        print(f"[METRIC] Final Page 03 Bản A Refined Black Density: {final_pct:.2f}% (Target: ~15.0%)")
        
    # Copy to variant_a
    brain_dir = r"C:/Users/Chau/.gemini/antigravity/brain/674909f7-e452-4364-a9b3-88ff0fbdeb5d"
    shutil.copy2(clean_path, os.path.join(brain_dir, "page_03_variant_a_refined.png"))
    
    # Build updated 4-panel comparison sheet
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
            "title": "3. PAGE 03 BẢN A REFINED (THEO YÊU CẦU)",
            "sub": f"Mật độ nét: {final_pct:.2f}% | Đã giảm về ~15%, giữ trọn vẹn tầng thác & lan can",
            "path": str(clean_path),
            "pos": (pad, header_h + pad * 2 + h),
            "border_color": (30, 136, 229)
        },
        {
            "title": "4. PAGE 03 BẢN B (TỐI GIẢN)",
            "sub": "Mật độ nét: 10.21% | Siêu thoáng, dải thác mở rộng tối đa",
            "path": "assets/canada/processed/page_03_vB_clean.png",
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
    shutil.copy2(out_sheet, os.path.join(brain_dir, "page_03_approval_sheet.jpg"))
    print(f"[OK] Updated comparison sheet -> {out_sheet}")

    return True

if __name__ == "__main__":
    run()
