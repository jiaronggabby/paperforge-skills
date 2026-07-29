# Writing and Story Contract

Load this reference before choosing the title, novelty claim, manuscript
structure, or final prose.

## One scientific line

Define:

1. the real decision or scientific problem;
2. the prediction, observation, patient, station, event, or study unit;
3. the information available at decision time;
4. the uncertainty left unresolved by the strongest matched baseline;
5. one falsifiable primary claim;
6. one primary comparison;
7. one result that would weaken or falsify the claim.

Prefer the smallest mechanism that tests this line. Every physical,
mechanistic, or architectural component needs a proxy, diagnostic,
contribution check, and failure boundary. Do not stack modules to manufacture
novelty.

## Narrative spine

Use:

`problem -> observed gap -> why existing evidence is insufficient -> mechanism
or study design -> matched test -> measured result -> bounded implication`

Make each section serve the same question:

- Title: name the scientific object and contribution without advertising.
- Abstract: state context, gap, method/design, primary evidence, uncertainty,
  and bounded conclusion.
- Introduction: establish what is known, what remains unresolved, why it
  matters, and the exact question tested.
- Methods: make the test reproducible and mirror the claims.
- Results: report observations in protocol order without interpretation drift.
- Discussion: interpret the primary result, compare with verified literature,
  explain failures and limits, and define the supported scope.
- Conclusion: state the bounded answer, not generic significance.

Prioritize reader-facing order when time is limited:

`title -> abstract -> introduction -> key figures -> methods/results details`

## Paragraph contract

Give each paragraph one job:

1. opening claim or observation;
2. concrete evidence or citation;
3. interpretation limited to that evidence;
4. transition only when needed.

Use full paragraphs in manuscripts. Use bullets only when the venue or genre
requires them, such as highlights, checklists, or rebuttals.

Define every abbreviation once and keep terminology stable. After renaming a
method, route, dataset, or integrity concept, audit the full manuscript,
figures, tables, supplement, filenames, and reviewer response for stale names.

## Claim ceiling

Do not claim beyond:

- the tested population and data source;
- the available-information boundary;
- the actual unit of inference;
- the comparator strength;
- the validation depth;
- the observed uncertainty;
- the implemented mechanism;
- the evaluated use case.

Use `associated with` rather than causal language for observational evidence.
Use `internal validation` rather than external/generalizable language when no
independent setting was tested. Use `no evidence of additional benefit` only
when the interval and design support that statement; non-significance alone
does not prove a plateau.

## Low-AI academic prose

Write like a careful human coauthor:

- prefer ordinary verbs and concrete nouns;
- state the evidence before praising importance;
- replace vague praise with measured quantities and scope;
- vary sentence length naturally without manufacturing personality;
- keep necessary uncertainty, but remove stacked hedging;
- state limitations once, specifically, in the correct section;
- preserve the user's established terminology and tone.

Remove:

- generic openings such as `in recent years`, `it is important to note`, and
  `this study highlights`;
- inflated clusters such as `novel`, `robust`, `comprehensive`, `leveraging`,
  `significant potential`, and `shown promise` when unsupported;
- repeated contrast scaffolds such as `not A but B`, `not only`, `rather than`,
  and `this does not mean`;
- reviewer-facing emphasis such as `the key message is` or `this is important
  because`;
- internal workflow language such as `main story`, `paper-facing`, `audit`,
  `route`, `artifact`, `selection firewall`, `corrected-cycle`, and
  `published-style repair`;
- prompt residue, meta-commentary, and explanations of how the text was written.

Do not add invented first-person experiences, opinions, interviews, anecdotes,
humor, or emotional language to make scientific prose sound human.

## Section boundaries

### Introduction

- Begin with the scientific or clinical problem, not the proposed model name.
- Cite the closest evidence, not a long generic field history.
- Distinguish an ingredient already used from a question not yet tested under
  matched controls.
- End with the exact question, design, and contribution.

### Methods

- Follow the real execution order.
- State data sources, dates, inclusion, exclusions, units, split boundaries,
  train-only processing, route definitions, selection, locked test, metrics,
  uncertainty, software, and compute truthfully.
- Keep equations identical to code and evaluator.

### Results

- Follow the predeclared primary-to-secondary order.
- Report estimates, units, intervals, paired units, and sample/seed counts.
- Separate primary, robustness, ablation, external, subgroup, and exploratory
  analyses.
- Report null, unfavorable, and failure evidence without defensive prose.

### Discussion

- Start with the primary answer, not a summary of every result.
- Explain the mechanism only to the level supported by controls.
- Compare with the 20-paper benchmark and strongest close studies.
- Discuss contradictory settings and failure boundaries.
- Avoid converting internal validation into deployment or clinical utility.

## Titles and captions

Use one descriptive title. Do not add a subtitle or tagline unless the venue
requires one.

Make captions stand alone. Identify:

- scientific object and panel mapping;
- population, dataset, region, or subset;
- metric and units;
- comparison and reference;
- uncertainty definition;
- sample, event, fold, region, or seed count;
- evaluation split/status;
- only the directional interpretation supported by the display.

For a multipart figure, treat the caption mapping as a closed set. The figure
registry must contain the exact rendered panel-label list, and the caption must
describe every label exactly once in that order. Each description must identify
the plotted object and relevant subset or metric; do not write “A–D show ...”
without explaining what A, B, C, and D individually show. Do not introduce a
caption label that is absent from the figure. Freeze the venue-required case
(`a, b, c` or `A, B, C`) across all figures; if the venue is unspecified, use
lowercase labels consistently.

Do not put workflow instructions, prompt labels, or unsupported conclusions in
captions.

## Final language pass

Check:

- one term per concept;
- no stale names;
- no internal project-management vocabulary;
- no invented evidence or citations;
- no stronger wording than the claim map permits;
- no repeated filler, caveat, or contrast pattern;
- no AI-like polishing that changes scientific meaning;
- abstract, figures, tables, and conclusion state the same primary result.
