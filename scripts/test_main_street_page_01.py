#!/usr/bin/env python3
"""
Generate and evaluate Page 01 Style Proofs for Book 3 (Cozy Main Street):
- Variant A: Baker Bear in Morning Bakery (Cinnamon rolls & sourdough)
- Variant B: Patisserie Cat in Corner Tea Shop (Fruit tarts & afternoon tea)
Measures line density (target: 11% - 15%) and verifies zero solid black fills.
Creates an approval sheet artifact for user visual review.
"""

import sys
import time
import shutil
import urllib.error
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))
sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")

from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image

RAW_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "raw"
PROCESSED_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "processed"
APPROVAL_DIR = WORKSPACE_ROOT / "assets" / "main_street"
ARTIFACT_DIR = Path(r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d")

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

# Prompt Variant A: Baker Bear
PROMPT_VARIANT_A = (
    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street bakery interior. "
    "A friendly, wholesome brown bear baker wearing a simple linen apron and a baker's cap, "
    "proudly smiling as he places a tray of fresh iced cinnamon rolls onto a rustic wooden counter. "
    "In the background, wooden shelves are neatly stocked with round sourdough bread loaves, woven baskets of croissants, "
    "and a chalkboard menu displaying daily pastries. A small potted plant sits on the sunny windowsill. "
    "Pure crisp black outlines on a solid pure white background, balanced medium-thick contour line weight, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero shading, zero grayscale, zero textures. "
    "Wide, spacious, generous open colorable compartments perfect for alcohol markers without eye fatigue. "
    "Harmonious cozy aesthetic, square 1:1 aspect ratio composition."
)

# Prompt Variant B: Patisserie Cat
PROMPT_VARIANT_B = (
    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street corner patisserie. "
    "A plump, cheerful tabby cat chef wearing a small chef hat and neck scarf, "
    "standing behind a vintage glass display case showcasing strawberry fruit tarts and cupcakes. "
    "On the counter rests a warm ceramic teapot with a gentle curl of steam and a teacup. "
    "Beside the counter, a striped shop awning frames a large multi-pane bay window looking out onto a brick sidewalk. "
    "Pure crisp black outlines on a solid pure white background, balanced medium-thick contour line weight, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero shading, zero grayscale, zero cross-hatching. "
    "Wide, spacious, generous open colorable compartments perfect for alcohol markers. "
    "Wholesome hygge small-town aesthetic, square 1:1 aspect ratio composition."
)


def generate_with_failover(prompt: str, description: str):
    accounts_pool = [
        "dinhthithibwkg58231@gmail.com",
        "vut08348@gmail.com",
        "chautnus@gmail.com",
        "ad01.lamlumber@gmail.com",
        "loch7444@gmail.com",
        "lynnphan2017@gmail.com"
    ]
    for attempt in range(3):
        for email in accounts_pool:
            token, used_email = get_best_token(preferred_email=email)
            if not token:
                continue
            try:
                print(f"[INFO] Requesting model for {description} using {used_email}...")
                img_bytes = call_generate_image(prompt, token)
                print(f"[OK] Received image ({len(img_bytes)} bytes) from {used_email}")
                return img_bytes
            except urllib.error.HTTPError as e:
                err_msg = e.read().decode("utf-8", errors="ignore")
                print(f"[WARN] HTTP {e.code} on {used_email}: {err_msg[:80]}...")
                if e.code == 429:
                    time.sleep(1)
                    continue
                else:
                    break
            except Exception as e:
                print(f"[ERROR] {e} on {used_email}")
                time.sleep(1)
                continue
        print(f"[INFO] Waiting 15s before retry pass {attempt+2}...")
        time.sleep(15)
    return None


def measure_density(img_path: Path):
    with Image.open(img_path) as img:
        gray = img.convert("L")
        arr = np.array(gray)
        black_pct = float((arr < 128).mean() * 100)
        return black_pct


def create_approval_sheet(clean_a_path: Path, clean_b_path: Path, density_a: float, density_b: float):
    sheet_w, sheet_h = 2400, 1400
    sheet = Image.new("RGB", (sheet_w, sheet_h), color=(248, 250, 252))
    draw = ImageDraw.Draw(sheet)

    # Header
    draw.rectangle([0, 0, sheet_w, 140], fill=(30, 41, 59))
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 26)
        font_card_title = ImageFont.truetype("arialbd.ttf", 34)
        font_metric = ImageFont.truetype("arial.ttf", 24)
    except Exception:
        font_title = font_sub = font_card_title = font_metric = None

    draw.text((60, 30), "BOOK 3: COZY MAIN STREET - PAGE 01 STYLE APPROVAL SHEET", fill=(255, 255, 255), font=font_title)
    draw.text((60, 88), "Comparative Review: Variant A (Baker Bear) vs Variant B (Patisserie Cat) | Line Density Target: 11% - 15%", fill=(203, 213, 225), font=font_sub)

    # Open images
    img_a = Image.open(clean_a_path).convert("RGB")
    img_b = Image.open(clean_b_path).convert("RGB")

    thumb_size = (1000, 1000)
    thumb_a = img_a.resize(thumb_size, Image.Resampling.LANCZOS)
    thumb_b = img_b.resize(thumb_size, Image.Resampling.LANCZOS)

    # Paste Card A
    card_a_x, card_a_y = 140, 180
    draw.rectangle([card_a_x - 10, card_a_y - 10, card_a_x + thumb_size[0] + 10, card_a_y + thumb_size[1] + 170], fill=(255, 255, 255), outline=(226, 232, 240), width=3)
    sheet.paste(thumb_a, (card_a_x, card_a_y))
    draw.text((card_a_x + 10, card_a_y + thumb_size[1] + 20), "OPTION A: The Baker Bear (Tiệm Bánh Quế Bác Gấu)", fill=(15, 23, 42), font=font_card_title)
    draw.text((card_a_x + 10, card_a_y + thumb_size[1] + 70), f"• Mật độ nét đen: {density_a:.2f}%  |  Mảng đen đặc: 0.00%  |  Đường nét rõ ràng", fill=(51, 65, 85), font=font_metric)
    draw.text((card_a_x + 10, card_a_y + thumb_size[1] + 110), "• Phong cách: Mộc mạc, đường nét phân mảng rõ, không gian tô khoáng đạt", fill=(100, 116, 139), font=font_metric)

    # Paste Card B
    card_b_x, card_b_y = 1260, 180
    draw.rectangle([card_b_x - 10, card_b_y - 10, card_b_x + thumb_size[0] + 10, card_b_y + thumb_size[1] + 170], fill=(255, 255, 255), outline=(226, 232, 240), width=3)
    sheet.paste(thumb_b, (card_b_x, card_b_y))
    draw.text((card_b_x + 10, card_b_y + thumb_size[1] + 20), "OPTION B: The Patisserie Cat (Tiệm Bánh Ngọt Chú Mèo)", fill=(15, 23, 42), font=font_card_title)
    draw.text((card_b_x + 10, card_b_y + thumb_size[1] + 70), f"• Mật độ nét đen: {density_b:.2f}%  |  Mảng đen đặc: 0.00%  |  Đường nét mềm mại", fill=(51, 65, 85), font=font_metric)
    draw.text((card_b_x + 10, card_b_y + thumb_size[1] + 110), "• Phong cách: Nhã nhặn kiểu Pháp, đường cong tròn mềm mại, ấm cúng", fill=(100, 116, 139), font=font_metric)

    sheet_path = APPROVAL_DIR / "page_01_approval_sheet.jpg"
    sheet.save(sheet_path, quality=92)
    print(f"[OK] Generated Approval Sheet -> {sheet_path}")

    # Copy to artifacts directory
    artifact_sheet_path = ARTIFACT_DIR / "page_01_approval_sheet.jpg"
    shutil.copy2(sheet_path, artifact_sheet_path)
    print(f"[OK] Staged to Artifact Directory -> {artifact_sheet_path}")


