"""Figures 2-5 of the CADIS paper, built from the causal-evaluation results.

Run from the causal-evaluation repository so its environment and data are used:

    cd ~/Repositorios/causal-evaluation
    uv run python ../tesispp/cadis-extended-abstract/figures/make_figures.py

Also prints the numbers quoted in the Results section (AUROC, equivalence bounds,
cell-level accuracies) so the text can be checked against the figures.
"""

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import gaussian_kde

CE_ROOT = Path(os.environ.get("CE_ROOT", Path.home() / "Repositorios" / "causal-evaluation"))
sys.path.insert(0, str(CE_ROOT / "src"))

from causal_evaluation.evaluation.stats import wilson_ci  # noqa: E402
from causal_evaluation.evaluation.variant_analysis import (  # noqa: E402
    load_scored,
    paired_accuracy_gap,
    p_yes_shift,
)

INTERIM = CE_ROOT / "data" / "interim"
FIG_DIR = Path(__file__).resolve().parent

# Two categorical slots, validated for CVD separation (dataviz palette, light mode).
BLUE, ORANGE = "#2a78d6", "#eb6834"
GRAY, INK, MUTED = "#8a8985", "#1f1f1e", "#6b6a66"
EQUIV = 0.04  # smallest effect of interest for H1 / H1b, see Sect. 4.6

MODELS = ["SmolLM2-1.7B-Instruct", "Qwen2.5-1.5B-Instruct", "Phi-3.5-mini-instruct", "Qwen2.5-7B-Instruct"]
LABEL = {
    "SmolLM2-1.7B-Instruct": "SmolLM2-1.7B",
    "Qwen2.5-1.5B-Instruct": "Qwen2.5-1.5B",
    "Phi-3.5-mini-instruct": "Phi-3.5-mini (3.8B)",
    "Qwen2.5-7B-Instruct": "Qwen2.5-7B",
}
QUERY_ORDER = [  # grouped by rung
    ("marginal", 1), ("correlation", 1), ("exp_away", 1),
    ("ate", 2), ("backadj", 2), ("collider_bias", 2),
    ("ett", 3), ("nde", 3), ("nie", 3), ("det-counterfactual", 3),
]
QUERY_LABEL = {
    "marginal": "marginal", "correlation": "conditional", "exp_away": "explain away",
    "ate": "ATE", "backadj": "adjustment set", "collider_bias": "collider bias",
    "ett": "ETT", "nde": "NDE", "nie": "NIE", "det-counterfactual": "det. counterf.",
}
GRAPH_ORDER = ["chain", "fork", "collision", "confounding", "mediation",
               "IV", "arrowhead", "diamond", "diamondcut", "frontdoor"]

plt.rcParams.update({
    "font.family": "serif", "font.size": 7, "axes.titlesize": 7.5, "axes.labelsize": 7,
    "xtick.labelsize": 6, "ytick.labelsize": 6, "legend.fontsize": 6.5,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.6, "xtick.color": MUTED, "ytick.color": MUTED,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6, "axes.labelcolor": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "pdf.fonttype": 42, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
})
TEXTWIDTH = 4.8  # LNCS text block, inches


def load():
    direct = [p for p in sorted(INTERIM.glob("logprobs-*.jsonl")) if "causal_cot" not in p.name]
    cot = sorted(INTERIM.glob("logprobs-*-causal_cot.jsonl"))
    df = load_scored(INTERIM / "variants-sample.jsonl", direct + cot)
    df["strategy"] = np.where(df["model"].str.endswith("-causal_cot"), "cot", "direct")
    df["base"] = df["model"].str.replace("-causal_cot", "", regex=False).str.split("/").str[-1]
    df["y"] = (df["answer"] == "yes").astype(int)
    return df


