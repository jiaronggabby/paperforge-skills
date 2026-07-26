from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "demo_results.csv"
OUT = ROOT / "demo_figure.png"

PALETTE = {
    "background": "#FFFFFF",
    "text": "#2F3437",
    "grid": "#D9DEE7",
    "reference": "#7A828A",
    "error": "#2F3437",
    "missing": "#B8BEC6",
    "blue": "#4C78A8",
    "teal": "#5AA6A6",
    "purple": "#8E7CC3",
    "slate": "#8A95A5",
    "coral": "#D98373",
    "neutral": "#F7F8FA",
}

METHOD_ORDER = ["Baseline", "Prompt-only", "Audit-only", "PaperForge"]
METHOD_COLORS = {
    "Baseline": PALETTE["slate"],
    "Prompt-only": PALETTE["purple"],
    "Audit-only": PALETTE["teal"],
    "PaperForge": PALETTE["blue"],
}
METHOD_MARKERS = {
    "Baseline": "o",
    "Prompt-only": "s",
    "Audit-only": "^",
    "PaperForge": "D",
}


def read_rows() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def index_rows(rows: list[dict[str, str]]) -> dict[tuple[str, int], dict[str, float]]:
    indexed: dict[tuple[str, int], dict[str, float]] = {}
    numeric = (
        "accuracy",
        "accuracy_ci_low",
        "accuracy_ci_high",
        "f1",
        "f1_ci_low",
        "f1_ci_high",
    )
    for row in rows:
        indexed[(row["method"], int(row["horizon_h"]))] = {
            key: float(row[key]) for key in numeric
        }
    return indexed


def apply_paper_style() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "savefig.dpi": 600,
            "font.family": "DejaVu Sans",
            "font.size": 8.4,
            "axes.labelsize": 8.6,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "legend.fontsize": 7.8,
            "axes.edgecolor": PALETTE["text"],
            "axes.labelcolor": PALETTE["text"],
            "xtick.color": PALETTE["text"],
            "ytick.color": PALETTE["text"],
            "text.color": PALETTE["text"],
            "figure.facecolor": PALETTE["background"],
            "savefig.facecolor": PALETTE["background"],
            "savefig.edgecolor": PALETTE["background"],
        }
    )


def style_axes(ax: plt.Axes, grid_axis: str = "y") -> None:
    ax.set_facecolor(PALETTE["background"])
    ax.grid(
        axis=grid_axis,
        color=PALETTE["grid"],
        linewidth=0.55,
        alpha=0.9,
    )
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for name in ("left", "bottom"):
        ax.spines[name].set_color(PALETTE["text"])
        ax.spines[name].set_linewidth(0.8)
    ax.tick_params(length=3, width=0.7, color=PALETTE["text"])


def add_panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.14,
        1.07,
        label,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=10.5,
        fontweight="bold",
        clip_on=False,
    )


def asymmetric_error(point: float, low: float, high: float) -> np.ndarray:
    return np.array([[point - low], [high - point]])


def draw_grouped_bars(
    ax: plt.Axes,
    indexed: dict[tuple[str, int], dict[str, float]],
    horizon: int,
) -> None:
    metrics = [("accuracy", "Accuracy"), ("f1", "F1")]
    x = np.arange(len(metrics))
    width = 0.17
    offsets = (np.arange(len(METHOD_ORDER)) - 1.5) * width

    for method, offset in zip(METHOD_ORDER, offsets):
        row = indexed[(method, horizon)]
        points = [row[key] for key, _ in metrics]
        lows = [row[f"{key}_ci_low"] for key, _ in metrics]
        highs = [row[f"{key}_ci_high"] for key, _ in metrics]
        yerr = np.array(
            [
                [point - low for point, low in zip(points, lows)],
                [high - point for point, high in zip(points, highs)],
            ]
        )
        ax.bar(
            x + offset,
            points,
            width=width * 0.92,
            color=METHOD_COLORS[method],
            edgecolor=PALETTE["error"],
            linewidth=0.7,
            yerr=yerr,
            error_kw={
                "ecolor": PALETTE["error"],
                "elinewidth": 0.75,
                "capsize": 2.0,
                "capthick": 0.75,
            },
            zorder=3,
        )

    add_panel_label(ax, "a")
    ax.set_ylabel("Score")
    ax.set_xticks(x, [label for _, label in metrics])
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.0, 0.25, 0.50, 0.75, 1.0])
    style_axes(ax)


