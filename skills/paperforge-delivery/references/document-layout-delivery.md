# Document Layout and Delivery

Load this reference for repository layout, Word, LaTeX, PDF, PowerPoint,
spreadsheet, code-package, or final-submission work.

## Minimal project hygiene

Reuse the project's existing canonical structure. Do not reorganize a mature
project merely to match an example. For a new project, use the smallest useful
separation:

```text
project-root/
├── code-or-src/              canonical tracked code and manuscript sources
├── results/                  unique formal run outputs and canonical tables
├── paper/                    current manuscript, supplement, figure sources
├── work/                     ignored scratch, previews, caches, failed exports
└── delivery/
    ├── submission-vN/        immutable final manuscript package
    ├── code-package-vN/      archive from the canonical verified commit
    └── provenance/           one contract and one final audit record
```

Do not create a nested Git repository. Do not copy the checkout into `v2`,
`v3`, `final`, `latest`, `fixed`, `clean`, `release`, or timestamped sibling
directories.

Use Git branches/commits/tags for source history. Use a new delivery version
only after a material formal change. Never edit a generated submission bundle
as the canonical source.

## Remote/WKU project hygiene

Keep every remote project inside its existing verified project root. Do not move
projects into one shared cleanup folder and do not store one project's transfer
bundle under another project's `tmp/`.

Reuse existing directory roles. For a new remote project, use:

```text
remote-project-root/
├── repository/ or current checkout/   one canonical Git checkout
├── data/                              immutable/versioned inputs
├── runs/                              unique formal and failed run IDs
├── work/                              temporary transfers, smoke, caches
└── delivery/                          verified exports and hash manifests
```

Require:

- one canonical remote checkout, branch, remote, and commit;
- one data/input version or hash and one machine-readable protocol;
- unique run directories keyed by run ID plus commit/config fingerprint;
- explicit `planned`, `running`, `failed`, `partial`, `complete`, and
  `verified` states;
- failed/partial runs retained but excluded from formal summaries;
- transfer archives removed after source/destination SHA256 agreement unless
  they are the only recovery evidence;
- final artifacts pulled locally and checked by SHA256 before remote cleanup.

Before any remote cleanup, create a read-only inventory of resolved absolute
paths, repository identity, size, age, run state, and evidence role. Classify
each item as canonical, formal evidence, failed evidence, temporary, stale
duplicate, or unknown. Delete or move only explicitly verified temporary or
stale duplicate targets; never use broad globs, guessed paths, or another
project's directory as a cleanup staging area.

## File-count discipline

Default to these internal records per delivery cycle:

1. `paper_contract.json`;
2. `claim_evidence_map.csv` or one equivalent workbook;
3. `matched_papers.csv`;
4. `figure_style_registry.json`;
5. `package_audit.json`.

Do not create per-artifact Markdown summaries or a reviewer/self-review `.md`
file. Put structured findings in the existing `package_audit.json`, a single
`review_findings.json`, or the approved audit workbook. Keep Markdown only when
it is a true source document, required README, manuscript source, response
letter, or sole reproducibility record supplied by the user.

Do not create `*.tmp`, `*.temp`, `*.bak`, `*.swp`, or nested `tmp/`, `temp/`,
`scratch/`, `preview/`, or timestamped directories. If a tool requires
transient files, use one flat ignored `work/` directory, never write generated
Markdown there, and remove it after validation. The final project handoff must
contain no transient directory or generated review Markdown.

## Formal submission package

Include only what the venue or user needs:

- final editable manuscript or LaTeX source;
- final rendered PDF when required;
- supplementary manuscript/material;
- final main and supplementary figures;
- editable tables or final spreadsheet when required;
- cover letter, highlights, checklist, response letter, or declarations when
  required;
- compact provenance/audit record when appropriate.

Exclude source-data copies, caches, plotting experiments, temporary previews,
unpacked Office XML, raw logs, failed outputs, duplicate drafts, and internal
review chatter.

