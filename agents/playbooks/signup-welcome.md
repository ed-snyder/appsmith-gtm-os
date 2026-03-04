---
title: Signup Welcome Agent Playbook
updated: 2026-03-03
status: active
---

# Signup Welcome Agent

## Purpose
Automatically process every new free signup, enrich the account, score it, segment it, and deliver a personalized welcome sequence.

## Trigger
New user creates a free Appsmith account (webhook from product or CRM).

## Workflow

### Step 1: Enrich
- Pull company data via Clay (domain, size, industry, tech stack, funding)
- Pull person data (title, seniority, LinkedIn, role)
- Store enrichment in CRM contact record
- Script: `agents/actions/enrich_signup.py`

### Step 2: Score
- Apply ICP scoring based on `demand/icp.md` criteria
- Use scoring model from `agents/scoring/icp-scoring-model.md`
- Tier: A (perfect fit), B (good fit), C (low priority), D (disqualify)
- Scoring factors:
  - Company size 50-5,000 employees (+20)
  - Engineering team detected (+15)
  - Tech stack match: PostgreSQL (+10), MongoDB (+10), React (+10), Docker (+10)
  - Title match: Engineering Manager (+20), VP Eng (+20), Platform Lead (+20)
  - Self-hosting interest signal (+10)
  - Industry match: Technology (+5), FinServ (+5), Healthcare (+5), E-commerce (+5)
  - Funding detected (+5)
- Script: `agents/actions/score_lead.py`

### Step 3: Segment
- Match to `segments/segments.json` based on enrichment data
- Tag with primary segment in CRM
- Segment matching rules:
  - Retool detected in tech stack → retool-refugees
  - Multiple internal tools detected → internal-tool-sprawl
  - OSS signals (GitHub contributions, self-hosting search) → open-source-first
  - AI/Salesforce/Zendesk/Slack in stack + AI job posts → ai-agent-adopters
  - SOC 2/HIPAA signals → compliance-driven

### Step 4: Route

#### Tier A (Score 60+)
- Immediate Slack alert to sales team with enrichment summary
- Send personalized welcome email (reference their tech stack, company size)
- Queue LinkedIn connection request from assigned AE
- Add to high-touch nurture sequence
- Script: `agents/actions/slack_alert.py` + `agents/actions/send_sequence_email.py`

#### Tier B (Score 30-59)
- Send welcome email with relevant use case content
- Add to automated nurture sequence
- Monitor for PQL signals

#### Tier C (Score 10-29)
- Send standard welcome email
- Add to community nurture (blog content, templates, webinars)

#### Tier D (Score <10)
- Send standard welcome email only
- No further automation

### Step 5: Log
- Record all actions in `agents/action-log.json`
- Update CRM with agent activity notes
- Script: `agents/actions/log_action.py`

## Messaging Templates
Reference: `messaging/voice.md` for tone
Reference: `.claude/reference/templates.md` for email templates

### Welcome Email (Tier A)
Subject: "{{first_name}}, your Appsmith instance is ready"
Body: Acknowledge their role + company. Reference a relevant use case for their industry. Offer a quick call to discuss their use case. Include link to relevant template.

### Welcome Email (Tier B)
Subject: "Get started with Appsmith in 10 minutes"
Body: Link to quickstart guide. Show 3 relevant templates. Invite to next community event.

### Welcome Email (Tier C/D)
Subject: "Welcome to Appsmith"
Body: Quickstart link. Documentation link. Community link.

## Escalation Rules
- If Tier A signup is from a company with 500+ employees: immediate Slack ping to sales leadership
- If signup email domain matches existing customer: flag for expansion team (route to expansion-spotter)
- If competitor tech detected (Retool, ToolJet): tag for competitive migration campaign
- If enrichment fails (no company data): flag for manual review, send generic welcome

## Performance Metrics
- Time from signup to first email: <5 minutes
- Enrichment success rate: >85%
- Tier A to meeting booked rate: target 15%
- Tier B to PQL conversion: target 8%
- Overall welcome email open rate: >50%
- Tier A Slack alert to AE first touch: <2 hours
