---
name: paperforge-delivery
description: End-to-end academic delivery workflow for manuscripts, LaTeX projects, PNG paper figures, verified references, tables, slide decks, safe PPT/PDF handling, low-AI academic polishing, reviewer-facing revisions, and final submission folders. Use when the user asks to turn rough research artifacts into a clean paper-ready or presentation-ready deliverable, reconcile claims with results, redraw figures with consistent style, convert or audit PPT/PDF outputs without disturbing open Office apps, make manuscript language less AI-like, prepare a response package, clean temporary delivery files, or assemble final files for submission.
---

# PaperForge Delivery

Use this skill as the single controller for paper-facing deliverables. It
absorbs the reusable workflow previously split across broad paper delivery
skills, while narrower skills remain specialists for their file type or task.

Work from the current project files, user-provided drafts, result tables,
figures, review comments, and explicit instructions.

## Source order

1. Read project-local memory, `AGENTS.md`/`agent.md`, README files, current
   draft notes, result summaries, and latest generated artifacts before writing
   or converting anything.
2. Prefer live source files over old rollout memories. Use historical memories
   only to infer stable user preferences or avoid repeated mistakes.
3. Trace each manuscript claim, figure, table, and citation to a real source:
   code, CSV/XLSX, Word table, LaTeX draft, verified paper, log, or
   user-provided note.
4. When source files disagree, stop and report the contradiction instead of
   smoothing it over.

## Non-negotiable safety rules

- Never overwrite original manuscripts, appendices, decks, PDFs, images, or
  data unless the user explicitly asks for overwrite in the current turn.
- Create a new output folder or copy first. Use names such as `*_revised`,
  `*_paper_ready`, `output_sci_figures`, `final_submission_bundle`, or a dated
  delivery folder.
- Keep scratch files in a clearly named working folder while working. Put only
  final deliverables in the user-facing output folder.
- Clean temporary files by default before the final response: delete generated
  scratch scripts, preview renders, contact sheets, extraction caches,
  temporary CSVs, logs, unpacked Office folders, and conversion intermediates
  unless the user explicitly asked to keep them or they are the only
  reproducibility record for a final claim.
- Never delete source files, final deliverables, user-provided assets, or
  intermediate evidence files that are the only reproducibility record. If such
  evidence must be retained, place it in a small `evidence` or `audit` subfolder
  and mention it.
- Do not close, kill, or quit Word, PowerPoint, or Excel applications that the
  user may be using.
- Treat active Office files as dangerous. If `WINWORD`, `POWERPNT`, or `EXCEL`
  is running, avoid COM automation that can touch the live application unless
  there is no safer route.
- For PPT/PPTX-to-PDF conversion, prefer headless/offline conversion tools when
  available. If PowerPoint COM is unavoidable:
  - work on a copied input file;
  - open only that copied file;
  - close only the presentation object opened by this workflow;
  - never call `Application.Quit()` when PowerPoint was already running;
  - never kill `POWERPNT`;
  - verify the original file still exists and its timestamp did not change.
- If a file is locked by Office, save a new version and tell the user. Do not
  force-replace it.

## Workflow

1. Define the deliverable.
   - Identify whether the task is manuscript prose, LaTeX, references, figures,
     tables, PPT/deck work, PDF conversion, reviewer response, submission
     bundle, or a combined delivery.
   - Choose the narrowest specialist skills needed: Word/document handling,
     deck handling, PDF handling, editable-PPT reconstruction, figure styling,
     result auditing, prose polishing, evidence ranking, or reviewer response.

2. Build an evidence map.
   - List source artifacts and what each supports.
   - For results, read canonical CSV/XLSX/table sources first; avoid duplicated
     exports unless they are explicitly canonical.
   - For figures, extract numbers from tables/CSV/XLSX/code outputs, not
     screenshots. Do not OCR chart values if a table exists.
   - For references, search or verify real papers and retrieve BibTeX from
     DOI, arXiv, CrossRef, Semantic Scholar, or the publisher page. Never invent
     BibTeX.
   - If sources disagree, report the conflict before writing around it.

