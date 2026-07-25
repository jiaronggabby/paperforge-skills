# Figure, Color, and Chart Contract

Load this reference before creating, revising, or accepting any paper figure,
table-as-figure, map, workflow diagram, or result graphic.

## Freeze a figure registry

Copy
[figure-style-registry.template.json](../assets/figure-style-registry.template.json)
to the project internal work area. Before drawing, record:

- figure ID, scientific question, and manuscript claim ID;
- canonical data source and SHA256;
- plotting code and commit;
- sample/unit, split, metric, direction, and uncertainty;
- final surface and physical dimensions;
- palette version and semantic role of color, marker, line style, and lightness;
- caption, render, visual-review, and evidence-review status.

Assign a color by scientific identity, never by current plotting order. Freeze
the mapping once and reuse it across all panels, figures, tables-as-figures, and
slides. Change it only through an explicit registry update.

## Core visual system

### Structural neutrals

Use:

- background: `#FFFFFF`;
- text and axes: `#2F3437`;
- grid/rules: `#D9DEE7`;
- reference line: `#7A828A`;
- error bars and outlines: `#2F3437`;
- missing or unavailable: `#B8BEC6`.

Keep grids thin and quiet. Avoid colored axes, heavy shadows, gradients, glossy
effects, and decorative backgrounds.

### PaperForge muted categorical palette

Use this approved default for methods, models, routes, cohorts, or comparison
families when no project-specific registry exists:

- muted blue: `#4C78A8`;
- teal: `#5AA6A6`;
- sage: `#7A9E7E`;
- gold: `#D8A657`;
- coral: `#D98373`;
- slate: `#8A95A5`;
- muted purple: `#8E7CC3`.

Default semantic mapping:

- baseline/reference: slate;
- primary method: muted blue;
- secondary method: muted purple;
- ablation or mechanism control: teal;
- supporting cohort/group: sage;
- warning, adverse direction, or failure: coral;
- single emphasis or budget/cost highlight: gold.

Do not automatically color the proposed method red, green, or gold. Do not give
`ours` a new color in each figure.

Use at most six active categorical accents in one normal paper panel. When more
identities exist, facet, use direct labels, add line/marker styles, or move the
complete comparison to a table.

### Aggregation-method palette

Use this fixed approved mapping when the scientific comparison is aggregation
strategy:

- mean: `#4F81BD`;
- top-2 mean: `#8064A2`;
- max: `#F79646`;
- fourth strategy: `#4BACC6`;
- fifth strategy or adverse control: `#C0504D`;
- sixth strategy: `#9BBB59`.

Use charcoal outlines and error bars. Do not reuse these colors for unrelated
methods in the same paper.

### Coast/PRIME palette

Use only for an explicitly identified CoastGATE, PRIME, TopoLead, EventOT, or
closely related coastal visual identity:

- Deep Navy `#0B1D33`;
- Dusk Blue `#2B4A6F`;
- Steel Blue `#5A6F8C`;
- Soft Peach `#F7D9C6`;
- Sunset Orange `#F08A4B`;
- Warm Amber `#FDBA4D`;
- Charcoal `#1B1F24`;
- Pale Gray-Blue `#E8EDF3`.

Use Charcoal for outlines/error bars and reserve warm colors for event,
extreme, anomaly, or emphasis roles defined in the registry. Do not let this
project-specific palette override medical or generic PaperForge figures.

## Encoding hierarchy

Use one declared semantic role per visual channel:

| Meaning | Preferred channel |
|---|---|
| method/model identity | fixed categorical color |
| dataset/cohort/site | marker, line style, facet, or shape |
| horizon/time/order | x-position, line style, or ordered lightness |
| severity/ordinal category | ordered lightness or sequential scale |
| signed effect/change | diverging scale centered at the scientific null |
| uncertainty | charcoal interval or same-hue low-alpha band |
| baseline/reference | neutral color and/or reference line |
| missing data | gray hatch or explicit missing token |
| significance | exact text/symbol plus estimate and interval, never color alone |

Color must not carry two unrelated categorical variables. Provide a redundant
cue when color is scientifically essential so the figure survives grayscale
and common color-vision deficiencies.

## Sequential and diverging scales

For nonnegative magnitude, count, intensity, prevalence, or error, use a
perceptually ordered sequential scale derived from a declared approved hue.
Label the colorbar with units. Never map missing values to zero.

For signed effects, residuals, gains/losses, or anomalies:

