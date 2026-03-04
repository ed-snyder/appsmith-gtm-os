---
title: Appsmith GTM-OS Master Instructions
updated: 2026-03-03
status: active
---

# Appsmith GTM-OS

This is the go-to-market operating system for Appsmith. It contains demand intelligence, buyer segmentation, messaging frameworks, campaign operations, sales agent configurations, and the full GTM engine spec.

## Company Context

Appsmith is an open-source low-code platform for building internal tools. Founded in 2019, based in San Francisco, Series B ($51.5M raised). The platform lets developers build dashboards, admin panels, CRUD apps, and workflow tools using drag-and-drop UI + JavaScript. They recently launched Appsmith Agents, an agentic AI platform that embeds context-aware AI into enterprise tools via Chrome extension.

## Product Lines
- **Appsmith (Core)**: Open-source low-code platform for internal tools
- **Appsmith Agents**: Agentic AI platform for enterprise teams (sales, support, CS, HR)

## Pricing
- Free: Up to 5 users, core features
- Business: $15/user/month (workflows, custom roles, audit logs)
- Enterprise: $2,500/month for 100 users (SSO, SAML, managed hosting, SLAs)

## Rules for Working in This Repo

1. Always check status.md before starting work
2. Always update log.md after completing a session
3. Reference demand/ files before writing any messaging or campaign content
4. Never fabricate data points. Pull from messaging/proof-points.md or cite the source
5. When agents take actions, log them in agents/action-log.json
6. Check agents/playbooks/ before configuring any new agent behavior
7. All outbound copy must pass through messaging/voice.md guidelines

## File Conventions
- Markdown for prose, analysis, playbooks
- JSON for queryable/structured state
- Python for executable automation and agent scripts

## Directory Map
- `.claude/` — AI methodology, slash commands, reference templates
- `demand/` — WHO buys, WHEN, WHY (ICP, positioning, competitors, buyer insights)
- `segments/` — TARGET groups by buyer situation
- `messaging/` — WHAT we say (angles, proof points, voice, objections)
- `campaigns/` — HOW we execute (active operations, sequences, results)
- `agents/` — SALES AGENTS that take actions on behalf of the team
- `engine/` — THE MACHINE (full GTM tech stack config)
- `scripts/` — EXECUTABLE code (pulls + pushes data)
- `content/` — PUBLISHING (side effect of working)
- `status.md` — Current phase + TODOs
- `log.md` — Reverse-chronological session timeline

## Agent Architecture

This repo contains 6 sales agents that autonomously handle GTM motions:

1. **signup-welcomer** — Processes new signups, enriches, scores, sends welcome sequences
2. **pql-hunter** — Detects product-qualified leads and triggers outreach
3. **trial-nudger** — Nurtures Business plan trial users through 15-day trial
4. **expansion-spotter** — Identifies expansion opportunities in existing accounts
5. **reactivation-agent** — Re-engages churned/inactive users
6. **agents-evangelist** — Cross-sells Appsmith Agents to existing customers

Agent playbooks are in `agents/playbooks/`. Agent configs are in `agents/agents.json`. All agent actions are logged in `agents/action-log.json`.

## Autonomy Levels
- **full_auto**: Agent acts without human approval (welcome emails, enrichment, low-risk nurture)
- **human_in_loop**: Agent prepares the action, human approves before sending (PQL outreach, expansion, cross-sell)
- **human_only**: Agent provides research/recommendations, human executes (enterprise deals, legal, contracts)

See `.claude/reference/agent-delegation.md` for the full decision matrix.
