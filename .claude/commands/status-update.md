---
title: Status Update
updated: 2026-03-03
status: active
---

# /status-update — Generate GTM-OS Status Update

## Steps

1. **Read current status**: Pull from `status.md` for current phase, active agents, open TODOs, and blockers.

2. **Read recent log entries**: Pull last 3-5 entries from `log.md` for recent activity context.

3. **Check agent status**: Read `agents/agents.json` for current agent states and `agents/action-log.json` for recent agent activity.

4. **Check campaign status**: Read `campaigns/campaigns.json` for active campaign states.

5. **Generate update** with:
   - **Current Phase**: Where we are in the GTM-OS buildout
   - **Completed Since Last Update**: Key wins and milestones
   - **Active Work**: What's in progress right now
   - **Agent Status**: Which agents are live, configuring, or drafting
   - **Blockers**: What's preventing progress
   - **Next Priorities**: Top 3 things to focus on next

6. **Update status.md**: Refresh the status file with current state.
