---
name: research-ideation
description: Generate and refine research ideas from a topic, literature set, method family, dataset, or problem statement. Use when the user asks for research directions, novelty analysis, proposal drafting, idea ranking, experiment design, or turning a rough concept into a manuscript-quality research plan.
---

# Research Ideation

Use this skill to move from a broad topic to ranked, testable research
directions. Work from provided papers, notes, datasets, constraints, and current
field context. Do not depend on private memory.

## Workflow

1. Ground the topic.
   - Identify the domain, target venue or field, available data, constraints,
     likely baselines, and evaluation standard.

2. Map the literature gap.
   - What has been solved?
   - What remains weak, expensive, brittle, under-validated, or poorly explained?
   - Which assumptions are repeated without enough testing?

3. Generate candidates from three angles.
   - Innovator: higher-risk idea with stronger novelty.
   - Pragmatist: feasible idea using available data and tools.
   - Critic: idea designed to fix a known weakness or avoid a common failure.

4. Stress-test each candidate.
   - Novelty
   - Feasibility
   - Data availability
   - Evaluation clarity
   - Baseline strength
   - Failure modes
   - Paper story

5. Rank and expand.
   - Rank ideas for the user's stated goal.
   - Expand the best idea into problem, hypothesis, method, experiments,
     expected figures, risks, and first implementation steps.

## Output

Return a compact idea table plus a detailed plan for the top direction. Keep
claims conditional until literature or experiments support them.
