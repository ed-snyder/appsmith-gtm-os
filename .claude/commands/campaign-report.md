---
title: Campaign Report
updated: 2026-03-03
status: active
---

# /campaign-report — Generate Campaign Performance Report

## Steps

1. **Pull campaign metrics**: Read current data from `campaigns/results.json` or pull fresh data from the sequencer API (Lemlist).

2. **Calculate key metrics**:
   - Emails sent / delivered / bounced
   - Open rate (target: >40%)
   - Reply rate (target: >5%)
   - Positive reply rate
   - Meetings booked
   - Meeting show rate
   - Pipeline generated ($)
   - Cost per meeting

3. **Update results.json**: Write updated metrics to `campaigns/results.json` with timestamp.

4. **Compare to benchmarks**: Flag any metrics significantly above or below targets.

5. **Summarize learnings**:
   - Which subject lines performed best?
   - Which angles generated the most replies?
   - Which segments responded best?
   - What objections came up in replies?

6. **Write report**: Update `campaigns/{campaign-name}/learnings.md` with findings and recommendations.

7. **Recommend actions**:
   - Pause underperforming variants
   - Scale winning angles
   - Update messaging/angles.md if new insights found
   - Adjust segment targeting if response patterns suggest refinement
