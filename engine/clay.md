---
title: Clay Enrichment Setup
updated: 2026-03-03
status: draft
---

# Clay Enrichment Configuration

## Overview
Clay is the primary enrichment tool for processing new signups and building account intelligence.

## Tables

### Signup Enrichment Table
Triggered by new signup webhook. Processes one contact at a time.

**Input Columns**:
| Column | Type | Source |
|--------|------|--------|
| email | string | Signup webhook |
| signup_date | datetime | Signup webhook |
| domain | string | Extracted from email |

**Enrichment Columns (Waterfall)**:
| Column | Type | Sources (in priority order) |
|--------|------|---------------------------|
| company_name | string | Clearbit → LinkedIn → Domain |
| employee_count | number | Clearbit → LinkedIn → Crunchbase |
| industry | string | Clearbit → LinkedIn |
| tech_stack | array | BuiltWith → Wappalyzer → StackShare |
| funding_total | number | Crunchbase → PitchBook |
| funding_stage | string | Crunchbase → PitchBook |
| company_linkedin | url | Clearbit → Google |
| full_name | string | Clearbit → LinkedIn → Hunter |
| title | string | Clearbit → LinkedIn |
| seniority | string | Clearbit → LinkedIn |
| person_linkedin | url | Clearbit → LinkedIn → Hunter |
| phone | string | Clearbit → ZoomInfo |
| location | string | Clearbit → LinkedIn |

**Computed Columns**:
| Column | Type | Logic |
|--------|------|-------|
| is_personal_email | boolean | Domain in personal email list |
| has_engineering_team | boolean | employee_count > 10 AND tech signals detected |
| icp_score | number | Scoring model applied to enrichment data |
| icp_tier | string | A/B/C/D based on score |
| primary_segment | string | Segment matching logic |

### Company Research Table
For deeper research on high-priority accounts.

**Input**: Company domain
**Enrichment**: Full company profile + recent news + job posts + tech stack deep dive

## Waterfall Configuration

### Company Enrichment Waterfall
1. **Clearbit** (primary): Company firmographics, tech stack
2. **LinkedIn** (fallback): Company size, industry
3. **Crunchbase** (funding): Funding data, investors
4. **BuiltWith** (tech): Detailed technology stack

### Person Enrichment Waterfall
1. **Clearbit** (primary): Name, title, seniority
2. **LinkedIn** (fallback): Profile data
3. **Hunter** (email verification): Email validity

## API Integration
- Clay API endpoint: `https://api.clay.com/v3`
- Authentication: Bearer token
- Rate limits: Check current plan limits
- Webhook: Configure for real-time signup processing

## Setup Checklist
- [ ] Create Clay account and get API key
- [ ] Build Signup Enrichment table with columns above
- [ ] Configure waterfall sources
- [ ] Set up webhook trigger for new signups
- [ ] Test enrichment with sample signups
- [ ] Configure CRM push (HubSpot integration)
- [ ] Set up error handling for failed enrichments
