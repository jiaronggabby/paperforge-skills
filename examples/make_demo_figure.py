from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "demo_results.csv"
OUT = ROOT / "demo_figure.png"

COLORS = {
    "indigo": "#315C99",
    "cyan": "#00A6A6",
    "magenta": "#B23A8E",
    "amber": "#E6A23C",
    "ink": "#24313D",
    "muted": "#667085",
    "grid": "#DDE3EA",
    "panel": "#F8FAFC",
}


def read_rows() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    rows = read_rows()
    methods = [row["method"] for row in rows]
    accuracy = [float(row["accuracy"]) for row in rows]
    f1 = [float(row["f1"]) for row in rows]
    calibration = [float(row["calibration_error"]) for row in rows]

    x = np.arange(len(methods))
    width = 0.32

    plt.rcParams.update({
        "figure.dpi": 150,
        "savefig.dpi": 600,
        "font.size": 10,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "axes.edgecolor": "#AAB4C0",
        "axes.labelcolor": COLORS["ink"],
        "xtick.color": COLORS["ink"],
        "ytick.color": COLORS["ink"],
        "grid.color": COLORS["grid"],
        "grid.linewidth": 0.6,
    })

    fig = plt.figure(figsize=(8.4, 4.9), facecolor="white")
    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[1.35, 1.0],
        wspace=0.25,
        left=0.08,
        right=0.98,
        bottom=0.12,
        top=0.76,
    )
    ax_score = fig.add_subplot(gs[0, 0])
    ax_cal = fig.add_subplot(gs[0, 1])

    for ax in (ax_score, ax_cal):
        ax.set_facecolor(COLORS["panel"])
        panel = FancyBboxPatch(
            (-0.08, -0.16),
            1.16,
            1.28,
            boxstyle="round,pad=0.018,rounding_size=0.035",
            linewidth=0,
            facecolor=COLORS["panel"],
            transform=ax.transAxes,
            clip_on=False,
            zorder=-10,
        )
        ax.add_patch(panel)

    bars_a = ax_score.bar(
        x - width / 2,
        accuracy,
        width,
        label="Accuracy",
        color=COLORS["indigo"],
        edgecolor="white",
        linewidth=0.7,
    )
    bars_f = ax_score.bar(
        x + width / 2,
        f1,
        width,
        label="F1",
        color=COLORS["cyan"],
        edgecolor="white",
        linewidth=0.7,
    )
    ax_score.set_ylim(0.70, 0.88)
    ax_score.set_ylabel("Score")
    ax_score.set_xticks(x)
    ax_score.set_xticklabels(methods)
    ax_score.grid(axis="y")
    ax_score.spines["top"].set_visible(False)
    ax_score.spines["right"].set_visible(False)
    ax_score.legend(loc="upper left", frameon=False, ncol=2)
    ax_score.set_title("Outcome quality", loc="left", fontweight="bold", color=COLORS["ink"])

    gain = (accuracy[-1] - accuracy[0]) * 100
    ax_score.annotate(
        f"+{gain:.1f} pts",
        xy=(x[-1] - width / 2, accuracy[-1]),
        xytext=(x[-1] - 0.6, accuracy[-1] + 0.018),
        arrowprops=dict(arrowstyle="-|>", color=COLORS["magenta"], lw=1.3),
        color=COLORS["magenta"],
        fontweight="bold",
    )

    for bars in (bars_a, bars_f):
        for bar in bars:
            height = bar.get_height()
            ax_score.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.004,
                f"{height:.2f}",
                ha="center",
                va="bottom",
                fontsize=8,
                color=COLORS["muted"],
            )

    ax_cal.plot(
        x,
        calibration,
        marker="o",
        markersize=7,
        linewidth=2.6,
        color=COLORS["amber"],
        markeredgecolor="white",
        markeredgewidth=1.2,
    )
    ax_cal.fill_between(x, calibration, [max(calibration)] * len(calibration), color=COLORS["amber"], alpha=0.16)
    ax_cal.set_ylim(0.045, 0.098)
    ax_cal.set_xticks(x)
    ax_cal.set_xticklabels(methods, rotation=18, ha="right")
    ax_cal.set_ylabel("Calibration error")
    ax_cal.grid(axis="y")
    ax_cal.spines["top"].set_visible(False)
    ax_cal.spines["right"].set_visible(False)
    ax_cal.set_title("Calibration discipline", loc="left", fontweight="bold", color=COLORS["ink"])
    ax_cal.annotate(
        "lower is better",
        xy=(x[-1], calibration[-1]),
        xytext=(x[-1] - 1.25, calibration[-1] + 0.011),
        arrowprops=dict(arrowstyle="-|>", color=COLORS["ink"], lw=1.0),
        color=COLORS["ink"],
        fontsize=9,
    )

    fig.suptitle("PaperForge demo: evidence-aware reporting workflow", x=0.04, y=0.97, ha="left", fontsize=14, fontweight="bold", color=COLORS["ink"])
    fig.text(
        0.04,
        0.90,
        "A compact example of metric reporting, calibrated interpretation, and journal-style visual polish.",
        ha="left",
        va="top",
        fontsize=9.5,
        color=COLORS["muted"],
    )

    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
