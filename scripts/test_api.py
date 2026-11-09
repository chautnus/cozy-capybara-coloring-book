import json
import urllib.request
import sys
from pathlib import Path
sys.path.insert(0, ".")
from scripts.check_db import p
import sqlite3

# Get token for vut08348@gmail.com
conn = sqlite3.connect(str(p))
conn.row_factory = sqlite3.Row
acc = conn.execute("SELECT * FROM accounts WHERE email='vut08348@gmail.com'").fetchone()
conn.close()

from scripts.preprocess_lines import clean_and_threshold_image
# Import refresh logic from check_image_quota
import sys
sys.path.insert(0, r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")
from check_image_quota import refresh_token_if_needed

token = refresh_token_if_needed(dict(acc))
print("Got valid token for vut08348:", bool(token))

# Test fetchAvailableModels
url = "https://daily-cloudcode-pa.googleapis.com/v1internal:fetchAvailableModels"
req = urllib.request.Request(
    url,
    data=b'{"project":"aicode-consumers"}',
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "antigravity/cli/1.1.26"}
)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("fetchAvailableModels OK! Keys:", list(data.keys()))
        models = data.get("models", {})
        print("Available models:", list(models.keys()))
except Exception as e:
    print("Error:", e)
