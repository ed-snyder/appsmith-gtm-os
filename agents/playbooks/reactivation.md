---
title: Reactivation Agent Playbook
updated: 2026-03-03
status: draft
---

# Churned User Reactivation Agent

## Purpose
Identify users who have stopped using Appsmith (30+ days inactive) and send re-engagement sequences highlighting new features released since their last activity. Win back churned accounts with relevant updates and offers.

## Trigger
User account inactive for 30+ consecutive days (no login, no API activity).

## Workflow

### Step 1: Identify Inactive Accounts
- Query product analytics for accounts with no activity in 30+ days
- Exclude: accounts that explicitly cancelled, accounts in active sales conversations
- Categorize by last activity type and tenure:
  - **Recent churn** (30-60 days inactive): Highest reactivation probability
  - **Medium churn** (60-90 days inactive): Moderate probability
  - **Deep churn** (90+ days inactive): Low probability, one final attempt

### Step 2: Build Context
- What was their last activity? (last app edited, last feature used)
- What features have been released since their last login?
- What was their usage level before churning? (casual, moderate, heavy)
- Were they on a paid plan that lapsed?

### Step 3: Personalize Sequence
- Match new features to their previous usage patterns
- If they used PostgreSQL → highlight new PostgreSQL features
- If they built dashboards → highlight new chart widgets
- If they had multiple team members → highlight new collaboration features

### Step 4: Execute Re-engagement Sequence (Full Auto)

#### Email 1 — "What's new" (Day 1 after 30-day trigger)
Subject A: "Appsmith shipped {{feature_count}} updates since you left"
Subject B: "Your Appsmith workspace is still here"

Body: "Since your last login on {{last_active_date}}, we've shipped:
- {{feature_1_relevant_to_their_usage}}
- {{feature_2_relevant_to_their_usage}}
- {{feature_3_general_highlight}}

Your workspace and apps are right where you left them: {{login_link}}"

#### Email 2 — "Relevant use case" (Day 5)
Subject: "Teams like {{company_name}} are building {{use_case}}"

Body: Share a relevant case study or template based on their previous usage pattern. "Here's how a similar team is using Appsmith for {{relevant_use_case}}. Template: {{template_link}}"

#### Email 3 — "Personal offer" (Day 12)
Subject: "Want a fresh start with Appsmith?"

Body: Offer based on their history:
- **Previous free user**: "We can set you up with a 1:1 walkthrough of the new features"
- **Previous paid user**: "Want to try the latest version free for 15 days?"
- **Heavy previous user**: "I'd love to understand what didn't work last time"

### Step 5: Archive or Escalate
- If no engagement after 3 emails: Archive from reactivation (do not re-contact for 6 months)
- If email opened but no action: One final "Is there anything we can help with?" note
- If reply received: Route to appropriate human (sales for paid, community for free)

### Step 6: Log
- Record all reactivation attempts and outcomes in `agents/action-log.json`
- Update CRM with reactivation status

## Exclusion Rules
- Do not reactivate accounts that explicitly requested to stop contact
- Do not reactivate accounts with bounced emails (clean list first)
- Do not reactivate accounts that are in active legal/billing disputes
- Max 1 reactivation cycle per account per 6 months

## Escalation Rules
- If previous paid customer replies: immediate route to Account Manager
- If previous Enterprise customer inactive: route to CSM before any automated outreach
- If reactivation response mentions competitor: tag for competitive intelligence

## Performance Metrics
- Reactivation email open rate: target >30%
- Reactivation to re-login rate: target 8%
- Reactivation to paid conversion: target 3%
- Previous paid user re-conversion rate: target 10%
- Unsubscribe rate from reactivation: monitor (<2% acceptable)
