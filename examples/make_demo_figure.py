from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "demo_results.csv"
OUT = ROOT / "demo_figure.png"

PALETTE = {
    "text": "#2F3437",
    "muted": "#6B7280",
    "grid": "#D9DEE7",
    "rule": "#111827",
    "white": "#FFFFFF",
    "blue": "#4C78A8",
    "teal": "#5AA6A6",
    "slate": "#8A95A5",
}

METHOD_COLORS = {
    "Baseline": PALETTE["blue"],
    "Prompt-only": PALETTE["slate"],
    "PaperForge": PALETTE["teal"],
}


def read_rows() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def values(rows: list[dict[str, str]], column: str) -> list[float]:
    return [float(row[column]) for row in rows]


def ci_yerr(point: list[float], low: list[float], high: list[float]) -> np.ndarray:
    return np.array([[p - lo for p, lo in zip(point, low)], [hi - p for p, hi in zip(point, high)]])


def apply_paper_style() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 600,
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.titlesize": 10,
            "axes.labelsize": 8.5,
            "xtick.labelsize": 7.6,
            "ytick.labelsize": 7.6,
            "legend.fontsize": 8,
            "axes.edgecolor": PALETTE["rule"],
            "axes.labelcolor": PALETTE["text"],
            "xtick.color": PALETTE["text"],
            "ytick.color": PALETTE["text"],
            "text.color": PALETTE["text"],
            "grid.color": PALETTE["grid"],
            "grid.linewidth": 0.55,
            "figure.facecolor": PALETTE["white"],
            "savefig.facecolor": PALETTE["white"],
            "savefig.edgecolor": PALETTE["white"],
        }
    )


def style_panel(ax: plt.Axes, grid_axis: str = "y") -> None:
    ax.set_facecolor(PALETTE["white"])
    ax.grid(axis=grid_axis, color=PALETTE["grid"], linewidth=0.55)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color(PALETTE["rule"])
        spine.set_linewidth(1.0)
    ax.tick_params(length=3, width=0.8, color=PALETTE["rule"])


def add_panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.07,
        1.07,
        label,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=11,
        fontweight="bold",
    )


def draw_bar_panel(
    ax: plt.Axes,
    methods: list[str],
    accuracy: list[float],
    accuracy_low: list[float],
    accuracy_high: list[float],
    f1: list[float],
    f1_low: list[float],
    f1_high: list[float],
) -> None:
    metric_names = ["Accuracy", "F1"]
    x = np.arange(len(metric_names))
    width = 0.22
    offsets = np.linspace(-width, width, len(methods))
    metric_points = [accuracy, f1]
    metric_low = [accuracy_low, f1_low]
    metric_high = [accuracy_high, f1_high]

    for method_index, (method, offset) in enumerate(zip(methods, offsets)):
        points = [metric_points[i][method_index] for i in range(len(metric_names))]
        lows = [metric_low[i][method_index] for i in range(len(metric_names))]
        highs = [metric_high[i][method_index] for i in range(len(metric_names))]
        yerr = ci_yerr(points, lows, highs)
        bars = ax.bar(
            x + offset,
            points,
            width=width,
            color=METHOD_COLORS[method],
            edgecolor=PALETTE["rule"],
            linewidth=0.8,
            yerr=yerr,
            error_kw={"ecolor": PALETTE["rule"], "elinewidth": 0.8, "capsize": 2.4, "capthick": 0.8},
            zorder=3,
        )
        for bar, value in zip(bars, points):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value + 0.007,
                f"{value:.2f}",
                ha="center",
                va="bottom",
                fontsize=6.8,
                color=PALETTE["muted"],
            )

    add_panel_label(ax, "a")
    ax.set_ylabel("Score")
    ax.set_xticks(x, metric_names)
    ax.set_ylim(0.70, 0.89)
    ax.set_yticks([0.70, 0.75, 0.80, 0.85])
    style_panel(ax)


def draw_ci_band_panel(
    ax: plt.Axes,
    methods: list[str],
    calibration: list[float],
    calibration_low: list[float],
    calibration_high: list[float],
) -> None:
    y = np.arange(len(methods))
    for yi, method, point, low, high in zip(y, methods, calibration, calibration_low, calibration_high):
        ax.hlines(yi, low, high, color=METHOD_COLORS[method], linewidth=7.5, alpha=0.42, zorder=2)
        ax.errorbar(
            point,
            yi,
            xerr=np.array([[point - low], [high - point]]),
            fmt="o",
            markersize=5.4,
            markerfacecolor=METHOD_COLORS[method],
            markeredgecolor=PALETTE["rule"],
            markeredgewidth=0.7,
            ecolor=PALETTE["rule"],
            elinewidth=0.85,
            capsize=3,
            capthick=0.85,
            zorder=3,
        )
        ax.text(high + 0.002, yi, f"{point:.3f}", va="center", ha="left", fontsize=7.0, color=PALETTE["muted"])

    add_panel_label(ax, "b")
    ax.set_xlabel("Calibration error")
    ax.set_yticks(y, methods)
    ax.set_xlim(0.04, 0.108)
    ax.set_xticks([0.05, 0.075, 0.10])
    ax.invert_yaxis()
    style_panel(ax, grid_axis="x")


