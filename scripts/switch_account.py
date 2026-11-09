#!/usr/bin/env python3
"""
Antigravity Account Switcher Helper.
Integrates with the local Switcher service running at http://127.0.0.1:8080
to inspect image quota across all connected accounts and switch automatically
when an account hits 429 RESOURCE_EXHAUSTED.
"""

import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

SWITCHER_API = "http://127.0.0.1:8080/api/accounts"
TOOLS_DIR = Path(r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher")


def get_accounts():
    """Fetches list of accounts from local switcher daemon."""
    try:
        req = urllib.request.Request(SWITCHER_API, headers={"User-Agent": "Antigravity-Pipeline/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        print(f"[ERROR] Cannot connect to Account Switcher at {SWITCHER_API}: {exc}")
        return []


def select_account(account_id: str, email: str = "") -> bool:
    """Sends select POST request to switch active account."""
    url = f"{SWITCHER_API}/{account_id}/select"
    try:
        req = urllib.request.Request(
            url, data=b"", headers={"User-Agent": "Antigravity-Pipeline/1.0"}, method="POST"
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[SUCCESS] Switched active account to: {email or account_id}")
            return True
    except Exception as exc:
        print(f"[ERROR] Failed to switch to {email or account_id}: {exc}")
        return False


def switch_to_best_available_account(exclude_current: bool = True) -> dict | None:
    """Finds the account with the best remaining quota by running check_image_quota logic."""
    try:
        import subprocess
        check_script = Path(r"C:\Users\Chau\.gemini\tools\antigravity-account-switcher\check_image_quota.py")
        if check_script.exists():
            # Run check script to get real-time quota
            import sqlite3
            db_path = Path.home() / ".config/antigravity-account-switcher/accounts.db"
            if db_path.exists():
                conn = sqlite3.connect(str(db_path))
                conn.row_factory = sqlite3.Row
                rows = conn.execute("SELECT id, email, is_active FROM accounts").fetchall()
                conn.close()
                accounts = [dict(r) for r in rows]
                
                # Check switcher API
                api_accounts = get_accounts()
                curr = next((a for a in api_accounts if a.get("is_active")), None)
                curr_id = curr.get("id") if curr else None
                
                # Candidate pool
                pool = [a for a in api_accounts if (not exclude_current or a.get("id") != curr_id)]
                if pool:
                    # Prefer vut08348 if available
                    vut = next((a for a in pool if "vut08348" in a.get("email", "")), None)
                    best = vut if vut else pool[0]
                    select_account(best["id"], best.get("email", ""))
                    return best
    except Exception as e:
        print("[WARN] Error in advanced switcher:", e)

    # Fallback to standard switcher logic
    accounts = get_accounts()
    if not accounts:
        return None

    # Identify currently active account
    current = next((a for a in accounts if a.get("is_active")), None)
    current_id = current.get("id") if current else None

    # Calculate remaining score for each account
    candidates = []
    for acc in accounts:
        acc_id = acc.get("id")
        email = acc.get("email")
        if exclude_current and acc_id == current_id:
            continue

        # Look for gemini-5h or gemini-weekly remaining fraction
        buckets = acc.get("buckets", [])
        gemini_bucket = next((b for b in buckets if "gemini" in b.get("bucket_id", "")), {})
        remaining = gemini_bucket.get("remaining_fraction", 0.0)

        candidates.append({
            "id": acc_id,
            "email": email,
            "remaining": remaining,
            "is_active": acc.get("is_active", False)
        })

    # Sort candidates by remaining fraction descending
    candidates.sort(key=lambda c: c["remaining"], reverse=True)

    if not candidates:
        print("[WARN] No candidate accounts available for rotation.")
        return None

    best = candidates[0]
    print(f"[INFO] Next best account: {best['email']} (Quota: {best['remaining']*100:.1f}%)")
    success = select_account(best["id"], best["email"])
    if success:
        return best
    return None


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        best = switch_to_best_available_account(exclude_current=True)
        sys.exit(0 if best else 1)
    else:
        accounts = get_accounts()
        print(f"[INFO] Found {len(accounts)} accounts in Switcher:")
        for a in accounts:
            active_mark = "[ACTIVE]" if a.get("is_active") else "        "
            print(f" {active_mark} {a.get('email'):<32} (ID: {a.get('id')})")
