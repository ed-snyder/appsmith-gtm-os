"""
Lemlist Campaign Stats Puller
Pulls campaign performance metrics from Lemlist API and updates campaigns/results.json.
"""

import os
import json
from datetime import datetime
import httpx
from dotenv import load_dotenv

load_dotenv()

LEMLIST_API_KEY = os.getenv("LEMLIST_API_KEY")
LEMLIST_BASE_URL = "https://api.lemlist.com/api"
RESULTS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "campaigns", "results.json"
)


def get_campaigns() -> list:
    """Fetch all campaigns from Lemlist."""
    headers = {"Authorization": f"Bearer {LEMLIST_API_KEY}"}
    response = httpx.get(
        f"{LEMLIST_BASE_URL}/campaigns",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def get_campaign_stats(campaign_id: str) -> dict:
    """Fetch stats for a specific campaign."""
    headers = {"Authorization": f"Bearer {LEMLIST_API_KEY}"}
    response = httpx.get(
        f"{LEMLIST_BASE_URL}/campaigns/{campaign_id}/stats",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def calculate_metrics(stats: dict) -> dict:
    """Calculate derived metrics from raw stats."""
    sent = stats.get("sent", 0)
    delivered = stats.get("delivered", 0)
    opened = stats.get("opened", 0)
    replied = stats.get("replied", 0)
    bounced = stats.get("bounced", 0)

    return {
        "emails_sent": sent,
        "emails_delivered": delivered,
        "emails_bounced": bounced,
        "open_rate": round(opened / delivered, 4) if delivered > 0 else 0,
        "reply_rate": round(replied / delivered, 4) if delivered > 0 else 0,
        "positive_reply_rate": 0,  # Requires manual classification
        "meetings_booked": 0,  # Requires CRM integration
        "meeting_show_rate": 0,
        "pipeline_generated": 0,
        "cost_per_meeting": 0,
    }


def update_results(campaign_name: str, metrics: dict) -> None:
    """Update campaigns/results.json with new metrics."""
    try:
        with open(RESULTS_PATH, "r") as f:
            results_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        results_data = {"results": []}

    entry = {
        "campaign_name": campaign_name,
        "period": datetime.utcnow().strftime("%Y-%m"),
        "metrics": metrics,
        "updated": datetime.utcnow().isoformat(),
    }

    # Update existing or append new
    existing = next(
        (r for r in results_data["results"] if r["campaign_name"] == campaign_name),
        None
    )
    if existing:
        existing.update(entry)
    else:
        results_data["results"].append(entry)

    with open(RESULTS_PATH, "w") as f:
        json.dump(results_data, f, indent=2)


def pull_all_stats() -> None:
    """Pull stats for all campaigns and update results.json."""
    campaigns = get_campaigns()
    for campaign in campaigns:
        campaign_id = campaign.get("_id")
        campaign_name = campaign.get("name", "unknown")
        print(f"Pulling stats for: {campaign_name}")

        stats = get_campaign_stats(campaign_id)
        metrics = calculate_metrics(stats)
        update_results(campaign_name, metrics)

    print(f"Updated {len(campaigns)} campaign results.")


if __name__ == "__main__":
    pull_all_stats()
