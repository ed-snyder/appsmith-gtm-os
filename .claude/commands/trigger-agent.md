---
title: Trigger Agent Action
updated: 2026-03-03
status: active
---

# /trigger-agent — Trigger a Sales Agent Action

## Steps

1. **Identify the agent**: Read `agents/agents.json` and select the appropriate agent by ID. Confirm the agent's status is "active".

2. **Check the playbook**: Read the agent's playbook from `agents/playbooks/{playbook-file}`. Understand the full workflow, triggers, and routing logic.

3. **Verify prospect/account context**: Ensure you have the required data:
   - Contact information (name, email, title, company)
   - Enrichment data (if available)
   - Current CRM stage
   - Any previous agent interactions (check `agents/action-log.json`)

4. **Check autonomy level**:
   - **full_auto**: Proceed with execution
   - **human_in_loop**: Prepare the action and present for approval before executing
   - **human_only**: Prepare research and recommendations only

5. **Execute the action**: Run the appropriate script from `agents/actions/`:
   - `enrich_signup.py` — for enrichment steps
   - `score_lead.py` — for scoring steps
   - `send_sequence_email.py` — for email sends
   - `check_pql_signals.py` — for PQL checks
   - `slack_alert.py` — for team notifications

6. **Log the action**: Append to `agents/action-log.json` with:
   - timestamp
   - agent_id
   - action_type
   - target_contact
   - target_company
   - details
   - result
   - next_action

7. **Set next action**: Based on playbook workflow, queue the next step or schedule follow-up.

## Safety Rules
- Never send outreach to contacts who have opted out
- Never exceed daily sending limits per agent
- Always check for duplicate actions in action-log.json
- Escalate to human if confidence is low on personalization
