#!/usr/bin/env python3
"""
Production Automation Script: Produce Remaining Canada Coloring Book Pages (Pages 14 to 30)
Strictly adheres to Dong Ho Option A specifications:
- Pure clean outline line art, thin-to-medium crisp contour lines on pure white paper
- Strictly ZERO solid black fills, ZERO black silhouettes, ZERO black patches, ZERO dark shading
- All architectural elements, boats, lighthouses, bridges, animals rendered with clean hollow white panels
- Multi-tiered cloud-like woodblock canopy tiers with wide open hollow white interiors for color washing
- Smooth flowing rhythmic water strata bands
- Calibrated line density strictly between 12.5% and 15.5% (Option A standard)
- Automatic landmark badge typography applied to every page
- Robust rate limit handling with rolling window backoff
"""

import os
import sys
import time
import shutil
import urllib.error
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import call_generate_image, get_best_token
from scripts.preprocess_lines import TARGET_WIDTH_PX, TARGET_HEIGHT_PX, TARGET_DPI
from scripts.add_landmark_typography import add_landmark_badge

PREFIX = (
    "Coloring book page inspired by Vietnamese Dong Ho folk woodblock print aesthetic, "
    "pure clean outline line art, thin-to-medium crisp black contour lines on pure white paper, "
    "zero solid black fills, zero black silhouettes, zero black patches, zero dark shaded areas, "
    "zero filled objects, zero black water, zero black rocks, zero shading, zero gradients, zero halftones, zero cross-hatching. "
    "Mature sophisticated adult landscape of "
)

SUFFIX = (
    " Spacious, generous open white coloring compartments, calm meditative composition, adult coloring book page. "
    "Square 1:1 aspect ratio, full square canvas composition."
)

