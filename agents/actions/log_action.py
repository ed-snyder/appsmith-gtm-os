"""
Action Logger
Appends agent actions to agents/action-log.json with timestamps.
"""

import json
import os
from datetime import datetime

ACTION_LOG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "action-log.json"
)


def log_action(
    agent_id: str,
    action_type: str,
    target_contact: str = "",
    target_company: str = "",
    details: str = "",
    result: str = "",
    next_action: str = ""
) -> dict:
    """
    Log an agent action to action-log.json.
    """
    action = {
        "timestamp": datetime.utcnow().isoformat(),
        "agent_id": agent_id,
        "action_type": action_type,
        "target_contact": target_contact,
        "target_company": target_company,
        "details": details,
        "result": result,
        "next_action": next_action,
    }

    # Read existing log
    try:
        with open(ACTION_LOG_PATH, "r") as f:
            log_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log_data = {"actions": []}

    # Remove placeholder entries (empty timestamps)
    log_data["actions"] = [
        a for a in log_data["actions"] if a.get("timestamp")
    ]

    # Append new action
    log_data["actions"].append(action)

    # Write updated log
    with open(ACTION_LOG_PATH, "w") as f:
        json.dump(log_data, f, indent=2)

    return action


def get_recent_actions(agent_id: str = None, limit: int = 10) -> list:
    """Get recent actions, optionally filtered by agent_id."""
    try:
        with open(ACTION_LOG_PATH, "r") as f:
            log_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    actions = log_data.get("actions", [])
    if agent_id:
        actions = [a for a in actions if a.get("agent_id") == agent_id]

    # Sort by timestamp descending, return latest
    actions.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    return actions[:limit]


def get_actions_for_contact(contact_email: str) -> list:
    """Get all actions targeting a specific contact."""
    try:
        with open(ACTION_LOG_PATH, "r") as f:
            log_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    return [
        a for a in log_data.get("actions", [])
        if a.get("target_contact") == contact_email
    ]


if __name__ == "__main__":
    # Example usage
    action = log_action(
        agent_id="signup-welcomer",
        action_type="enrichment",
        target_contact="example@company.com",
        target_company="Example Corp",
        details="Enriched via Clay API",
        result="success",
        next_action="score_lead"
    )
    print(f"Logged action: {json.dumps(action, indent=2)}")
