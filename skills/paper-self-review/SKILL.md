---
name: paper-self-review
description: Perform a pre-submission self-review of an academic manuscript, thesis chapter, conference paper, journal article, or revision package. Use when the user asks to check paper quality, submission readiness, structure, novelty, method clarity, result support, figures, tables, citations, limitations, or reviewer risk before submission.
---

# Paper Self Review

Use this skill as a final author-side review before submission.

## Review checklist

1. Contribution
   - Is the main problem clear?
   - Is the contribution specific rather than generic?
   - Does the title/abstract match the real method and evidence?

2. Method
   - Are inputs, outputs, assumptions, and algorithms clear enough to reproduce?
   - Are baselines and ablations justified?
   - Are implementation details placed where readers can find them?

3. Results
   - Do tables and figures answer the stated research questions?
   - Are metric names, directions, units, and sample counts clear?
   - Are statistical claims supported by the reported analysis?

4. Figures and tables
   - Are labels readable?
   - Are captions self-contained?
   - Is the visual style consistent?
   - Is every main figure/table discussed in the text?

5. Claims and limitations
   - Are claims scoped to tested data, settings, and validation?
   - Are limitations honest but not repetitive?
   - Are future-work statements specific?

6. Citations
   - Are key related works present?
   - Are factual claims source-backed?
   - Are references real and correctly formatted?

## Output

Return:

- readiness verdict;
- top risks;
- concrete revision actions;
- claim/evidence mismatches;
- figure/table issues;
- citation or formatting issues.
