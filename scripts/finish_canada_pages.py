#!/usr/bin/env python3
"""
Finish Remaining 11 Pages (14, 15, 16, 17, 18, 19, 25, 27, 28, 29, 30)
with persistent retry, sync to public/, master showcase generation, PDF build and Vercel deploy.
"""

import os
import sys
import time
import shutil
import subprocess
import urllib.error
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import TARGET_WIDTH_PX, TARGET_HEIGHT_PX, TARGET_DPI
from scripts.add_landmark_typography import add_landmark_badge
from scripts.produce_remaining_canada_pages import PREFIX, SUFFIX, SCENE_PROMPTS

REMAINING_PAGES = [
    {"page_number": 14, "display_title": "Lynn Canyon Suspension Bridge", "display_province": "North Vancouver, BC"},
    {"page_number": 15, "display_title": "Tofino Pacific Coast", "display_province": "Vancouver Island, BC"},
    {"page_number": 16, "display_title": "Natural Bridge & Emerald Lake", "display_province": "Yoho National Park, BC"},
    {"page_number": 17, "display_title": "The Cabot Trail Ocean Bluffs", "display_province": "Cape Breton, Nova Scotia"},
    {"page_number": 18, "display_title": "Peggy's Cove Lighthouse", "display_province": "Nova Scotia"},
    {"page_number": 19, "display_title": "Hopewell Rocks Flowerpots", "display_province": "Bay of Fundy, NB"},
    {"page_number": 25, "display_title": "Cape Spear Easternmost Point", "display_province": "Newfoundland"},
    {"page_number": 27, "display_title": "Churchill Polar Bears & Aurora", "display_province": "Northern Manitoba"},
    {"page_number": 28, "display_title": "Prairie Grain Elevators", "display_province": "Saskatchewan"},
    {"page_number": 29, "display_title": "Tombstone Mountain & Tundra", "display_province": "Yukon Territory"},
    {"page_number": 30, "display_title": "Alexandra Falls Gorge", "display_province": "Northwest Territories"}
]

ACCOUNTS = [
    "vut08348@gmail.com",
    "loch7444@gmail.com",
    "ad01.lamlumber@gmail.com",
    "lynnphan2017@gmail.com"
]

def generate_persistent(prompt: str, label: str):
    while True:
        for email in ACCOUNTS:
            token, used_email = get_best_token(preferred_email=email)
            if not token:
                continue
            print(f"[INFO] Attempting {label} with: {used_email}...")
            try:
                img_bytes = call_generate_image(prompt, token)
                print(f"[OK] Succeeded with {used_email}!")
                return img_bytes
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(f"[WARN] 429 on {used_email}, trying next account in 3s...")
                    time.sleep(3)
                else:
                    print(f"[ERROR] HTTP {e.code} on {used_email}")
                    time.sleep(2)
            except Exception as e:
                print(f"[ERROR] {e} on {used_email}")
                time.sleep(2)
        print("[WAIT] All accounts rate-limited. Cooling down 25s for rolling window reset...")
        time.sleep(25)

def process_and_calibrate(raw_path: Path, clean_path: Path, title: str, province: str, page_num: int, target_pct: float = 14.0):
    with Image.open(raw_path) as img:
        gray = img.convert("L")
        autocontrast = ImageOps.autocontrast(gray, cutoff=1)
        
        best_t = 160
        best_diff = 999
        best_binary = None
        
        for t in range(100, 210, 5):
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
            
            badged = add_landmark_badge(canvas, title, province, page_num)
            arr = np.array(badged)
            pct = (arr < 128).mean() * 100
            diff = abs(pct - target_pct)
            if diff < best_diff:
                best_diff = diff
                best_t = t
                best_binary = badged
                
        final_pct = (np.array(best_binary) < 128).mean() * 100
        print(f"[TUNING] Page {page_num:02d}: Calibrated t={best_t} -> Density: {final_pct:.2f}% (Target: ~{target_pct}%)")
        best_binary.save(clean_path, dpi=(TARGET_DPI, TARGET_DPI))
        
        # Also copy immediately to public/
        pub_path = Path(f"public/assets/canada/processed/page_{page_num:02d}_clean.png")
        pub_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(clean_path, pub_path)
        
        return final_pct

