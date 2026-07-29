---
name: paperforge-delivery
description: Coordinate end-to-end, evidence-safe academic paper delivery from live experiment artifacts to a submission-ready manuscript, figures, tables, matched-paper review, reproducible code package, and clean final bundle. Use when a task combines two or more of experiment/result audit, literature-grounded story design, manuscript drafting or low-AI polishing, publication figures and semantic color control, Word/LaTeX/PDF layout, reviewer-style self-review, reviewer response, or final GitHub/submission packaging. Use specialist skills alone for isolated single-file edits.
---

# PaperForge Delivery

Act as the single controller for a paper-facing project. Reuse specialist skills
for narrow implementation work, but keep one PaperForge contract as the source
of truth for evidence, story, figures, layout, review, and delivery.

## Default outcome

Continue autonomously from the live project files to the strongest truthful
deliverable the evidence permits. Do not ask the user to repeat established
style, palette, folder, audit, or prose preferences.

Distinguish these states:

1. `PLANNED`: the contract or matrix exists, but work has not run.
2. `LAUNCHED`: a process exists, but result evidence is incomplete.
3. `ARTIFACT_READY`: required outputs exist and are non-empty.
4. `EVIDENCE_VERIFIED`: provenance, metrics, statistics, and claim links pass.
5. `DELIVERY_VERIFIED`: rendered files and the final package pass inspection.

Never call a paper submission-ready before state 5. If evidence is incomplete,
produce the admissible draft, figure, audit, or gap report and label the blocked
claims; never fill gaps with invented results, citations, metadata, or prose.

Ask only for truth that cannot be recovered safely from the project, such as
author order, affiliations, ethics/consent identifiers, funding, conflicts,
data permissions, or a venue choice that materially changes formatting.

## Source and workspace order

1. Resolve the active project root and canonical repository before creating or
   changing files. Verify branch, commit, remote, and working tree before GitHub
   operations.
2. Read project instructions, the machine-readable protocol, current manuscript,
   canonical result sources, figure code, review comments, and latest verified
   artifacts. Treat remembered paths and old summaries as leads, not live truth.
3. Prefer one canonical source for each number, table, figure, and claim. Report
   contradictions instead of smoothing them over.
4. Keep all project work inside the active project root. Never create a sibling
   clone, nested repository, or fallback project root.
5. Copy [paper-contract.template.json](assets/paper-contract.template.json) to a
   project-local internal work directory when no equivalent contract exists.
   Populate it from live files before drafting strong claims.

## Non-destructive file policy

- Preserve original manuscripts, data, results, figures, and Office files.
- Edit the canonical code checkout in place on its verified branch. Use Git
  history, branches, commits, tags, and release archives for versions; never
  copy an entire repository into `v2`, `v3`, `final`, or timestamped clones.
- Create a new versioned delivery folder only for a formal manuscript package,
  not for every failed attempt or intermediate artifact.
- Do not create standalone reviewer, self-review, figure, conversion, or audit
  Markdown files. Write structured findings into the existing JSON/CSV/XLSX
  audit record or one machine-readable review record per delivery cycle.
- Do not create `*.tmp`, `*.temp`, `*.bak`, `*.swp`, or nested `tmp/`, `temp/`,
  `scratch/`, `preview/`, or timestamped worktrees. If transient computation is
  unavoidable, use one ignored project-local `work/` directory, keep it flat,
  use machine-readable/log files rather than Markdown, and remove it after
  validation. Final delivery and code packages must contain none of these.
- Maintain at most one paper contract, one claim/evidence map, one literature
  benchmark table, one figure registry, one caption audit, and one final audit
  record per delivery cycle.
- If Word, PowerPoint, or Excel is open, do not quit or kill it. Work on copies
  when conversion or automation could touch an active file.

Read [document-layout-delivery.md](references/document-layout-delivery.md) before
creating a folder layout, Word/LaTeX/PDF/PPT output, code package, GitHub release,
or submission bundle.

## End-to-end workflow

### 1. Freeze the paper contract

Record the scientific question, decision/prediction unit, information boundary,
primary claim, primary comparison, primary outcomes, canonical protocol,
split/test boundary, seeds/folds/regions/horizons, code commit, data/config
fingerprints, target venue status, and expected final artifacts.

Do not silently replace the user's mainline with a new module stack, baseline,
or project direction. Classify every route as mainline, baseline, ablation,
robustness, or future work.

### 2. Pass the experiment-to-claim gates

Read [evidence-experiment-gates.md](references/evidence-experiment-gates.md).
Audit protocol/code/evaluator agreement, data and split integrity, feature
availability, formal route completeness, raw per-run retention, locked-test
discipline, statistics, negative results, and claim traceability.

Treat syntax checks, CI, smoke tests, PIDs, logs, checkpoints, and GPU use as
engineering evidence only. Formal paper evidence requires verified result
artifacts and the prescribed evaluation.

### 3. Build the matched literature benchmark

Read [matched-paper-review.md](references/matched-paper-review.md). Before final
story approval or reviewer-style self-review, inspect 20 verified published
papers matched by task, article type, evidence family, validation depth, and
venue level. Freeze inclusion rules before using the papers to defend a claim.

