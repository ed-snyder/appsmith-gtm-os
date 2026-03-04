---
title: Appsmith Agents Cross-Sell Playbook
updated: 2026-03-03
status: draft
---

# Appsmith Agents Cross-Sell Agent

## Purpose
Identify existing Appsmith customers who are strong fits for Appsmith Agents based on their tech stack (Salesforce, Zendesk, Slack), team composition (sales, support, CS teams), and AI readiness signals. Execute cross-sell outreach with human approval.

## Trigger
Existing customer matches Agents fit score threshold (calculated from enrichment + usage data).

## Fit Criteria

### Must-Have (all required)
- Active Appsmith customer (paid plan, active usage in last 30 days)
- Uses at least one of: Salesforce, Zendesk, Slack, HubSpot, Intercom
- Has sales, support, or CS team of 10+ people
- Company size 100+ employees

### Nice-to-Have (increase fit score)
- Active AI initiative (AI job posts, AI budget, ChatGPT Enterprise)
- Using multiple qualifying tools (Salesforce + Zendesk + Slack)
- Has voiced AI interest (support tickets, feature requests, community posts)
- Industry with strong AI adoption (tech, finserv, e-commerce)

### Fit Scoring

| Criteria | Points |
|----------|--------|
| Active Appsmith customer | Required (gate) |
| Uses Salesforce | +20 |
| Uses Zendesk | +20 |
| Uses Slack (business) | +15 |
| Uses HubSpot | +15 |
| Uses Intercom | +15 |
| Sales team 10+ | +15 |
| Support team 10+ | +15 |
| CS team 10+ | +15 |
| Company 100-500 employees | +10 |
| Company 500+ employees | +20 |
| AI initiative detected | +20 |
| Multiple qualifying tools (3+) | +10 bonus |
| AI interest voiced | +15 |

**Fit Threshold**: 60+ points = qualified for cross-sell outreach

## Workflow

### Step 1: Score Existing Customers
- Query CRM for active paid customers
- Enrich with Clay for tech stack and team composition data
- Apply fit scoring model above
- Rank by fit score

### Step 2: Research Top Accounts (Human-in-Loop)
- For each qualified account, research:
  - Which qualifying tools they use
  - Which teams would benefit (sales, support, CS)
  - Any AI initiatives or mentions from the account
  - Relationship status (healthy, at-risk, expanding)
- Script: `agents/actions/enrich_signup.py` (reused for enrichment)

### Step 3: Prepare Outreach (Human Approval Required)
- Draft personalized cross-sell email tailored to their stack:
  - If Salesforce user: "AI inside Salesforce" angle
  - If Zendesk user: "AI-powered support" angle
  - If Slack user: "AI assistant in Slack" angle
- Include:
  - Their current Appsmith usage as credibility anchor
  - Specific Agents use case for their team type
  - Demo video link
  - Pilot offer (free 2-week trial)
- Present to account owner for approval

### Step 4: Execute (After Approval)
- Send approved email
- If LinkedIn outreach approved: send connection/message via account owner's profile
- Schedule follow-up in CRM

### Step 5: Log
- Record cross-sell attempt and outcome in `agents/action-log.json`
- Update CRM with Agents opportunity if interest expressed

## Outreach Templates

### Template A — Salesforce Users
Subject: "AI inside Salesforce for your sales team"
Body: "You're already building great internal tools on Appsmith. We just launched Appsmith Agents — context-aware AI that works inside Salesforce (via Chrome extension). Your sales team gets AI that knows your customer data, pipeline, and processes. No new tab, no workflow change. Want to see a 10-minute demo?"

### Template B — Zendesk Users
Subject: "Faster support responses with AI + Zendesk"
Body: "Your support team uses Zendesk. Appsmith Agents gives them an AI assistant inside Zendesk that knows your product, documentation, and customer history. It drafts responses, surfaces relevant articles, and flags escalations — all in-context. Interested in a pilot?"

### Template C — Multi-Tool Users
Subject: "AI that connects {{tool_1}}, {{tool_2}}, and {{tool_3}}"
Body: "Your team uses {{tool_list}} — Appsmith Agents works across all of them via Chrome extension. One AI assistant that knows your data across tools and helps your team in whatever app they're working in. 2-week free pilot to test it?"

## Escalation Rules
- Enterprise customers (1,000+ employees): Route to Enterprise AE, not standard cross-sell
- Customers with active support escalation: Do NOT cross-sell, flag for CSM attention first
- Customers in contract renewal (<90 days): Coordinate with renewal team
- High-fit accounts with no response to email: Offer webinar invitation as softer touch

## Performance Metrics
- Fit scoring accuracy (qualified accounts that express interest): target >20%
- Cross-sell email response rate: target >10%
- Demo/meeting booking rate: target 15% of responses
- Cross-sell to pilot rate: target 8% of qualified accounts
- Pilot to paid conversion: target 40%
