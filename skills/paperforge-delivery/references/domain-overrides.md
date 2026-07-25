# Domain Overrides

Load only the applicable section. Current official venue and project protocols
override these defaults.

## Medical and ophthalmic studies

- Establish the clinical question and cohort before introducing the model.
- Keep patient-, eye-, image-, lesion-, visit-, and duplicate-group units
  distinct.
- When patient IDs exist, make patient-level partitioning the primary integrity
  statement: all images from one patient remain in one split or fold.
- Treat duplicate/near-duplicate auditing as secondary evidence unless it is
  itself the research question.
- Separate discrimination, calibration, operating-point performance, clinical
  utility, and reader comparison.
- Report exact positive class, prevalence, threshold selection, sensitivity,
  specificity, PPV/NPV when applicable, and uncertainty.
- Do not call internal holdout evidence external, prospective, clinical, or
  deployable.
- Apply the correct reporting guideline and verify ethics, consent, privacy,
  image use, data availability, and external-dataset licenses.
- Use structured abstracts only when the venue/article type requires them.
- Keep public code/example data distinct from full clinical dataset
  availability.

## Coastal and spatiotemporal forecasting

- Define issue time, valid time, lead/horizon, observation source, forcing
  availability, train-only statistics, and hindcast/forecast status.
- Keep station-, region-, event-, window-, seed-, and horizon-level evidence
  distinct.
- Prevent random windows or events from crossing temporal or station split
  boundaries.
- Keep continuous point forecasts, event-set outputs, calibration products, and
  verifier/risk products separate when they answer different questions.
- Preserve physical units. Do not mix hours, water level, magnitude, and
  percentage change on one axis or in one unlabeled table column.
- Keep equations, residual sequence, signs, lag/lead indexing, normalization,
  topology masks, and evaluator formulas identical to implementation.
- Use formal geography such as verified Natural Earth or project-approved
  sources and formal coordinates. Never generate scientific geography.
- Apply the Coast/PRIME palette only when the project has adopted that visual
  identity.

## Mechanism papers

- Give every claimed mechanism a measurable proxy, matched control, diagnostic,
  contribution test, and failure boundary.
- Use the simplest capacity-matched baseline that can falsify the mechanism.
- Do not let backbone replacement alone become the main scientific claim.
- Report contradictory backbones, cohorts, regions, and seeds rather than
  averaging them away.
- Keep mainline, baseline, ablation, robustness, and future extension labels
  explicit in the internal contract, while removing workflow labels from
  reader-facing prose.

## Remote GPU experiments

- Resolve one canonical remote project root and keep repository, data, formal
  runs, temporary work, and deliveries inside it. Never create sibling clones
  or leave transfer copies under another project's temporary directory.
- Verify root, branch, commit, protocol/config hash, data completeness, imports,
  tests, manifest, and device before formal launch.
- Fail closed when explicit CUDA execution is unavailable; never silently use
  CPU.
- Inspect existing PIDs, heartbeats, logs, GPU state, and output artifacts
  before stopping, restarting, or duplicating a run.
- Record actual device, PID/job ID, log, output root, first artifact, and
  realized settings.
- A process or checkpoint proves engineering state only. Require formal result
  artifacts, evaluator decision, and local hash-verified delivery before
  reporting experimental completion.
- Inventory and classify remote paths before cleanup. Remove only resolved,
  explicitly verified temporary artifacts after local SHA256 delivery; retain
  formal and failed-run evidence.
- Never kill, pause, preempt, or fake-occupy another user's shared-GPU work.
