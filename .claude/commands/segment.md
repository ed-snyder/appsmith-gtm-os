---
title: Create New Segment
updated: 2026-03-03
status: active
---

# /segment — Create a New Buyer Segment

## Steps

1. **Check existing segments**: Read `segments/segments.json` to ensure this segment doesn't already exist or overlap significantly with an existing one.

2. **Create segment file**: Create `segments/{segment-name}.md` with the following sections:
   - **Segment Definition**: One-sentence description of who this segment is
   - **Qualifying Criteria**: Firmographic, technographic, and behavioral signals that define membership
   - **Estimated Volume + Sources**: How many accounts fit this segment and where the estimate comes from
   - **Evidence**: What data supports this segment's existence (call transcripts, market research, product usage)
   - **Primary Pain Points**: Top 3-5 pain points ranked by frequency and severity
   - **Messaging Hooks**: 2-3 opening angles that resonate with this segment
   - **Recommended Angles**: Reference specific angles from `messaging/angles.md`

3. **Update segments.json**: Add an entry to `segments/segments.json` with:
   - `name`: kebab-case segment identifier
   - `status`: "draft" (until validated with data)
   - `criteria`: object with qualifying signals
   - `estimated_volume`: number
   - `priority`: "high", "medium", or "low"
   - `campaigns`: empty array (populated when campaigns target this segment)
   - `file`: filename of the segment markdown file

4. **Cross-reference**: Check if any existing campaigns or agent playbooks should target this new segment and note recommendations.

## Validation
- Does this segment represent a distinct buying situation (not just a demographic)?
- Is the estimated volume large enough to justify dedicated messaging?
- Are the qualifying criteria actionable (can we actually identify these accounts)?
