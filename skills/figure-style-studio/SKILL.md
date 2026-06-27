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
- Prefer colorblind-friendly, low-saturation colors.
- Use direct labels when they reduce legend lookup.
- Keep font sizes readable at the final publication size.
- Remove chart titles when the manuscript caption already names the figure.
- Use thin, quiet grid lines and avoid heavy borders.
- Export PNG at 300-600 dpi for raster use; export PDF/SVG when vector output is
  needed.

Read `references/palette.md` for default palettes and matplotlib settings.
