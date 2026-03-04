---
title: "Signal: Retool Usage Detection"
updated: 2026-03-03
status: active
---

# Signal: Retool Usage Detection

## Purpose
Identify companies currently using Retool to target with the retool-refugees segment and migration campaign.

## Detection Methods

### Job Board Signals
- **Source**: LinkedIn Jobs, Indeed, Glassdoor
- **Query**: "Retool" in job descriptions
- **Indicators**: "Experience with Retool", "Build internal tools using Retool", "Retool admin"
- **Frequency**: Weekly scan

### Tech Stack Databases
- **Source**: BuiltWith, Wappalyzer, StackShare
- **Query**: Companies with Retool in their stack
- **Frequency**: Monthly refresh

### G2/Capterra Reviews
- **Source**: G2, Capterra review APIs
- **Query**: Recent Retool reviews mentioning pricing concerns or alternatives
- **Indicators**: Negative reviews about cost, looking for alternatives

### Community Signals
- **Source**: Reddit, Hacker News, Twitter/X
- **Query**: "Retool alternative", "Retool pricing", "Retool expensive"
- **Indicators**: Active discussions about switching

### Website Signals
- **Source**: Exa API
- **Query**: Blog posts or docs mentioning Retool in tech stack
- **Indicators**: "We use Retool for...", "Our Retool setup"

## Scoring
- Job post mentioning Retool: +10 (ICP signal)
- Retool in tech stack DB: +10 (ICP signal)
- Negative Retool review: +15 (active pain)
- Searching for alternatives: +20 (buying intent)

## Action
- Tag in CRM with `competitor_retool` property
- Assign to `retool-refugees` segment
- Route to `retool-migration` campaign