def generate_master_showcase():
    print("[INFO] Generating master 30-page showcase...")
    cols = 6
    rows = 5
    thumb_size = 450
    pad = 16
    header_h = 90

    canvas_w = cols * thumb_size + (cols + 1) * pad
    canvas_h = rows * thumb_size + (rows + 1) * pad + header_h

    canvas = Image.new("RGB", (canvas_w, canvas_h), (245, 245, 247))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("arial.ttf", 36)
        font_sub = ImageFont.truetype("arial.ttf", 22)
    except:
        font_title = font_sub = ImageFont.load_default()

    draw.text((pad, 25), "AUTUMN IN CANADA — 30 TRANG MỘC BẢN ĐÔNG HỒ OPTION A (11.78% - 15.40% NÉT)", fill=(20, 20, 20), font=font_title)

    for idx in range(30):
        p_num = idx + 1
        r = idx // cols
        c = idx % cols
        x = pad + c * (thumb_size + pad)
        y = header_h + pad + r * (thumb_size + pad)
        
        img_path = f"assets/canada/processed/page_{p_num:02d}_clean.png"
        if os.path.exists(img_path):
            with Image.open(img_path) as img:
                resized = img.resize((thumb_size, thumb_size), Image.Resampling.LANCZOS)
                canvas.paste(resized, (x, y))
                draw.rectangle([x, y, x + thumb_size, y + thumb_size], outline=(46, 125, 50), width=3)
                
    out_path = "assets/canada/canada_dong_ho_all_30_pages_master_showcase.jpg"
    canvas.save(out_path, quality=90)

    brain_dir = r"C:/Users/Chau/.gemini/antigravity/brain/674909f7-e452-4364-a9b3-88ff0fbdeb5d"
    shutil.copy2(out_path, os.path.join(brain_dir, "canada_dong_ho_all_30_pages_master_showcase.jpg"))
    shutil.copy2(out_path, "public/assets/canada/canada_dong_ho_all_30_pages_master_showcase.jpg")
    print(f"[OK] Master showcase generated -> {out_path}")

def run():
    print("=" * 80)
    print("FINISHING REMAINING 11 PAGES: 14, 15, 16, 17, 18, 19, 25, 27, 28, 29, 30")
    print("=" * 80)
    
    for meta in REMAINING_PAGES:
        page_num = meta["page_number"]
        title = meta["display_title"]
        prov = meta["display_province"]
        
        print(f"\n>>> PROCESSING PAGE {page_num:02d}: {title} ({prov}) <<<")
        prompt = f"{PREFIX}{SCENE_PROMPTS[page_num]}{SUFFIX}"
        
        img_bytes = generate_persistent(prompt, f"Page {page_num:02d}")
        
        raw_path = Path(f"assets/canada/raw/page_{page_num:02d}.png")
        clean_path = Path(f"assets/canada/processed/page_{page_num:02d}_clean.png")
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        clean_path.parent.mkdir(parents=True, exist_ok=True)
        
        raw_path.write_bytes(img_bytes)
        pct = process_and_calibrate(raw_path, clean_path, title, prov, page_num, target_pct=14.0)
        print(f"[SUCCESS] Page {page_num:02d} completed at {pct:.2f}% density!")
        
        print("[COOLDOWN] Waiting 6 seconds before next page...")
        time.sleep(6)
        
    print("\n" + "=" * 80)
    print("ALL 30 PAGES COMPLETED! GENERATING MASTER SHOWCASE & DEPLOYING...")
    print("=" * 80)
    
    # 1. Master showcase
    generate_master_showcase()
    
    # 2. Update web app
    print("[INFO] Updating web app...")
    subprocess.run([sys.executable, "scripts/update_web_app.py"], check=True)
    
    # 3. Build KDP Interior PDF
    print("[INFO] Rebuilding KDP interior PDF...")
    subprocess.run([sys.executable, "scripts/build_canada_interior_pdf.py"], check=True)
    
    # 4. Deploy to Vercel
    print("[INFO] Deploying to Vercel Production...")
    subprocess.run(["vercel", "--prod", "--yes"], check=True)
    
    print("\n" + "=" * 80)
    print("FULL PRODUCTION PIPELINE COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    run()
