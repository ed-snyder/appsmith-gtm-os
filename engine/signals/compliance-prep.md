---
title: "Signal: Compliance Preparation"
updated: 2026-03-03
status: active
---

# Signal: Compliance Preparation

## Purpose
Identify companies preparing for compliance certifications (SOC 2, HIPAA, ISO 27001) where internal tool security gaps may create urgency.

## Detection Methods

### Job Board Signals
- **Roles**: "Compliance Manager", "Security Engineer", "GRC Analyst"
- **Keywords in JD**: "SOC 2", "HIPAA", "ISO 27001", "audit preparation", "compliance program"
- **Sources**: LinkedIn, Indeed

### News & PR Signals
- **Source**: Exa, Google News
- **Query**: Company name + "SOC 2" OR "compliance" OR "security certification"
- **Indicators**: Blog posts about compliance journey, PR about certification

### Vendor Signals
- **Source**: Vanta, Drata, Secureframe customer lists (where public)
- **Indicators**: Using compliance automation tools = actively pursuing certification

### Community Signals
- **Source**: Reddit, LinkedIn posts
- **Query**: "SOC 2 preparation", "audit logging", "access control audit"

## Scoring
- Compliance role hiring: +5 (ICP signal)
- SOC 2/HIPAA mentioned in job posts: +5 (compliance signal)
- Compliance tool detected (Vanta, Drata): +10 (active compliance work)
- Blog/PR about compliance journey: +10 (active compliance work)

## Action
- Tag in CRM with `compliance_prep` property
- Assign to `compliance-driven` segment
- Highlight self-hosting, RBAC, audit logs, SSO in outreach
