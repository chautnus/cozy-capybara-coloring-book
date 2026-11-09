import sqlite3
from pathlib import Path

p = Path.home() / ".config/antigravity-account-switcher/accounts.db"
conn = sqlite3.connect(str(p))
c = conn.cursor()
types = c.execute("SELECT DISTINCT event_type FROM proxy_events").fetchall()
print("Event types:", types)
conn.close()