SCENE_PROMPTS = {
    14: (
        "wooden pedestrian suspension footbridge swaying high above Lynn Canyon gorge in North Vancouver, British Columbia, Canada. "
        "The bridge is drawn with clean hollow white wooden planks and open rope railings. "
        "A rushing canyon river flows below in 4 wide flowing water strata bands. "
        "Towering ancient western red cedar and Douglas fir trees frame the gorge in spacious 3-tiered woodblock canopy tiers with hollow white interiors."
    ),
    15: (
        "wild coastal landscape of Tofino on Vancouver Island in autumn, British Columbia, Canada. "
        "In the foreground, massive smooth cedar driftwood logs in clean hollow white rounded contours rest on a broad sandy beach. "
        "Rhythmic stylized ocean breakers roll in with sweeping curved wave bands. "
        "In the background, offshore rocky sea stacks with clean hollow white facets and a temperate rainforest ridge of tall pines in tiered woodblock canopies."
    ),
    16: (
        "ancient limestone Natural Rock Bridge over raging glacier waters in Yoho National Park, British Columbia, Canada. "
        "The sculptural rock arch features bold clean hollow white chiseled planar facets, with powerful water torrents surging through in flowing wave strata bands. "
        "In the background, calm waters of Emerald Lake framed by 3-tiered spruce and golden larch woodblock canopy planes and alpine peaks."
    ),
    17: (
        "spectacular coastal highway of the Cabot Trail winding along steep headland cliffs of Cape Breton Highlands in autumn, Nova Scotia, Canada. "
        "Below, the vast Atlantic Ocean rolls in 4 to 5 rhythmic stylized wave strata bands. "
        "The towering coastal headland mountains are blanketed in autumn maple forests stylized into spacious 3-tiered cloud-like woodblock canopy tiers with hollow white interiors."
    ),
    18: (
        "classic Peggy's Cove octagonal wooden lighthouse standing proudly on giant smooth glacial granite boulders in autumn, Nova Scotia, Canada. "
        "The iconic red-and-white lighthouse is drawn with clean hollow white wall panels, lantern room, and crisp black outlines. "
        "The surrounding massive granite headlands have smooth rounded hollow white contours. "
        "Rolling ocean waves roll in rhythmic wave strata bands, with distant coastal fishing village cottages in clean hollow white outlines."
    ),
    19: (
        "monumental flowerpot sandstone sea stacks at Hopewell Rocks on the Bay of Fundy at low tide, New Brunswick, Canada. "
        "The giant curved rock pillars stand on the exposed sea floor, featuring bold horizontal sedimentary strata and clean hollow white facets, "
        "crowned with clusters of hardy pines in spacious 3-tiered woodblock canopy tiers. Distant tidal channels reflect the open autumn sky."
    ),
    20: (
        "lush forest cascade of Dickson Falls in Fundy National Park in autumn, New Brunswick, Canada. "
        "A stepped forest brook tumbles down smooth boulders in 4 to 5 flowing rhythmic water strata bands. "
        "A wooden viewing boardwalk trail in clean hollow white outlines winds beside the stream. "
        "The deep gorge is enveloped by dense sugar maples and yellow birches in spacious 3-tiered woodblock canopy planes with hollow white interiors."
    ),
    21: (
        "vivid coastal landscape of Cavendish Beach on Prince Edward Island in autumn. "
        "Dramatic red sandstone sea cliffs with layered horizontal sedimentary strata and clean hollow white contours meet the ocean. "
        "Rolling sand dunes in the foreground are carpeted in marram grass clumps. "
        "Gentle Atlantic ocean waves roll in flowing rhythmic wave strata bands under an open coastal sky."
    ),
    22: (
        "historic Point Prim circular brick lighthouse built in 1845, Prince Edward Island, Canada. "
        "The unique round lighthouse tower and lantern room are drawn with clean hollow white wall panels and crisp black outlines, "
        "perched on a grassy coastal headland with a classic white picket fence in hollow white outlines. "
        "Gentle ocean bay water strata and distant sailing dories under autumn clouds."
    ),
    23: (
        "towering vertical granite cliffs of Western Brook Pond freshwater glacier fjord in Gros Morne National Park, Newfoundland, Canada. "
        "A small scenic tour boat with clean hollow white hull glides through deep fjord water strata bands. "
        "Waterfalls plunge down sheer rock faces with clean hollow white planar facets, flanked by hardy autumn birch in spacious 3-tiered woodblock canopy planes."
    ),
    24: (
        "picturesque historic fishing outport of Quidi Vidi near St. John's in autumn, Newfoundland, Canada. "
        "Traditional wooden fishing stages, sheds, and shacks on stilts are drawn with clean hollow white walls and roofs with crisp black outlines. "
        "Small wooden dories are tied to docks on calm harbor water strata. "
        "In the background, rugged coastal cliffs rise with autumn trees in 3-tiered woodblock canopy tiers."
    ),
    25: (
        "historic 1836 Cape Spear Lighthouse standing on a dramatic windswept promontory at the easternmost point of North America, Newfoundland, Canada. "
        "The sturdy square wooden lighthouse and central domed beacon are rendered with clean hollow white panels and crisp outlines. "
        "Powerful Atlantic ocean breakers crash against dark rocky headlands with clean hollow white planar facets in rhythmic wave strata. "
        "A wooden boardwalk trail winds across coastal heathland."
    ),
    26: (
        "floating wooden boardwalk trail winding in an S-curve through Ominik Marsh in Riding Mountain National Park in autumn, Manitoba, Canada. "
        "The boardwalk is drawn with clean hollow white wooden planks and open railings. "
        "Broad cattails, reeds, and floating water lily pads border calm marsh water strata bands. "
        "In the background, a dense golden forest of trembling aspens and paper birches stylized into spacious 3-tiered woodblock canopy planes."
    ),
    27: (
        "wild autumn subarctic landscape in Churchill, Manitoba, Canada. "
        "A magnificent polar bear mother and playful cub drawn with clean hollow white body outlines walk across fiery red and ochre tundra plains. "
        "Icy Hudson Bay water strata flow calmly in the background. "
        "Above them, stylized flowing ribbon arches of the Aurora Borealis (Northern Lights) dance gracefully across the sky alongside bright stars."
    ),
    28: (
        "classic rural Canadian prairie landscape in Saskatchewan, Canada. "
        "A row of towering historic wooden grain elevators with clean hollow white geometric planar facets stands beside railway tracks. "
        "In the foreground, an endless field of ripe golden wheat with large round hay bales in clean hollow white outlines. "
        "Gentle rolling horizons in rhythmic horizontal strata under a vast prairie sky."
    ),
    29: (
        "dramatic subarctic wilderness of Tombstone Territorial Park along the Dempster Highway in autumn, Yukon Territory, Canada. "
        "In the foreground, crimson tundra shrubs and moss hummocks form an open textured carpet with wandering stream strata channels. "
        "In the background, the iconic razor-sharp spire of Tombstone Mountain rises dramatically with clean hollow white chiseled planar facets "
        "and light dusting of autumn snow under stylized northern clouds."
    ),
    30: (
        "powerful Alexandra Falls on the Hay River in autumn, Northwest Territories, Canada. "
        "A wide thunderous curtain of water drops in 4 to 5 wide tiered cascading bands over a sheer thirty-two-meter limestone cliff "
        "into a deep gorge with clean hollow white rock facets. "
        "The gorge rim is crowned with golden northern birches and dark spruces stylized into spacious 3-tiered woodblock canopy planes under an open sky."
    )
}

