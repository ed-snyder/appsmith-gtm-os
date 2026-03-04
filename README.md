---
title: Appsmith GTM-OS
updated: 2026-03-03
status: active
---

# Appsmith GTM-OS

The go-to-market operating system for Appsmith. A markdown-first, agent-readable system for running GTM strategy, sales agent orchestration, and revenue operations.

## What This Is

This repo serves two purposes:

1. **Central context layer** for the GTM team — demand intelligence, buyer segments, messaging frameworks, campaign operations, and engine configuration
2. **Sales agent orchestration hub** — AI agents that autonomously handle lifecycle motions like signup processing, PQL outreach, trial nurturing, and account expansion

## Agent Architecture

Six sales agents handle key GTM motions:

| Agent | Trigger | Autonomy | Status |
|-------|---------|----------|--------|
| **signup-welcomer** | New free signup | Full auto | Active |
| **pql-hunter** | PQL threshold crossed | Human-in-loop | Active |
| **trial-nudger** | Business trial started | Full auto | Active |
| **expansion-spotter** | Expansion signal detected | Human-in-loop | Draft |
| **reactivation-agent** | 30-day inactivity | Full auto | Draft |
| **agents-evangelist** | Agents fit score threshold | Human-in-loop | Draft |

See [agents/](agents/) for full configurations and playbooks.

## Directory Structure

```
appsmith-gtm-os/
├── .claude/              # AI methodology + workflow layer
│   ├── CLAUDE.md         # Master instructions
│   ├── commands/         # Slash commands (/segment, /draft-sequence, etc.)
│   └── reference/        # Templates + agent delegation matrix
├── demand/               # WHO buys, WHEN, WHY
│   ├── icp.md            # Ideal customer profile
│   ├── positioning.md    # Product positioning
│   ├── competitors.md    # Competitive landscape
│   ├── buyer-insights.md # Synthesized buyer intelligence
│   └── pull-analyses/    # Individual call/interaction analyses
├── segments/             # TARGET groups by buyer situation
│   ├── segments.json     # Segment index
│   └── *.md              # Detailed segment files
├── messaging/            # WHAT we say
│   ├── angles.md         # Messaging angles by segment
│   ├── proof-points.md   # Data-backed claims
│   ├── voice.md          # Brand voice guidelines
│   └── objections.md     # Objection response frameworks
├── campaigns/            # HOW we execute
│   ├── campaigns.json    # Campaign index
│   ├── results.json      # Performance metrics
│   └── */                # Campaign folders with sequences + learnings
├── agents/               # SALES AGENTS that take actions
│   ├── agents.json       # Agent registry
│   ├── action-log.json   # All agent actions logged
│   ├── playbooks/        # Detailed agent playbooks
│   ├── scoring/          # ICP, PQL, engagement scoring models
│   └── actions/          # Python scripts for agent actions
├── engine/               # THE MACHINE (tech stack config)
│   ├── architecture.md   # System architecture + data flows
│   ├── engine.json       # Tech stack snapshot
│   ├── clay.md           # Enrichment config
│   ├── hubspot.md        # CRM config
│   ├── lemlist.md        # Email sequencer config
│   ├── prompts/          # AI prompt templates
│   └── signals/          # Intent signal detection
├── scripts/              # Executable automation
│   ├── process_signups.py
│   ├── check_pql_thresholds.py
│   ├── run_agent.py
│   └── pull_*.py         # Data pull scripts
├── content/              # Publishing (side effect of GTM work)
│   ├── seeds.md          # Content ideas
│   └── drafts/           # WIP content
├── status.md             # Current phase + TODOs
├── log.md                # Session timeline
└── requirements.txt      # Python dependencies
```

## Getting Started

### 1. Clone the repo
```bash
git clone <repo-url>
cd appsmith-gtm-os
```

### 2. Set up environment
```bash
cp .env.example .env
# Fill in API keys for: Clay, HubSpot, Lemlist, Slack, etc.
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Connect APIs
Follow setup guides in:
- [engine/clay.md](engine/clay.md) — Enrichment
- [engine/hubspot.md](engine/hubspot.md) — CRM
- [engine/lemlist.md](engine/lemlist.md) — Email sequencing

### 5. Run your first agent
```bash
# List available agents
python scripts/run_agent.py --list

# Process a signup
python scripts/run_agent.py signup-welcomer '{"email": "user@company.com"}'

# Check PQL thresholds
python scripts/run_agent.py pql-hunter
```

## Using with Claude Code

This repo is designed to be used with Claude Code. The `.claude/CLAUDE.md` file provides full context about the system.

### Key Commands
- `/segment` — Create a new buyer segment
- `/draft-sequence` — Draft an outbound email sequence
- `/analyze-call` — Analyze a sales call transcript
- `/campaign-report` — Pull and summarize campaign performance
- `/status-update` — Generate a status update
- `/trigger-agent` — Trigger a sales agent action
- `/signup-followup` — Process new signups

### Workflow
1. Check `status.md` before starting work
2. Reference `demand/` files before writing messaging
3. Use `messaging/voice.md` for all outbound copy
4. Log agent actions in `agents/action-log.json`
5. Update `log.md` after each session

## How to Add New Segments
1. Run `/segment` command
2. Follow the template in `.claude/commands/segment.md`
3. Update `segments/segments.json` index

## How to Add New Agent Playbooks
1. Create a new playbook in `agents/playbooks/`
2. Follow the structure: Purpose, Trigger, Workflow, Templates, Escalation, Metrics
3. Add the agent to `agents/agents.json`
4. Create action scripts in `agents/actions/` if needed
5. Update `.claude/reference/agent-delegation.md` with autonomy classification

## How to Trigger Agents
- **Automatically**: Via webhooks (signup events, usage events)
- **Scheduled**: Via cron jobs running `scripts/check_pql_thresholds.py`
- **Manually**: Via `python scripts/run_agent.py <agent_id>`
- **Via Claude Code**: Using `/trigger-agent` command
