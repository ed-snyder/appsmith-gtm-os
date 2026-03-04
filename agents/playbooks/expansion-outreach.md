---
title: Expansion Outreach Agent Playbook
updated: 2026-03-03
status: draft
---

# Expansion Opportunity Agent

## Purpose
Monitor existing paid customers for expansion signals — growing usage, new teams adopting, approaching tier limits — and trigger CSM-style check-ins to drive plan upgrades or seat expansion.

## Trigger
Expansion signal detected from product analytics or CRM data.

## Expansion Signals

| Signal | Weight | Detection Method |
|--------|--------|-----------------|
| Approaching user limit (80%+ of plan capacity) | High | Product analytics |
| New workspace created | Medium | Product analytics |
| API usage growth >50% month-over-month | High | Product analytics |
| New data source types connected | Medium | Product analytics |
| New department/team using the platform | High | Enrichment + usage patterns |
| SSO/SAML inquiry | High | Support tickets, feature requests |
| Managed hosting inquiry | High | Support tickets |
| App count growth >3x in 30 days | Medium | Product analytics |
| Custom widget development | Medium | Product analytics |

## Workflow

### Step 1: Detect Expansion Signal
- Monitor product analytics for threshold crossings (checked daily)
- Cross-reference with CRM for current plan and contract details
- Calculate expansion potential (estimated additional revenue)

### Step 2: Research Account Context
- Pull current plan details, usage metrics, and contract renewal date
- Review recent support tickets and feature requests
- Check for any open opportunities or active sales conversations
- Identify the primary contact and any new stakeholders

### Step 3: Prepare Outreach (Human-in-Loop)
- Draft a CSM-style check-in email based on the expansion signal
- Include:
  - Usage report showing their growth
  - Relevant upgrade path (more seats, higher tier, add-ons)
  - ROI calculation based on their usage
- Present draft to account owner (CSM or AE) for approval

### Step 4: Execute (After Approval)
- Send approved outreach email
- Create CRM opportunity if upgrade discussion is likely
- Schedule follow-up task for account owner

### Step 5: Log
- Record expansion signal, outreach, and outcome in `agents/action-log.json`
- Update CRM with expansion opportunity details

## Outreach Templates

### Approaching User Limit
Subject: "Your Appsmith team is growing — let's plan ahead"
Body: "Your team has {{current_users}}/{{max_users}} users on the {{plan_name}} plan. As you add more people, here's what upgrading looks like: [pricing details]. Happy to discuss the best option for {{company_name}}."

### Usage Growth
Subject: "Your Appsmith usage is up {{growth_pct}}% — nice"
Body: Acknowledge growth. Share usage stats. Suggest features that could help at their scale. Offer usage review call.

### New Team/Department
Subject: "Saw new teams are using Appsmith at {{company_name}}"
Body: Acknowledge expansion to new use cases. Offer templates for common patterns. Suggest RBAC setup for multi-team governance.

## Escalation Rules
- Expansion potential >$10K ARR: Route to AE, not CSM
- Contract renewal within 60 days + expansion signal: Priority flag for account review
- Customer at risk signals (declining usage + expansion signal in different team): Flag for CSM review
- Enterprise feature inquiry (SSO, managed hosting): Route to Enterprise team

## Performance Metrics
- Expansion signal detection accuracy: >75%
- Signal to outreach time: <48 hours
- Expansion outreach to meeting rate: target 25%
- Expansion revenue per quarter: track and report
- Net revenue retention contribution: measure impact
