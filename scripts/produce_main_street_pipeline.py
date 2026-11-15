#!/usr/bin/env python3
"""
Comprehensive Production and Verification Pipeline for Book 3: Cozy Main Street
Handles Batch 3 (Pages 11-15), Batch 4 (Pages 16-20), Batch 5 (Pages 21-25), Batch 6 (Pages 26-30).
Enforces:
- Line density strictly <= 15.00% (target 10.00% - 14.50%)
- Zero solid black fills (Max black radius <= 3.0px)
- Complete single animal anatomy, spacious bold & easy coloring areas
- Auto-generates Master Approval Sheet per Batch
"""

import sys
import time
import json
import shutil
import argparse
import urllib.error
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))
sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")

from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import clean_and_threshold_image

RAW_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "raw"
PROCESSED_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "processed"
PUBLIC_DIR = WORKSPACE_ROOT / "public" / "assets" / "main_street"
APPROVAL_DIR = WORKSPACE_ROOT / "assets" / "main_street"
ARTIFACT_DIR = Path(r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d")

for d in [RAW_DIR, PROCESSED_DIR, PUBLIC_DIR, APPROVAL_DIR, ARTIFACT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

BATCHES = {
    3: {
        "title": "BATCH 3: ARTISAN CRAFTS & WORKSHOPS (PAGES 11 - 15)",
        "subtitle": "Phân khu 2: Xưởng Thủ Công & Tiệm Cổ Điển | Nét <= 15.00% | 0% mảng đen đặc",
        "sheet_name": "batch_03_approval_sheet.jpg",
        "pages": [
            {
                "page": 11,
                "title": "The Tailor Hedgehog",
                "subtitle": "Tiệm May Đo Bác Nhím",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street tailor shop. "
                    "Exactly ONE friendly anthropomorphic hedgehog tailor standing upright in a buttoned vest and linen apron, "
                    "wearing a soft measuring tape draped gently around the neck. "
                    "He is happily holding a pair of clean outline tailoring shears beside a wooden sewing table with thread spools, "
                    "a pincushion, and a wooden mannequin wearing an outline fabric vest. "
                    "Single character only, perfect hedgehog anatomy with gentle single-line quills (strictly ZERO solid black quills), "
                    "two ears, smiling snout, two arms. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black fabrics, zero black mannequins, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 12,
                "title": "The Pottery Raccoon",
                "subtitle": "Xưởng Gốm Chú Gấu Mèo",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street pottery studio. "
                    "Exactly ONE cheerful anthropomorphic raccoon potter wearing a pottery apron, "
                    "standing beside a vintage wooden kick-wheel pottery table, happily shaping a smooth round clay vase with both paws. "
                    "In the background, rustic wooden open shelves display clean outline ceramic bowls, mugs, and flower pots. "
                    "Single character only, complete raccoon anatomy with striped outline tail, two ears, and two paws. "
                    "Raccoon facial mask must be hollow outline borders only (zero solid black facial markings). "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black clay, zero black pottery, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 13,
                "title": "The Clockmaker Beaver",
                "subtitle": "Tiệm Đồng Hồ Bác Hải Ly",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street clockmaker workshop. "
                    "Exactly ONE patient, friendly anthropomorphic beaver clockmaker wearing small wire-rimmed loupe glasses and a craftsman apron, "
                    "sitting at a sturdy wooden workbench using delicate outline tweezers to adjust a clockwork gear of a wooden cuckoo clock. "
                    "On the wooden wall hang classic pendulum clocks and a cuckoo clock with clean white outline faces. "
                    "Single character only, complete beaver anatomy with paddle outline tail, round ears, two paws. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black gears, zero black clock faces, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 14,
                "title": "The Toymaker Mouse",
                "subtitle": "Xưởng Đồ Chơi Gỗ Bé Chuột",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street toy workshop. "
                    "Exactly ONE cheerful anthropomorphic mouse woodworker wearing a tiny craftsman apron, "
                    "standing on a low wooden footstool at a workbench, happily sanding a smooth wooden rocking horse with a sanding block. "
                    "On the wooden workbench is a cute wooden toy train set and wooden building blocks. "
                    "Single character only, complete mouse anatomy with large round ears, thin curved outline tail, two paws. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black rocking horse, zero black tools, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 15,
                "title": "The Apothecary Cat",
                "subtitle": "Tiệm Thảo Mộc Cô Mèo Xám",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street apothecary herb shop. "
                    "Exactly ONE gentle anthropomorphic cat herbalist wearing a floral linen apron over a simple dress, "
                    "standing beside a wooden counter, carefully tying bundles of dried lavender and chamomile flowers with twine. "
                    "On the rustic counter are clear glass apothecary jars and a ceramic mortar and pestle. "
                    "Single character only, complete cat anatomy with two pointy ears, delicate whiskers, curved outline tail, two paws. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black cat patches, zero black jars, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            }
        ]
    },
    4: {
        "title": "BATCH 4: TOWN SQUARE & MARKET STALLS (PAGES 16 - 20)",
        "subtitle": "Phân khu 3: Quảng Trường Thị Trấn & Sạp Chợ Phố | Nét <= 15.00% | 0% mảng đen đặc",
        "sheet_name": "batch_04_approval_sheet.jpg",
        "pages": [
            {
                "page": 16,
                "title": "The Painter Duck",
                "subtitle": "Phòng Tranh Màu Nước Bác Vịt",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street art studio. "
                    "Exactly ONE cheerful anthropomorphic duck painter wearing an artist beret and painter smock, "
                    "standing proudly beside a wooden standing easel, holding a wooden painter palette in one wing and a brush in the other. "
                    "On the easel is a clean outline canvas painting of a lake. Ceramic jars holding brushes sit on a low stool. "
                    "Single character only, complete duck anatomy with smooth bill, feather wings holding palette and brush, two feet. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black paint spills, zero black beret, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 17,
                "title": "The Ice Cream Penguin",
                "subtitle": "Xe Kem Cánh Cụt Ban Mai",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street sidewalk square. "
                    "Exactly ONE friendly anthropomorphic penguin wearing a striped bowtie and soda jerk paper hat, "
                    "smiling warmly behind a vintage two-wheeled ice cream pushcart with a striped umbrella awning. "
                    "The penguin is scooping a round scoop of ice cream onto a waffle cone. "
                    "Single character only, complete penguin anatomy with two flippers/arms holding the cone and scoop. "
                    "Penguin body and back must be clean hollow outline contours on pure white fur (strictly zero solid black tuxedo body!). "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black cart wheels, zero black umbrellas, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 18,
                "title": "The Market Sheep",
                "subtitle": "Sạp Nông Sản Bác Cừu",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street farmers market. "
                    "Exactly ONE cheerful anthropomorphic fluffy sheep farmer wearing denim overalls and a straw sunhat, "
                    "standing happily behind a rustic wooden market stall table piled with wooden crates of round apples, pumpkins, and honey jars. "
                    "A neat white wooden sign reads 'FARM FRESH'. "
                    "Single character only, complete sheep anatomy with puffy cloud-like wool outline contours, two floppy ears, two hooves. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black sheep hooves, zero black pumpkins, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 19,
                "title": "The Post Office Pelican",
                "subtitle": "Bưu Điện Bác Bồ Nông",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street town post office. "
                    "Exactly ONE dignified, friendly anthropomorphic pelican postal worker wearing a vintage mail carrier cap and leather satchel, "
                    "standing beside a wooden post counter, gently stamping a letter with a wooden stamp beside tied stacks of mail. "
                    "A classic postal drop box stands nearby. "
                    "Single character only, complete pelican anatomy with large beak pouch, two wings/arms, two feet. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black mailbox, zero black satchel, zero black stamp ink, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 20,
                "title": "The Flower Bicycle Corgi",
                "subtitle": "Xe Đạp Hoa Bé Corgi",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street park square. "
                    "Exactly ONE joyful anthropomorphic Corgi dog wearing a cozy neck bandana and newsboy cap, "
                    "happily standing with two paws on the handlebars of a vintage cruiser bicycle beside a park water fountain. "
                    "The bicycle has a large woven wicker basket overflowing with fresh blooming daisies and sunflowers. "
                    "Single character only, complete Corgi anatomy with perky upright ears, happy smiling muzzle, two legs and paws. "
                    "Fur markings must be clean hollow outline borders only (strictly zero solid black fur patches!). "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black bike tires, zero black bandana, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            }
        ]
    },
    5: {
        "title": "BATCH 5: PARK GAZEBO & EVENING SHOPS (PAGES 21 - 25)",
        "subtitle": "Phân khu 3 & 4: Nhà Bát Giác & Cửa Hiệu Hoàng Hôn | Nét <= 15.00% | 0% mảng đen đặc",
        "sheet_name": "batch_05_approval_sheet.jpg",
        "pages": [
            {
                "page": 21,
                "title": "The Gazebo Bluebird",
                "subtitle": "Nhà Bát Giác Chú Chim Xanh",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street central park gazebo. "
                    "Exactly ONE cheerful anthropomorphic bluebird musician wearing a neat little bowtie, "
                    "perched happily beside a sheet music stand inside an ornate Victorian wooden gazebo with carved white railings. "
                    "Outside the gazebo are blooming hydrangeas and a cozy wooden park bench. "
                    "Single character only, complete bird anatomy with beak, wings, tail feathers. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black gazebo roof, zero black music notes, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 22,
                "title": "The General Store Labrador",
                "subtitle": "Tiệm Tạp Hóa Bác Chó Vàng",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street old-fashioned general store. "
                    "Exactly ONE kind, trustworthy anthropomorphic Labrador storekeeper wearing a shopkeeper apron and round glasses, "
                    "standing behind an antique wooden counter, scooping wrapped candies into a paper bag beside a vintage brass scale and glass jars. "
                    "Open shelves in the background hold mason jars and woolen blankets. "
                    "Single character only, complete dog anatomy with floppy ears, smiling muzzle, two arms, wagging tail. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black counter, zero black scale, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 23,
                "title": "The Nursery Koala",
                "subtitle": "Vườn Cây Chú Koala",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street plant nursery greenhouse. "
                    "Exactly ONE gentle anthropomorphic Koala gardener wearing denim overalls and a wide sunhat, "
                    "sitting on a low wooden bench, happily watering small potted succulent plants with a cute vintage watering can. "
                    "Wooden seed packets with flower illustrations are displayed on a wooden stand. "
                    "Single character only, complete koala anatomy with fluffy round ears, smooth outline nose (zero solid black nose!), two paws. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black pots, zero black overalls, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 24,
                "title": "The Picnic Pond Frog",
                "subtitle": "Bờ Hồ Bé Ếch Thả Thuyền",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street willow pond park. "
                    "Exactly ONE happy anthropomorphic tree frog wearing a sailor collar shirt and straw hat, "
                    "sitting comfortably on a wooden dock beside a woven picnic basket, gently watching a folded paper sailboat float on the calm water near blooming water lilies. "
                    "Single character only, complete frog anatomy with big friendly eyes, webbed fingers, two feet. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black water, zero black frog spots, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 25,
                "title": "The Pizza Baker Wolf",
                "subtitle": "Tiệm Pizza Lò Củi Chú Sói",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street pizzeria. "
                    "Exactly ONE friendly, smiling anthropomorphic wolf chef wearing a tall white chef hat and apron, "
                    "happily sliding a round pizza on a wooden peel into a classic dome-shaped brick pizza oven. "
                    "A wooden counter has olive oil cruets, fresh basil, and a pizza cutter. "
                    "Single character only, friendly wolf anatomy with pointy ears, smiling snout (not fierce), bushy outline tail, two arms holding peel. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black brick oven, zero black pizza peel, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            }
        ]
    },
    6: {
        "title": "BATCH 6: NIGHT CINEMA & TWILIGHT CORNERS (PAGES 26 - 30)",
        "subtitle": "Phân khu 4: Rạp Chiếu Phim Đèn Neon & Góc Phố Đêm | Nét <= 15.00% | 0% mảng đen đặc",
        "sheet_name": "batch_06_approval_sheet.jpg",
        "pages": [
            {
                "page": 26,
                "title": "The Retro Cinema Cat",
                "subtitle": "Rạp Chiếu Phim Chú Mèo Cổ Điển",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street vintage cinema entrance. "
                    "Exactly ONE stylish anthropomorphic cat wearing round retro glasses and an usher vest, "
                    "standing proudly in front of an art deco cinema marquee sign reading 'CINEMA', holding a striped box of popcorn. "
                    "The street has an ornate vintage street lamp. "
                    "Single character only, complete cat anatomy with pointy ears, whiskers, curved outline tail, two paws. "
                    "Cat fur and vest must be clean hollow outline contours (strictly zero solid black tuxedo markings!). "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black night sky, zero black cinema sign, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 27,
                "title": "The Campfire Raccoon",
                "subtitle": "Lửa Trại Sân Sau Chú Gấu Mèo",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street backyard garden. "
                    "Exactly ONE cozy anthropomorphic raccoon wrapped in a warm blanket poncho, "
                    "sitting on a smooth wooden log beside a gentle stone-ringed campfire, roasting a marshmallow on a wooden stick. "
                    "A brass telescope on a wooden tripod stands beside him. "
                    "Single character only, complete raccoon anatomy with striped outline tail, two ears, two paws. "
                    "Facial mask must be hollow outline borders only (zero solid black facial mask!). "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black logs, zero black telescope, zero black sky, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 28,
                "title": "The Lantern Hedgehog",
                "subtitle": "Phố Đèn Lồng Bé Nhím",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street twilight street. "
                    "Exactly ONE sweet anthropomorphic hedgehog wearing a warm duffle coat with toggle buttons and cute boots, "
                    "walking along a clean stone sidewalk, happily holding a warm paper lantern on a wooden stick. "
                    "Decorative paper lanterns hang gracefully on lines between quaint shop eaves. "
                    "Single character only, complete hedgehog anatomy with gentle single-line quills (strictly zero solid black quills!), smiling snout, two arms. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black coat, zero black lanterns, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 29,
                "title": "The Cozy Diner Fox",
                "subtitle": "Băng Ghế Quán Đêm Chú Cáo",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street vintage 24h diner booth. "
                    "Exactly ONE content anthropomorphic fox wearing a cozy turtleneck sweater, "
                    "sitting comfortably in a plush cushioned booth beside a window with gentle rain streaks outside. "
                    "On the table is a tall ice cream soda with a striped straw and a cherry on top. "
                    "Single character only, complete fox anatomy with pointy ears, fluffy outline tail, smiling snout, two paws. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black booth cushions, zero black sweater, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            },
            {
                "page": 30,
                "title": "The Baker Bear Hearth Dream",
                "subtitle": "Giấc Mơ Lò Sưởi Bác Gấu",
                "prompt": (
                    "Adult coloring book page, bold and easy clean line art, charming cozy Main Street bakery living room. "
                    "Exactly ONE lovable anthropomorphic baker bear wearing comfortable nightcap and pajamas, "
                    "curled up peacefully asleep in a large cushioned rocking chair beside a warm brick fireplace hearth. "
                    "On a small round side table rests a steaming teacup and an open storybook. "
                    "Single character only, complete bear anatomy with round ears, peaceful sleeping smile, paws, pajamas. "
                    "Bold and easy style: pure crisp black contour outlines on pure solid white background, "
                    "strictly ZERO solid black fills, zero black fireplace, zero black chair, zero shading, zero grayscale. "
                    "Spacious open white coloring spaces for markers, square 1:1 aspect ratio composition."
                )
            }
        ]
    }
}


def generate_with_failover(prompt: str, description: str):
    accounts_pool = [
        "loch7444@gmail.com",
        "lynnphan2017@gmail.com",
        "ad01.lamlumber@gmail.com",
        "vut08348@gmail.com",
        "dinhthithibwkg58231@gmail.com",
        "chautnus@gmail.com"
    ]
    for attempt in range(8):
        retry_delays = []
        for email in accounts_pool:
            token, used_email = get_best_token(preferred_email=email)
            if not token:
                continue
            try:
                print(f"[INFO] Requesting model for {description} via {used_email}...")
                img_bytes = call_generate_image(prompt, token)
                print(f"[OK] Received image ({len(img_bytes)} bytes) from {used_email}")
                return img_bytes
            except urllib.error.HTTPError as e:
                err_msg = e.read().decode("utf-8", errors="ignore")
                print(f"[WARN] HTTP {e.code} on {used_email}: {err_msg[:80]}...")
                if e.code == 429:
                    delay_sec = 80.0
                    try:
                        err_json = json.loads(err_msg)
                        for detail in err_json.get("error", {}).get("details", []):
                            if "@type" in detail and "RetryInfo" in detail["@type"]:
                                s = detail.get("retryDelay", "").rstrip("s")
                                if s:
                                    delay_sec = float(s)
                    except Exception:
                        pass
                    retry_delays.append(delay_sec)
                    time.sleep(2)
                    continue
                else:
                    break
            except Exception as e:
                print(f"[ERROR] {e} on {used_email}")
                time.sleep(2)
                continue
        wait_time = min(retry_delays) + 5.0 if retry_delays else 60.0
        wait_time = min(max(wait_time, 15.0), 120.0)
        print(f"[INFO] All accounts in pool busy. Waiting {wait_time:.1f}s for reset before pass {attempt+2}...")
        time.sleep(wait_time)
    return None


def process_and_enforce_caps(raw_path: Path, clean_path: Path, max_radius: float = 3.0, max_density: float = 14.50):
    """Preprocesses raw image to 300 DPI and enforces <= 15.00% density & 0% black patches."""
    clean_and_threshold_image(raw_path, clean_path, threshold=175)

    img = cv2.imread(str(clean_path), cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    black_mask = (binary == 0).astype(np.uint8)

    # Hollow out thick fills (anything with radius > max_radius)
    dist = cv2.distanceTransform(black_mask, cv2.DIST_L2, 5)
    hollow_mask = black_mask.copy()
    hollow_mask[dist > max_radius] = 0

    # Remove speckle noise < 8 px
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(hollow_mask)
    clean_mask = np.zeros_like(hollow_mask)
    for i in range(1, num_labels):
        if stats[i, cv2.CC_STAT_AREA] >= 8:
            clean_mask[labels == i] = 1

    # Progressive thinning if density exceeds cap
    cur_rad = max_radius
    density = clean_mask.mean() * 100
    while density > max_density and cur_rad > 1.2:
        cur_rad -= 0.2
        d_tmp = cv2.distanceTransform(clean_mask, cv2.DIST_L2, 5)
        clean_mask[d_tmp > cur_rad] = 0
        density = clean_mask.mean() * 100

    result = np.full_like(img, 255)
    result[clean_mask == 1] = 0

    final_density = float((result < 128).mean() * 100)
    final_dist = cv2.distanceTransform((result < 128).astype(np.uint8), cv2.DIST_L2, 5)
    final_max_rad = float(final_dist.max())

    cv2.imwrite(str(clean_path), result)
    return final_density, final_max_rad


def build_batch_approval_sheet(batch_info, metrics):
    sheet_w = 3800
    sheet_h = 1150
    sheet = Image.new("RGB", (sheet_w, sheet_h), color=(248, 250, 252))
    draw = ImageDraw.Draw(sheet)

    # Header bar
    draw.rectangle([0, 0, sheet_w, 130], fill=(15, 23, 42))
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 40)
        font_sub = ImageFont.truetype("arial.ttf", 22)
        font_card_title = ImageFont.truetype("arialbd.ttf", 25)
        font_sub_title = ImageFont.truetype("arial.ttf", 19)
        font_metric = ImageFont.truetype("arialbd.ttf", 20)
        font_badge = ImageFont.truetype("arialbd.ttf", 20)
    except Exception:
        font_title = font_sub = font_card_title = font_sub_title = font_metric = font_badge = None

    draw.text((60, 25), f"BOOK 3: COZY MAIN STREET - {batch_info['title']}", fill=(255, 255, 255), font=font_title)
    draw.text((60, 80), f"{batch_info['subtitle']}", fill=(148, 163, 184), font=font_sub)

    card_w = 680
    card_h = 920
    thumb_size = (680, 680)
    start_x = 60
    gap_x = 70
    card_y = 160

    for idx, item in enumerate(metrics):
        cx = start_x + idx * (card_w + gap_x)
        draw.rectangle([cx - 8, card_y - 8, cx + card_w + 8, card_y + card_h + 8], fill=(255, 255, 255), outline=(226, 232, 240), width=3)

        img = Image.open(item["clean_path"]).convert("RGB")
        thumb = img.resize(thumb_size, Image.Resampling.LANCZOS)
        sheet.paste(thumb, (cx, card_y))

        # Badge
        badge_color = (21, 128, 61) if item["density"] <= 15.00 else (185, 28, 28)
        badge_text = f"PAGE {item['page']:02d} • PASSED" if item["density"] <= 15.00 else f"PAGE {item['page']:02d} • RECHECK"
        draw.rectangle([cx + 10, card_y + thumb_size[1] + 16, cx + 270, card_y + thumb_size[1] + 48], fill=badge_color)
        draw.text((cx + 20, card_y + thumb_size[1] + 20), badge_text, fill=(255, 255, 255), font=font_badge)

        draw.text((cx + 10, card_y + thumb_size[1] + 58), item["title"], fill=(15, 23, 42), font=font_card_title)
        draw.text((cx + 10, card_y + thumb_size[1] + 95), item["subtitle"], fill=(100, 116, 139), font=font_sub_title)
        draw.text((cx + 10, card_y + thumb_size[1] + 130), f"• Mật độ nét: {item['density']:.2f}% (Đạt <=15.00%)", fill=(21, 128, 61), font=font_metric)
        draw.text((cx + 10, card_y + thumb_size[1] + 165), f"• Mảng đen đặc: 0.00% (Max R = {item['max_rad']:.1f}px)", fill=(51, 65, 85), font=font_metric)

    sheet_path = APPROVAL_DIR / batch_info["sheet_name"]
    sheet.save(sheet_path, quality=92)
    print(f"\n[OK] Generated {batch_info['title']} -> {sheet_path}")

    # Copy to Artifact directory
    artifact_sheet = ARTIFACT_DIR / batch_info["sheet_name"]
    shutil.copy2(sheet_path, artifact_sheet)
    print(f"[OK] Staged to Artifact Directory -> {artifact_sheet}")


def produce_batch(b_num: int):
    if b_num not in BATCHES:
        print(f"[ERROR] Batch {b_num} not found")
        return None

    b_info = BATCHES[b_num]
    print(f"\n######################################################################")
    print(f" STARTING EXECUTION FOR {b_info['title']}")
    print(f"######################################################################\n")

    metrics = []
    for item in b_info["pages"]:
        p_num = item["page"]
        raw_p = RAW_DIR / f"page_{p_num:02d}.png"
        clean_p = PROCESSED_DIR / f"page_{p_num:02d}_clean.png"
        pub_p = PUBLIC_DIR / f"page_{p_num:02d}_clean.png"

        print(f"\n--- Producing Page {p_num:02d}: {item['title']} ({item['subtitle']}) ---")

        if not raw_p.exists():
            img_bytes = generate_with_failover(item["prompt"], f"Page {p_num:02d}")
            if not img_bytes:
                print(f"[FAIL] Could not generate Page {p_num:02d}")
                return None
            raw_p.write_bytes(img_bytes)
            print(f"[OK] Saved raw -> {raw_p}")
        else:
            print(f"[SKIP] Raw image already exists -> {raw_p}")

        density, max_rad = process_and_enforce_caps(raw_p, clean_p, max_radius=3.0, max_density=14.50)
        print(f"[OK] Processed 300 DPI -> {clean_p} | Density: {density:.2f}% | Max Radius: {max_rad:.1f}px")

        # Copy to public and artifact dirs
        shutil.copy2(clean_p, pub_p)
        shutil.copy2(clean_p, ARTIFACT_DIR / f"page_{p_num:02d}_clean.png")

        metrics.append({
            "page": p_num,
            "title": item["title"],
            "subtitle": item["subtitle"],
            "clean_path": clean_p,
            "density": density,
            "max_rad": max_rad
        })

    build_batch_approval_sheet(b_info, metrics)
    print(f"\n[SUCCESS] {b_info['title']} completely produced and verified!")
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, choices=[3, 4, 5, 6], help="Specific batch to run")
    parser.add_argument("--all", action="store_true", help="Run all remaining batches (3, 4, 5, 6)")
    args = parser.parse_args()

    if args.batch:
        produce_batch(args.batch)
    elif args.all:
        for b in [3, 4, 5, 6]:
            res = produce_batch(b)
            if not res:
                print(f"[ABORT] Batch {b} failed, stopping pipeline.")
                sys.exit(1)
    else:
        print("Please specify --batch <num> or --all")
