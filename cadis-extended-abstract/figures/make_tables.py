"""Rows for the Results tables of the CADIS paper and the numbers quoted in Sect. 5.

Two tests, each reported as a difference with its 95% confidence interval and p-value
(two-sided, alpha = 0.05):
- paired t-test, for the same items measured twice: a commonsensical item and its
  anti-commonsensical twin (accuracy or P(Yes));
- two-proportion z-test, for independent groups: commonsensical vs nonsensical items,
  one rung vs another.
The exploratory CausalCoT run is descriptive: its differences are only compared with
the sampling-variation threshold 1.96 * sqrt(2 * 0.25 / n) of Sect. 4.5.

Run from the causal-evaluation repository:

    cd ~/Repositorios/causal-evaluation
    uv run python ../tesispp/cadis-extended-abstract/figures/make_tables.py
"""

import os
import sys
from pathlib import Path

import numpy as np
from scipy import stats

CE_ROOT = Path(os.environ.get("CE_ROOT", Path.home() / "Repositorios" / "causal-evaluation"))
sys.path.insert(0, str(CE_ROOT / "src"))

from causal_evaluation.data.variants import RELATIONAL_QUERY_TYPES  # noqa: E402
from causal_evaluation.evaluation.prior_analysis import join_prior  # noqa: E402
from causal_evaluation.evaluation.variant_analysis import load_scored  # noqa: E402

INTERIM = CE_ROOT / "data" / "interim"
SAMPLE = INTERIM / "variants-sample.jsonl"
TAB_DIR = Path(__file__).resolve().parent.parent / "tables"
MODELS = ["SmolLM2-1.7B-Instruct", "Qwen2.5-1.5B-Instruct", "Phi-3.5-mini-instruct", "Qwen2.5-7B-Instruct"]
VARIANTS = ["commonsense", "noncommonsense", "anticommonsense"]
Z95 = 1.959963984540054


# ----------------------------------------------------------------------------- tests
def paired_t(diff):
    """Mean paired difference, 95% t interval, two-sided p for H0: mean difference = 0."""
    diff = np.asarray(diff, dtype=float)
    n, mean = len(diff), diff.mean()
    se = diff.std(ddof=1) / np.sqrt(n)
    if se == 0:
        return mean, mean, mean, 1.0
    half = stats.t.ppf(0.975, n - 1) * se
    return mean, mean - half, mean + half, 2 * stats.t.sf(abs(mean / se), n - 1)


