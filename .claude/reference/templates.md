---
title: GTM Templates
updated: 2026-03-03
status: active
---

# Common Templates

## Email Templates

### Cold Outreach Email
```
Subject: {{subject_line}}

Hi {{first_name}},

{{opening_line_personalized_to_their_situation}}

{{one_sentence_about_the_problem}}

{{one_sentence_about_how_appsmith_solves_it}}

{{proof_point_from_messaging/proof-points.md}}

{{cta_question}}

{{sender_name}}
```

### Welcome Email (Tier A)
```
Subject: {{first_name}}, your Appsmith instance is ready

Hi {{first_name}},

Welcome to Appsmith. I saw that {{company_name}} is {{relevant_observation_from_enrichment}} — that's exactly the kind of team that gets the most out of the platform.

Teams like yours typically start by building {{relevant_use_case_for_their_industry}}. Here's a template to get you started: {{template_link}}

I work with {{industry}} teams using Appsmith. Happy to do a quick 15-minute walkthrough of how {{similar_company}} set up their internal tools.

Worth a chat this week?

{{sender_name}}
```

### Welcome Email (Tier B)
```
Subject: Get started with Appsmith in 10 minutes

Hi {{first_name}},

Welcome to Appsmith. Here's how to build your first internal tool in under 10 minutes:

1. Connect your data source: {{quickstart_link}}
2. Try a template: {{template_link}}
3. Invite your team: {{invite_link}}

Most teams start with a simple admin panel or dashboard and go from there.

Questions? Reply to this email or join our community: {{community_link}}

{{sender_name}}
```

### Welcome Email (Tier C/D)
```
Subject: Welcome to Appsmith

Hi {{first_name}},

Welcome to Appsmith! Here are your next steps:

- Quickstart guide: {{quickstart_link}}
- Documentation: {{docs_link}}
- Community: {{community_link}}
- Templates: {{templates_link}}

Happy building!

The Appsmith Team
```

### PQL Outreach Email
```
Subject: {{first_name}}, your team is building some great stuff

Hi {{first_name}},

I noticed your team at {{company_name}} has been active on Appsmith — {{specific_usage_observation}}.

Teams at your stage often benefit from {{relevant_feature_they_havent_used}}. It typically cuts {{relevant_metric}} by {{percentage}}.

Want me to show you how {{similar_company}} set this up? Takes 15 minutes.

{{sender_name}}
```

### Trial Expiry Reminder
```
Subject: Your Appsmith Business trial ends in {{days_remaining}} days

Hi {{first_name}},

Your Business plan trial wraps up on {{expiry_date}}. Here's what you'll lose access to:

- {{feature_1_they_used}}
- {{feature_2_they_used}}
- {{feature_3_they_used}}

Your apps will still work on the free tier, but {{specific_impact_of_downgrade}}.

Want to chat about the right plan for {{company_name}}? I can also extend the trial if you need more time.

{{sender_name}}
```

## LinkedIn Templates

### Connection Request
```
Hi {{first_name}} — I work with {{industry}} engineering teams building internal tools. Noticed {{company_name}} is {{relevant_observation}}. Would love to connect.
```

### Follow-up Message (after connection)
```
Thanks for connecting, {{first_name}}. I saw {{company_name}} is {{relevant_observation}}. We helped {{similar_company}} {{specific_outcome}} with Appsmith. Thought it might be relevant to your team. Happy to share more if useful.
```

## Call Prep Template

### Pre-Call Research Brief
```
# Call Prep: {{company_name}}

## Company
- Industry: {{industry}}
- Size: {{employee_count}} employees
- Funding: {{funding_stage}}
- Tech stack: {{known_tech}}

## Contact
- Name: {{full_name}}
- Title: {{title}}
- LinkedIn: {{linkedin_url}}
- Previous interactions: {{interaction_history}}

## Hypothesized Pain Points
1. {{pain_point_1_based_on_segment}}
2. {{pain_point_2_based_on_enrichment}}

## Discovery Questions
1. How is your team currently building internal tools?
2. How much engineering time goes to internal tooling vs core product?
3. What's driving the evaluation right now?

## Relevant Proof Points
- {{proof_point_from_messaging/proof-points.md}}

## Competitive Intel
- {{any_competitor_signals_from_enrichment}}
```

## Segment Brief Template
```
# Segment: {{segment_name}}

## Definition
{{one_sentence_description}}

## Qualifying Criteria
- {{criterion_1}}
- {{criterion_2}}

## Volume
{{estimated_accounts}} accounts (source: {{source}})

## Pain Points
1. {{pain_1}}
2. {{pain_2}}

## Messaging Hooks
- {{hook_1}}
- {{hook_2}}

## Recommended Angles
Reference: messaging/angles.md — {{angle_names}}
```

## Agent Prompt Template
```
You are the {{agent_name}} for Appsmith's GTM team.

## Your Role
{{agent_description}}

## Context
- Company: Appsmith (open-source low-code platform for internal tools)
- Product: {{relevant_product_line}}
- Target: {{target_segment}}

## Instructions
{{playbook_steps}}

## Constraints
- Follow messaging/voice.md guidelines
- Only use proof points from messaging/proof-points.md
- Log all actions in agents/action-log.json
- Autonomy level: {{autonomy_level}}

## Output
{{expected_output_format}}
```
