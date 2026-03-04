---
title: Signup Welcome Email Prompt
updated: 2026-03-03
status: active
---

# AI Prompt: Generate Personalized Welcome Email

## System Instructions

You are writing a welcome email for a new Appsmith signup. Follow the voice guidelines from messaging/voice.md strictly.

## Input Variables
- `first_name`: Contact's first name
- `company_name`: Their company name
- `title`: Their job title
- `industry`: Their industry
- `employee_count`: Company size
- `tech_stack`: Known technologies they use
- `icp_tier`: A, B, C, or D
- `primary_segment`: Their buyer segment

## Prompt

```
Write a personalized welcome email for a new Appsmith signup.

Contact: {{first_name}} ({{title}} at {{company_name}})
Company: {{employee_count}} employees, {{industry}} industry
Tech stack: {{tech_stack}}
ICP Tier: {{icp_tier}}
Segment: {{primary_segment}}

Rules:
1. Subject line under 50 characters, specific to them
2. Opening line references something specific about their company or role — never start with "I" or "We"
3. Body is ONE short paragraph (under 100 words)
4. Include one relevant use case for their industry
5. End with a question as CTA, not a demand
6. Total email under 150 words
7. Tone: conversational, technical credibility, no buzzwords
8. Do NOT use: "revolutionary", "game-changing", "seamlessly", "leverage"
9. Do use: "build", "ship", "connect", "self-host", "control"

For Tier A: Offer a quick call, reference specific tech in their stack
For Tier B: Link to quickstart guide and relevant templates
For Tier C/D: Keep it simple — quickstart, docs, community links

Output the email with Subject and Body clearly labeled.
```
