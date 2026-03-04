---
title: GTM Engine Architecture
updated: 2026-03-03
status: active
---

# GTM Engine Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│                    DATA SOURCES                          │
│                                                          │
│  Product (Appsmith Cloud)    Website    Community         │
│       │                        │           │              │
│       ▼                        ▼           ▼              │
│  Signup Webhook          Analytics    Discord/Forum       │
└──────┬─────────────────────┬───────────────┬────────────┘
       │                     │               │
       ▼                     ▼               ▼
┌─────────────────────────────────────────────────────────┐
│                    CRM (HubSpot)                         │
│                                                          │
│  Contacts │ Companies │ Deals │ Lists │ Workflows        │
└──────┬──────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│                 ENRICHMENT (Clay)                        │
│                                                          │
│  Company Data │ Person Data │ Tech Stack │ Signals        │
└──────┬──────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│                 SCORING ENGINE                           │
│                                                          │
│  ICP Score │ PQL Score │ Engagement Score │ Tier          │
└──────┬──────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│              AGENT ORCHESTRATION                         │
│                                                          │
│  signup-welcomer ──► Tier A/B/C/D routing                │
│  pql-hunter ──────► PQL detection + outreach             │
│  trial-nudger ────► 15-day trial nurture                 │
│  expansion-spotter► Upsell signal detection              │
│  reactivation ────► Churn re-engagement                  │
│  agents-evangelist► Cross-sell Appsmith Agents            │
└──────┬──────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│              EXECUTION LAYER                             │
│                                                          │
│  Lemlist (Email)  │  Slack (Alerts)  │  LinkedIn          │
│  Calendar (Mtgs)  │  CRM (Updates)   │  Action Log        │
└──────────────────────────────────────────────────────────┘
```

## Data Flow Details

### 1. Signup Flow
```
New Signup → Product Webhook → CRM Contact Created
    → Clay Enrichment → ICP Scoring → Segment Assignment
    → Agent Routing → Welcome Email + (Slack Alert for Tier A)
```

### 2. PQL Detection Flow
```
Product Analytics → PQL Signal Check (every 6 hours)
    → PQL Score Calculation → Tier Assignment
    → PQL-Hot: Slack Alert + AE Draft (human approval)
    → PQL-Warm: Email Sequence Draft (human approval)
    → PQL-Early: Auto Nurture
```

### 3. Trial Nurture Flow
```
Trial Started → CRM Workflow Trigger
    → Day 1: Welcome + Setup
    → Day 3: Usage Check (Branch A/B)
    → Day 7: Mid-trial + High Engagement Detection
    → Day 10: Feature Highlight
    → Day 13: Reminder + Extension Offer
    → Day 15: Expiry Follow-up
```

### 4. Expansion Flow
```
Product Analytics → Expansion Signal Detection (daily)
    → Account Research + Context Building
    → CSM-Style Outreach Draft (human approval)
    → CRM Opportunity Creation
```

### 5. Reactivation Flow
```
Product Analytics → 30-Day Inactivity Trigger
    → New Features Since Last Activity
    → 3-Email Re-engagement Sequence (auto)
    → Archive or Route to Human
```

## Tech Stack

| Component | Tool | Purpose |
|-----------|------|---------|
| CRM | HubSpot | Contact/company/deal management |
| Enrichment | Clay | Company + person data enrichment |
| Email Sequencing | Lemlist | Automated email campaigns |
| Product Analytics | TBD | Usage signals + PQL detection |
| Call Recording | Gong/Fireflies | Call analysis + transcript ingestion |
| Search/Signals | Exa | Intent signal detection |
| Slack | Slack Webhooks | Team alerts + notifications |
| Calendar | Google Calendar | Meeting scheduling |
| AI/LLM | Anthropic Claude | Email personalization, call analysis |

## Integration Points

### Inbound
- Product signup webhook → CRM
- Product usage events → Analytics → PQL detection
- Call recordings → Transcript → Analysis

### Outbound
- Agent actions → Email (Lemlist)
- Agent alerts → Slack
- Agent updates → CRM (HubSpot)
- Agent logs → action-log.json

### Scheduled
- PQL signal check: every 6 hours
- Expansion signal check: daily
- Reactivation check: daily
- Engagement score decay: daily
- Campaign metrics pull: daily
