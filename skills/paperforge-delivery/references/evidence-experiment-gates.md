# Evidence and Experiment Gates

Load this reference before drafting quantitative, comparative, mechanistic,
generalization, clinical, or operational claims.

## Canonical evidence record

Maintain one claim/evidence map. Give every primary manuscript claim a stable
ID and record:

- exact manuscript location and wording;
- claim type and allowed scope;
- population, unit of inference, horizon, and information boundary;
- source artifact, table row, figure panel, evaluator, and code commit;
- point estimate, unit, direction, uncertainty, sample or seed count;
- statistical comparison, paired unit, multiplicity handling, and test status;
- development, validation, locked-test, external, or replication layer;
- allowed wording, prohibited stronger wording, and current status.

Do not maintain competing evidence maps in multiple Markdown files. Prefer one
machine-readable JSON/CSV/XLSX record and generate reader-facing text from it.

## Mandatory gates

### Gate 1: canonical project and protocol

Require:

- verified project root, repository root, branch, remote, and commit;
- one machine-readable protocol controlling data version, split,
  preprocessing, features, model identity, routes, seeds, ratios, thresholds,
  primary outcomes, and availability;
- data/input hash and configuration fingerprint;
- unique formal output root.

Block formal claims when code, evaluator, tables, or manuscript disagree with
the protocol. Never repair disagreement only in prose.

### Gate 2: implementation and formula alignment

Compare the protocol with:

- training entrypoint and configuration;
- model identity and implemented components;
- preprocessing and feature availability;
- training loss and target construction;
- saved predictions;
- evaluator formulas and metric direction;
- equations, tables, captions, and method names.

Require identical soft/hard gate definitions, correction formulas,
normalization, indexing, threshold logic, and units. Do not call an
implementation by a stronger model or mechanism name than the code supports.

### Gate 3: split, leakage, and information boundary

Verify:

- grouping unit, such as patient, station, event, subject, site, or time block;
- no cross-partition identity, duplicate, temporal, augmentation, or
  preprocessing leakage;
- train-only fitting of normalization, imputation, augmentation statistics,
  teacher models, feature selection, and calibration when required;
- no future observations, hindsight reanalysis, or unavailable deployment
  features unless the run is explicitly labeled hindcast;
- windows, events, and grouped samples do not cross split boundaries.

Lead with the strongest true integrity unit. When patient IDs define the split,
describe patient-level partitioning first; treat duplicate audits as secondary
support rather than a competing main claim.

### Gate 4: formal experiment matrix

Enumerate expected and realized:

- mainline routes;
- strong matched baselines;
- mechanism controls and ablations;
- robustness and external analyses;
- seeds, folds, horizons, regions, ratios, and backbones;
- failed, missing, partial, superseded, and completed runs.

Require a manifest-driven matrix with one unique output directory per declared
run. Preserve requested and realized settings. Do not infer matrix completion
from a launcher, PID, checkpoint, or partial summary.

### Gate 5: run and seed integrity

Retain every declared seed, failure, null, unfavorable result, and runtime
exception with provenance. Never delete non-winning runs.

Use only the predeclared validation rule for selection. A post-hoc best-three
seed subset is exploratory or appendix evidence; it cannot replace the
confirmatory all-seed analysis.

Separate corrected runs from legacy or invalid runs. Corrected runs require
their own manifest, raw predictions, summaries, hashes, and evaluator decision.
Do not mix old and corrected routes in one primary table.

### Gate 6: locked-test firewall

Keep model, threshold, ratio, checkpoint, feature, backbone, gate, and narrative
selection outside the locked test. Record when and why the test was opened.

Block claims when test results influenced selection. Do not relabel a test set
as validation after inspection.

### Gate 7: statistical integrity

Define before testing:

- estimand and direction;
- unit of inference and paired unit;
- repeated-measure or hierarchical structure;
- sample, event, subject, station, region, fold, and seed counts;
- uncertainty type and interval method;
- missing-data handling;
- multiplicity family;
- subgroup and sensitivity status;
- equivalence or non-inferiority margin when applicable.

Prefer estimates and intervals over isolated p-values. Use a test that matches
the dependency structure. Do not translate non-significance into equivalence or
absence of benefit without an appropriate margin and adequate precision.

Keep discrimination/ranking, calibration/probability quality, threshold
performance, robustness, and decision value separate.

### Gate 8: negative and contradictory evidence

Retain:

- failed routes and training failures;
- unfavorable seeds or regions;
- null mechanism checks;
- contradictory backbones or external cohorts;
- instability, sensitivity, and calibration failures;
- protocol deviations.

Place prespecified primary outcomes and central mechanism analyses in the main
table. Put secondary, exploratory, negative, null, or unfavorable evidence in
the supplement or one audit workbook with provenance. Never hide it.

### Gate 9: literature and citation truth

For every scientific citation:

- inspect the primary source or official record;
- verify title, authors, venue, year, DOI/URL, publication status, and version;
- check that the cited passage entails the manuscript claim;
- separate accepted, online-first, indexed, preprint, and under-review status;
- check retraction or correction status when consequential;
- prefer primary research over snippets, aggregators, or secondary summaries.

Do not infer individual indexing from a conference's planned indexing statement.
Do not count forks, mirrors, example repositories, or request-only data as
independent public datasets.

### Gate 10: narrative consistency

Cross-check the same facts across title, abstract, Introduction, Methods,
Results, tables, figures, captions, Discussion, limitations, supplement, cover
letter, and reviewer response.

Require exact agreement for:

- sample and unit counts;
- split names and boundaries;
- seed/fold/region/horizon counts;
- model, route, dataset, and acronym names;
- metric direction and units;
- estimates, intervals, p-values, and comparison direction;
- validation scope and externality;
- words such as first, robust, generalizable, significant, clinical,
  operational, causal, prospective, and state of the art.

Treat any unresolved contradiction as a delivery blocker.

### Gate 11: publication ethics and permissions

Check authorship, acknowledgments, conflicts, funding, ethics, consent, privacy,
data-use permission, image manipulation, plagiarism/self-plagiarism, duplicate
publication, preregistration where applicable, code/data licensing, and
required AI-use disclosure.

Do not fabricate or infer truth-only metadata. Leave explicit placeholders and
ask the user once at the end.

### Gate 12: delivery evidence

Require:

- manuscript and supplement render successfully;
- tables and figures match canonical evidence;
- references resolve;
- figure and table callouts are complete;
- final package inventory and SHA256 hashes exist;
- source commit, protocol/data/config fingerprints, and evaluator decision are
  recorded;
- original files remain unchanged;
- temporary and failed artifacts are absent from formal packages.

## Status decision

Return one verdict:

- `PASS`: all applicable hard gates pass.
- `WARN`: scientific claims are supportable, but named non-critical delivery or
  reporting items remain.
- `BLOCKED`: any integrity, evidence, permission, locked-test, contradiction, or
  missing-primary-artifact gate fails.

Do not downgrade `BLOCKED` because a deadline is close or because comparable
papers report weakly.