def draw_horizon_lines(
    ax: plt.Axes,
    indexed: dict[tuple[str, int], dict[str, float]],
    horizons: list[int],
) -> None:
    x = np.asarray(horizons)
    for method in METHOD_ORDER:
        mean = np.array([indexed[(method, horizon)]["accuracy"] for horizon in horizons])
        low = np.array(
            [indexed[(method, horizon)]["accuracy_ci_low"] for horizon in horizons]
        )
        high = np.array(
            [indexed[(method, horizon)]["accuracy_ci_high"] for horizon in horizons]
        )
        ax.fill_between(
            x,
            low,
            high,
            color=METHOD_COLORS[method],
            alpha=0.13,
            linewidth=0,
            zorder=1,
        )
        ax.plot(
            x,
            mean,
            color=METHOD_COLORS[method],
            marker=METHOD_MARKERS[method],
            markersize=4.0,
            markeredgecolor=PALETTE["error"],
            markeredgewidth=0.45,
            linewidth=1.55,
            zorder=3,
        )

    add_panel_label(ax, "b")
    ax.set_xlabel("Forecast horizon (h)")
    ax.set_ylabel("Accuracy")
    ax.set_xticks(horizons)
    ax.set_ylim(0.68, 0.88)
    ax.set_yticks([0.70, 0.75, 0.80, 0.85])
    style_axes(ax)


def effect_interval(
    indexed: dict[tuple[str, int], dict[str, float]],
    method: str,
    horizon: int,
) -> tuple[float, float, float]:
    baseline = indexed[("Baseline", horizon)]
    candidate = indexed[(method, horizon)]
    point = candidate["accuracy"] - baseline["accuracy"]
    low = candidate["accuracy_ci_low"] - baseline["accuracy_ci_high"]
    high = candidate["accuracy_ci_high"] - baseline["accuracy_ci_low"]
    return point, low, high


def draw_forest(
    ax: plt.Axes,
    indexed: dict[tuple[str, int], dict[str, float]],
    horizon: int,
) -> None:
    methods = ["Prompt-only", "Audit-only", "PaperForge"]
    y = np.arange(len(methods))
    ax.axvline(0, color=PALETTE["reference"], linestyle="--", linewidth=0.9, zorder=1)

    for yi, method in zip(y, methods):
        point, low, high = effect_interval(indexed, method, horizon)
        ax.errorbar(
            point,
            yi,
            xerr=asymmetric_error(point, low, high),
            fmt=METHOD_MARKERS[method],
            markersize=5.4,
            markerfacecolor=METHOD_COLORS[method],
            markeredgecolor=PALETTE["error"],
            markeredgewidth=0.65,
            ecolor=PALETTE["error"],
            elinewidth=0.85,
            capsize=2.8,
            capthick=0.85,
            zorder=3,
        )
        ax.text(
            high + 0.005,
            yi,
            f"{point:+.3f}",
            va="center",
            ha="left",
            fontsize=7.1,
        )

    add_panel_label(ax, "c")
    ax.set_xlabel(f"Accuracy difference vs baseline ({horizon} h)")
    ax.set_yticks(y, methods)
    ax.set_xlim(-0.04, 0.12)
    ax.set_xticks([-0.04, 0.00, 0.04, 0.08, 0.12])
    ax.invert_yaxis()
    style_axes(ax, grid_axis="x")


