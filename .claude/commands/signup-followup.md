---
title: Signup Follow-up
updated: 2026-03-03
status: active
---

# /signup-followup — Process New Signups

## Steps

1. **Pull signup data**: Ingest new signup data from the source:
   - Webhook payload (real-time)
   - CRM export (batch)
   - CSV upload (manual)
   Required fields: email, signup_date. Optional: name, company, role.

2. **Enrich via Clay**: For each signup, call the enrichment pipeline:
   - Company: domain, size, industry, tech stack, funding, LinkedIn URL
   - Person: full name, title, seniority, LinkedIn profile, location
   - Use `scripts/process_signups.py` or `agents/actions/enrich_signup.py`

3. **Score and segment**: Apply ICP scoring model from `agents/scoring/icp-scoring-model.md`:
   - Calculate total score based on enrichment data
   - Assign tier: A (60+), B (30-59), C (10-29), D (<10)
   - Match to primary segment from `segments/segments.json`

4. **Route to agent playbook**: Based on tier and segment:
   - Tier A: Route to signup-welcomer with high-touch playbook
   - Tier B: Route to signup-welcomer with standard playbook
   - Tier C/D: Route to signup-welcomer with low-touch playbook
   - If existing customer domain detected: route to expansion-spotter

5. **Queue first touch**: Trigger the appropriate welcome email:
   - Prepare personalization variables from enrichment data
   - Select email template based on tier and segment
   - Queue via sequencer (Lemlist) or direct send
   - Log action in `agents/action-log.json`

6. **Slack alert** (Tier A only): Send formatted alert to sales channel with:
   - Contact name, title, company
   - Company size, industry, tech stack
   - ICP score and tier
   - Recommended next action

## Batch Processing
For CSV uploads with multiple signups:
- Process sequentially to respect API rate limits
- Generate summary report: total processed, tier distribution, errors
- Log batch in action-log.json with batch_id
