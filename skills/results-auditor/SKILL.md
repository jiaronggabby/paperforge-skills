---
name: results-auditor
description: Audit experimental results, tables, metrics, splits, baselines, ablations, statistical tests, figures, and manuscript claims against source files. Use when the user asks whether results can be trusted, why a table looks wrong, whether claims match code/results, how to rebuild final tables, or how to interpret significance, confidence intervals, seeds, folds, regions, or horizons.
---

# Results Auditor

Use this skill before writing strong claims from experimental outputs.

## Workflow

1. Identify the result contract.
   - Task, dataset, split, metric, horizon, seed/fold, baseline set, ablation
     structure, and expected output files.

2. Find authoritative sources.
   - Prefer raw result CSV/XLSX/JSON/log exports and code that computes metrics.
   - Treat copied tables, screenshots, and manuscript text as secondary unless
     the user explicitly marks them canonical.

3. Audit consistency.
   - Check sample counts, split definitions, baseline names, metric direction,
     missing runs, duplicate rows, non-finite values, and unit conversions.
   - Compare figure values, table values, and prose claims.
   - Verify statistical tests match the data structure.

4. Assess reliability.
   - Separate descriptive wins from statistically supported wins.
   - Flag leakage, overfitting, cherry-picked seeds, weak baselines, and
     unsupported generalization.
   - Mark unresolved issues instead of smoothing them into polished language.

5. Produce an audit summary.
   - State what is trustworthy.
   - State what is incomplete or fragile.
   - List exact files, commands, or tables used as evidence.
   - Recommend the minimal rerun, rebuild, or wording change needed.

## Hard rules

- Do not fabricate missing metrics, p-values, confidence intervals, or runs.
- Do not treat internal validation as external generalization.
- Do not call a result robust because it looks visually large.
- If the evidence is incomplete, label the claim as unresolved.
