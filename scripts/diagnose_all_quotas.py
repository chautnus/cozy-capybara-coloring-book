#!/usr/bin/env python3
"""
Comprehensive Quota & Limit Diagnostic Script for Antigravity Accounts.
"""

import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.generate_canada_book import get_all_accounts, refresh_token_if_needed, GENERATE_URL
MODELS_ENDPOINT = "https://daily-cloudcode-pa.googleapis.com/v1internal:fetchAvailableModels"

print("=" * 90)
print("BÁO CÁO KIỂM TRA HẠN MỨC TỪNG TÀI KHOẢN (gemini-3.1-flash-image)")
print("=" * 90)

accounts = get_all_accounts()
for a in accounts:
    email = a["email"]
    token = refresh_token_if_needed(a)
    print(f"\n[ACCOUNT]: {email}")
    
    # 1. Fetch available models quota
    req = urllib.request.Request(
        MODELS_ENDPOINT,
        data=b'{"project":"aicode-consumers"}',
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "antigravity/cli/1.1.26"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            models = data.get("models", {})
            img_model = models.get("gemini-3.1-flash-image", {})
            quota_info = img_model.get("quotaInfo", {})
            rem = quota_info.get("remainingFraction")
            reset = quota_info.get("resetTime")
            print(f"  > API Quota Fraction : {rem * 100 if rem is not None else 'N/A'}%")
            print(f"  > Quota Reset Time   : {reset}")
    except urllib.error.HTTPError as e:
        print(f"  > fetchAvailableModels HTTP {e.code}: {e.reason}")
    except Exception as e:
        print(f"  > fetchAvailableModels Error: {e}")

    # 2. Test actual generation call
    payload = {
        "project": "aicode-consumers",
        "model": "gemini-3.1-flash-image",
        "request": {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": "Minimalist single line test"}]
                }
            ]
        }
    }
    gen_req = urllib.request.Request(
        GENERATE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "antigravity/cli/1.1.26"
        }
    )
    try:
        with urllib.request.urlopen(gen_req, timeout=20) as resp:
            print("  > Trạng thái tạo ảnh: HOẠT ĐỘNG (Sinh ảnh thành công)")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"  > Trạng thái tạo ảnh: HTTP {e.code} ({e.reason})")
        try:
            err_json = json.loads(body)
            err = err_json.get("error", {})
            msg = err.get("message", "")
            details = err.get("details", [])
            print(f"    - Message        : \"{msg}\"")
            for d in details:
                meta = d.get("metadata", {})
                if "quotaResetDelay" in meta:
                    print(f"    - quotaResetDelay: {meta.get('quotaResetDelay')}")
        except Exception:
            print(f"    - Body: {body[:250]}")
    except Exception as e:
        print(f"  > Lỗi khác: {e}")

print("\n" + "=" * 90)
