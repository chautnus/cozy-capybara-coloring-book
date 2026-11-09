import json
import urllib.request
import base64
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")
import sqlite3
from check_image_quota import DB_PATH, refresh_token_if_needed

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
acc = conn.execute("SELECT * FROM accounts WHERE email='vut08348@gmail.com'").fetchone()
conn.close()

token = refresh_token_if_needed(dict(acc))

url = "https://daily-cloudcode-pa.googleapis.com/v1internal:generateContent"
payload = {
    "project": "aicode-consumers",
    "model": "gemini-3.1-flash-image",
    "request": {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": "A simple black and white line art coloring page of an elk in autumn."}
                ]
            }
        ]
    }
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "antigravity/cli/1.1.26"
    }
)

with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode("utf-8"))
    inner = res.get("response", {})
    candidates = inner.get("candidates", [])
    print(f"Candidates count: {len(candidates)}")
    if candidates:
        parts = candidates[0].get("content", {}).get("parts", [])
        for i, p in enumerate(parts):
            print(f"Part {i} keys: {list(p.keys())}")
            if "inlineData" in p:
                b64_data = p["inlineData"].get("data", "")
                mime = p["inlineData"].get("mimeType", "")
                raw_bytes = base64.b64decode(b64_data)
                print(f"Extracted image! Mime: {mime}, Size: {len(raw_bytes)} bytes")
                test_out = Path("assets/canada/raw/test_direct_api.jpg")
                test_out.write_bytes(raw_bytes)
                print(f"Saved test image to {test_out}!")
