"""
Signup Processing Pipeline
Orchestrates the signup-welcomer agent workflow:
1. Enrich via Clay
2. Score using ICP model
3. Segment
4. Route to appropriate action
5. Send welcome email
6. Log all actions

Can process single signups (real-time) or batch (CSV upload).
"""

import os
import sys
import json
import csv
from datetime import datetime

# Add parent directory to path for agent imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from agents.actions.enrich_signup import enrich_signup
from agents.actions.score_lead import score_lead
from agents.actions.log_action import log_action
from agents.actions.slack_alert import send_tier_a_alert

SEGMENTS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "segments", "segments.json"
)


def load_segments() -> dict:
    """Load segment definitions."""
    with open(SEGMENTS_PATH, "r") as f:
        return json.load(f)


def match_segment(enrichment_data: dict, segments: dict) -> str:
    """Match enrichment data to a segment."""
    tech_stack = enrichment_data.get("tech_stack", [])
    tech_lower = [t.lower() for t in tech_stack]

    # Check for Retool usage
    if "retool" in tech_lower:
        return "retool-refugees"

    # Check for AI initiative signals
    ai_tools = ["salesforce", "zendesk", "slack"]
    ai_signals = enrichment_data.get("signals", {})
    if ai_signals.get("ai_initiative") and any(t in tech_lower for t in ai_tools):
        return "ai-agent-adopters"

    # Check for compliance signals
    if ai_signals.get("compliance_signals"):
        return "compliance-driven"

    # Check for OSS signals
    if ai_signals.get("self_hosting_interest"):
        return "open-source-first"

    # Default to internal-tool-sprawl for mid-market companies
    employee_count = enrichment_data.get("employee_count", 0)
    if 200 <= employee_count <= 1000:
        return "internal-tool-sprawl"

    return "unclassified"


def process_single_signup(email: str) -> dict:
    """Process a single new signup through the full pipeline."""
    result = {"email": email, "timestamp": datetime.utcnow().isoformat()}

    # Step 1: Enrich
    log_action("signup-welcomer", "enrichment_start", target_contact=email)
    enrichment = enrich_signup(email)
    result["enrichment"] = enrichment

    if enrichment.get("status") == "skipped_personal_email":
        log_action(
            "signup-welcomer", "enrichment_skipped",
            target_contact=email,
            details="Personal email domain"
        )
        result["tier"] = "D"
        result["action"] = "standard_welcome"
        return result

    # Step 2: Score
    combined_data = {
        **enrichment.get("company", {}),
        **enrichment.get("person", {}),
    }
    scoring = score_lead(combined_data)
    result["scoring"] = scoring

    # Step 3: Segment
    segments = load_segments()
    segment = match_segment(combined_data, segments)
    result["segment"] = segment

    # Step 4: Route based on tier
    tier = scoring["tier"]
    result["tier"] = tier

    if tier == "A":
        # Slack alert for Tier A
        company = combined_data.get("company_name", "Unknown")
        try:
            send_tier_a_alert(
                contact_name=combined_data.get("full_name", "Unknown"),
                contact_title=combined_data.get("title", "Unknown"),
                company_name=company,
                company_size=combined_data.get("employee_count", 0),
                industry=combined_data.get("industry", "Unknown"),
                tech_stack=combined_data.get("tech_stack", []),
                icp_score=scoring["total_score"],
                tier=tier,
                signup_email=email,
            )
            result["slack_alert"] = "sent"
        except Exception as e:
            result["slack_alert_error"] = str(e)

        result["action"] = "high_touch_welcome"
        log_action(
            "signup-welcomer", "tier_a_routing",
            target_contact=email,
            target_company=company,
            details=f"Score: {scoring['total_score']}, Segment: {segment}",
            result="success",
            next_action="send_personalized_welcome"
        )

    elif tier == "B":
        result["action"] = "standard_welcome_with_content"
        log_action(
            "signup-welcomer", "tier_b_routing",
            target_contact=email,
            details=f"Score: {scoring['total_score']}, Segment: {segment}",
            next_action="send_welcome_email"
        )

    elif tier == "C":
        result["action"] = "standard_welcome"
        log_action(
            "signup-welcomer", "tier_c_routing",
            target_contact=email,
            details=f"Score: {scoring['total_score']}",
            next_action="send_standard_welcome"
        )

    else:  # D
        result["action"] = "minimal_welcome"
        log_action(
            "signup-welcomer", "tier_d_routing",
            target_contact=email,
            details=f"Score: {scoring['total_score']}",
            next_action="send_minimal_welcome"
        )

    return result


def process_batch(csv_path: str) -> list:
    """Process a batch of signups from a CSV file."""
    results = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row.get("email")
            if not email:
                continue
            print(f"Processing: {email}")
            result = process_single_signup(email)
            results.append(result)
            print(f"  Tier: {result['tier']}, Action: {result['action']}")

    # Summary
    tier_counts = {}
    for r in results:
        tier = r.get("tier", "Unknown")
        tier_counts[tier] = tier_counts.get(tier, 0) + 1

    print(f"\nBatch Summary: {len(results)} signups processed")
    for tier, count in sorted(tier_counts.items()):
        print(f"  Tier {tier}: {count}")

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single: python process_signups.py <email>")
        print("  Batch:  python process_signups.py --batch <csv_path>")
        sys.exit(1)

    if sys.argv[1] == "--batch" and len(sys.argv) > 2:
        process_batch(sys.argv[2])
    else:
        result = process_single_signup(sys.argv[1])
        print(json.dumps(result, indent=2))