- use a diverging scale;
- center it on the scientifically meaningful zero or null;
- use symmetric limits when defensible;
- label direction explicitly;
- provide signs, annotations, or another redundant cue;
- do not use red/green as the only distinction.

Never use rainbow, `jet`, or an unordered multi-hue scale for ordered data.

## Uncertainty

When intervals exist, display them unless the venue or figure purpose makes the
display unreadable and the exact values are provided nearby.

- Use charcoal error bars on light/muted fills.
- Use same-hue confidence bands at approximately `0.10-0.18` alpha.
- State CI/SD/SE/bootstrap type, paired unit, sample or seed count in the
  caption.
- Do not reconstruct an interval from a point estimate or AUC alone.
- Do not encode significance only by saturation or opacity.
- Avoid multiple overlapping confidence bands when blending destroys meaning;
  facet or use interval plots instead.

## Chart selection and rules

### Bar charts

Use only for a small number of discrete categorical magnitudes.

- Order groups by protocol or a prespecified rule.
- Use color for method identity only.
- Use dark neutral outlines around muted fills, approximately `0.8-1.0 pt`.
- Show supported uncertainty with charcoal caps.
- Start magnitude bars at zero. For tightly clustered AUC or effect estimates,
  prefer dot/interval or forest plots instead of a truncated bar axis.
- Avoid 3D bars, gradients, stacked bars without a compositional question, and
  a different color for every metric.
- Do not label every bar when labels collide; provide a table or selective
  direct labels.

### Dot and interval plots

Prefer for model comparisons, tightly clustered metrics, effect sizes, paired
changes, and multi-region or multi-seed summaries.

- Show the exact point estimate and interval.
- Include a neutral reference line when a scientific null exists.
- Preserve ordering across panels.
- Use position for value, color for method, and shape/facet for cohort.

### Line charts

Use for ordered horizons, time, budget, threshold, or continuous x-values.

- Use fixed method colors.
- Add markers when curves are close or grayscale matters.
- Use same-hue low-alpha confidence bands.
- Use a neutral dashed no-skill/reference line.
- Do not smooth or interpolate in a way that changes the scientific claim.
- Separate panels when units or scales differ.
- Place legends outside the data region when they cover curves or bands.

### Forest plots

Use for effects or paired differences with intervals.

- Show point, lower bound, upper bound, unit, and comparator from the canonical
  source table.
- Use charcoal intervals and a neutral dashed null line.
- Use a log scale for ratio measures when appropriate and label it.
- Do not imply significance through color intensity.
- Keep subgroup hierarchy and sample sizes visible.

### ROC and precision-recall curves

Generate curves from raw predictions or valid fold-level curve data.

- Do not simulate ROC/PR curves from AUC/AP alone.
- Use fixed method colors.
- Use a neutral dashed ROC diagonal.
- Use and label the prevalence-based PR baseline.
- Avoid filled area under every curve.
- Highlight the predeclared primary comparison by line width or ordering, not a
  new ad hoc color.
- Report AUC/AP with uncertainty in the legend or accompanying table.
- State cohort, positive class, averaging method, and uncertainty in the
  caption.

### Calibration plots

- Use fixed method colors and a neutral dashed perfect-calibration line.
- Show same-hue bands or neutral pointwise intervals when supported.
- Include bin counts, rug, or sample-size information when sparse bins matter.
- Keep discrimination, calibration, and threshold performance distinct.
- Do not use a heatmap palette to imply good/bad calibration.

### Distribution plots

Use box, violin, raincloud, ECDF, histogram, or raw points when the distribution
is the evidence.

- Show individual observations or a faithful distribution when feasible.
- State the aggregation and sample unit.
- Do not replace a skewed or multimodal distribution with a mean-only bar.
- Avoid violin smoothing that implies unsupported density detail for very small
  samples.

### Heatmaps and confusion matrices

- Use sequential fill for nonnegative magnitude/frequency.
- Use diverging fill only for signed residual/change and center it at zero.
- Label axes and colorbar units.
- Use a neutral missing-data token or hatch.
- Use square cells for conceptually square matrices.
- Omit in-cell values when too small; put exact values in a supplement table.
- Do not use method identity colors as a heatmap scale.
- Use a sequential scale for confusion counts/proportions unless displaying
  signed residuals.

### Ablation plots