def draw_effect_heatmap(
    ax: plt.Axes,
    indexed: dict[tuple[str, int], dict[str, float]],
    horizons: list[int],
) -> np.ndarray:
    methods = ["Prompt-only", "Audit-only", "PaperForge"]
    matrix = np.array(
        [
            [
                indexed[(method, horizon)]["accuracy"]
                - indexed[("Baseline", horizon)]["accuracy"]
                for horizon in horizons
            ]
            for method in methods
        ]
    )
    limit = max(abs(matrix.min()), abs(matrix.max()))
    cmap = LinearSegmentedColormap.from_list(
        "paperforge_effect",
        [PALETTE["coral"], PALETTE["neutral"], PALETTE["blue"]],
    )
    image = ax.imshow(
        matrix,
        cmap=cmap,
        norm=TwoSlopeNorm(vmin=-limit, vcenter=0.0, vmax=limit),
        aspect="equal",
    )

    add_panel_label(ax, "d")
    ax.set_xlabel("Forecast horizon (h)")
    ax.set_xticks(np.arange(len(horizons)), horizons)
    ax.set_yticks(np.arange(len(methods)), methods)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    colorbar = ax.figure.colorbar(image, ax=ax, fraction=0.045, pad=0.035)
    colorbar.set_label("Accuracy difference vs baseline", fontsize=7.8)
    colorbar.ax.tick_params(labelsize=7.0, length=2)
    colorbar.outline.set_linewidth(0.6)
    return matrix


def draw_exact_value_table(
    ax: plt.Axes,
    matrix: np.ndarray,
    horizons: list[int],
) -> None:
    methods = ["Prompt-only", "Audit-only", "PaperForge"]
    ax.axis("off")
    table = ax.table(
        cellText=[
            [method, *[f"{value:+.3f}" for value in row]]
            for method, row in zip(methods, matrix)
        ],
        colLabels=["Method", *[f"{h} h" for h in horizons]],
        colWidths=[0.30, 0.175, 0.175, 0.175, 0.175],
        cellLoc="center",
        loc="center",
        bbox=[0.0, 0.12, 1.0, 0.76],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(7.2)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(PALETTE["grid"])
        cell.set_linewidth(0.6)
        if row == 0:
            cell.set_facecolor("#EEF1F5")
            cell.set_text_props(weight="bold", color=PALETTE["text"])
        elif col == 0:
            cell.set_facecolor("#F7F8FA")
            cell.set_text_props(color=PALETTE["text"], ha="left")
        else:
            cell.set_facecolor(PALETTE["background"])
            cell.set_text_props(color=PALETTE["text"])
    add_panel_label(ax, "e")
    ax.text(
        0.5,
        0.02,
        "Exact accuracy difference vs baseline",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=8.4,
        color=PALETTE["text"],
    )


def main() -> int:
    indexed = index_rows(read_rows())
    horizons = sorted({horizon for _, horizon in indexed})
    apply_paper_style()

    fig = plt.figure(figsize=(9.6, 5.25))
    grid = fig.add_gridspec(
        2,
        6,
        left=0.075,
        right=0.975,
        bottom=0.105,
        top=0.90,
        wspace=1.05,
        hspace=0.48,
    )
    ax_bars = fig.add_subplot(grid[0, 0:3])
    ax_lines = fig.add_subplot(grid[0, 3:6])
    ax_forest = fig.add_subplot(grid[1, 0:2])
    ax_heatmap = fig.add_subplot(grid[1, 2:4])
    ax_values = fig.add_subplot(grid[1, 4:6])

    draw_grouped_bars(ax_bars, indexed, horizon=24)
    draw_horizon_lines(ax_lines, indexed, horizons)
    draw_forest(ax_forest, indexed, horizon=24)
    matrix = draw_effect_heatmap(ax_heatmap, indexed, horizons)
    draw_exact_value_table(ax_values, matrix, horizons)

    handles = [
        Line2D(
            [0],
            [0],
            color=METHOD_COLORS[method],
            marker=METHOD_MARKERS[method],
            markeredgecolor=PALETTE["error"],
            markeredgewidth=0.45,
            linewidth=1.5,
            markersize=5.0,
            label=method,
        )
        for method in METHOD_ORDER
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.52, 0.995),
        ncol=4,
        frameon=False,
        handletextpad=0.45,
        columnspacing=1.35,
    )
    fig.savefig(OUT, bbox_inches="tight", pad_inches=0.04)
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
