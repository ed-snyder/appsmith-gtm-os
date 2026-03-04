---
title: Agent Delegation Matrix
updated: 2026-03-03
status: active
---

# Agent Delegation Decision Matrix

This document defines which tasks are handled by AI agents autonomously, which require human approval, and which are human-only.

## Fully Automated (AI Agent Acts Independently)

| Task | Agent | Rationale |
|------|-------|-----------|
| Signup acknowledgment email | signup-welcomer | Low risk, high volume, time-sensitive |
| Lead enrichment (Clay/Clearbit) | signup-welcomer | Data lookup, no outbound communication |
| ICP scoring | signup-welcomer | Algorithmic, based on defined model |
| Segment tagging in CRM | signup-welcomer | Rule-based classification |
| Trial nurture emails (Day 1-10) | trial-nudger | Pre-approved templates, low risk |
| Inactive user re-engagement (email 1) | reactivation-agent | Standard template, low stakes |
| Slack alerts for Tier A signups | signup-welcomer | Internal notification only |
| Action logging | all agents | Record keeping |
| Meeting scheduling (via Calendly link) | all agents | Self-serve, no commitment |

## Human-in-the-Loop (AI Prepares, Human Approves)

| Task | Agent | Approval Needed From |
|------|-------|---------------------|
| PQL outreach (first touch) | pql-hunter | AE assigned to account |
| Expansion outreach | expansion-spotter | CSM or Account Manager |
| Appsmith Agents cross-sell | agents-evangelist | Account owner |
| Trial extension offers | trial-nudger | Sales manager |
| Custom pricing discussions | — | Sales leadership |
| Enterprise demo scheduling | — | AE |
| LinkedIn outreach (personalized) | pql-hunter | AE |
| Competitive displacement campaigns | — | Marketing + Sales |
| Re-engagement with discount offer | reactivation-agent | Sales manager |

## Human-Only (AI Provides Research/Recommendations)

| Task | Rationale |
|------|-----------|
| Contract negotiation | Legal implications, custom terms |
| Custom security reviews | Technical and legal complexity |
| Executive relationship management | Requires personal rapport |
| Enterprise pricing decisions | Revenue impact, requires context |
| Legal/compliance commitments | Binding obligations |
| Partner/channel discussions | Strategic relationships |
| Press/analyst interactions | Brand reputation risk |
| Customer escalations | Emotional intelligence required |
| Reference customer requests | Relationship sensitivity |

## Decision Criteria

When deciding where a new task falls:

1. **What's the blast radius if the agent gets it wrong?**
   - Low (wrong email template) → Fully automated
   - Medium (inappropriate outreach) → Human-in-loop
   - High (legal/financial/reputation) → Human-only

2. **Is the task templatable?**
   - Yes, with clear rules → Fully automated
   - Mostly, but needs judgment → Human-in-loop
   - No, requires nuance → Human-only

3. **What's the volume?**
   - High volume, low variance → Fully automated
   - Medium volume, some variance → Human-in-loop
   - Low volume, high variance → Human-only

4. **Is the recipient internal or external?**
   - Internal (Slack alerts, CRM updates) → Fully automated
   - External, existing template → Fully automated or human-in-loop
   - External, custom communication → Human-in-loop or human-only

## Escalation Rules

- If an agent encounters a situation not covered by its playbook → Escalate to human
- If enrichment data is incomplete (score confidence <60%) → Flag for human review
- If contact has had previous negative interaction → Human-only
- If company is a named/strategic account → Human-in-loop minimum
- If outreach involves C-suite (VP+) → Human-in-loop minimum
