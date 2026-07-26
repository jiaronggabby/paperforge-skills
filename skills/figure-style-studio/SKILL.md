---
name: figure-style-studio
description: Create or revise publication-quality academic figures, diagrams, tables-as-figures, ablation plots, result charts, and slide figures with consistent colors and readable typography. Use when the user asks for paper figure design, figure recoloring, SCI/Nature-style plots, ML conference figures, architecture diagrams, chart selection, or visual consistency across a manuscript or deck.
---

# Figure Style Studio

Use this skill to turn results and method descriptions into clear academic
figures. Prefer reproducible plotting from data over manual visual editing.

## Figure choice

- Use line charts for trends over time, epochs, horizons, or sample sizes.
- Use grouped bars for small method-by-metric comparisons.
- Use heatmaps for matrix-like results, ablations, confusion matrices, or
  region-by-horizon tables.
- Use scatter plots for relationships between two continuous variables.
- Use box/violin plots for distributions when sample-level values exist.
- Use diagrams for systems, workflows, model architecture, and data flow.
- Avoid pie charts unless the task is truly part-to-whole composition.

## Data rules

- Plot from CSV/XLSX/JSON/code outputs whenever available.
- Do not estimate chart values from screenshots if a table exists.
- Do not invent missing error bars, confidence intervals, p-values, or sample
  sizes.
- Label derived values as derived.

## Style rules

- Use one main palette across the paper or slide deck.
- Prefer a reusable plotting style module or shared block with a `PALETTE`,
  `apply_paper_style()`, `style_axes()`, `bar_kwargs()`, `err_kwargs()`, and
  `add_panel_label()` pattern so every figure uses the same fonts, axes, grids,
  bar outlines, error bars, and panel labels.
- Keep the same method, model, case type, dataset, route, severity level, or
  comparison family in the same color across every panel and figure.
- Prefer colorblind-friendly, low-saturation colors.
- Use direct labels when they reduce legend lookup.
- Keep font sizes readable at the final publication size.
- Remove chart titles and descriptive panel titles for manuscript figures; the
  caption should explain the figure. Keep only panel letters, axis labels,
  legends, scale bars, direct data labels, and necessary group labels.
- Use thin, quiet grid lines and avoid heavy borders.
- Use black or very dark neutral outlines for bars and other filled marks when
  that improves legibility.
- Show error bars on bar charts when standard error, standard deviation, or
  confidence intervals are available.
- Show 95% CI as horizontal bars, vertical error bars, ribbons, or shaded bands
  for point estimates, trends, smooth curves, or effect-size summaries when
  intervals are available. Do not fabricate intervals from point estimates.
- If the source table has `estimate`, `ci_lower`, and `ci_upper` fields, compute
  uncertainty marks directly from those fields and keep them attached to the
  plotted estimate.
- Put panel labels immediately outside the upper-left corner of each axes,
  fully left of the y-axis. Anchor at `(0, 1)` in axes-fraction coordinates and
  apply a fixed `(-8 pt, +4 pt)` offset with right/bottom alignment. Never use
  `set_title`, data coordinates, or figure-level absolute coordinates for panel
  letters. Render and fail the figure if a label is not left of the axes,
  differs in offset across panels, or is clipped.
- For multi-panel heatmaps, use equal-width data axes, shared row labels only on
  the first panel, and inset/shared colorbars that do not shrink panels
  unequally. Center the union of heatmap data axes on the fixed figure canvas
  within 2% of figure width and require panel-width variation below 1%. If long
  row labels need extra left margin, reserve the same margin on the right. Do
  not rely on asymmetric tight cropping for Word centering.
- Remove unexplained arrows, prompt-like labels, decorative tips, process
  labels, and any text that describes the workflow rather than the scientific
  object.
- Export PNG by default, preferably 600 dpi for paper plots. Export PDF/SVG only
  when the user explicitly requests vector output or a venue/template requires
  it.

Read `references/palette.md` for default palettes and matplotlib settings.
