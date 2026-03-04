---
title: PQL Scoring Model
updated: 2026-03-03
status: active
---

# Product-Qualified Lead Scoring Model

PQL scoring is based entirely on product usage signals. Combined with ICP score for total lead prioritization.

## Usage Signals

| Signal | Criteria | Points |
|--------|----------|--------|
| Apps created | 3-4 apps | +20 |
| Apps created | 5-9 apps | +30 |
| Apps created | 10+ apps | +40 |
| Data sources | 2-3 connected | +15 |
| Data sources | 4+ connected | +25 |
| Team members | 3-4 invited | +15 |
| Team members | 5 (at free limit) | +25 |
| Team members | Attempted 6+ (hit limit) | +30 |
| Last active | Within 3 days | +20 |
| Last active | Within 7 days | +10 |
| Last active | 8-14 days | +5 |
| Last active | 15+ days | +0 |

## Feature Adoption Signals

| Signal | Criteria | Points |
|--------|----------|--------|
| API queries | >100/week | +15 |
| API queries | >500/week | +25 |
| Custom widgets | Created at least 1 | +10 |
| JS objects | Created at least 1 | +10 |
| Git integration | Enabled | +15 |
| Workflow attempt | Tried Business feature (gated) | +20 |
| RBAC attempt | Tried custom roles (gated) | +15 |
| Audit log search | Searched for audit logs (gated) | +10 |
| SSO attempt | Tried SSO configuration (gated) | +15 |

## Engagement Velocity Signals

| Signal | Criteria | Points |
|--------|----------|--------|
| Login frequency | Daily for 5+ days | +15 |
| Login frequency | 3-4 times/week | +10 |
| App edits | 5+ edits in last 7 days | +10 |
| New app created | In last 3 days | +10 |
| Team member added | In last 7 days | +10 |

## PQL Tiers

| Tier | Score Range | Action | Autonomy |
|------|------------|--------|----------|
| PQL-Hot | 80+ | Immediate personalized outreach | Human-in-loop |
| PQL-Warm | 50-79 | Standard outreach sequence | Human-in-loop |
| PQL-Early | 30-49 | Add to nurture, monitor | Full auto |
| Not PQL | <30 | Continue standard nurture | Full auto |

## Combined Score (ICP + PQL)

For total lead prioritization, combine ICP score and PQL score:

| ICP Tier | PQL Tier | Priority | Action |
|----------|----------|----------|--------|
| A | Hot | Critical | Immediate AE outreach, Slack alert |
| A | Warm | High | AE outreach within 24 hours |
| A | Early | Medium | Nurture with AE awareness |
| B | Hot | High | AE outreach within 24 hours |
| B | Warm | Medium | Standard outreach sequence |
| B | Early | Low | Automated nurture |
| C/D | Hot | Medium | Standard outreach (usage-led) |
| C/D | Warm | Low | Automated nurture |
| C/D | Early | Minimal | Community nurture only |

## Recalculation Schedule
- PQL scores are recalculated every 6 hours
- Significant score changes (>20 point increase) trigger immediate re-evaluation
- Accounts that cross tier thresholds upward are flagged immediately
