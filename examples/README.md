# Examples

This folder contains a small reproducible demo for the figure workflow.

Run:

```powershell
python examples/make_demo_figure.py
```

The script reads illustrative synthetic values from `demo_results.csv` and
writes `demo_figure.png`, a four-panel example of the PaperForge visual
contract: zero-based grouped bars, horizon trends with 95% confidence bands, a
forest comparison against the baseline, and a signed-effect heatmap. Method
colors remain fixed, uncertainty uses neutral/dark marks, and paper panels carry
no plot titles.
