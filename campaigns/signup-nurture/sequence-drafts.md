---
title: "Signup Nurture Campaign — Sequence Drafts"
updated: 2026-03-03
status: draft
---

# Signup Nurture Sequence Drafts

**Target Segment**: free-to-paid
**Primary Angle**: You've outgrown free
**Voice Reference**: messaging/voice.md
**Agent Owner**: signup-welcomer, trial-nudger

## Upgrade Trigger Sequence

Triggered when free users approach plan limits (5 users, feature gates).

### Email 1 — Value Recognition (Trigger Day)

**Subject A**: "Your team is building great stuff on Appsmith"
**Subject B**: "{{app_count}} apps and counting"

Hi {{first_name}},

Your team at {{company_name}} has built {{app_count}} apps on Appsmith — that's real adoption.

A few things that could help your team move faster:
- **Workflows**: Automate multi-step processes
- **Custom roles**: Granular permissions per app and page
- **Audit logs**: Track every change for compliance

These are all on the Business plan at $15/user/month.

Want a quick walkthrough of what unlocks?

{{sender_name}}

---

### Email 2 — Feature Highlight (Day 3)

**Subject A**: "The feature your {{app_count}} apps are missing"
**Subject B**: "Workflows would save {{company_name}} time"

Hi {{first_name}},

Most teams your size start needing workflows — automating data syncs, approval chains, and scheduled tasks without writing cron jobs.

Here's a 2-minute video of how it works: {{workflow_video_link}}

Business plan starts at $15/user/month. Want to try it free for 15 days?

{{sender_name}}

---

### Email 3 — Trial Offer (Day 7)

**Subject A**: "15 days of Business — on us"
**Subject B**: "Try workflows and RBAC free"

Hi {{first_name}},

I can set up a 15-day Business trial for {{company_name}} — no credit card needed.

Your team keeps everything they've built, and you unlock:
- Workflows for automation
- Custom roles and RBAC
- Audit logging
- Custom branding

Reply "yes" and I'll activate it today.

{{sender_name}}
