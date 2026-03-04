---
title: Trial Nurture Agent Playbook
updated: 2026-03-03
status: active
---

# Trial Nurture Agent

## Purpose
Guide Business plan trial users (15-day trial) through onboarding, feature adoption, and conversion via usage-based automated nudges. Escalate high-engagement trials to sales.

## Trigger
User starts a Business plan 15-day trial.

## Workflow

### Day 1: Welcome + Setup Guide

**Email**: "Your Business trial is live — here's your setup checklist"

Content:
- Confirm trial activated with expiry date
- Setup checklist:
  1. Enable workflows for your first automation
  2. Set up custom roles for your team
  3. Turn on audit logs
  4. Configure Git integration
- Link to Business features documentation
- Calendar link for optional 1:1 setup call

**Action**: Create CRM task to check Day 3 usage

---

### Day 3: Usage-Based Check-in

**Branch A — Active User (has used Business features)**:
Email: "Nice — you've already set up {{feature_used}}"
Content: Acknowledge their progress. Suggest next feature to try. Share relevant use case.

**Branch B — Inactive User (hasn't used Business features)**:
Email: "Need help getting started with Business features?"
Content: Quick-start guide for top 3 Business features. Offer 15-minute walkthrough call. Link to video tutorials.

**Action**: Log usage status, update CRM

---

### Day 7: Mid-Trial Value Reminder

**Email**: "Halfway through your trial — here's what you've unlocked"

Content:
- Summary of Business features they've used
- Highlight features they haven't tried yet
- Relevant case study for their industry/use case
- Reminder of what changes when trial ends

**If high engagement (3+ Business features used)**:
- Slack alert to sales: "High-engagement trial at {{company_name}}"
- Add to PQL-Hot queue

---

### Day 10: Feature They Haven't Tried

**Email**: "You haven't tried {{untried_feature}} yet"

Content:
- Pick the most relevant Business feature they haven't used
- 2-minute video walkthrough of the feature
- Specific benefit for their use case
- "Reply if you need help setting it up"

---

### Day 13: Trial Ending Reminder

**Email**: "Your Business trial ends in 2 days"

Content:
- Clear statement of what happens when trial ends
- List of Business features they'll lose access to (personalized to their usage)
- Pricing: $15/user/month
- Two CTAs:
  1. Upgrade now
  2. "Need more time? Reply and I'll extend your trial"

**If Tier A/B ICP score**: Offer to connect with an AE for pricing discussion

---

### Day 15: Trial Expired Follow-up

**Email**: "Your Business trial has ended"

Content:
- Their apps still work on the free tier
- Specific impact of downgrade (personalized):
  - Workflows they created are paused
  - Custom roles revert to default
  - Audit logs stop recording
- Upgrade link with pricing
- "Want to chat about the right plan? Reply to this email."

**If no upgrade within 3 days**: Add to reactivation nurture (lower frequency)

## Escalation Rules
- High engagement trial (3+ Business features used by Day 7): Slack alert + AE assignment
- Trial user from 500+ employee company: AE assignment from Day 1
- Trial user requests extension: Auto-extend 7 days, notify AE
- Trial user asks about Enterprise features (SSO, managed hosting): Route to Enterprise AE
- Trial user has 5+ team members: Flag as upgrade-ready (hitting free user limit post-trial)

## Personalization Rules
- Reference specific Business features they've used in every email
- If they connected data sources, mention those by name
- If they created workflows, reference the workflow names
- Industry-specific case study selection based on enrichment data

## Performance Metrics
- Day 1 email open rate: >60%
- Day 3 active vs inactive split: target 50%+ active
- Day 7 high-engagement detection rate: target 25% of trials
- Trial to paid conversion rate: target 15%
- Trial extension request rate: monitor (not a negative signal)
- Average time from trial start to paid: target <20 days