3. Produce paper-facing content.
   - Preserve the user's template and file format unless asked to redesign.
   - Write in direct SCI/conference prose, not marketing prose.
   - Preserve technical meaning when reducing AI feel. Do not over-compress
     claims or remove necessary caveats.
   - Prefer method-forward but still searchable titles when the user says a
     title is too blunt or wants something more indirect.
   - Use full paragraphs for manuscript sections. Use bullets only for planning,
     checklists, internal reports, or reviewer response structure.

4. Create or audit figures.
   - Generate data-backed figures from extracted data.
   - Output PNG only by default for paper figures, preferably 600 dpi when
     generated from plots. Create SVG/PDF vector files only when the user
     explicitly asks for them or a venue/template requires vector output.
   - Keep figures data-backed and visually consistent across the manuscript or
     deck.
   - Reuse a project-local plotting style module when one exists, such as a
     `paper_style.py`, `style.py`, or shared `PALETTE`/`MODEL_COLORS` mapping.
     Keep the rule project-general: fixed palette, shared rcParams, white
     background, dark gray text, light gray grid, and consistent colors for the
     same method across every panel.
   - Do not simulate ROC curves from AUC alone, invent missing values, or
     recompute unsupported metrics.
   - If data is missing, create a missing-data note instead of making an
     unsupported chart.

5. Prepare LaTeX and references.
   - Copy the full target template before editing. Do not modify venue `.sty`
     files unless the user explicitly asks.
   - Compile early after structural changes.
   - Compare manuscript numbers, table captions, figure captions, and claims
     against the evidence map.
   - Audit terminology drift after renaming methods, models, datasets, or
     routes.

6. Build PPT or PDF deliverables.
   - Use deck work for communication, not decoration: each slide needs one main
     claim and one proof object.
   - Keep figure labels readable at presentation size; simplify dense paper
     figures for slides.
   - For conversion-only tasks, preserve the source file and verify output page
     count, file size, and readability.
   - For editable PPT reconstruction from an image, use a specialist PPT visual
     replica workflow; do not hand-draw semantic visual units as fake editable
     shapes.

7. Verify.
   - Check expected files exist and are non-empty.
   - Render or compile visual/document outputs when possible.
   - Confirm manuscript numbers, captions, tables, and figure labels match the
     evidence map.
   - Confirm no original source file was modified unintentionally.
   - Clean temporary files and leave the output folder tidy by default.
   - Report exact output paths, validation checks, and any remaining unsupported
     claims or missing data.

## Delivery standards

- Do not fabricate citations, metrics, p-values, confidence intervals, baselines,
  reviewer changes, or venue rules.
- State unresolved missing evidence directly.
- Keep final user-facing folders small: source inputs, final outputs, and any
  necessary evidence notes.

## Manuscript prose rules

- Write like a careful human coauthor, not like a reviewer response or a prompt
  template.
- Do not use self-referential wording such as "the manuscript", "this
  manuscript", "the paper avoids", or "the manuscript was structured using"
  inside the draft unless the genre requires it.
- Do not leave internal workflow language in the draft: no "main story line",
  "FNR focus", "published-style repair", "workflow question", "paper-facing",
  "supportive rather than confirmatory", or similar process labels unless the
  phrase is genuinely part of the scientific method being reported.
- Avoid repetitive contrast scaffolds such as "not A but B", "not only X but
  also Y", "should be read as X rather than Y", "this does not mean", and
  "these results support X; they do not show Y". State the claim directly once.
- Avoid repeated defensive caveats. Keep limitations plain, specific, and brief.
- Do not overuse reviewer-facing emphasis phrases such as "this is important
  because", "not a minor detail", "the key message is", or similar sentence
  frames.
- When a term is ordinary and sufficient, use the ordinary term. Prefer
  "patient ID", "patient-level partitioning", "review", "repeat capture",
  "supporting analysis", and "internal holdout" over inflated or awkward
  substitutes.
