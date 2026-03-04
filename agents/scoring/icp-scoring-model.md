---
title: ICP Scoring Model
updated: 2026-03-03
status: active
---

# ICP Scoring Model

Total score determines lead tier: A (60+), B (30-59), C (10-29), D (<10).

## Company Attributes

| Attribute | Criteria | Points |
|-----------|----------|--------|
| Company size | 50-199 employees | +10 |
| Company size | 200-1,000 employees (sweet spot) | +20 |
| Company size | 1,001-5,000 employees | +15 |
| Company size | 5,000+ employees | +10 |
| Company size | <50 employees | +0 |
| Revenue | $10M-$500M ARR | +5 |
| Industry | Technology | +5 |
| Industry | Financial Services | +5 |
| Industry | Healthcare | +5 |
| Industry | E-commerce | +5 |
| Industry | SaaS | +5 |
| Funding | Series A+ detected | +5 |

## Engineering Team Signals

| Attribute | Criteria | Points |
|-----------|----------|--------|
| Engineering team | 5-20 developers detected | +10 |
| Engineering team | 20+ developers detected | +15 |
| Platform engineering | Dedicated platform/internal tools team | +10 |
| Engineering hiring | Active engineering job posts | +5 |

## Tech Stack Signals

| Attribute | Criteria | Points |
|-----------|----------|--------|
| Database | PostgreSQL detected | +10 |
| Database | MongoDB detected | +10 |
| Database | MySQL detected | +8 |
| Database | Snowflake/BigQuery/Redshift | +8 |
| Backend | Node.js detected | +5 |
| Backend | REST APIs detected | +5 |
| Frontend | React detected | +10 |
| Infrastructure | Docker detected | +10 |
| Infrastructure | Kubernetes detected | +10 |
| Version control | GitHub/GitLab active usage | +5 |

## Role/Title Match

| Attribute | Criteria | Points |
|-----------|----------|--------|
| Title | Engineering Manager | +20 |
| Title | VP Engineering | +20 |
| Title | CTO | +15 |
| Title | Platform Lead/Engineer | +20 |
| Title | DevOps Lead | +15 |
| Title | Data Team Lead | +10 |
| Title | Software Engineer (individual) | +5 |
| Title | Non-technical role | +0 |

## Intent Signals

| Attribute | Criteria | Points |
|-----------|----------|--------|
| Self-hosting interest | Visited self-hosting docs or mentioned | +10 |
| Competitor usage | Using Retool (migration opportunity) | +10 |
| Compliance | SOC 2/HIPAA signals | +5 |
| AI initiative | AI hiring or AI tool evaluation | +5 |
| Internal tools | Job posts mentioning internal tools | +10 |

## Negative Signals (Deductions)

| Attribute | Criteria | Points |
|-----------|----------|--------|
| No engineering team | No developers detected | -20 |
| Consumer app focus | Building consumer-facing products only | -15 |
| No databases/APIs | No data infrastructure detected | -10 |
| Competitor employee | Works at a competing company | -100 |
| Student/hobby | Personal email, no company | -15 |

## Tier Definitions

| Tier | Score Range | Action |
|------|------------|--------|
| A | 60+ | High-touch: personalized welcome, Slack alert, AE assignment, LinkedIn outreach |
| B | 30-59 | Standard: personalized welcome email, automated nurture, PQL monitoring |
| C | 10-29 | Low-touch: standard welcome email, community nurture |
| D | <10 | Minimal: standard welcome email only |

## Scoring Notes
- Maximum theoretical score: ~150+ (perfect ICP match with all signals)
- Typical Tier A score: 65-90
- Score should be recalculated when enrichment data is updated
- Negative signals are applied after positive signals
