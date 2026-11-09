import time
from pathlib import Path

now = time.time()
paths = [
    Path.home() / ".gemini",
    Path.home() / ".config",
    Path.home() / "AppData/Roaming/Antigravity",
    Path.home() / "AppData/Local/antigravity"
]

for p in paths:
    if p.exists():
        for f in p.rglob("*"):
            if f.is_file():
                try:
                    mtime = f.stat().st_mtime
                    if now - mtime < 900:  # modified in last 15 mins
                        print(f"{f} ({(now-mtime)/60:.1f} mins ago)")
                except Exception:
                    pass