- Do not call aims "prespecified" unless there is real preregistration or a
  locked protocol that supports that wording.
- Preserve the user's preferred terminology exactly once it is established, and
  audit old names after renaming.
- If the user has settled on one integrity concept, keep the wording aligned to
  that concept. Example: if patient IDs define the split, lead with
  patient-level partitioning; do not keep foregrounding duplicate-aware wording
  in parallel.

## Split and evidence wording

- When patient IDs exist, describe dataset integrity primarily at the
  patient level.
- Use a simple statement such as: all partitions were created by patient ID, so
  all photographs from the same patient remained within the same split or fold.
- Treat duplicate or near-duplicate auditing as optional secondary context. Keep
  it in supplementary materials or a single short methods clause if needed; do
  not let it compete with patient-level partitioning in the title, abstract,
  figure text, or main claims.
- Keep the unit of evidence consistent across prose, tables, and figures. Do
  not mix patient-level, image-level, duplicate-group, and fold-level language
  loosely.
- If the user wants a narrow main claim, align the visuals and wording to that
  claim instead of preserving every auxiliary analysis at equal prominence.

## Figure and plotting rules

- Main-paper figures must be data-backed and tied to the current manuscript
  story, not stale template language.
- Remove process labels, placeholder titles, prompt residue, and decorative
  callouts from figure panels. Do not leave phrases such as "published-style",
  "repair analysis", "schematic" when the user wants real results, or arrows
  that merely restate the obvious.
- Figures should be submission-ready on first delivery. Remove unexplained
  arrows, prompt-like labels, decorative tips, "published-style" labels,
  "repair analysis" labels, and any text that describes the workflow rather
  than the scientific object.
- Paper figures should not carry plot titles, figure titles, or descriptive
  panel titles by default. Let the manuscript caption explain the figure. Keep
  only panel letters, axis labels, tick labels, legends, scale bars, direct data
  labels, and necessary group labels.
- Use arrows only when they encode a necessary data flow, causal flow, or model
  path. Keep those arrows sparse, neutral, and caption-supported.
- If the user asks for patient-level wording, remove duplicate-aware wording
  from the figure canvas, figure caption, and surrounding prose.
- Prefer low-saturation, publication-style palettes. Keep colors consistent for
  the same method, model, case type, dataset, route, severity level, or
  comparison family across all figures.
- Maintain a manuscript-level color map before drawing multi-figure packages.
  Assign colors once, then reuse them in every panel, legend, table-as-figure,
  and slide figure unless the user explicitly changes the mapping.
- Use black or very dark neutral error bars and outlines when the palette is
  light or muted, so uncertainty marks stay legible.
- For bar charts, use black or very dark neutral outlines by default and show
  error bars when standard error, standard deviation, or confidence intervals
  are available. Do not omit uncertainty marks from a bar chart when the source
  table provides them.
- If the user requests confidence bands, use bands consistently instead of
  switching between bands and bars without reason.
- For point estimates, trends, smooth curves, or effect-size summaries, show
  95% CI as horizontal CI bars, vertical error bars, ribbons, or shaded bands
  when those intervals are available. Do not fabricate CI bands from point
  estimates alone.
- Avoid cluttered legends, too many endpoint labels in one panel, and mixed
  visual metaphors in the same figure.
- For workflow schematics, ensure the implementation shown in the figure matches
  the actual method description. Do not draw a fancier module than the method
  section supports.

## Word and layout rules

- Preserve the journal template, page size, margins, section order, heading
  hierarchy, paragraph styles, table style, caption style, reference style, and
  supplementary structure unless the user explicitly asks for a redesign.
- Preserve embedded figures when editing `.docx` manuscripts. After any major
  Word edit, verify that the main document still contains the expected number of
  figures and that captions are followed by image objects, not captions alone.
- For Word and similar document deliverables, set document author and creator
  metadata to `jiarong` unless the user explicitly asks for a different author
  name.
