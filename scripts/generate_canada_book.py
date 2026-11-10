#!/usr/bin/env python3
"""
Production Image Generation & Processing Engine for Canada Coloring Book.
Directly communicates with Google Cloud Code API (gemini-3.1-flash-image)
using accounts and tokens from antigravity-account-switcher (accounts.db).
Automatically fails over and rotates accounts when 429 quota is encountered.
Integrates full line cleaning (300 DPI) and colorable landmark badge typography.
"""

import os
import sys
import json
import base64
import time
import sqlite3
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image

# Add current workspace and tools dir to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")

from scripts.preprocess_lines import clean_and_threshold_image
from scripts.add_landmark_typography import add_landmark_badge
from check_image_quota import DB_PATH, refresh_token_if_needed

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

GENERATE_URL = "https://daily-cloudcode-pa.googleapis.com/v1internal:generateContent"
MODEL_ID = "gemini-3.1-flash-image"


def get_all_accounts():
    """Reads all accounts from account switcher database."""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT id, email, access_token, refresh_token, token_expiry, is_active FROM accounts").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_best_token(preferred_email=None):
    """Finds account with valid token, prioritizing preferred_email or accounts with high quota."""
    accounts = get_all_accounts()
    
    # Priority order
    priority_emails = [
        "vut08348@gmail.com",
        "ad01.lamlumber@gmail.com",
        "lynnphan2017@gmail.com",
        "loch7444@gmail.com",
        "chautnus@gmail.com",
        "dinhthithibwkg58231@gmail.com"
    ]
    if preferred_email:
        priority_emails.insert(0, preferred_email)
        
    for email in priority_emails:
        acc = next((a for a in accounts if a["email"] == email), None)
        if acc:
            try:
                token = refresh_token_if_needed(acc)
                if token:
                    return token, acc["email"]
            except Exception as e:
                print(f"[WARN] Failed refreshing token for {email}: {e}")
                
    # Fallback to any account
    for acc in accounts:
        try:
            token = refresh_token_if_needed(acc)
            if token:
                return token, acc["email"]
        except Exception:
            pass
    return None, None


def call_generate_image(prompt: str, token: str) -> bytes:
    """Calls gemini-3.1-flash-image directly and returns raw image bytes."""
    payload = {
        "project": "aicode-consumers",
        "model": MODEL_ID,
        "request": {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
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
        inner = res.get("response", {})
        candidates = inner.get("candidates", [])
        if not candidates:
            raise RuntimeError("No candidates returned in model response")
            
        parts = candidates[0].get("content", {}).get("parts", [])
        for p in parts:
            if "inlineData" in p:
                b64_data = p["inlineData"].get("data", "")
                return base64.b64decode(b64_data)
                
    raise RuntimeError("No inlineData image found in candidates parts")


def generate_single_page(page_meta: dict, preferred_email: str = "ad01.lamlumber@gmail.com") -> bool:
    """Generates, cleans, and badges a single coloring book page."""
    page_num = page_meta["page_number"]
    title = page_meta.get("display_title", page_meta.get("title", f"Page {page_num}"))
    province = page_meta.get("display_province", page_meta.get("province", "Canada"))
    prompt = page_meta["prompt"]
    
    raw_path = Path(f"assets/canada/raw/page_{page_num:02d}.png")
    clean_path = Path(f"assets/canada/processed/page_{page_num:02d}_clean.png")
    pub_path = Path(f"public/assets/canada/page_{page_num:02d}_clean.png")
    
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    pub_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"\n=======================================================")
    print(f" GENERATING PAGE {page_num:02d}: {title} ({province})")
    print(f"=======================================================")
    
    # Priority order across all 6 accounts with automatic retry on burst limit
    accounts_pool = [
        "ad01.lamlumber@gmail.com",
        "loch7444@gmail.com",
        "lynnphan2017@gmail.com",
        "vut08348@gmail.com",
        "chautnus@gmail.com",
        "dinhthithibwkg58231@gmail.com"
    ]
    img_bytes = None
    
    for attempt in range(6):  # Up to 6 rotation passes
        for email_candidate in accounts_pool:
            token, used_email = get_best_token(preferred_email=email_candidate)
            if not token:
                continue
                
            try:
                print(f"[INFO] Requesting model using account: {used_email}...")
                img_bytes = call_generate_image(prompt, token)
                print(f"[OK] Received image: {len(img_bytes)} bytes from {used_email}")
                break
            except urllib.error.HTTPError as e:
                err_msg = e.read().decode("utf-8", errors="ignore")
                print(f"[WARN] HTTP {e.code} on {used_email}: {err_msg[:100]}...")
                if e.code == 429:
                    print(f"[INFO] 429 on {used_email}. Rotating to next account...")
                    time.sleep(2)
                    continue
                else:
                    break
            except Exception as e:
                print(f"[ERROR] Generation error on {used_email}: {e}")
                time.sleep(2)
                continue
                
        if img_bytes:
            break
            
        print(f"[INFO] All accounts currently in rolling burst window. Waiting 30s for cooldown before pass {attempt+2}...")
        time.sleep(30)
            
    if not img_bytes:
        print(f"[FAIL] Could not generate Page {page_num:02d} with any available account.")
        return False
        
    # Save raw
    raw_path.write_bytes(img_bytes)
    print(f"[OK] Saved raw image -> {raw_path}")
    
    # Preprocess & Clean to 300 DPI
    clean_and_threshold_image(raw_path, clean_path, threshold=185)
    print(f"[OK] Preprocessed 300 DPI -> {clean_path}")
    
    # Add Colorable Landmark Typography Badge
    with Image.open(clean_path) as img:
        badged = add_landmark_badge(img, title, province, page_num)
        badged.save(clean_path)
        badged.save(pub_path)
    print(f"[OK] Inscribed typography badge & saved -> {clean_path}")
    
    return True


def run_pipeline(target_pages=None):
    prompts_file = Path("prompts/canada_prompts.json")
    with open(prompts_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    pages = data.get("pages", [])
    
    if target_pages:
        pages_to_run = [p for p in pages if p["page_number"] in target_pages]
    else:
        # Run all remaining missing pages
        pages_to_run = []
        for p in pages:
            num = p["page_number"]
            clean_file = Path(f"assets/canada/processed/page_{num:02d}_clean.png")
            if not clean_file.exists():
                pages_to_run.append(p)
                
    print(f"[INFO] Total pages to generate in this run: {len(pages_to_run)}")
    for p in pages_to_run:
        success = generate_single_page(p)
        if not success:
            print(f"[STOP] Stopped at Page {p['page_number']:02d} due to generation failure.")
            break
        # Gentle pacing between calls
        time.sleep(3)


if __name__ == "__main__":
    target = None
    if len(sys.argv) > 1:
        target = [int(x) for x in sys.argv[1:]]
    run_pipeline(target)
