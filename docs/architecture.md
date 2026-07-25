# Architecture

PaperForge has one controller and a set of narrow specialists.

## Controller

`paperforge-delivery` owns the end-to-end contract:

```text
live project evidence
        |
        v
canonical paper contract
        |
        +--> experiment and claim gates
        +--> 20-paper matched benchmark
        +--> one falsifiable story
        +--> semantic figure/color registry
        +--> manuscript and layout
        +--> submission + code packages
        |
        v
verified delivery audit
```

Its `SKILL.md` remains a concise controller. Detailed, conditionally loaded
rules live in:

- `references/evidence-experiment-gates.md`
- `references/writing-story-contract.md`
- `references/figure-color-chart-contract.md`
- `references/matched-paper-review.md`
- `references/document-layout-delivery.md`
- `references/domain-overrides.md`

Machine-readable starter assets prevent repeated free-form setup:

- `assets/paper-contract.template.json`
- `assets/figure-style-registry.template.json`
- `assets/matched-paper-benchmark.template.csv`

`scripts/validate_delivery.py` validates the contract, project confinement,
evidence paths, matched-paper count, final artifacts, hashes, and hard gates.

## Specialists

The controller routes isolated work to:

- `results-auditor` for result and claim consistency;
- `evidence-ranker` for evidence strength;
- `paper-polish` and `bilingual-anti-ai-writing` for bounded prose revision;
- `figure-style-studio` for focused figure work;
- `paper-self-review` for a final checklist;
- `reviewer-response` for rebuttals;
- `research-ideation` for literature-grounded directions.

Specialists add task-specific tests but do not create competing project
contracts, palettes, evidence maps, or delivery manifests.

## Project hygiene

Use one canonical checkout. Keep version history in Git, failed/temporary work
under ignored project-local directories, and formal deliverables in one
versioned bundle. Build the code package from the verified canonical commit;
never maintain a copied editable repository as `v2`, `final`, or `latest`.

Do not create one Markdown report per generated artifact. Keep one contract, one
claim/evidence map, one matched-paper table, one figure registry, and one final
audit record per delivery cycle.
