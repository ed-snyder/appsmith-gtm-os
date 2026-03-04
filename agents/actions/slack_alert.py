"""
Slack Alert Script
Sends formatted alerts to Slack channels for high-priority leads and agent events.
"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def send_tier_a_alert(
    contact_name: str,
    contact_title: str,
    company_name: str,
    company_size: int,
    industry: str,
    tech_stack: list,
    icp_score: int,
    tier: str,
    signup_email: str,
    recommended_action: str = "Reach out within 2 hours"
) -> dict:
    """
    Send a Tier A signup alert to Slack.
    """
    tech_stack_str = ", ".join(tech_stack) if tech_stack else "Unknown"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Tier {tier} Signup Alert"
            }
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Contact:*\n{contact_name}"},
                {"type": "mrkdwn", "text": f"*Title:*\n{contact_title}"},
                {"type": "mrkdwn", "text": f"*Company:*\n{company_name}"},
                {"type": "mrkdwn", "text": f"*Size:*\n{company_size} employees"},
                {"type": "mrkdwn", "text": f"*Industry:*\n{industry}"},
                {"type": "mrkdwn", "text": f"*ICP Score:*\n{icp_score}"},
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Tech Stack:* {tech_stack_str}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Email:* {signup_email}\n*Recommended Action:* {recommended_action}"
            }
        },
        {"type": "divider"}
    ]

    payload = {"blocks": blocks}
    response = httpx.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    response.raise_for_status()
    return {"status": "sent", "channel": "sales-alerts"}


def send_pql_alert(
    company_name: str,
    contact_email: str,
    pql_score: int,
    pql_tier: str,
    signals: list,
    recommended_action: str
) -> dict:
    """
    Send a PQL detection alert to Slack.
    """
    signals_str = "\n".join([f"- {s}" for s in signals])

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"PQL Detected: {pql_tier}"
            }
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Company:*\n{company_name}"},
                {"type": "mrkdwn", "text": f"*Contact:*\n{contact_email}"},
                {"type": "mrkdwn", "text": f"*PQL Score:*\n{pql_score}"},
                {"type": "mrkdwn", "text": f"*Tier:*\n{pql_tier}"},
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Signals:*\n{signals_str}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Recommended Action:* {recommended_action}"
            }
        },
        {"type": "divider"}
    ]

    payload = {"blocks": blocks}
    response = httpx.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    response.raise_for_status()
    return {"status": "sent", "channel": "sales-alerts"}


def send_generic_alert(title: str, message: str) -> dict:
    """Send a generic text alert to Slack."""
    payload = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{title}*\n{message}"
                }
            }
        ]
    }
    response = httpx.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    response.raise_for_status()
    return {"status": "sent"}


if __name__ == "__main__":
    print("Slack alert module ready.")
    print("Use send_tier_a_alert() or send_pql_alert() to send alerts.")