def two_proportion_z(a, b):
    """p_a - p_b, 95% interval, two-sided p for H0: p_a = p_b (pooled SE for the test)."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    pa, pb, na, nb = a.mean(), b.mean(), len(a), len(b)
    diff = pa - pb
    half = Z95 * np.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    pooled = (a.sum() + b.sum()) / (na + nb)
    se0 = np.sqrt(pooled * (1 - pooled) * (1 / na + 1 / nb))
    p = 2 * stats.norm.sf(abs(diff / se0)) if se0 > 0 else 1.0
    return diff, diff - half, diff + half, p


def fmt_p(p):
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def fmt(r):
    return f"{r[0]:+.3f} [{r[1]:+.3f}, {r[2]:+.3f}] p={fmt_p(r[3])}{'*' if r[3] < 0.05 else ''}"


def cell(r):
    """Table cell: difference, bold when p < 0.05."""
    return f"$\\mathbf{{{r[0]:+.3f}}}$" if r[3] < 0.05 else f"${r[0]:+.3f}$"


def short(name):
    return name.replace("-Instruct", "").replace("-instruct", "")


# ----------------------------------------------------------------------------- data
def paths(kind):
    files = sorted(INTERIM.glob("logprobs-*.jsonl"))
    if kind == "direct":
        return [p for p in files if "causal_cot" not in p.name and "question_only" not in p.name]
    return [p for p in files if p.name.endswith(f"-{kind}.jsonl")]


def load():
    df = load_scored(SAMPLE, paths("direct") + paths("causal_cot"))
    df["cond"] = np.where(df["model"].str.endswith("-causal_cot"), "cot", "direct")
    df["base"] = df["model"].str.replace("-causal_cot", "", regex=False).str.split("/").str[-1]
    return df


def by_variant(g, value="correct"):
    return {v: g.loc[g["variant"] == v, value] for v in VARIANTS}


def pair_diff(group, value):
    """Commonsensical minus anti-commonsensical `value`, one row per matched pair."""
    wide = group[group["pair_id"].notna()].pivot_table(
        index="pair_id", columns="variant", values=value, aggfunc="first"
    ).dropna(subset=["commonsense", "anticommonsense"])
    return wide["commonsense"].astype(float) - wide["anticommonsense"].astype(float)


# ----------------------------------------------------------------------------- tables
def direct_tables(df):
    """Accuracy by type of question; differences between types and rungs (with tests)."""
    lines, diff_lines = [], []
    print("\n[Sect. 5.1] direct run  (* = p < 0.05)")
    for m in MODELS:
        g = df[(df["base"] == m) & (df["cond"] == "direct")]
        v = by_variant(g)
        cells = [f"{v[k].mean():.2f}" for k in VARIANTS]
        rel = g[g["query_type"].isin(RELATIONAL_QUERY_TYPES) & (g["answer"] == "yes")]
        wide = rel[rel["pair_id"].notna()].pivot_table(index="pair_id", columns="variant", values="p_yes").dropna()
        cells.append(f"{wide['commonsense'].mean():.2f} / {wide['anticommonsense'].mean():.2f}")
        lines.append(f"{short(m)} & " + " & ".join(cells) + " \\\\")

        rung = {k: g.loc[g["rung"] == k, "correct"] for k in (1, 2, 3)}
        tests = {
            "comm-anti (paired t)": paired_t(pair_diff(g, "correct")),
            "comm-nons (z)": two_proportion_z(v["commonsense"], v["noncommonsense"]),
            "L2-L1 (z)": two_proportion_z(rung[2], rung[1]),
            "L3-L1 (z)": two_proportion_z(rung[3], rung[1]),
        }
        h1b = paired_t(pair_diff(rel, "p_yes"))
        diff_lines.append(f"{short(m)} & " + " & ".join(cell(r) for r in tests.values()) + " \\\\")
        print(f"  {short(m)}")
        for name, r in {**tests, "H1b P(Yes) shift, relational Yes (paired t)": h1b}.items():
            print(f"    {name:44s} {fmt(r)}")
    (TAB_DIR / "variants_rows.tex").write_text("\n".join(lines) + "\n")
    (TAB_DIR / "differences_rows.tex").write_text("\n".join(diff_lines) + "\n")


def cot_table(df):
    """Accuracy by type of question, direct vs CausalCoT, and the change (descriptive)."""
    same = df[df["item_id"].isin(set(df.loc[df["cond"] == "cot", "item_id"]))]
    lines = []
    print("\n[Sect. 5.2] CausalCoT run, descriptive (thresholds: 0.065 overall, 0.113 per type)")
    for m in MODELS:
        g = same[same["base"] == m]
        acc = g.pivot_table(index="cond", columns="variant", values="correct")
        overall = g.groupby("cond")["correct"].mean()
        change = overall["cot"] - overall["direct"]
        cells = " & ".join(f"{acc.loc[c, v]:.2f}" for c in ("direct", "cot") for v in VARIANTS)
        lines.append(f"{short(m)} & {cells} & ${change:+.3f}$ \\\\")
        cot = acc.loc["cot"]
        print(f"  {short(m):13s} change {change:+.3f} | after CoT comm-anti "
              f"{cot['commonsense'] - cot['anticommonsense']:+.3f}, comm-nons "
              f"{cot['commonsense'] - cot['noncommonsense']:+.3f}")
    (TAB_DIR / "cot_variants_rows.tex").write_text("\n".join(lines) + "\n")


def prior_table():
    """Question-only prior gap vs the same gap in context (paired t-tests on matched pairs)."""
    joined = join_prior(load_scored(SAMPLE, paths("direct")), load_scored(SAMPLE, paths("question_only")))
    joined["base"] = joined["base"].str.split("/").str[-1]
    lines = []
    print("\n[Sect. 5.3] question-only run  (paired t-tests, * = p < 0.05)")
    for m in MODELS:
        g = joined[joined["base"] == m]
        means = g.pivot_table(index="variant", values="p_prior")["p_prior"]
        prior = paired_t(pair_diff(g, "p_prior"))
        ctx = paired_t(pair_diff(g, "p_yes"))
        lines.append(
            f"{short(m)} & {means['commonsense']:.2f} / {means['anticommonsense']:.2f} & "
            f"${prior[0]:+.3f}$ [${prior[1]:+.2f}$, ${prior[2]:+.2f}$] & "
            f"${ctx[0]:+.3f}$ [${ctx[1]:+.2f}$, ${ctx[2]:+.2f}$] & {fmt_p(ctx[3])} \\\\"
        )
        print(f"  {short(m):13s} prior {fmt(prior)} | in context {fmt(ctx)}")
    (TAB_DIR / "prior_rows.tex").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    data = load()
    direct_tables(data)
    cot_table(data)
    prior_table()
