#!/usr/bin/env python3
"""
Generate 3 distinct colorways for the Dong Ho Layered Prototype (Page 01 Algonquin Canoe)
using exact multimodal image-to-image colorization and 100% line preservation via Multiply blend.

Colorways:
1. Traditional Dong Ho Folk Heritage (Hồn Dân Gian Đông Hồ - Vàng hoa hòe, đỏ son, xanh chàm, giấy điệp)
2. Vibrant Canadian Maple Glow (Hoàng Hôn Rực Lửa - Đỏ phong rực rỡ, cam lửa, hồ xanh ngọc bích)
3. Misty Nordic Hygge / Mindful Calm (Sương Khói Tĩnh Lặng - Ochre mù tạt, cam đất nung, xám sương mù)
"""

import os
import sys
import json
import base64
import time
import urllib.request
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")
from check_image_quota import get_accounts, refresh_token_if_needed

GENERATE_URL = "https://daily-cloudcode-pa.googleapis.com/v1internal:generateContent"
MODEL_ID = "gemini-3.1-flash-image"

COLORWAYS = [
    {
        "id": "colorway_1_heritage",
        "name": "1. Hồn Dân Gian Đông Hồ (Folk Heritage)",
        "desc": "Bảng màu truyền thống: Giấy điệp óng ả, vàng hoa hòe, đỏ sỏi son, xanh lá chàm",
        "prompt": (
            "Color this exact coloring book line art using the authentic natural palette of traditional "
            "Vietnamese Dong Ho folk woodblock prints (tranh Dan gian Dong Ho). "
            "The background paper should have a warm off-white scallop shell diep paper glow. "
            "The layered maple tree foliage is colored with warm sophora flower yellow (vang hoa hoe) "
            "layered beneath vibrant red cinnabar stone (do soi son) and orange madder (vang cam). "
            "The serene lake water is colored in soft indigo plant green and verdigris blue-green (xanh cham, xanh gi dong). "
            "The wooden canoe is rich warm earth wood brown. "
            "Clean flat woodblock color planes with gentle traditional layered washes, 100% maintaining all black outlines."
        )
    },
    {
        "id": "colorway_2_vibrant",
        "name": "2. Thu Rực Rỡ Canada (Vibrant Maple Glow)",
        "desc": "Hoàng hôn ngũ sắc: Đỏ phong rực lửa, cam hổ phách, hồ xanh ngọc bích sâu thẳm",
        "prompt": (
            "Color this exact coloring book line art in a breathtaking vibrant Canadian autumn twilight palette. "
            "The sky glows with golden-hour amber and warm peach sunset. "
            "The maple canopies burst with fiery scarlet red, rich crimson, and golden amber layered color tones. "
            "The calm lake water is a deep luminous turquoise and glacial sapphire blue reflecting the warm sky. "
            "The wooden cedar canoe is polished rich warm mahogany wood. "
            "Rich saturated colors, clean woodcut color blocking, perfectly filled compartments, maintaining all black outlines."
        )
    },
    {
        "id": "colorway_3_nordic",
        "name": "3. Sương Khói Tĩnh Lặng (Misty Nordic Hygge)",
        "desc": "Tĩnh tâm thiền định: Vàng mù tạt, cam đất nung terracotta, xanh rêu sage, hồ sương mù",
        "prompt": (
            "Color this exact coloring book line art in a calm, mindful, cozy Nordic Hygge and earth-tone palette. "
            "The sky and distant hills are misty morning fog gray and muted slate blue. "
            "The layered autumn trees are colored in muted mustard yellow ochre, warm burnt terracotta, and gentle sage green. "
            "The tranquil lake is soft fog-gray with subtle water reflections. "
            "The canoe is weathered driftwood gray-brown. "
            "Sophisticated, relaxing, meditative color harmony, matte aesthetic, maintaining all black outlines."
        )
    }
]


def colorize_image(b64_line_img: str, prompt_text: str, token: str) -> bytes:
    payload = {
        "project": "aicode-consumers",
        "model": MODEL_ID,
        "request": {
            "contents": [{
                "role": "user",
                "parts": [
                    {"text": prompt_text},
                    {"inlineData": {"mimeType": "image/png", "data": b64_line_img}}
                ]
            }]
        }
    }
    req = urllib.request.Request(
        GENERATE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "antigravity/cli/1.1.26"
        }
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        parts = res.get("response", {}).get("candidates", [])[0].get("content", {}).get("parts", [])
        for p in parts:
            if "inlineData" in p:
                return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError("No image data returned from colorization call.")


