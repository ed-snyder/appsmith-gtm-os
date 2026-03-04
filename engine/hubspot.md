---
title: HubSpot CRM Configuration
updated: 2026-03-03
status: draft
---

# HubSpot CRM Configuration

## Overview
HubSpot is the CRM backbone. All agent actions flow through HubSpot for contact management, lifecycle tracking, and reporting.

## Custom Properties

### Contact Properties
| Property | Type | Group | Description |
|----------|------|-------|-------------|
| icp_score | number | Scoring | ICP score from scoring model |
| icp_tier | dropdown (A/B/C/D) | Scoring | ICP tier classification |
| pql_score | number | Scoring | Product-qualified lead score |
| pql_tier | dropdown | Scoring | PQL-Hot/Warm/Early/Not PQL |
| engagement_score | number | Scoring | Multi-channel engagement score |
| primary_segment | dropdown | Segmentation | Primary buyer segment |
| enrichment_status | dropdown | Enrichment | completed/failed/pending |
| enrichment_source | string | Enrichment | Clay/manual/etc |
| tech_stack | multi-line text | Enrichment | Comma-separated tech list |
| funding_stage | dropdown | Enrichment | Seed/A/B/C/D/Public |
| agent_last_action | string | Agents | Last agent action type |
| agent_last_action_date | datetime | Agents | When last agent acted |
| agent_assigned | dropdown | Agents | Which agent owns this contact |
| signup_source | string | Product | How they signed up |
| apps_created | number | Product | Number of apps built |
| data_sources_connected | number | Product | Data sources count |
| team_members_count | number | Product | Team members invited |
| last_product_activity | datetime | Product | Last login/activity date |
| trial_start_date | datetime | Product | Business trial start |
| trial_end_date | datetime | Product | Business trial end |

### Company Properties
| Property | Type | Description |
|----------|------|-------------|
| icp_company_score | number | Company-level ICP score |
| total_appsmith_users | number | All users from this company |
| expansion_potential | dropdown | Low/Medium/High |
| agents_fit_score | number | Fit score for Appsmith Agents cross-sell |

## Lifecycle Stages
1. **Subscriber**: Signed up for newsletter/content only
2. **Lead**: Free signup, not yet qualified
3. **MQL**: Meets ICP criteria (Tier A or B)
4. **SQL**: PQL detected + sales outreach initiated
5. **Opportunity**: Active deal, demo completed
6. **Customer**: Paid plan active
7. **Evangelist**: Active customer + referral source

## Lists (Smart)
| List Name | Criteria | Agent |
|-----------|----------|-------|
| Tier A Signups | icp_tier = A, lifecycle = Lead | signup-welcomer |
| Tier B Signups | icp_tier = B, lifecycle = Lead | signup-welcomer |
| PQL Hot | pql_tier = PQL-Hot | pql-hunter |
| PQL Warm | pql_tier = PQL-Warm | pql-hunter |
| Active Trials | trial_start_date exists, trial_end_date > today | trial-nudger |
| Expansion Ready | expansion_potential = High, lifecycle = Customer | expansion-spotter |
| Inactive 30d | last_product_activity < 30 days ago | reactivation-agent |
| Agents Fit | agents_fit_score > 60, lifecycle = Customer | agents-evangelist |
| Retool Refugees | primary_segment = retool-refugees | — |

## Workflows
| Workflow | Trigger | Actions |
|----------|---------|---------|
| New Signup Processing | Contact created with signup_source | Call signup-welcomer webhook |
| PQL Escalation | pql_tier changes to PQL-Hot | Slack notification, assign AE |
| Trial Started | trial_start_date set | Enroll in trial nurture sequence |
| Trial Ending | trial_end_date = 2 days from now | Send trial ending email |
| Expansion Alert | expansion_potential changes to High | Notify CSM |

## Setup Checklist
- [ ] Create all custom properties listed above
- [ ] Configure lifecycle stages
- [ ] Build smart lists
- [ ] Set up workflows
- [ ] Configure webhook for signup-welcomer integration
- [ ] Test end-to-end flow with sample data
- [ ] Set up HubSpot API key in .env
