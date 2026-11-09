import sqlite3
from pathlib import Path

p = Path.home() / ".config/antigravity-account-switcher/accounts.db"
conn = sqlite3.connect(str(p))
c = conn.cursor()
tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
print("Tables:", tables)
for t in tables:
    count = c.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
    print(f"  {t}: {count} rows")
conn.close()
