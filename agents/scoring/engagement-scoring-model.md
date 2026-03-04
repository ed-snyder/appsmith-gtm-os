---
title: Engagement Scoring Model
updated: 2026-03-03
status: active
---

# Engagement Scoring Model

Tracks prospect engagement across marketing and sales touchpoints. Used to prioritize outreach and measure campaign effectiveness.

## Email Engagement

| Signal | Criteria | Points | Decay |
|--------|----------|--------|-------|
| Email opened | Single open | +2 | -1 after 7 days |
| Email opened | Multiple opens (same email) | +5 | -2 after 7 days |
| Link clicked | Clicked link in email | +10 | -3 after 14 days |
| Email replied | Positive reply | +25 | None |
| Email replied | Negative reply / objection | +10 | None |
| Email replied | Unsubscribe request | -50 | None |
| Meeting booked | Via email CTA | +50 | None |

## Website Engagement

| Signal | Criteria | Points | Decay |
|--------|----------|--------|-------|
| Pricing page visit | Single visit | +15 | -5 after 14 days |
| Pricing page visit | Multiple visits | +25 | -5 after 14 days |
| Documentation visit | Technical docs browsed | +5 | -2 after 14 days |
| Self-hosting docs | Visited self-host guides | +10 | -3 after 14 days |
| Blog content | Read 2+ articles | +5 | -2 after 14 days |
| Template gallery | Browsed templates | +8 | -3 after 14 days |
| Comparison page | Visited vs. competitor page | +15 | -5 after 14 days |
| Sign up page | Visited but didn't sign up | +20 | -10 after 7 days |

## LinkedIn Engagement

| Signal | Criteria | Points | Decay |
|--------|----------|--------|-------|
| Connection accepted | Accepted LinkedIn request | +10 | None |
| Message reply | Replied to LinkedIn message | +20 | None |
| Profile viewed | Viewed sender's profile | +5 | -2 after 14 days |
| Content engaged | Liked/commented on Appsmith post | +8 | -3 after 14 days |

## Content Engagement

| Signal | Criteria | Points | Decay |
|--------|----------|--------|-------|
| Webinar registered | Registered for event | +15 | -5 after 30 days |
| Webinar attended | Actually attended | +25 | -5 after 30 days |
| Case study downloaded | Downloaded PDF | +10 | -3 after 14 days |
| Template used | Forked a template | +15 | -5 after 30 days |
| Community joined | Joined Discord/forum | +10 | None |

## Engagement Tiers

| Tier | Score Range | Interpretation |
|------|------------|----------------|
| Hot | 50+ | Actively evaluating, ready for outreach |
| Warm | 25-49 | Interested, needs nurturing |
| Cool | 10-24 | Aware, low engagement |
| Cold | <10 | Minimal engagement |

## Score Decay
- Engagement scores decay over time to reflect recency
- Decay is applied daily based on the rules above
- Actions with "None" decay are permanent (meeting booked, reply received)
- Maximum decay reduces a signal to 0, never negative

## Integration with Lead Scoring
- Engagement score is combined with ICP score and PQL score for total lead priority
- High engagement + high ICP = immediate action
- High engagement + low ICP = investigate (may be wrong ICP assumptions)
- Low engagement + high ICP = different channel or angle needed
