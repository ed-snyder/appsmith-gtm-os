"""
Sequence Email Sender
Sends personalized emails via Lemlist API.
Handles template variable substitution and delivery tracking.
"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

LEMLIST_API_KEY = os.getenv("LEMLIST_API_KEY")
LEMLIST_BASE_URL = "https://api.lemlist.com/api"


def substitute_variables(template: str, variables: dict) -> str:
    """Replace {{variable}} placeholders with actual values."""
    result = template
    for key, value in variables.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result


def send_email(
    to_email: str,
    subject: str,
    body: str,
    campaign_id: str,
    variables: dict = None
) -> dict:
    """
    Send a single email via Lemlist API.
    """
    if variables:
        subject = substitute_variables(subject, variables)
        body = substitute_variables(body, variables)

    headers = {"Authorization": f"Bearer {LEMLIST_API_KEY}"}
    payload = {
        "campaignId": campaign_id,
        "email": to_email,
        "subject": subject,
        "body": body,
    }

    response = httpx.post(
        f"{LEMLIST_BASE_URL}/campaigns/{campaign_id}/leads",
        headers=headers,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def add_to_sequence(
    to_email: str,
    campaign_id: str,
    variables: dict = None
) -> dict:
    """
    Add a lead to an existing Lemlist campaign sequence.
    The sequence will handle multi-step email delivery.
    """
    headers = {"Authorization": f"Bearer {LEMLIST_API_KEY}"}
    payload = {
        "email": to_email,
    }
    if variables:
        payload["variables"] = variables

    response = httpx.post(
        f"{LEMLIST_BASE_URL}/campaigns/{campaign_id}/leads",
        headers=headers,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def check_delivery_status(campaign_id: str, lead_email: str) -> dict:
    """Check delivery status for a specific lead in a campaign."""
    headers = {"Authorization": f"Bearer {LEMLIST_API_KEY}"}
    response = httpx.get(
        f"{LEMLIST_BASE_URL}/campaigns/{campaign_id}/leads/{lead_email}",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("Sequence email sender ready. Use send_email() or add_to_sequence().")
