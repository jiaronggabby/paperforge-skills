---
name: evidence-ranker
description: Rank papers, citations, and evidence sources by methodological strength, validation depth, relevance, and claim support. Use when the user asks which papers to cite first, how to prioritize literature, whether a source can support a strong claim, or how to compare reviews, trials, cohorts, mechanism studies, omics papers, and ML validation papers.
---

# Evidence Ranker

Use this skill to decide which sources deserve strong citation roles and which
should be used only for context.

## Workflow

1. Define the ranking purpose.
   - Background framing, central claim support, mechanism support, method
     comparison, clinical evidence, benchmark evidence, or cautionary context.

2. Identify the true evidence family.
   - Systematic review/meta-analysis
   - Randomized or non-randomized intervention
   - Cohort, case-control, cross-sectional, registry, or real-world evidence
   - Diagnostic/prognostic/predictive validation
   - Mechanism, animal, cell, omics, computational, or benchmark study

3. Judge execution quality.
   - Sampling logic, confounding control, outcome definition, comparator choice,
     statistical handling, multiplicity, calibration, validation, transparency,
     and reproducibility.

4. Judge validation depth.
   - No validation
   - Internal split/resampling
   - External cohort
   - Orthogonal confirmation
   - Independent replication
   - Prospective or implementation-level support

5. Assign citation role.
   - Anchor citation
   - High-value support citation
   - Context-setting citation
   - Mechanistic support citation
   - Caution citation

## Rules

- Do not rank by journal prestige alone.
- Do not treat statistical significance as reliability.
- Do not treat internal validation as generalizability.
- Do not fabricate publication metadata, DOIs, PMIDs, sample sizes, or validation
  claims.
- If bibliographic details are unverified, mark them as unverified.
