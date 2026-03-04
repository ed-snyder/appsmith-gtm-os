---
title: Call Analysis Prompt
updated: 2026-03-03
status: active
---

# AI Prompt: Analyze Sales Call Transcript

## System Instructions

You are analyzing a sales call transcript to extract structured intelligence for the GTM team. Be thorough, objective, and precise. Use direct quotes where possible.

## Prompt

```
Analyze the following sales call transcript and extract structured intelligence.

Transcript:
{{transcript}}

Extract the following:

1. CALL METADATA
   - Participants (names, titles, roles)
   - Call type (discovery, demo, evaluation, negotiation)
   - Duration estimate
   - Overall sentiment (positive, neutral, negative)

2. KEY PAIN POINTS (rank by emphasis, max 5)
   - What specific problems did the buyer articulate?
   - How severe does each pain point seem?
   - Include direct quotes where possible

3. OBJECTIONS RAISED (max 5)
   - What concerns or pushbacks came up?
   - Were they addressed? How well?
   - Map to known objections from messaging/objections.md if applicable

4. COMPETITORS MENTIONED
   - Which tools were discussed?
   - What was said about them (positive or negative)?
   - Any switching signals?

5. BUYING SIGNALS
   - Timeline mentions ("by Q2", "next month", etc.)
   - Budget discussions
   - Stakeholder references ("I need to check with my CTO")
   - Process mentions ("we're evaluating 3 vendors")
   - Enthusiasm indicators

6. NOTABLE QUOTES (max 5)
   - Verbatim quotes that capture pain, excitement, or objections
   - These will be used for messaging and sales enablement

7. RECOMMENDED FOLLOW-UP
   - What should happen next?
   - What materials should be sent?
   - Who else should be involved?
   - Any urgency signals?

8. INTELLIGENCE UPDATES
   - Should buyer-insights.md be updated?
   - Should competitors.md be updated?
   - Should objections.md be updated?
   - Any new segment evidence?

Format as structured markdown with clear headings.
```
