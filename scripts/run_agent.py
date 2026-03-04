"""
Generic Agent Runner
Takes an agent_id, loads the playbook, and executes the workflow.
Entry point for triggering any agent action from the command line or scheduler.
"""

import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from agents.actions.log_action import log_action

AGENTS_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "agents", "agents.json"
)


def load_agents_config() -> dict:
    """Load agents configuration."""
    with open(AGENTS_CONFIG_PATH, "r") as f:
        return json.load(f)


def get_agent(agent_id: str) -> dict:
    """Get a specific agent's configuration."""
    config = load_agents_config()
    for agent in config.get("agents", []):
        if agent["id"] == agent_id:
            return agent
    return None


def run_agent(agent_id: str, context: dict = None) -> dict:
    """
    Execute an agent's workflow.

    Args:
        agent_id: The agent to run (from agents.json)
        context: Runtime context (contact info, trigger data, etc.)

    Returns:
        Execution result with status and actions taken
    """
    agent = get_agent(agent_id)
    if not agent:
        return {"error": f"Agent '{agent_id}' not found"}

    if agent["status"] != "active":
        return {"error": f"Agent '{agent_id}' is not active (status: {agent['status']})"}

    print(f"[{datetime.utcnow().isoformat()}] Running agent: {agent['name']}")
    print(f"  Playbook: {agent['playbook']}")
    print(f"  Autonomy: {agent['autonomy_level']}")
    print(f"  Tools: {', '.join(agent['tools'])}")

    # Log the agent invocation
    log_action(
        agent_id=agent_id,
        action_type="agent_invoked",
        details=f"Context: {json.dumps(context or {})}",
        result="started",
        next_action="execute_workflow"
    )

    # Route to agent-specific handler
    result = {"agent_id": agent_id, "status": "started"}

    if agent_id == "signup-welcomer":
        email = (context or {}).get("email")
        if email:
            from scripts.process_signups import process_single_signup
            result = process_single_signup(email)
        else:
            result["error"] = "Missing 'email' in context"

    elif agent_id == "pql-hunter":
        from scripts.check_pql_thresholds import run_pql_check
        result = run_pql_check()

    elif agent_id == "trial-nudger":
        # TODO: Implement trial nurture workflow
        result["status"] = "not_implemented"
        result["message"] = "Trial nurture workflow pending implementation"

    elif agent_id == "expansion-spotter":
        # TODO: Implement expansion detection workflow
        result["status"] = "not_implemented"
        result["message"] = "Expansion detection workflow pending implementation"

    elif agent_id == "reactivation-agent":
        # TODO: Implement reactivation workflow
        result["status"] = "not_implemented"
        result["message"] = "Reactivation workflow pending implementation"

    elif agent_id == "agents-evangelist":
        # TODO: Implement cross-sell workflow
        result["status"] = "not_implemented"
        result["message"] = "Cross-sell workflow pending implementation"

    else:
        result["error"] = f"No handler for agent '{agent_id}'"

    # Log completion
    log_action(
        agent_id=agent_id,
        action_type="agent_completed",
        details=json.dumps(result),
        result=result.get("status", "unknown")
    )

    return result


def list_agents() -> None:
    """List all configured agents and their status."""
    config = load_agents_config()
    print("\nConfigured Agents:")
    print("-" * 60)
    for agent in config.get("agents", []):
        status_icon = "+" if agent["status"] == "active" else "o"
        autonomy = agent["autonomy_level"].replace("_", " ")
        print(f"  [{status_icon}] {agent['id']}: {agent['name']}")
        print(f"      Trigger: {agent['trigger']} | Autonomy: {autonomy}")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python run_agent.py <agent_id> [context_json]")
        print("  python run_agent.py --list")
        print()
        list_agents()
        sys.exit(0)

    if sys.argv[1] == "--list":
        list_agents()
    else:
        agent_id = sys.argv[1]
        context = json.loads(sys.argv[2]) if len(sys.argv) > 2 else None
        result = run_agent(agent_id, context)
        print(json.dumps(result, indent=2))
