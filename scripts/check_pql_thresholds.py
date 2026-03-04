"""
PQL Threshold Checker
Queries product analytics to identify accounts crossing PQL thresholds.
Triggers the pql-hunter agent for qualified accounts.
Designed to run on a schedule (every 6 hours via cron or workflow).
"""

import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from agents.actions.check_pql_signals import check_all_accounts, calculate_pql_score
from agents.actions.log_action import log_action
from agents.actions.slack_alert import send_pql_alert


def get_active_free_accounts() -> list:
    """
    Fetch list of active free-tier account IDs from product analytics.
    Stub: Replace with actual product analytics API call.
    """
    # TODO: Integrate with product analytics API
    # Should return list of account IDs for free-tier users
    # who have been active in the last 30 days
    return []


def get_existing_pqls() -> set:
    """Load already-detected PQLs to avoid duplicate notifications."""
    pql_cache_path = os.path.join(
        os.path.dirname(__file__), ".pql_cache.json"
    )
    try:
        with open(pql_cache_path, "r") as f:
            data = json.load(f)
            return set(data.get("detected_accounts", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()


def save_pql_cache(account_ids: set) -> None:
    """Save detected PQL account IDs to cache."""
    pql_cache_path = os.path.join(
        os.path.dirname(__file__), ".pql_cache.json"
    )
    with open(pql_cache_path, "w") as f:
        json.dump({
            "detected_accounts": list(account_ids),
            "last_checked": datetime.utcnow().isoformat()
        }, f, indent=2)


def run_pql_check() -> dict:
    """
    Main PQL detection pipeline.
    Returns summary of new PQLs detected.
    """
    print(f"[{datetime.utcnow().isoformat()}] Starting PQL threshold check...")

    # Get active accounts
    account_ids = get_active_free_accounts()
    print(f"  Checking {len(account_ids)} active free accounts")

    if not account_ids:
        print("  No active accounts to check. Ensure product analytics API is connected.")
        return {"checked": 0, "new_pqls": 0}

    # Check PQL signals
    pql_results = check_all_accounts(account_ids)
    existing_pqls = get_existing_pqls()

    # Filter to new PQLs only
    new_pqls = [
        r for r in pql_results
        if r["account_id"] not in existing_pqls
    ]

    print(f"  Total PQLs detected: {len(pql_results)}")
    print(f"  New PQLs: {len(new_pqls)}")

    # Process new PQLs
    for pql in new_pqls:
        tier = pql["pql_tier"]

        # Log detection
        log_action(
            agent_id="pql-hunter",
            action_type="pql_detected",
            target_contact=pql["account_id"],
            details=f"PQL Score: {pql['pql_score']}, Tier: {tier}, Signals: {', '.join(pql['signals_matched'])}",
            result=tier,
            next_action="prepare_outreach" if tier in ["PQL-Hot", "PQL-Warm"] else "add_to_nurture"
        )

        # Slack alert for Hot PQLs
        if tier == "PQL-Hot":
            try:
                send_pql_alert(
                    company_name=pql.get("account_id", "Unknown"),
                    contact_email="",  # Need to resolve from account
                    pql_score=pql["pql_score"],
                    pql_tier=tier,
                    signals=pql["signals_matched"],
                    recommended_action="Prepare personalized outreach within 24 hours"
                )
                print(f"  Slack alert sent for PQL-Hot: {pql['account_id']}")
            except Exception as e:
                print(f"  Slack alert failed: {e}")

    # Update cache
    all_pql_ids = existing_pqls | {r["account_id"] for r in pql_results}
    save_pql_cache(all_pql_ids)

    summary = {
        "checked": len(account_ids),
        "total_pqls": len(pql_results),
        "new_pqls": len(new_pqls),
        "by_tier": {
            "hot": len([r for r in new_pqls if r["pql_tier"] == "PQL-Hot"]),
            "warm": len([r for r in new_pqls if r["pql_tier"] == "PQL-Warm"]),
            "early": len([r for r in new_pqls if r["pql_tier"] == "PQL-Early"]),
        },
        "timestamp": datetime.utcnow().isoformat()
    }

    print(f"\nPQL Check Summary: {json.dumps(summary, indent=2)}")
    return summary


if __name__ == "__main__":
    run_pql_check()
