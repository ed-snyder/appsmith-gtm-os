---
title: Lemlist Sequencer Configuration
updated: 2026-03-03
status: draft
---

# Lemlist Email Sequencer Configuration

## Overview
Lemlist handles all automated email sequences triggered by sales agents.

## Sender Accounts

| Account | Email | Warmup Status | Daily Limit |
|---------|-------|---------------|-------------|
| TBD | TBD | Not started | 50 (warmup) → 200 (warmed) |

## Warmup Plan
1. **Week 1-2**: 10 emails/day, gradual increase
2. **Week 3-4**: 30 emails/day
3. **Week 5+**: 50-200 emails/day (based on reputation)
4. Monitor deliverability weekly

## Active Campaigns

| Campaign ID | Name | Segment | Agent | Status |
|-------------|------|---------|-------|--------|
| TBD | Signup Welcome (Tier A) | All Tier A | signup-welcomer | Planning |
| TBD | Signup Welcome (Tier B) | All Tier B | signup-welcomer | Planning |
| TBD | PQL Hot Outreach | PQL-Hot | pql-hunter | Planning |
| TBD | PQL Warm Sequence | PQL-Warm | pql-hunter | Planning |
| TBD | Trial Nurture | Active Trials | trial-nudger | Planning |
| TBD | Retool Migration | retool-refugees | — | Planning |
| TBD | Agents Launch | ai-agent-adopters | — | Planning |

## Campaign Settings
- **Tracking**: Open tracking ON, click tracking ON
- **Unsubscribe**: Auto-include unsubscribe link
- **Timezone**: Send in recipient's timezone
- **Send window**: 8am-6pm recipient local time, weekdays only
- **Reply detection**: Auto-pause sequence on reply
- **Bounce handling**: Auto-remove on hard bounce

## Integration with Agents
- Agents add leads to campaigns via Lemlist API
- Campaign ID is referenced in agent playbooks
- Reply notifications trigger Slack alerts for human follow-up
- Delivery stats pulled daily by `scripts/pull_lemlist_stats.py`

## Setup Checklist
- [ ] Create Lemlist account
- [ ] Add sender email accounts
- [ ] Start email warmup
- [ ] Create campaign shells for each sequence
- [ ] Configure tracking and unsubscribe settings
- [ ] Set up API key in .env
- [ ] Test API integration with `agents/actions/send_sequence_email.py`
