---
title: PQL Outreach Agent Playbook
updated: 2026-03-03
status: active
---

# Product-Qualified Lead Hunter

## Purpose
Monitor product usage signals to identify accounts that have reached product-qualified lead (PQL) thresholds, then trigger personalized outreach to convert them to paid plans or book meetings.

## Trigger
Account crosses PQL threshold (checked on schedule or via product event webhook).

## PQL Definition

An account is product-qualified when it meets **3 or more** of these criteria:
- **3+ apps created** (shows platform adoption beyond exploration)
- **2+ data sources connected** (shows real data integration)
- **3+ team members invited** (shows team adoption)
- **Active in last 7 days** (shows ongoing usage, not a one-time test)
- **API query volume >100/week** (shows production-level usage)
- **Custom widget or JS object created** (shows advanced usage)

## PQL Scoring Model

| Signal | Points | Rationale |
|--------|--------|-----------|
| 3+ apps created | +20 | Multi-use case adoption |
| 5+ apps created | +30 | Deep platform investment |
| 2+ data sources connected | +15 | Real data integration |
| 4+ data sources connected | +25 | Complex data layer |
| 3+ team members invited | +15 | Team adoption |
| 5+ team members (at free limit) | +25 | Hitting growth ceiling |
| Active last 7 days | +10 | Current engagement |
| Active last 3 days | +20 | High engagement |
| API queries >100/week | +15 | Production usage |
| API queries >500/week | +25 | Heavy production usage |
| Custom widget created | +10 | Advanced user |
| Git integration enabled | +15 | Developer workflow adoption |
| Workflow attempted (Business feature gate) | +20 | Feature upgrade trigger |

**PQL Tiers**:
- **PQL-Hot** (Score 80+): Immediate outreach, high conversion probability
- **PQL-Warm** (Score 50-79): Standard outreach sequence
- **PQL-Early** (Score 30-49): Add to nurture, monitor for escalation

## Workflow

### Step 1: Detect PQL Signals
- Query product analytics API for accounts crossing thresholds
- Script: `agents/actions/check_pql_signals.py` (runs every 6 hours)
- Cross-reference with CRM to exclude existing paid customers and active opportunities

### Step 2: Enrich & Score
- If not already enriched, run enrichment via Clay
- Apply PQL scoring model above
- Combine with ICP score from signup for total lead score
- Script: `agents/actions/score_lead.py`

### Step 3: Research & Personalize
- Pull specific usage data for personalization:
  - Which data sources they connected (PostgreSQL, MongoDB, etc.)
  - Types of apps built (admin panels, dashboards, forms)
  - Features used most
  - Features NOT used that would help them
- Prepare personalized outreach draft

### Step 4: Route (Human-in-Loop)
- **PQL-Hot**: Draft personalized email + present to AE for approval
  - Include: usage summary, ICP score, recommended talk track, calendar link
  - Slack alert to assigned AE with full context
- **PQL-Warm**: Draft email sequence + present for approval
  - 3-email sequence over 10 days
- **PQL-Early**: Add to automated nurture sequence
  - No human approval needed for standard nurture emails

### Step 5: Execute Outreach (after approval for Hot/Warm)
- Send personalized email via sequencer
- Queue LinkedIn touchpoint for PQL-Hot accounts
- Schedule follow-up reminders in CRM
- Script: `agents/actions/send_sequence_email.py`

### Step 6: Log
- Record PQL detection, score, outreach actions in `agents/action-log.json`
- Update CRM with PQL status and score
- Script: `agents/actions/log_action.py`

## Outreach Sequence

### PQL-Hot (3 touches over 7 days)

**Email 1 — Usage Recognition (Day 1)**
Subject: "{{first_name}}, your team is building great stuff"
Body: Acknowledge specific usage (apps, data sources, team size). Reference a feature they haven't tried that would help. Offer quick call.

**LinkedIn (Day 2)**
Connection request or message referencing their Appsmith usage and offering value.

**Email 2 — Value Expansion (Day 5)**
Subject: "One feature that could change your workflow"
Body: Highlight a Business feature relevant to their usage pattern (workflows for heavy API users, RBAC for large teams).

**Email 3 — Direct Ask (Day 7)**
Subject: "Quick question about {{company_name}}'s internal tools"
Body: Direct CTA for a 15-minute call. Include Calendly link.

### PQL-Warm (3 touches over 10 days)

**Email 1 (Day 1)**: Usage milestone recognition + relevant content link
**Email 2 (Day 5)**: Feature highlight they haven't tried + case study
**Email 3 (Day 10)**: Upgrade CTA with trial offer

## Handoff Criteria to Human AE
- PQL-Hot account at a company with 200+ employees: immediate AE assignment
- Prospect replies to any outreach email: route reply to AE
- Prospect books a meeting: AE owns the meeting
- Enterprise signals detected (SSO inquiry, managed hosting question): route to Enterprise AE

## Meeting Scheduling
- Include Calendly link in all outreach emails
- If prospect clicks Calendly but doesn't book: send follow-up with alternative times
- Meeting booked: auto-create prep brief using `.claude/reference/templates.md` call prep template

## Escalation Rules
- If PQL-Hot account has no AE response within 4 hours: escalate to sales manager
- If prospect from 1,000+ employee company: flag for enterprise team
- If competitor usage detected alongside Appsmith: tag for competitive motion

## Performance Metrics
- PQL detection accuracy: >80% (validated against actual conversions)
- PQL-Hot to meeting booked: target 20%
- PQL-Warm to meeting booked: target 8%
- Time from PQL detection to first outreach: <24 hours (Hot), <48 hours (Warm)
- PQL to paid conversion rate: target 12%