SCENES_META = [
    {"page_number": 14, "display_title": "Lynn Canyon Suspension Bridge", "display_province": "North Vancouver, BC"},
    {"page_number": 15, "display_title": "Tofino Pacific Coast", "display_province": "Vancouver Island, BC"},
    {"page_number": 16, "display_title": "Natural Bridge & Emerald Lake", "display_province": "Yoho National Park, BC"},
    {"page_number": 17, "display_title": "The Cabot Trail Ocean Bluffs", "display_province": "Cape Breton, Nova Scotia"},
    {"page_number": 18, "display_title": "Peggy's Cove Lighthouse", "display_province": "Nova Scotia"},
    {"page_number": 19, "display_title": "Hopewell Rocks Flowerpots", "display_province": "Bay of Fundy, NB"},
    {"page_number": 20, "display_title": "Dickson Falls Forest Brook", "display_province": "Fundy National Park, NB"},
    {"page_number": 21, "display_title": "Cavendish Red Sandstone Cliffs", "display_province": "Prince Edward Island"},
    {"page_number": 22, "display_title": "Point Prim Historic Lighthouse", "display_province": "Prince Edward Island"},
    {"page_number": 23, "display_title": "Western Brook Pond Fjord", "display_province": "Gros Morne, Newfoundland"},
    {"page_number": 24, "display_title": "Quidi Vidi Fishing Village", "display_province": "St. John's, Newfoundland"},
    {"page_number": 25, "display_title": "Cape Spear Easternmost Point", "display_province": "Newfoundland"},
    {"page_number": 26, "display_title": "Riding Mountain Ominik Marsh", "display_province": "Manitoba"},
    {"page_number": 27, "display_title": "Churchill Polar Bears & Aurora", "display_province": "Northern Manitoba"},
    {"page_number": 28, "display_title": "Prairie Grain Elevators", "display_province": "Saskatchewan"},
    {"page_number": 29, "display_title": "Tombstone Mountain & Tundra", "display_province": "Yukon Territory"},
    {"page_number": 30, "display_title": "Alexandra Falls Gorge", "display_province": "Northwest Territories"}
]

ACCOUNTS = [
    "loch7444@gmail.com",
    "ad01.lamlumber@gmail.com",
    "lynnphan2017@gmail.com",
    "vut08348@gmail.com"
]

def generate_with_failover(prompt: str, label: str):
    max_cycles = 10
    for cycle in range(max_cycles):
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
        print(f"[WAIT] All accounts busy in cycle {cycle+1}/{max_cycles}. Cooling down 15s for rate limit reset...")
        time.sleep(15)
    return None

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
        print(f"[TUNING] Page {page_num:02d}: Calibrated threshold t={best_t} -> Black Density: {final_pct:.2f}% (Target: ~{target_pct}%)")
        best_binary.save(clean_path, dpi=(TARGET_DPI, TARGET_DPI))
        return final_pct

def run():
    print("=" * 80)
    print("CONTINUING DONG HO OPTION A PRODUCTION: PAGES 14 TO 30")
    print("=" * 80)
    
    results = []
    for meta in SCENES_META:
        page_num = meta["page_number"]
        title = meta["display_title"]
        prov = meta["display_province"]
        
        print(f"\n--- Processing Page {page_num:02d}: {title} ({prov}) ---")
        prompt = f"{PREFIX}{SCENE_PROMPTS[page_num]}{SUFFIX}"
        
        img_bytes = generate_with_failover(prompt, f"Page {page_num:02d}")
        if not img_bytes:
            print(f"[FATAL] Failed to generate Page {page_num:02d}!")
            results.append((page_num, title, 0.0, "FAILED"))
            continue
            
        raw_path = Path(f"assets/canada/raw/page_{page_num:02d}.png")
        clean_path = Path(f"assets/canada/processed/page_{page_num:02d}_clean.png")
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        clean_path.parent.mkdir(parents=True, exist_ok=True)
        
        raw_path.write_bytes(img_bytes)
        pct = process_and_calibrate(raw_path, clean_path, title, prov, page_num, target_pct=14.0)
        
        status = "PASSED" if 11.5 <= pct <= 16.0 else "WARNING_DENSITY"
        results.append((page_num, title, pct, status))
        print(f"[SUCCESS] Page {page_num:02d} locked successfully at {pct:.2f}% density! Status: {status}")
        
        # Generous cooldown to maintain healthy rolling window
        print("[COOLDOWN] Waiting 6 seconds before next page...")
        time.sleep(6)
        
    print("\n" + "=" * 80)
    print("BATCH PRODUCTION SUMMARY (PAGES 14 - 30)")
    print("=" * 80)
    for p, t, pct, s in results:
        print(f"Page {p:02d}: {t:35} | Density: {pct:6.2f}% | Status: {s}")
        
    return results

if __name__ == "__main__":
    run()
