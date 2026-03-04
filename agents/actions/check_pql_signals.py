"""
PQL Signal Checker
Queries product analytics to identify accounts crossing PQL thresholds.
Triggers pql-hunter agent for qualified accounts.
"""

import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# PQL thresholds from agents/scoring/pql-scoring-model.md
PQL_THRESHOLDS = {
    "apps_created": 3,
    "data_sources_connected": 2,
    "team_members_invited": 3,
    "active_days_last_7": 1,
    "api_queries_per_week": 100,
}

PQL_SCORING = {
    "apps_3_4": 20,
    "apps_5_9": 30,
    "apps_10_plus": 40,
    "datasources_2_3": 15,
    "datasources_4_plus": 25,
    "team_3_4": 15,
    "team_5": 25,
    "team_6_plus_attempted": 30,
    "active_3_days": 20,
    "active_7_days": 10,
    "api_100_plus": 15,
    "api_500_plus": 25,
    "custom_widget": 10,
    "js_object": 10,
    "git_integration": 15,
    "workflow_attempted": 20,
    "rbac_attempted": 15,
    "audit_log_search": 10,
    "sso_attempted": 15,
    "daily_login_5_plus": 15,
    "login_3_4_weekly": 10,
    "edits_5_plus_weekly": 10,
    "new_app_3_days": 10,
    "team_added_7_days": 10,
}


def get_product_usage(account_id: str) -> dict:
    """
    Fetch product usage data for an account.
    Stub: Replace with actual product analytics API call.
    """
    # TODO: Integrate with product analytics API (Amplitude, Mixpanel, etc.)
    return {
        "account_id": account_id,
        "apps_created": 0,
        "data_sources_connected": 0,
        "team_members_invited": 0,
        "last_active": None,
        "api_queries_last_week": 0,
        "custom_widgets_created": 0,
        "js_objects_created": 0,
        "git_integration_enabled": False,
        "workflow_attempted": False,
        "rbac_attempted": False,
        "audit_log_searched": False,
        "sso_attempted": False,
        "login_days_last_7": 0,
        "app_edits_last_7": 0,
    }


def calculate_pql_score(usage: dict) -> dict:
    """Calculate PQL score from usage data."""
    score = 0
    signals_matched = []

    # Apps created
    apps = usage.get("apps_created", 0)
    if apps >= 10:
        score += PQL_SCORING["apps_10_plus"]
        signals_matched.append("10+ apps")
    elif apps >= 5:
        score += PQL_SCORING["apps_5_9"]
        signals_matched.append("5-9 apps")
    elif apps >= 3:
        score += PQL_SCORING["apps_3_4"]
        signals_matched.append("3-4 apps")

    # Data sources
    ds = usage.get("data_sources_connected", 0)
    if ds >= 4:
        score += PQL_SCORING["datasources_4_plus"]
        signals_matched.append("4+ data sources")
    elif ds >= 2:
        score += PQL_SCORING["datasources_2_3"]
        signals_matched.append("2-3 data sources")

    # Team members
    team = usage.get("team_members_invited", 0)
    if team >= 6:
        score += PQL_SCORING["team_6_plus_attempted"]
        signals_matched.append("6+ team (hit limit)")
    elif team >= 5:
        score += PQL_SCORING["team_5"]
        signals_matched.append("5 team (at limit)")
    elif team >= 3:
        score += PQL_SCORING["team_3_4"]
        signals_matched.append("3-4 team")

    # Activity recency
    login_days = usage.get("login_days_last_7", 0)
    if login_days >= 5:
        score += PQL_SCORING["active_3_days"]
        signals_matched.append("daily active")
    elif login_days >= 1:
        score += PQL_SCORING["active_7_days"]
        signals_matched.append("active this week")

    # API usage
    api = usage.get("api_queries_last_week", 0)
    if api >= 500:
        score += PQL_SCORING["api_500_plus"]
        signals_matched.append("heavy API usage")
    elif api >= 100:
        score += PQL_SCORING["api_100_plus"]
        signals_matched.append("API usage >100/week")

    # Feature adoption
    if usage.get("custom_widgets_created", 0) > 0:
        score += PQL_SCORING["custom_widget"]
        signals_matched.append("custom widget")
    if usage.get("js_objects_created", 0) > 0:
        score += PQL_SCORING["js_object"]
        signals_matched.append("JS object")
    if usage.get("git_integration_enabled"):
        score += PQL_SCORING["git_integration"]
        signals_matched.append("git integration")
    if usage.get("workflow_attempted"):
        score += PQL_SCORING["workflow_attempted"]
        signals_matched.append("workflow attempted (gated)")
    if usage.get("rbac_attempted"):
        score += PQL_SCORING["rbac_attempted"]
        signals_matched.append("RBAC attempted (gated)")
    if usage.get("sso_attempted"):
        score += PQL_SCORING["sso_attempted"]
        signals_matched.append("SSO attempted (gated)")

    # Determine tier
    if score >= 80:
        tier = "PQL-Hot"
    elif score >= 50:
        tier = "PQL-Warm"
    elif score >= 30:
        tier = "PQL-Early"
    else:
        tier = "Not PQL"

    return {
        "account_id": usage.get("account_id"),
        "pql_score": score,
        "pql_tier": tier,
        "signals_matched": signals_matched,
        "checked_at": datetime.utcnow().isoformat(),
    }


def check_all_accounts(account_ids: list) -> list:
    """Check PQL signals for a batch of accounts."""
    results = []
    for account_id in account_ids:
        usage = get_product_usage(account_id)
        pql_result = calculate_pql_score(usage)
        if pql_result["pql_tier"] != "Not PQL":
            results.append(pql_result)
    return results


if __name__ == "__main__":
    print("PQL signal checker ready.")
    print("Usage: Import and call check_all_accounts() with account IDs.")
    # Example:
    # results = check_all_accounts(["account_1", "account_2"])
    # for r in results:
    #     print(json.dumps(r, indent=2))
