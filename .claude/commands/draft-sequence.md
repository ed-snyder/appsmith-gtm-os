---
title: Draft Outbound Sequence
updated: 2026-03-03
status: active
---

# /draft-sequence — Create an Outbound Sequence

## Steps

1. **Identify target segment**: Confirm which segment from `segments/segments.json` this sequence targets. Read the segment file for pain points and messaging hooks.

2. **Pull relevant angles**: Read `messaging/angles.md` and select 2-3 angles that align with the target segment's pain points.

3. **Pull proof points**: Read `messaging/proof-points.md` and select data points that support the chosen angles. Never fabricate statistics.

4. **Reference voice guidelines**: Read `messaging/voice.md` to ensure tone, vocabulary, and style match Appsmith's brand voice.

5. **Draft the sequence**: Create multi-touch sequences with A/B variants:

   ### Email Sequence (4-5 touches over 14 days)
   - **Email 1**: Problem-aware opener (lead with pain, not product)
   - **Email 2**: Social proof / case study (3 days later)
   - **Email 3**: Different angle or insight (5 days later)
   - **Email 4**: Direct value prop + CTA (3 days later)
   - **Email 5**: Breakup / last chance (3 days later)

   Each email needs: Subject line (A/B), Body, CTA, Personalization variables

   ### LinkedIn Sequence (parallel track)
   - **Connection request**: Short, relevant note
   - **Follow-up message**: After connection accepted, reference their specific situation
   - **Content share**: Share relevant Appsmith content

6. **Save drafts**: Write to `campaigns/{campaign-name}/sequence-drafts.md`

## Quality Checklist
- [ ] Subject lines under 50 characters
- [ ] Body under 150 words per email
- [ ] Each email has exactly one CTA
- [ ] Personalization variables marked with {{variable}}
- [ ] No buzzwords from the messaging/voice.md avoid list
- [ ] Proof points sourced from messaging/proof-points.md
