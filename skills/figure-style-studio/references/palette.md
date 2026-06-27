# Figure palettes

## Default muted palette

Use this palette for most academic figures:

| Role | Hex |
| --- | --- |
| Blue | `#4C78A8` |
| Teal | `#5AA6A6` |
| Sage | `#7A9E7E` |
| Gold | `#D8A657` |
| Coral | `#D98373` |
| Slate | `#8A95A5` |
| Purple | `#8E7CC3` |

## Neutral colors

| Role | Hex |
| --- | --- |
| Background | `#FFFFFF` |
| Soft background | `#F7F8FA` |
| Text | `#2F3437` |
| Grid | `#D9DEE7` |
| Light rule | `#E8ECF2` |

## Matplotlib defaults

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 600,
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.edgecolor": "#8A95A5",
    "axes.labelcolor": "#2F3437",
    "xtick.color": "#2F3437",
    "ytick.color": "#2F3437",
    "grid.color": "#D9DEE7",
    "grid.linewidth": 0.6,
    "axes.grid": True,
    "axes.spines.top": False,
    "axes.spines.right": False,
})
```

## Avoid

- rainbow colormaps for ordinal or continuous scientific data;
- saturated red/green pairings;
- decorative shadows and gradients;
- low-contrast labels;
- crowded legends;
- 3D chart effects.