def auroc(y, score):
    y = np.asarray(y).astype(bool)
    ranks = pd.Series(score).rank().to_numpy()
    n1, n0 = y.sum(), (~y).sum()
    return (ranks[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def logit(p, clip=1e-6):
    p = np.clip(p, clip, 1 - clip)
    return np.log(p / (1 - p))


# --------------------------------------------------------------------------- Fig. 2
def fig_paired_scatter(df):
    d = df[(df["strategy"] == "direct") & df["pair_id"].notna()]
    fig, axes = plt.subplots(2, 2, figsize=(TEXTWIDTH, 4.5), sharex=True, sharey=True)
    lim = logit(np.array([1e-6, 1 - 1e-6])) * 1.04
    ticks_p = [1e-6, 1e-3, 0.1, 0.5, 0.9, 1 - 1e-3, 1 - 1e-6]
    tick_labels = ["$\\leq\\!10^{-6}$", ".001", ".1", ".5", ".9", ".999", ""]
    for ax, base in zip(axes.flat, MODELS, strict=True):
        wide = d[d["base"] == base].pivot_table(
            index=["pair_id", "answer"], columns="variant", values="p_yes", aggfunc="first"
        ).reset_index()
        ax.plot(lim, lim, color=GRAY, lw=0.7, ls="--", zorder=1)
        ax.axhline(0, color=GRAY, lw=0.4, zorder=1)
        ax.axvline(0, color=GRAY, lw=0.4, zorder=1)
        for answer, color in (("no", ORANGE), ("yes", BLUE)):
            w = wide[wide["answer"] == answer]
            ax.scatter(logit(w["commonsense"]), logit(w["anticommonsense"]), s=5, lw=0.25,
                       ec="white", fc=color, alpha=0.7, zorder=2,
                       label=f"correct answer: {answer.capitalize()}")
        diff = logit(wide["anticommonsense"], 1e-12) - logit(wide["commonsense"], 1e-12)
        below = (wide["anticommonsense"] < wide["commonsense"]).mean()
        flips = ((wide["commonsense"] > 0.5) != (wide["anticommonsense"] > 0.5)).mean()
        ax.text(0.03, 0.97, f"{LABEL[base]}\nbelow diagonal: {below:.2f}\n"
                f"answer flips: {flips:.2f}",
                transform=ax.transAxes, va="top", ha="left", fontsize=6, color=INK)
        ax.text(0.97, 0.03, "anti-C. lower\n(predicted)", transform=ax.transAxes, ha="right",
                va="bottom", fontsize=5.5, color=MUTED, style="italic")
        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_aspect("equal")
        ax.set_xticks(logit(np.array(ticks_p)), tick_labels)
        ax.set_yticks(logit(np.array(ticks_p)), tick_labels)
        print(f"[Fig2] {base}: share below diagonal {below:.3f}, median logit shift {np.median(diff):+.3f}, "
              f"answer flips {flips:.3f}, Spearman r {wide['commonsense'].corr(wide['anticommonsense'], method='spearman'):.3f}")
    for ax in axes[1]:
        ax.set_xlabel("$P(\\mathrm{Yes})$, commonsensical")
    for ax in axes[:, 0]:
        ax.set_ylabel("$P(\\mathrm{Yes})$, anti-commonsensical")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.01),
               markerscale=2)
    fig.tight_layout(rect=(0, 0, 1, 0.97), w_pad=0.4, h_pad=0.6)
    fig.savefig(FIG_DIR / "paired_pyes_scatter.pdf")
    plt.close(fig)


