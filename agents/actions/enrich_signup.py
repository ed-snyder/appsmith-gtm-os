"""
Signup Enrichment Script
Enriches a new signup with company and person data via Clay API.
Updates CRM (HubSpot) with enrichment results.
"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

CLAY_API_KEY = os.getenv("CLAY_API_KEY")
CLAY_BASE_URL = "https://api.clay.com/v3"
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")


def enrich_company(domain: str) -> dict:
    """Enrich company data via Clay API."""
    headers = {"Authorization": f"Bearer {CLAY_API_KEY}"}
    payload = {
        "domain": domain,
        "fields": [
            "name", "industry", "employee_count", "revenue",
            "tech_stack", "funding_total", "funding_stage",
            "linkedin_url", "description", "location"
        ]
    }
    response = httpx.post(
        f"{CLAY_BASE_URL}/enrich/company",
        headers=headers,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def enrich_person(email: str) -> dict:
    """Enrich person data via Clay API."""
    headers = {"Authorization": f"Bearer {CLAY_API_KEY}"}
    payload = {
        "email": email,
        "fields": [
            "full_name", "title", "seniority", "department",
            "linkedin_url", "location", "phone"
        ]
    }
    response = httpx.post(
        f"{CLAY_BASE_URL}/enrich/person",
        headers=headers,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def update_crm_contact(email: str, enrichment_data: dict) -> dict:
    """Update HubSpot contact with enrichment data."""
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }
    properties = {
        "company_size": enrichment_data.get("employee_count", ""),
        "industry": enrichment_data.get("industry", ""),
        "tech_stack": ", ".join(enrichment_data.get("tech_stack", [])),
        "funding_stage": enrichment_data.get("funding_stage", ""),
        "linkedin_url": enrichment_data.get("linkedin_url", ""),
        "enrichment_status": "completed",
        "enrichment_source": "clay"
    }
    payload = {"properties": properties}
    response = httpx.patch(
        f"https://api.hubapi.com/crm/v3/objects/contacts/{email}",
        headers=headers,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def enrich_signup(email: str) -> dict:
    """
    Full enrichment pipeline for a new signup.
    Returns combined enrichment data.
    """
    domain = email.split("@")[1] if "@" in email else None
    result = {"email": email, "status": "pending"}

    # Skip enrichment for personal email domains
    personal_domains = [
        "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
        "aol.com", "icloud.com", "protonmail.com"
    ]
    if domain in personal_domains:
        result["status"] = "skipped_personal_email"
        return result

    try:
        company_data = enrich_company(domain)
        result["company"] = company_data
    except Exception as e:
        result["company_error"] = str(e)

    try:
        person_data = enrich_person(email)
        result["person"] = person_data
    except Exception as e:
        result["person_error"] = str(e)

    # Update CRM with enrichment data
    try:
        combined = {**result.get("company", {}), **result.get("person", {})}
        update_crm_contact(email, combined)
        result["crm_updated"] = True
    except Exception as e:
        result["crm_error"] = str(e)

    result["status"] = "completed"
    return result


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python enrich_signup.py <email>")
        sys.exit(1)
    result = enrich_signup(sys.argv[1])
    print(result)
