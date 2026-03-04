---
title: Analyze Sales Call
updated: 2026-03-03
status: active
---

# /analyze-call — Analyze a Sales Call Transcript

## Steps

1. **Read the transcript**: Ingest the full call transcript (from Gong, Fireflies, or pasted text).

2. **Extract structured data**:
   - **Buyer role**: Title, seniority, department, decision-making authority
   - **Company context**: Size, industry, tech stack mentioned, current tools
   - **Pain points**: Specific problems articulated (rank by emphasis)
   - **Objections raised**: Concerns, pushbacks, hesitations
   - **Competitors mentioned**: Any alternative tools discussed
   - **Buying signals**: Timeline mentions, budget discussions, stakeholder references
   - **Notable quotes**: Verbatim quotes that capture pain, excitement, or objections
   - **Next steps**: What was agreed upon

3. **Create analysis file**: Save to `demand/pull-analyses/{id}.md` with all extracted data structured under clear headings:
   - Call Metadata (date, participants, duration, stage)
   - Key Pain Points
   - Objections Raised
   - Competitors Mentioned
   - Notable Quotes
   - Signals (buying intent indicators)
   - Recommended Follow-up

4. **Update pull index**: Add entry to `demand/pull-analyses/pull-index.json` with id, date, company, buyer_role, stage, tags, and file reference.

5. **Flag updates needed**: Check if any findings should update:
   - `demand/buyer-insights.md` — new pain points or buying triggers
   - `demand/competitors.md` — new competitive intelligence
   - `messaging/objections.md` — new objections or improved responses
   - `segments/` — evidence supporting or challenging segment definitions

## Output Format
Provide a summary with: 3 key takeaways, recommended next action, and any intelligence updates needed.