def main():
    line_path = Path("assets/canada/processed/prototype_dong_ho_page_01.png")
    if not line_path.exists():
        print(f"[FAIL] Line art not found at {line_path}")
        return

    accounts = get_accounts()
    token = None
    account_email = None
    for acc in accounts:
        if any(preferred in acc["email"] for preferred in ["ad01", "loch7444", "lynnphan", "vut08348"]):
            t = refresh_token_if_needed(acc)
            if t:
                token = t
                account_email = acc["email"]
                break

    if not token:
        print("[FAIL] Could not retrieve active access token.")
        return

    print(f"[INFO] Using account: {account_email} for colorway generation.")
    b64_line = base64.b64encode(line_path.read_bytes()).decode("utf-8")
    orig_line_img = Image.open(line_path).convert("RGB")

    colored_imgs = {}

    for cw in COLORWAYS:
        cid = cw["id"]
        cname = cw["name"]
        print(f"\n=======================================================")
        print(f" RENDERING: {cname}")
        print(f"=======================================================")
        out_raw = Path(f"assets/canada/raw/{cid}.png")
        out_clean = Path(f"assets/canada/processed/{cid}.png")

        try:
            raw_bytes = colorize_image(b64_line, cw["prompt"], token)
            out_raw.parent.mkdir(parents=True, exist_ok=True)
            out_clean.parent.mkdir(parents=True, exist_ok=True)
            out_raw.write_bytes(raw_bytes)

            # Resize colored image to match line art exactly
            raw_colored = Image.open(out_raw).convert("RGB")
            raw_resized = raw_colored.resize(orig_line_img.size, Image.Resampling.LANCZOS)

            # Preserve 100% original black lines via Multiply
            final_img = ImageChops.multiply(raw_resized, orig_line_img)
            final_img.save(out_clean)
            colored_imgs[cid] = final_img
            print(f"[OK] Saved -> {out_clean}")

        except Exception as exc:
            print(f"[ERROR] Failed {cid}: {exc}")
        time.sleep(3)

    # Build Master 4-Panel Showcase Collage
    print("\n[INFO] Compiling Master 4-Panel Showcase Collage...")
    sz = 750
    panel_w = sz
    panel_h = sz
    padding = 15

    canvas = Image.new("RGB", (panel_w * 4 + padding * 5, panel_h + 100), (248, 246, 242))
    draw = ImageDraw.Draw(canvas)

    panels = [
        ("BẢN GỐC: VÁN NÉT KHẮC GỖ\n(Black & White Line Art)", orig_line_img),
        ("PHỐI MÀU 1: HỒN DÂN GIAN ĐÔNG HỒ\n(Giấy điệp, hoa hòe, đỏ son, chàm)", colored_imgs.get("colorway_1_heritage")),
        ("PHỐI MÀU 2: THU RỰC RỠ CANADA\n(Hoàng hôn rực lửa, cam, ngọc bích)", colored_imgs.get("colorway_2_vibrant")),
        ("PHỐI MÀU 3: SƯƠNG KHÓI TĨNH LẶNG\n(Ochre, terracotta, rêu phong Hygge)", colored_imgs.get("colorway_3_nordic")),
    ]

    for idx, (title, img) in enumerate(panels):
        x = padding + idx * (panel_w + padding)
        y = 80
        if img:
            thumb = img.resize((panel_w, panel_h), Image.Resampling.LANCZOS)
            canvas.paste(thumb, (x, y))
        else:
            draw.rectangle([x, y, x + panel_w, y + panel_h], fill=(220, 220, 220))

        # Title
        color_tag = (120, 40, 20) if idx == 0 else ((180, 50, 20) if idx == 1 else ((160, 40, 90) if idx == 2 else (30, 90, 50)))
        draw.text((x + panel_w // 2, 40), title, fill=color_tag, anchor="mm")

    showcase_path = Path("assets/canada/canada_dong_ho_colorways_showcase.jpg")
    canvas.save(showcase_path, quality=92)
    print(f"[DONE] Saved Master Showcase -> {showcase_path}")

    # Copy to brain artifact directory
    import shutil
    artifact_dir = Path(r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d")
    shutil.copy(showcase_path, artifact_dir / "canada_dong_ho_colorways_showcase.jpg")
    print(f"[DONE] Copied to artifact directory.")


if __name__ == "__main__":
    main()
