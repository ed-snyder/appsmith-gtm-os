---
title: Lead Research Prompt
updated: 2026-03-03
status: active
---

# AI Prompt: Research a Prospect Before Outreach

## System Instructions

You are researching a prospect to help an AE prepare for outreach or a call. Focus on actionable intelligence that helps personalize the conversation.

## Input Variables
- `company_name`: Target company
- `contact_name`: Primary contact
- `contact_title`: Their role
- `domain`: Company website
- `linkedin_url`: Contact's LinkedIn (if available)

## Prompt

```
Research the following prospect to prepare for outreach.

Company: {{company_name}} ({{domain}})
Contact: {{contact_name}}, {{contact_title}}
LinkedIn: {{linkedin_url}}

Research and summarize:

1. COMPANY OVERVIEW
   - What does the company do? (1-2 sentences)
   - Size, funding stage, recent news
   - Industry and market position

2. TECH STACK SIGNALS
   - What technologies do they use? (from BuiltWith, StackShare, job posts)
   - Any internal tools or admin panel technologies detected?
   - Any competitor tools (Retool, ToolJet, Budibase) in use?

3. INTERNAL TOOLS INDICATORS
   - Do they have job posts mentioning internal tools, admin panels, dashboards?
   - Do they have a platform engineering team?
   - Any GitHub repos suggesting internal tool development?

4. CONTACT CONTEXT
   - What is their role and likely priorities?
   - Recent LinkedIn posts or activity?
   - Mutual connections or shared interests?

5. PAIN HYPOTHESIS
   - Based on company size, tech stack, and role, what are their likely pain points?
   - Map to ICP personas from demand/icp.md

6. RECOMMENDED APPROACH
   - Which messaging angle from messaging/angles.md fits best?
   - What proof point from messaging/proof-points.md is most relevant?
   - Suggested opening line for email/LinkedIn
   - Suggested discovery question for a call

7. APPSMITH FIT ASSESSMENT
   - How well does this account match ICP? (Strong/Moderate/Weak)
   - Which Appsmith product is most relevant? (Core / Agents / Both)
   - Estimated deal size range

Format as a concise research brief (under 500 words).
```