Use cohort prevalence to calibrate relative review priority only after hard
integrity gates pass. Common practice never waives ethics, leakage, statistical
validity, citation truth, privacy, or current venue requirements.

### 4. Lock one falsifiable story

Read [writing-story-contract.md](references/writing-story-contract.md).
Establish one decision problem, one unresolved gap, one primary mechanism, one
primary comparison, and one claim ceiling. Link every experiment and figure to
the claim it tests and state what result would weaken that claim.

Use this narrative order:

`observation or gap -> precise limitation -> method idea -> validation design
-> measured result -> scoped claim`

### 5. Draft from evidence

Write the title, abstract, introduction, key figures, methods, results,
discussion, limitations, conclusion, data/code availability, and supplement in
reader order appropriate to the venue. Keep Results descriptive and Discussion
interpretive. Keep ranking, calibration, threshold, robustness, and clinical or
operational claims distinct.

Apply low-AI editing only after scientific content stabilizes. Naturalness must
not add anecdotes, opinions, citations, experiments, or authorial experiences
that are absent from the evidence.

### 6. Produce figures and tables under one registry

Read [figure-color-chart-contract.md](references/figure-color-chart-contract.md).
Copy [figure-style-registry.template.json](assets/figure-style-registry.template.json)
when a project has no equivalent. Freeze semantic colors before drawing and
reuse them across every figure, table-as-figure, and slide.

Generate figures from canonical tables, predictions, or code outputs rather
than screenshots. Preserve source data and plotting code. Render at final
physical dimensions and inspect the actual output.

For every multipart figure, the registry must list the rendered panel labels and
one caption description for each label. The caption audit must confirm a
one-to-one mapping in panel order; an unexplained or extra A/B/C/D panel blocks
delivery. Panel-letter case is venue-defined and then frozen across the paper.
If no venue rule is available, use lowercase `a, b, c, ...` consistently.

### 7. Run calibrated review and compliance checks

Apply current official venue rules, the applicable reporting guideline, the
20-paper benchmark, and specialist self-review checks. Rank findings on two
axes:

- non-waivable scientific, ethical, statistical, and policy severity;
- prevalence among the 20 matched published papers.

Fix all non-waivable failures. Treat an issue absent from all 20 matched papers
but present in the target as high priority. A common issue may receive lower
comparative priority, but document it rather than calling it correct.

### 8. Package and verify

Create only:

1. a clean submission package containing the final manuscript and required
   submission assets;
2. a reproducible code package created from the canonical verified commit or
   release archive;
3. one compact provenance/audit record.

Keep plotting experiments, temporary renders, search caches, intermediate
Markdown, and failed outputs outside those packages. Run
`scripts/validate_delivery.py` against the completed contract. Render and inspect
Word/PDF/LaTeX/figures, verify hashes and cross-references, then report one exact
final delivery path.

## Specialist routing

Use only the narrowest required specialists:

- protocol/results first: `project-protocol-result-audit`, `results-auditor`,
  `result-reliability-checker`, `results-analysis`, `statistical-analysis`;
- literature/evidence: `evidence-ranker`, `evidence-level-ranker`, literature
  collection skills, and live primary-source search;
- manuscript prose: `scientific-writing`, `ml-paper-writing`,
  `review-safe-paper-polish`, `paper-polish`;
- constrained low-AI language: `bilingual-anti-ai-writing` or
  `writing-anti-ai`; do not use generic humanization that invents personality;
- figures: `academic-plotting` or `figure-style-studio`;
- file formats: the available Word/document, spreadsheet, presentation,
  LaTeX, or PDF specialist;
- final review: `reporting-guideline-compliance-checker`,
  `paper-self-review`, `peer-review-check`;
- revision: `reviewer-response` or `review-response`.

The canonical order is:

`audit -> statistics -> literature -> story -> writing -> figures/layout ->
reporting compliance -> matched review -> polish -> delivery audit`

## Final acceptance contract

Do not deliver until all applicable checks pass or are explicitly marked
blocked:

- one canonical root, repository, protocol, result source, and output path;
- formulas, names, splits, metrics, units, and counts agree everywhere;
- every primary claim links to a verified artifact or inspected source;
- every declared run, seed, failure, null, and unfavorable result is retained;
- the main table contains only scoped primary evidence; secondary and negative
  evidence remains traceable in the supplement or audit workbook;
- figures use the frozen semantic registry and pass final-size visual review;
- the current venue and reporting requirements are verified;
- the 20-paper benchmark is complete or has a documented genuine shortfall;
- originals are unchanged, temporary files are removed, and final files render;
- the submission and code packages contain no stale drafts, generated review
  Markdown, scratch Markdown, `*.tmp` files, temporary directories, failed
  outputs, caches, credentials, private data, or nested repositories;
- every multipart figure has an audited one-to-one caption mapping for all
  rendered panel letters;
- the final response gives the exact paths, validation results, commit/hash, and
  any remaining author-supplied truth or unsupported claim.

Read [domain-overrides.md](references/domain-overrides.md) only when medical,
ophthalmic, coastal, spatiotemporal, or remote-GPU specifics apply.
