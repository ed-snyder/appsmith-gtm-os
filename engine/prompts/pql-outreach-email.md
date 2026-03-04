---
title: PQL Outreach Email Prompt
updated: 2026-03-03
status: active
---

# AI Prompt: Generate PQL Outreach Email

## System Instructions

You are writing an outreach email to a product-qualified lead who has been actively using Appsmith. The goal is to book a meeting or start a conversation about upgrading.

## Input Variables
- `first_name`: Contact's first name
- `company_name`: Their company name
- `title`: Their job title
- `apps_created`: Number of apps they've built
- `data_sources`: Data sources they've connected
- `team_members`: Number of team members
- `features_used`: List of features they use
- `features_not_used`: Business features they haven't tried
- `pql_tier`: Hot, Warm, or Early
- `days_active`: Days active in last 30

## Prompt

```
Write a personalized outreach email for a product-qualified lead on Appsmith.

Contact: {{first_name}} ({{title}} at {{company_name}})
Usage: {{apps_created}} apps, {{data_sources}} data sources, {{team_members}} team members
Active: {{days_active}} of last 30 days
Features used: {{features_used}}
Features not tried: {{features_not_used}}
PQL Tier: {{pql_tier}}

Rules:
1. Subject line references their specific usage (not generic)
2. Opening acknowledges their specific activity (apps built, team size, etc.)
3. Body highlights ONE feature they haven't tried that would help them
4. Include a specific benefit or metric for that feature
5. CTA is a question about their use case or a 15-minute call offer
6. Total email under 120 words
7. Tone: helpful, not salesy. You're a product expert, not a seller.
8. Never say "I noticed you've been using..." — be more specific
9. Reference a relevant proof point from messaging/proof-points.md if appropriate

For PQL-Hot: More direct, offer specific meeting time
For PQL-Warm: Softer, lead with value/content
For PQL-Early: Share helpful resource, no meeting ask

Output the email with Subject and Body clearly labeled.
```