# --------------------------------------------------------------------------- Fig. 3
def fig_forest(df):
    gaps = paired_accuracy_gap(df)
    shifts = p_yes_shift(df)
    for t in (gaps, shifts):
        t["base"] = t["model"].str.replace("-causal_cot", "", regex=False).str.split("/").str[-1]
        t["strategy"] = np.where(t["model"].str.endswith("-causal_cot"), "cot", "direct")
    rows = [(b, s) for b in MODELS for s in ("direct", "cot")]
    ypos = {r: -i - (i // 2) * 0.6 for i, r in enumerate(rows)}  # gap between models
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.9), sharey=True)
    panels = [
        (axes[0], "(a) Accuracy gap", gaps, "gap", "gap_lo", "gap_hi"),
        (axes[1], "(b) $P(\\mathrm{Yes})$ shift", shifts, "shift", "shift_lo", "shift_hi"),
    ]
    for ax, title, table, est, lo, hi in panels:
        ax.axvspan(-EQUIV, EQUIV, color="#e9e8e4", zorder=0, lw=0)
        ax.axvline(0, color=GRAY, lw=0.7, zorder=1)
        for (base, strategy), y in ypos.items():
            color = BLUE if strategy == "direct" else ORANGE
            sub = table[(table["base"] == base) & (table["strategy"] == strategy)]
            if table is shifts:
                for dy, answer, filled in ((0.17, "yes", True), (-0.17, "no", False)):
                    r = sub[sub["answer"] == answer].iloc[0]
                    ax.plot([r[lo], r[hi]], [y + dy] * 2, color=color, lw=1.1, solid_capstyle="round")
                    ax.plot(r[est], y + dy, "o", ms=3.6, mfc=color if filled else "white", mec=color, mew=0.9)
            else:
                r = sub.iloc[0]
                ax.plot([r[lo], r[hi]], [y, y], color=color, lw=1.1, solid_capstyle="round")
                ax.plot(r[est], y, "D", ms=3.4, color=color)
                print(f"[Fig3] {base} {strategy}: gap {r[est]:+.3f} [{r[lo]:+.3f}, {r[hi]:+.3f}] "
                      f"pairs={r['pairs']} within ±{EQUIV}: {abs(r[lo]) < EQUIV and abs(r[hi]) < EQUIV}")
        ax.set_title(title, loc="left", color=INK)
        ax.set_xlim(-0.2, 0.2)
        ax.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
        ax.annotate("plausibility penalty $\\rightarrow$", xy=(0.99, -0.13), xycoords="axes fraction",
                    ha="right", fontsize=5.8, color=MUTED, style="italic", annotation_clip=False)
        ax.tick_params(axis="y", length=0)
        ax.spines["left"].set_visible(False)
    labels = [f"{LABEL[b]}, {'direct' if s == 'direct' else 'CausalCoT'}" for b, s in rows]
    axes[0].set_yticks(list(ypos.values()), labels)
    from matplotlib.lines import Line2D
    handles = [
        Line2D([], [], color=BLUE, marker="s", ls="-", ms=3.5, label="direct (1,000 pairs)"),
        Line2D([], [], color=ORANGE, marker="s", ls="-", ms=3.5, label="CausalCoT (150 pairs)"),
        Line2D([], [], color=INK, marker="o", ls="", ms=3.5, label="$P(\\mathrm{Yes})$: Yes items"),
        Line2D([], [], color=INK, marker="o", mfc="white", ls="", ms=3.5, label="No items"),
        plt.Rectangle((0, 0), 1, 1, fc="#e9e8e4", label=f"$\\pm${EQUIV:.2f} band"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.07),
               handlelength=1.5, columnspacing=1.0)
    fig.tight_layout(w_pad=1.2)
    fig.savefig(FIG_DIR / "forest_effects.pdf")
    plt.close(fig)
    for r in shifts.itertuples():
        print(f"[Fig3] shift {r.base} {r.strategy} {r.answer}: {r.shift:+.3f} [{r.shift_lo:+.3f}, {r.shift_hi:+.3f}] n={r.pairs}")


# --------------------------------------------------------------------------- Fig. 4
def half_violin(ax, values, x, side, color, width=0.36):
    values = np.asarray(values)
    grid = np.linspace(0, 1, 300)
    if values.std() < 1e-6:
        dens = np.exp(-0.5 * ((grid - values.mean()) / 0.01) ** 2)
    else:
        dens = gaussian_kde(values, bw_method=0.18)(grid)
    dens = dens / dens.max() * width
    lo, hi = np.quantile(values, [0.005, 0.995])
    keep = (grid >= lo - 0.02) & (grid <= hi + 0.02)
    xs = x + side * dens[keep]
    ax.fill_betweenx(grid[keep], x, xs, color=color, alpha=0.55, lw=0)
    ax.plot(xs, grid[keep], color=color, lw=0.7)
    med = np.median(values)
    ax.plot([x, x + side * width * 0.9], [med, med], color=color, lw=1.1)


