# Architecture

PaperForge is a collection of small, composable Codex skills rather than a
single monolithic agent.

## Skill layers

1. `paperforge-delivery`
   - Coordinates end-to-end paper, figure, deck, and submission work.
   - Routes tasks to narrower skills when a request is more specific.

2. Specialist skills
   - `paper-polish` handles prose and claim discipline.
   - `figure-style-studio` handles chart choice, palettes, and reproducible
     figure generation.
   - `results-auditor` checks tables, metrics, splits, and claim consistency.
   - `reviewer-response` converts peer-review comments into revision plans and
     response letters.
   - `paper-self-review` performs pre-submission checks.
   - `evidence-ranker` prioritizes citations by evidence strength.
   - `research-ideation` turns topics and constraints into testable directions.

3. Utility scripts
   - `scripts/validate_skills.py` checks skill metadata and folder names.
   - `scripts/install_skills.py` copies selected skills into a local Codex
     skills directory.

## Data flow

```text
User files / notes / tables / reviews
              |
              v
      PaperForge skill selection
              |
              v
Evidence map, style rules, and task-specific checks
              |
              v
Revised prose, figures, audit notes, response letters, or delivery folders
```

## Design choices

- Keep each skill readable enough to inspect quickly.
- Avoid private memory, project-specific names, and hard-coded local paths.
- Prefer verifiable evidence over polished narrative.
- Use scripts only where repeatability matters.