- Order configurations by the prespecified mechanism logic.
- Prefer differences from the full model with a zero-reference interval plot.
- Keep the main method color fixed; use position, marker, labels, or binary
  component indicators rather than a new hue for every configuration.
- Show uncertainty for repeated runs.
- Separate architecture, data, loss, and training-protocol ablations.
- Do not claim causal component contribution from one uncontrolled comparison.
- Retain non-winning and null ablations.

### Maps

- Use formal, versioned geography and verified coordinates.
- Use sequential color for scalar magnitude and diverging color for signed
  anomalies.
- Keep coastlines, borders, station markers, and topology masks structurally
  neutral unless the registry assigns a scientific role.
- Include units, projection, scale bar, and north arrow when appropriate.
- Never use generated geography, decorative terrain, screenshots, or invented
  coordinates as scientific map data.
- Inspect clipping, extent, labels, colorbar, and station overlap at final size.

### Workflow and architecture diagrams

- Use color for logical groups or data types, not decoration.
- Use one accent per logical group, not per box.
- Keep arrows neutral unless color encodes a documented flow type.
- Distinguish data, control, optional, and error paths by line style.
- Match every component, equation, arrow, and label to the implementation.
- Do not draw a richer architecture than the code supports.
- Check AI-generated raster labels or overlay them natively before delivery.

### Tables and tables-as-figures

- Use black text, white background, three-line rules, and no vertical rules or
  colored evidence cells in the main manuscript.
- Use color only for an optional restrained method key or supplemental visual.
- Preserve exact values, units, sample/seed count, uncertainty, and comparison
  direction.
- Put estimates and intervals on separate lines when dense.
- Do not encode significance by cell color alone.
- Place table captions above tables and figure captions below figures.

## Titles, labels, and legends

Paper plots carry no figure title or descriptive panel title by default. Keep
only:

- panel letters;
- axis and colorbar labels with units;
- tick labels;
- legends;
- scale bars;
- direct data labels;
- necessary group labels.

Use the manuscript caption for context. Slides may use a concise action title,
but the embedded result figure keeps the same semantic mapping.

Place panel letters in reserved outer margins, not above a bar, point, tick, or
error bar. Keep legends outside the data region whenever overlap is possible.
Avoid unexplained arrows, decorative callouts, workflow tips, and prompt-like
labels.

## Export contract

Preserve:

- canonical source data;
- plotting script or generation recipe;
- figure registry/manifest;
- vector master (`PDF` or `SVG`) for native plots when accepted;
- `600 dpi` PNG at final physical dimensions for Word, raster-only venues, and
  compatibility;
- `300 dpi` PNG only for slide previews or explicit venue requirements.

Use a white facecolor. Embed portable fonts when possible. Do not judge layout
from a loose high-resolution canvas; render at the actual single-column,
double-column, page, or slide size.

## Acceptance checklist

Mark every item `PASS`, `FAIL`, or `WAIVED` with a reason.

### Provenance

- source artifact exists and its hash is recorded;
- plot script/recipe and code commit exist;
- values come from data/code, not screenshots;
- units, metric direction, split, and sample unit are recorded;
- no fabricated values, intervals, labels, or geography;
- source conflicts are resolved or explicitly blocked.

### Semantic system

- palette version and role mapping are declared;
- fixed entity colors match the project registry;
- uncertainty, dataset, severity, and method are not conflated;
- no rainbow or red/green-only critical encoding;
- critical distinctions survive grayscale;
- no more than six dense categorical accents.

### Statistical display

- sample/seed count and uncertainty type are stated;
- supported intervals are visible;
- no interval is reconstructed from a point estimate;
- baseline/reference and metric direction are correct;
- exact values remain recoverable from a source table.

### Typography and geometry

- no unsupported plot title or prompt residue;
- caption contains required evidence fields;
- axes/colorbars include units;
- method names and acronyms match the manuscript;
- text is legible at final size;
- no clipping, overlap, collision, cropped colorbar, or invisible error cap;
- panel proportions, spacing, and alignment are consistent.

### Files and embedding

- vector and raster outputs meet the declared requirement;
- PNG dimensions match final size and DPI;
- Word contains the expected image objects and captions;
- PDF/DOCX/LaTeX renders successfully;
- originals remain unchanged;
- one final-size visual inspection, one grayscale inspection, and one
  data/provenance comparison are recorded.

Do not call a high-stakes figure complete on automated checks alone. Require an
independent visual critic or second inspection for the main figure set.