def draw_tradeoff_panel(
    ax: plt.Axes,
    methods: list[str],
    accuracy: list[float],
    accuracy_low: list[float],
    accuracy_high: list[float],
    calibration: list[float],
    calibration_low: list[float],
    calibration_high: list[float],
) -> None:
    for method, acc, acc_low, acc_high, cal, cal_low, cal_high in zip(
        methods,
        accuracy,
        accuracy_low,
        accuracy_high,
        calibration,
        calibration_low,
        calibration_high,
    ):
        ax.errorbar(
            acc,
            cal,
            xerr=np.array([[acc - acc_low], [acc_high - acc]]),
            yerr=np.array([[cal - cal_low], [cal_high - cal]]),
            fmt="o",
            markersize=6.5,
            markerfacecolor=METHOD_COLORS[method],
            markeredgecolor=PALETTE["rule"],
            markeredgewidth=0.8,
            ecolor=PALETTE["rule"],
            elinewidth=0.8,
            capsize=2.8,
            capthick=0.8,
            zorder=3,
        )
        ax.text(
            acc + 0.003,
            cal,
            method,
            va="center",
            ha="left",
            fontsize=7.2,
            color=PALETTE["text"],
            bbox={"facecolor": PALETTE["white"], "edgecolor": "none", "alpha": 0.86, "pad": 0.6},
        )

    add_panel_label(ax, "c")
    ax.set_xlabel("Accuracy")
    ax.set_ylabel("Calibration error")
    ax.set_xlim(0.74, 0.88)
    ax.set_ylim(0.04, 0.105)
    ax.set_xticks([0.75, 0.80, 0.85])
    ax.set_yticks([0.05, 0.075, 0.10])
    style_panel(ax)


def main() -> int:
    rows = read_rows()
    methods = [row["method"] for row in rows]
    accuracy = values(rows, "accuracy")
    accuracy_low = values(rows, "accuracy_ci_low")
    accuracy_high = values(rows, "accuracy_ci_high")
    f1 = values(rows, "f1")
    f1_low = values(rows, "f1_ci_low")
    f1_high = values(rows, "f1_ci_high")
    calibration = values(rows, "calibration_error")
    calibration_low = values(rows, "calibration_ci_low")
    calibration_high = values(rows, "calibration_ci_high")

    apply_paper_style()

    fig = plt.figure(figsize=(7.45, 4.55), facecolor=PALETTE["white"])
    gs = fig.add_gridspec(
        2,
        2,
        width_ratios=[1.15, 1.0],
        height_ratios=[1.0, 0.93],
        left=0.105,
        right=0.965,
        bottom=0.105,
        top=0.84,
        wspace=0.30,
        hspace=0.50,
    )
    ax_bar = fig.add_subplot(gs[0, 0])
    ax_ci = fig.add_subplot(gs[0, 1])
    ax_tradeoff = fig.add_subplot(gs[1, :])

    draw_bar_panel(ax_bar, methods, accuracy, accuracy_low, accuracy_high, f1, f1_low, f1_high)
    draw_ci_band_panel(ax_ci, methods, calibration, calibration_low, calibration_high)
    draw_tradeoff_panel(ax_tradeoff, methods, accuracy, accuracy_low, accuracy_high, calibration, calibration_low, calibration_high)

    handles = [
        Line2D([0], [0], color=METHOD_COLORS[method], marker="s", linestyle="", markersize=7, label=method)
        for method in methods
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.58, 0.945),
        ncol=3,
        frameon=False,
        handletextpad=0.45,
        columnspacing=1.3,
    )
    fig.add_artist(
        Rectangle(
            (0.012, 0.018),
            0.976,
            0.955,
            transform=fig.transFigure,
            fill=False,
            edgecolor=PALETTE["rule"],
            linewidth=1.45,
            zorder=20,
        )
    )

    fig.savefig(OUT, bbox_inches="tight", pad_inches=0.05)
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