## Reproducible code package

Build the code package from the verified canonical commit or Git archive. Do not
maintain a second editable repository.

Include:

- source code and entrypoints;
- frozen configuration/protocol;
- environment or lock file;
- tests and a bounded smoke command;
- small licensed fixtures when needed;
- data acquisition or path instructions without private data;
- model/checkpoint retrieval instructions when redistribution is not allowed;
- commit, tag, license, and minimal run/evaluation instructions.

Exclude:

- credentials and SSH keys;
- raw private or licensed data;
- unneeded checkpoints and large outputs;
- caches, virtual environments, temporary transfers, and nested `.git`;
- failed runs and obsolete release copies;
- manuscript plotting experiments unless needed to reproduce reported figures.

Publish large archives as release assets when appropriate instead of committing
them into Git history.

## Failed and partial work

Keep failed formal runs because they are evidence, but isolate them under the
existing run system with unique IDs and explicit status. Do not mix them into
the final result summary or submission package.

Record at least:

- run ID, command, commit, config, device, start/end time;
- failure status and error;
- partial artifacts retained;
- whether the run is eligible for analysis.

Do not create a repository copy for a failed code attempt. Fix the canonical
branch, retain the failure record, and rerun into a new unique output directory.

## Word defaults

Preserve a journal template when supplied. Otherwise:

- use Times New Roman, black text, consistent heading levels, standard margins,
  and one paragraph style;
- use one descriptive title without a subtitle unless required;
- place table captions above tables and figure captions below figures;
- keep equations as native editable objects where possible;
- preserve embedded figures and verify image-object counts after edits;
- use black-and-white three-line tables with no vertical rules or colored cells;
- keep estimates and intervals legible, using separate lines in dense cells;
- cite every main display naturally in the body;
- set Word author/creator metadata to `jiarong` by default; use a different
  value only when the user explicitly requests it for the current delivery.

When a `.docx` is locked or open, save a new formal version. Do not force
replacement.

## LaTeX defaults

- Copy the full target template before editing.
- Do not modify venue `.sty` files without explicit authorization.
- Compile after structural changes, then inspect the PDF.
- Keep labels, citations, tables, and figure paths stable.
- Audit overfull boxes, missing references, font substitution, equation breaks,
  float order, and supplementary numbering.

## PDF and presentation safety

- Prefer headless/offline conversion when available.
- Work from a copied Office file when COM automation is unavoidable.
- Close only the document/presentation object opened by the workflow.
- Never quit or kill an Office application that may contain unsaved user work.
- Verify output page count, size, readability, and source timestamp.

Slides may use concise action titles, larger type, fewer labels, and one proof
object per slide. Preserve manuscript semantic colors when reusing results.

## Spreadsheet defaults

- Keep one canonical result workbook, not one workbook per edit.
- Separate machine-readable data, display tables, statistical outputs, and
  audit notes into named sheets.
- Preserve formulas or export computed values with provenance.
- Check for formula errors, stale links, hidden rows/columns, inconsistent
  units, and threshold-free versus locked-operating-point mixing.
- Do not declare a workbook deliverable while any required formula cell errors.

## Build sequence

1. Sanitize names, terminology, result status, and display tables.
2. Regenerate figures from canonical data.
3. Regenerate manuscript and supplement from canonical sources.
4. Render and inspect all visual/document outputs.
5. Build submission and code packages from verified sources.
6. Generate the manifest and hashes once.
7. Run the final audit.
8. Report one exact final directory and one exact code commit/archive.

Do not generate the manifest early and repeatedly patch it after each cleanup.

## Cleanup

Delete only verified temporary artifacts inside the declared work directory:
previews, caches, extraction folders, unpacked Office files, temporary CSVs,
conversion intermediates, and throwaway scripts.

Retain any artifact that is the only evidence for a result. Never delete source
files, user files, formal results, failed-run evidence, or final deliverables
without explicit authorization.