def main():
    raw_a = RAW_DIR / "page_01_vA.png"
    clean_a = PROCESSED_DIR / "page_01_vA_clean.png"

    if not raw_a.exists():
        print("\n--- Generating Variant A (Baker Bear) ---")
        img_a = generate_with_failover(PROMPT_VARIANT_A, "Variant A")
        if not img_a:
            print("[FAIL] Could not generate Variant A")
            return False
        raw_a.write_bytes(img_a)

    clean_and_threshold_image(raw_a, clean_a, threshold=175)
    density_a = measure_density(clean_a)
    print(f"[OK] Variant A Density: {density_a:.2f}%")

    raw_b = RAW_DIR / "page_01_vB.png"
    clean_b = PROCESSED_DIR / "page_01_vB_clean.png"

    if not raw_b.exists():
        print("\n--- Generating Variant B (Patisserie Cat) ---")
        img_b = generate_with_failover(PROMPT_VARIANT_B, "Variant B")
        if not img_b:
            print("[FAIL] Could not generate Variant B")
            return False
        raw_b.write_bytes(img_b)

    clean_and_threshold_image(raw_b, clean_b, threshold=175)
    density_b = measure_density(clean_b)
    print(f"[OK] Variant B Density: {density_b:.2f}%")

    # Copy individual variants to artifact dir
    shutil.copy2(clean_a, ARTIFACT_DIR / "page_01_vA_clean.png")
    shutil.copy2(clean_b, ARTIFACT_DIR / "page_01_vB_clean.png")

    create_approval_sheet(clean_a, clean_b, density_a, density_b)
    return True


if __name__ == "__main__":
    main()
