"""
Lead Scoring Script
Applies ICP scoring model to enrichment data.
Returns tier (A/B/C/D) and total score.
"""

import json


# Scoring weights from agents/scoring/icp-scoring-model.md
COMPANY_SIZE_SCORES = {
    "1-49": 0,
    "50-199": 10,
    "200-1000": 20,
    "1001-5000": 15,
    "5000+": 10,
}

TARGET_INDUSTRIES = {
    "technology": 5,
    "financial services": 5,
    "healthcare": 5,
    "e-commerce": 5,
    "saas": 5,
}

TECH_STACK_SCORES = {
    "postgresql": 10,
    "mongodb": 10,
    "mysql": 8,
    "snowflake": 8,
    "bigquery": 8,
    "redshift": 8,
    "nodejs": 5,
    "node.js": 5,
    "react": 10,
    "docker": 10,
    "kubernetes": 10,
    "github": 5,
    "gitlab": 5,
}

TITLE_SCORES = {
    "engineering manager": 20,
    "vp engineering": 20,
    "vp of engineering": 20,
    "cto": 15,
    "platform lead": 20,
    "platform engineer": 20,
    "devops lead": 15,
    "data team lead": 10,
    "software engineer": 5,
}


def score_company_size(employee_count: int) -> int:
    """Score based on company size."""
    if employee_count < 50:
        return 0
    elif employee_count <= 199:
        return 10
    elif employee_count <= 1000:
        return 20
    elif employee_count <= 5000:
        return 15
    else:
        return 10


def score_industry(industry: str) -> int:
    """Score based on industry match."""
    if not industry:
        return 0
    return TARGET_INDUSTRIES.get(industry.lower(), 0)


def score_tech_stack(tech_stack: list) -> int:
    """Score based on tech stack matches."""
    total = 0
    if not tech_stack:
        return 0
    for tech in tech_stack:
        total += TECH_STACK_SCORES.get(tech.lower(), 0)
    return total


def score_title(title: str) -> int:
    """Score based on buyer persona title match."""
    if not title:
        return 0
    title_lower = title.lower()
    for key, score in TITLE_SCORES.items():
        if key in title_lower:
            return score
    return 0


def score_signals(signals: dict) -> int:
    """Score based on intent signals."""
    total = 0
    if signals.get("self_hosting_interest"):
        total += 10
    if signals.get("competitor_usage"):
        total += 10
    if signals.get("compliance_signals"):
        total += 5
    if signals.get("ai_initiative"):
        total += 5
    if signals.get("internal_tools_hiring"):
        total += 10
    if signals.get("engineering_team_detected"):
        total += 15
    if signals.get("funding_detected"):
        total += 5
    return total


def apply_negative_signals(signals: dict) -> int:
    """Apply negative scoring deductions."""
    deductions = 0
    if signals.get("no_engineering_team"):
        deductions -= 20
    if signals.get("consumer_app_focus"):
        deductions -= 15
    if signals.get("no_data_infrastructure"):
        deductions -= 10
    if signals.get("competitor_employee"):
        deductions -= 100
    if signals.get("personal_email"):
        deductions -= 15
    return deductions


def calculate_tier(score: int) -> str:
    """Determine lead tier from total score."""
    if score >= 60:
        return "A"
    elif score >= 30:
        return "B"
    elif score >= 10:
        return "C"
    else:
        return "D"


def score_lead(enrichment_data: dict) -> dict:
    """
    Full ICP scoring pipeline.
    Takes enrichment data, returns score and tier.
    """
    breakdown = {}

    breakdown["company_size"] = score_company_size(
        enrichment_data.get("employee_count", 0)
    )
    breakdown["industry"] = score_industry(
        enrichment_data.get("industry", "")
    )
    breakdown["tech_stack"] = score_tech_stack(
        enrichment_data.get("tech_stack", [])
    )
    breakdown["title"] = score_title(
        enrichment_data.get("title", "")
    )
    breakdown["signals"] = score_signals(
        enrichment_data.get("signals", {})
    )
    breakdown["negative"] = apply_negative_signals(
        enrichment_data.get("signals", {})
    )

    total_score = sum(breakdown.values())
    tier = calculate_tier(total_score)

    return {
        "total_score": total_score,
        "tier": tier,
        "breakdown": breakdown,
        "enrichment_summary": {
            "company": enrichment_data.get("company_name", "Unknown"),
            "employee_count": enrichment_data.get("employee_count", 0),
            "industry": enrichment_data.get("industry", "Unknown"),
            "title": enrichment_data.get("title", "Unknown"),
        }
    }


if __name__ == "__main__":
    # Example usage with sample data
    sample_data = {
        "company_name": "Example Corp",
        "employee_count": 350,
        "industry": "Technology",
        "tech_stack": ["postgresql", "react", "docker", "kubernetes"],
        "title": "Engineering Manager",
        "signals": {
            "engineering_team_detected": True,
            "self_hosting_interest": True,
            "funding_detected": True,
        }
    }
    result = score_lead(sample_data)
    print(json.dumps(result, indent=2))