- If supplementary figures or tables become substantial, place them in a
  separate supplementary Word document that matches the main manuscript layout.
- Keep the main manuscript visually clean: black body text, stable heading
  hierarchy, consistent numbering, no accidental blue font artifacts, no hidden
  prompt/workflow notes, no duplicated headings, no empty sections, and no
  orphaned appendix material left after references.
- Do not use scripted tracked changes or comments unless they are explicitly
  requested and can be validated in Word. If tracked changes/comments are
  required, use proper Word mechanisms and verify author/comment metadata.
- If the source `.docx` is locked or currently open, save a new version rather
  than force-replacing it.
- Ensure every main-paper figure and table is mentioned naturally in the body.
  Supplementary items can be cited once with a short directional sentence.
- If the user wants a journal-ready Word deliverable, verify figure order, table
  order, caption numbering, and that no panel references or labels are stale
  after rearrangement.
- When creating Word files from scratch and no journal template is available,
  use neutral manuscript formatting: black body text, readable serif or journal
  template font, consistent heading levels, standard margins, normal line
  spacing for the target venue, and captions placed immediately before or after
  the referenced object according to the target style.

## Default visual taste

Use a restrained publication style unless the project already has a stronger
identity:

- Background: white or very light neutral (`#FFFFFF`, `#F7F8FA`).
- Text: dark gray, not pure black (`#2F3437`).
- Grid/rules: light gray-blue (`#D9DEE7`), thin and quiet.
- Main palette: muted blue `#4C78A8`, teal `#5AA6A6`, sage `#7A9E7E`, gold
  `#D8A657`, coral `#D98373`, slate `#8A95A5`, muted purple `#8E7CC3`.
- This palette is the default SCI/Nature-style preference: white background,
  dark gray body/axis text, light gray grid, low-saturation method colors, and
  no high-saturation red/green or rainbow color scales.
- Prefer low-saturation, colorblind-friendly, Nature/SCI-style figures.
- Avoid high-saturation red/green, rainbow colormaps, decorative gradients,
  heavy shadows, cramped labels, and text over busy images.
- For plots: white background, readable axis labels, light grid, consistent
  decimals, and no chart title unless the user explicitly asks for one or the
  figure is a slide rather than a manuscript figure.
- For slides: use the same palette but larger type, fewer labels, more
  whitespace, and one dominant proof object per slide.
- For reusable plotting code, follow the same pattern as stable project plotting
  modules: define one `PALETTE` dictionary, define method-specific color maps,
  set `matplotlib`/`seaborn` rcParams once, hide top/right spines by default,
  and save with a white facecolor.

## Low-AI prose rules

- Cut generic openings such as "it is important to note", "in recent years",
  and "this study highlights" unless they carry specific information.
- Replace vague praise with concrete claims and numbers.
- Avoid repeated "framework", "leveraging", "significant potential", "shown
  promise", "warranted", "robust", and "comprehensive" clusters.
- Remove over-defensive wording around leakage, split protocols, and seeds;
  state the protocol plainly.
- Keep uncertainty where science needs it, but remove stacked hedging such as
  "may potentially suggest".

## Evidence from local history

This skill is the single paper-delivery controller because these patterns
repeated across local Codex history:

- 2026-05-01 to 2026-05-02: manuscript and appendix edits required copied
  outputs, no original overwrite, exact split/table corrections, and SCI figure
  redraws from Word tables/CSV with unified colors.
- 2026-05-04: a background plotting/conversion workflow closed the user's
  unsaved PowerPoint, so Office automation must not quit or kill active
  applications.
- 2026-05-06: manuscript AI-feel reduction required direct SCI prose, minimal
  paraphrase, terminology cleanup, and saving a new file when Word locked the
  original.
- 2026-05-11: PPT-to-PDF conversion needed small file size and verified page
  count, but COM export was brittle and must be handled carefully.
- 2026-05-13 to 2026-05-20: paper figures, presentation PPT, LaTeX layout,
  citation updates, terminology audits, and figure/code consistency checks
  recurred across projects.
