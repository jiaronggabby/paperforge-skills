---
name: paperforge-delivery
description: End-to-end academic delivery workflow for manuscripts, LaTeX projects, figures, tables, slide decks, reviewer-facing revisions, and final submission folders. Use when the user asks to turn rough research artifacts into a clean paper-ready or presentation-ready deliverable, reconcile claims with results, redraw figures with consistent style, prepare a response package, or assemble final files for submission.
---

# PaperForge Delivery

Use this skill as the controller for research deliverables. Work from the
current project files, user-provided drafts, result tables, figures, review
comments, and explicit instructions.

## Workflow

1. Define the deliverable.
   - Identify whether the output is prose, LaTeX, Word, figures, tables, slides,
     reviewer responses, or a final submission folder.
   - Choose the narrowest set of specialist workflows needed.

2. Build an evidence map.
   - Link each result claim to a source table, CSV/XLSX, figure script, log,
     manuscript table, or user-provided note.
   - Prefer raw tables and code outputs over screenshots.
   - If sources disagree, report the conflict before writing around it.

3. Produce the deliverable.
   - Preserve the user's template and file format unless asked to redesign.
   - Write in direct academic prose with concrete claims and measured scope.
   - Keep figures data-backed and visually consistent.
   - Keep slides claim-driven: one main point and one proof object per slide.

4. Verify.
   - Check expected files exist and are non-empty.
   - Render or compile visual/document outputs when possible.
   - Confirm manuscript numbers, captions, tables, and figure labels match the
     evidence map.
   - Clean scratch files and leave final artifacts in a tidy folder.

## Delivery standards

- Do not overwrite source manuscripts, data, figures, or decks unless the user
  explicitly asks.
- Create revised copies or dated output folders for final artifacts.
- Do not fabricate citations, metrics, p-values, confidence intervals, baselines,
  reviewer changes, or venue rules.
- State unresolved missing evidence directly.
- Keep final user-facing folders small: source inputs, final outputs, and any
  necessary evidence notes.

## Manuscript prose rules

- Write like a careful human coauthor, not like a reviewer response or a prompt
  template.
- Do not use self-referential wording such as "the manuscript", "this
  manuscript", "the paper avoids", or "the manuscript was structured using".
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
  story, not to stale template language.
- Remove process labels, placeholder titles, prompt residue, and decorative
  callouts from figure panels. Do not leave phrases such as "published-style",
  "repair analysis", "schematic" when the user wants real results, or arrows
  that merely restate the obvious.
- If the user asks for patient-level wording, remove duplicate-aware wording
  from the figure canvas, figure caption, and surrounding prose.
- Prefer low-saturation, publication-style palettes. Keep colors consistent for
  the same model or case across all figures.
- Use black or very dark neutral error bars and outlines when the palette is
  light or muted, so uncertainty marks stay legible.
- If the user requests confidence bands, use bands consistently instead of
  switching between bands and bars without reason.
- Avoid cluttered legends, too many endpoint labels in one panel, and mixed
  visual metaphors in the same figure.
- For workflow schematics, ensure the implementation shown in the figure matches
  the actual method description. Do not draw a fancier module than the method
  section supports.

## Word and layout rules

- Preserve embedded figures when editing `.docx` manuscripts. After any major
  Word edit, verify that the main document still contains the expected number of
  figures and that captions are followed by image objects, not captions alone.
- If supplementary figures or tables become substantial, place them in a
  separate supplementary Word document that matches the main manuscript layout.
- Keep the main manuscript visually clean: black body text, stable heading
  hierarchy, no accidental blue font artifacts, and no orphaned appendix
  material left after references.
- Ensure every main-paper figure and table is mentioned naturally in the body.
  Supplementary items can be cited once with a short directional sentence.
- If the user wants a journal-ready Word deliverable, verify figure order,
  table order, caption numbering, and that no panel references or labels are
  stale after rearrangement.

## Default visual taste

Use a restrained publication style unless the project already has a stronger
identity:

- white or very light neutral backgrounds;
- dark gray text;
- muted blue, teal, sage, gold, coral, slate, and soft purple accents;
- thin grid lines;
- readable labels;
- no rainbow colormaps, heavy shadows, decorative gradients, or crowded legends.
