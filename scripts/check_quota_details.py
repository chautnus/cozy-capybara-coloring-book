import json
import urllib.request
import urllib.error
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")
import sqlite3
from check_image_quota import DB_PATH, refresh_token_if_needed

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
accounts = conn.execute("SELECT * FROM accounts").fetchall()
conn.close()

for a in accounts:
    email = a["email"]
    token = refresh_token_if_needed(dict(a))
    url = "https://daily-cloudcode-pa.googleapis.com/v1internal:generateContent"
    payload = {
        "project": "aicode-consumers",
        "model": "gemini-3.1-flash-image",
        "request": {"contents": [{"role": "user", "parts": [{"text": "Test"}]}]}
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
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"[{email}] SUCCESS 200 OK!")
            break
    except urllib.error.HTTPError as e:
        body = json.loads(e.read().decode("utf-8"))
        details = body.get("error", {}).get("details", [])
        meta = {}
        for d in details:
            if "metadata" in d:
                meta = d["metadata"]
        print(f"[{email}] HTTP {e.code} - delay: {meta.get('quotaResetDelay')}, resetTime: {meta.get('quotaResetTimeStamp')}")