def fig_discrimination(df):
    cot_ids = set(df.loc[df["strategy"] == "cot", "item_id"])
    same = df[df["item_id"].isin(cot_ids)]
    fig, axes = plt.subplots(1, 4, figsize=(TEXTWIDTH, 2.3), sharey=True)
    for ax, base in zip(axes, MODELS, strict=True):
        ax.axhline(0.5, color=GRAY, lw=0.6, ls="--", zorder=0)
        for x, strategy in ((0, "direct"), (1, "cot")):
            g = same[(same["base"] == base) & (same["strategy"] == strategy)]
            half_violin(ax, g.loc[g["y"] == 0, "p_yes"], x, -1, ORANGE)
            half_violin(ax, g.loc[g["y"] == 1, "p_yes"], x, +1, BLUE)
            auc = auroc(g["y"], g["p_yes"])
            yes_rate = (g["p_yes"] > 0.5).mean()
            ax.text(x, 1.03, f"AUC {auc:.2f}", ha="center", va="bottom", fontsize=6, color=INK)
            full = df[(df["base"] == base) & (df["strategy"] == strategy)]
            print(f"[Fig4] {base} {strategy}: AUROC {auc:.3f} on {len(g)} shared items "
                  f"(all items: {auroc(full['y'], full['p_yes']):.3f}, n={len(full)}), Yes rate {yes_rate:.2f}")
        ax.set_xticks([0, 1], ["direct", "CausalCoT"])
        ax.set_xlim(-0.5, 1.5)
        ax.set_ylim(-0.02, 1.02)
        ax.set_title(LABEL[base], pad=11, color=INK)
        ax.tick_params(axis="x", length=0)
    axes[0].set_ylabel("$P(\\mathrm{Yes})$")
    from matplotlib.patches import Patch
    fig.legend(handles=[Patch(fc=ORANGE, alpha=0.6, label="correct answer: No (left half)"),
                        Patch(fc=BLUE, alpha=0.6, label="correct answer: Yes (right half)")],
               loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.06))
    fig.tight_layout(rect=(0, 0.04, 1, 1), w_pad=0.3)
    fig.savefig(FIG_DIR / "discrimination_pyes.pdf")
    plt.close(fig)


# --------------------------------------------------------------------------- Fig. 5
def fig_heatmap(df):
    d = df[df["strategy"] == "direct"]
    informative = ["Qwen2.5-1.5B-Instruct", "Phi-3.5-mini-instruct", "Qwen2.5-7B-Instruct"]
    panels = [("(a) Three models pooled", d[d["base"].isin(informative)]),
              ("(b) Qwen2.5-7B", d[d["base"] == "Qwen2.5-7B-Instruct"])]
    cmap = LinearSegmentedColormap.from_list("div", [ORANGE, "#f0efec", BLUE])
    queries = [q for q, _ in QUERY_ORDER]
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.75), sharey=True)
    for ax, (title, sub) in zip(axes, panels, strict=True):
        tab = sub.groupby(["query_type", "graph_id"])["correct"].agg(["sum", "size"])
        acc = (tab["sum"] / tab["size"]).unstack().reindex(index=queries, columns=GRAPH_ORDER)
        im = ax.imshow(acc.to_numpy(dtype=float), cmap=cmap, vmin=0.2, vmax=0.8, aspect="auto")
        for i, q in enumerate(queries):
            for j, g in enumerate(GRAPH_ORDER):
                if (q, g) not in tab.index:
                    continue
                k, n = tab.loc[(q, g)]
                lo, hi = wilson_ci(int(k), int(n))
                sig = hi < 0.5 or lo > 0.5
                ax.text(j, i, f"{k / n:.2f}"[1:], ha="center", va="center", fontsize=4.8,
                        color=INK, fontweight="bold" if sig else "normal")
        for boundary in (2.5, 5.5):
            ax.axhline(boundary, color="white", lw=1.5)
        ax.set_xticks(range(len(GRAPH_ORDER)), GRAPH_ORDER, rotation=55, ha="right")
        ax.set_yticks(range(len(queries)), [f"L{r} {QUERY_LABEL[q]}" for q, r in QUERY_ORDER])
        ax.set_title(title, loc="left", color=INK)
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_facecolor("white")
    cbar = fig.colorbar(im, ax=axes, fraction=0.025, pad=0.02)
    cbar.set_label("accuracy (direct)", fontsize=6)
    cbar.outline.set_visible(False)
    cbar.ax.tick_params(labelsize=5.5, length=0)
    fig.savefig(FIG_DIR / "heatmap_query_topology.pdf")
    plt.close(fig)

    # numbers for the text: collider cells and balanced accuracy by topology
    col = d[d["graph_id"] == "collision"]
    print("[Fig5] collision graph, accuracy / Yes-prediction rate by query type and answer:")
    print(col.groupby(["base", "query_type", "answer"])
          .agg(acc=("correct", "mean"), pred_yes=("pred", lambda s: (s == "yes").mean()), n=("y", "size"))
          .round(2).to_string())


if __name__ == "__main__":
    data = load()
    fig_paired_scatter(data)
    fig_forest(data)
    fig_discrimination(data)
    fig_heatmap(data)
    print("written to", FIG_DIR)
