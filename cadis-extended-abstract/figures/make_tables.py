"""Rows for Tables 2 and 3 of the CADIS paper (CausalCoT by question type; question-only prior).

Run from the causal-evaluation repository:

    cd ~/Repositorios/causal-evaluation
    uv run python ../tesispp/cadis-extended-abstract/figures/make_tables.py
"""

import os
import sys
from pathlib import Path

import numpy as np

CE_ROOT = Path(os.environ.get("CE_ROOT", Path.home() / "Repositorios" / "causal-evaluation"))
sys.path.insert(0, str(CE_ROOT / "src"))

from causal_evaluation.evaluation.prior_analysis import join_prior, paired_gaps  # noqa: E402
from causal_evaluation.evaluation.stats import bootstrap_mean_ci, mcnemar_exact  # noqa: E402
from causal_evaluation.evaluation.variant_analysis import load_scored  # noqa: E402

INTERIM = CE_ROOT / "data" / "interim"
SAMPLE = INTERIM / "variants-sample.jsonl"
TAB_DIR = Path(__file__).resolve().parent.parent / "tables"
MODELS = ["SmolLM2-1.7B-Instruct", "Qwen2.5-1.5B-Instruct", "Phi-3.5-mini-instruct", "Qwen2.5-7B-Instruct"]
VARIANTS = ["commonsense", "noncommonsense", "anticommonsense"]


def base(model):
    return model.str.replace(r"-(causal_cot|question_only)$", "", regex=True).str.split("/").str[-1]


def paths(kind):
    files = sorted(INTERIM.glob("logprobs-*.jsonl"))
    if kind == "direct":
        return [p for p in files if "causal_cot" not in p.name and "question_only" not in p.name]
    return [p for p in files if p.name.endswith(f"-{kind}.jsonl")]


def cot_table():
    df = load_scored(SAMPLE, paths("direct") + paths("causal_cot"))
    df["cond"] = np.where(df["model"].str.endswith("-causal_cot"), "cot", "direct")
    df["base"] = base(df["model"])
    same = df[df["item_id"].isin(set(df.loc[df["cond"] == "cot", "item_id"]))]
    lines = []
    for m in MODELS:
        g = same[same["base"] == m]
        acc = g.pivot_table(index="cond", columns="variant", values="correct")
        wide = g.pivot_table(index="item_id", columns="cond", values="correct").astype(bool)
        gain, lo, hi = bootstrap_mean_ci(wide["cot"].astype(int) - wide["direct"].astype(int))
        p = mcnemar_exact(int((wide["cot"] & ~wide["direct"]).sum()), int((~wide["cot"] & wide["direct"]).sum()))
        cells = " & ".join(f"{acc.loc[c, v]:.2f}" for c in ("direct", "cot") for v in VARIANTS)
        p_txt = "<0.01" if p < 0.01 else f"{p:.2f}"
        lines.append(f"{m.replace('-Instruct', '').replace('-instruct', '')} & {cells} & "
                     f"{gain:+.3f} [{lo:+.2f}, {hi:+.2f}] & {p_txt} \\\\")
    (TAB_DIR / "cot_variants_rows.tex").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def prior_table():
    direct = load_scored(SAMPLE, paths("direct"))
    prior = load_scored(SAMPLE, paths("question_only"))
    joined = join_prior(direct, prior)
    gaps = paired_gaps(joined).assign(base=lambda t: t["model"].str.split("/").str[-1]).set_index("base")
    means = joined.assign(b=joined["base"].str.split("/").str[-1]).pivot_table(
        index="b", columns="variant", values="p_prior"
    )
    lines = []
    for m in MODELS:
        r = gaps.loc[m]
        lines.append(
            f"{m.replace('-Instruct', '').replace('-instruct', '')} & "
            f"{means.loc[m, 'commonsense']:.2f} / {means.loc[m, 'anticommonsense']:.2f} & "
            f"{r.prior_gap:+.3f} [{r.prior_lo:+.2f}, {r.prior_hi:+.2f}] & "
            f"{r.context_gap:+.3f} [{r.context_lo:+.2f}, {r.context_hi:+.2f}] \\\\"
        )
    (TAB_DIR / "prior_rows.tex").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    cot_table()
    prior_table()
