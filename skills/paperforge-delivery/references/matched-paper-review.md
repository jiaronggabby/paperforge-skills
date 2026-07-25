# Twenty-Paper Matched Review

Use this workflow before final story approval, reviewer-style self-review, or a
submission-readiness verdict.

## Purpose

Calibrate the target manuscript against 20 verified published papers that a
reasonable reviewer would regard as comparable in level and evidence burden.
Use the cohort to separate unusual manuscript-specific weaknesses from common
field presentation choices.

Do not use the cohort to excuse scientific invalidity or to cherry-pick weak
precedents.

## Freeze the benchmark question

Record before searching:

- target venue or venue level;
- article type;
- scientific task and evidence family;
- population or data setting;
- prediction/decision and input units;
- validation depth;
- primary comparator and endpoint;
- publication window;
- review questions to calibrate.

Use current official publisher or venue sources for publication status and
requirements.

## Select the 20 papers

### Matching priority

Rank candidates by:

1. same scientific question and evidence family;
2. same article type and comparable venue level;
3. same population/data setting and information boundary;
4. same prediction/decision and input unit;
5. comparable validation depth and split design;
6. matched comparator and metric;
7. comparable cohort scale and uncertainty reporting;
8. implementation or mechanism similarity.

Headline performance is the last matching criterion, not the first.

### Inclusion rules

Include only papers with:

- verified published or formally accepted status;
- accessible primary text or sufficient official supplementary evidence;
- a defensible match rationale;
- independent publication identity after DOI/title deduplication;
- enough methodological detail to answer the review questions.

Prefer recent work, but retain older landmark papers when they define the
evaluation standard.

### Exclusion rules

Exclude:

- search snippets, unverified summaries, and LLM-generated bibliographies;
- duplicate versions, mirrors, forks, or conference/journal duplicates counted
  twice;
- preprints or under-review work when the benchmark is intended to represent
  published acceptance standards;
- papers chosen only because they support the desired narrative;
- adjacent tasks that cannot answer the calibrated question.

If fewer than 20 eligible papers exist after a documented high-recall search,
report the genuine shortfall and use all eligible papers. Do not pad the cohort
with incomparable work.

## Record the search

Copy
[matched-paper-benchmark.template.csv](../assets/matched-paper-benchmark.template.csv)
to the project internal work area. Record:

- search date, database/source, and exact query family;
- screening and deduplication counts;
- inclusion/exclusion reason;
- DOI/URL, publication status, venue, level, article type, and year;
- task, population, units, split, comparator, validation, metric, uncertainty;
- claim supported, limitations, issue tags, and verification status.

Inspect the paper and supplement. Cite only sources actually inspected.

## Extract review features

For each paper, record whether and how it handles:

- title and abstract structure;
- stated gap and novelty scope;
- mainline story and number of contributions;
- data provenance, sample/unit counts, and exclusions;
- split and leakage controls;
- baseline strength and matching;
- seed/fold/repeat reporting;
- locked-test or external validation;
- uncertainty, effect sizes, paired tests, and multiplicity;
- calibration and operating-point evidence;
- negative, null, or contradictory results;
- ablations and mechanism tests;
- number, type, and density of main figures/tables;
- caption completeness and visual conventions;
- limitations, ethics, data/code availability, and reporting checklist;
- language patterns and claim strength.

Use `not reported` when the paper does not provide evidence. Do not infer that a
check was performed.

## Calibrate issue priority

Separate non-waivable gates from frequency-calibrated issues.

### Non-waivable

Always treat these as major regardless of cohort prevalence:

- fabricated or unsupported data, citations, authorship, or metadata;
- ethics, consent, privacy, permission, or licensing failure;
- data leakage or test-dependent selection;
- invalid statistics or incorrect formulas;
- material contradiction between code, results, figures, and claims;
- plagiarism, duplicate publication, or manipulated images;
- violation of current mandatory venue rules;
- claims broader than the actual study design.

### Frequency-calibrated

For style, organization, display density, reporting detail, and optional
analysis choices, calculate the number of matched papers with the same issue:

- `0/20`: unusual; high-priority manuscript-specific correction;
- `1-4/20`: uncommon; medium-high priority;
- `5-10/20`: mixed practice; decide from scientific value and venue rules;
- `11-20/20`: common among matched papers; lower relative priority unless it
  obscures the target manuscript's central evidence.

One weak precedent is not enough to lower priority. Record both prevalence and
scientific consequence.

An issue absent from all 20 papers but present in the target manuscript is a
default high-priority fix. A feature consistently present in strong matched
papers but absent from the target is also high priority when applicable.

## Story calibration

Compare the target with the cohort on:

- whether the paper asks one central question or lists modules;
- how quickly the Introduction reaches the exact gap;
- how novelty is scoped against the closest work;
- whether every contribution has a matched experiment;
- whether key figures form a coherent argument;
- how null and failure evidence is handled;
- where the claim ceiling is set;
- how the Discussion separates mechanism, performance, and applicability.

Use this comparison to revise the narrative spine, not to imitate sentences.

## Review output

Produce one table with:

- finding;
- manuscript evidence and location;
- matched-paper prevalence;
- strongest comparable examples;
- scientific/ethical severity;
- venue requirement status;
- priority;
- concrete repair;
- verification needed after repair.

Use priorities:

- `P0`: integrity, ethics, evidence, or mandatory rule blocker;
- `P1`: absent from the matched cohort or central to the paper's validity;
- `P2`: material clarity, reproducibility, or persuasion problem;
- `P3`: common comparative weakness or cosmetic improvement.

Do not recommend extra experiments merely because one benchmark paper contains
them. Require a direct link to the target claim or reviewer risk.

## Freeze and reuse

Freeze the 20-paper cohort before the final review. Add or replace papers only
with a documented reason and rerun the prevalence analysis. Reuse the same
cohort for story calibration, self-review, cover letter, and reviewer response
unless the venue or scientific scope changes materially.
