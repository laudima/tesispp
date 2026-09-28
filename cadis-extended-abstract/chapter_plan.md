# Chapter Plan — CADIS 2026 paper

Deadline 2026-09-28. Limit 12 pages LNCS. Thesis confirmed 2026-09-24. Plan complete except the falsification criterion (Q5).

## Decisions (from the plan-mode dialogue)

| Topic | Decision |
|-------|----------|
| Main claim | LLM causal answers follow word plausibility more than the causal structure given in the prompt (commonsense vs anticommonsense) |
| Rung hypothesis | Kept as a secondary hypothesis: R2 and R3 accuracy lower than R1; reported either way |
| Theory | Follow Astorga & Letelier's position. CLadder data can only support the architectural reading; the constitutive claim is argued theoretically, not tested |
| Output probabilities | Yes: collect P(Yes)/P(No) per item |
| Human commonsense causality | Future work only |
| Models | Light open-weight models are the core comparison (run on Colab); gpt-4o-mini optional as a single larger reference point |
| Paper vs undergrad thesis | Separate piece of work that draws on the thesis project |

## INSIGHT Collection (your words)

- **[INSIGHT: thesis_statement — confirmed]** LLM answers follow "the priors of semantic concepts, the probability of the words" rather than the given causal structure; they "lack a model of reality", so "the causal inferences they can discover can only be related from statistics."
- **[INSIGHT: secondary_hypothesis]** "Rung 2 and rung 3 I expected them to have a lower accuracy than R1."
- **[INSIGHT: practitioner_message]** "Maintain experimental results or simulations to get causal relationships; otherwise with LLMs we will not be generating actual causal relationships."
- **[INSIGHT: theoretical_position]** "Take the claim of Astorga and Letelier."
- **[INSIGHT: future_work]** Human commonsense causality vs LLMs.
- **[INSIGHT: contribution_claim]** "Compare light open-source models, and relate the failures with a philosophical literature about why the models fail; also marking what could be actual limitations on these models to discover or infer causal relationships."
- **[INSIGHT: prediction]** Commonsense highest; noncommonsense close to commonsense; anticommonsense lower (word priors override the given graph).
- **[INSIGHT: stress_test]** "If the model fails in both, the problem is still that the models are bad at making causal inferences; if the models are right in both with high accuracy (above 85%), then the dataset should test larger causal inferences." Weak point: as stated, no outcome counts against the claim (see Q5).
- **[INSIGHT: origin]** The paper started as a failure-clustering graph; now kept as one Results figure, not the main contribution.

## Evidence in hand

- SmolLM2, CLadder easy, n = 10,560: 0.453 / 0.461 / 0.449 by rung. Flat and below chance, dominated by yes-bias (6,243 yes vs 3,467 no); ~500 near-miss answers and 347 context overflows scored as wrong. Rescore with the fixed parser; report as a small-model baseline only.
- gpt-4o-mini: 10-question pilot (not reportable).

## Experiment spec (run Sept 24–25)

| Item | Setting |
|------|---------|
| Data | CLadder commonsense, anticommonsense, noncommonsense files; ~1,000 items each, stratified by rung (same seed 20260903) |
| Prompt | `default` (single answer); CausalCoT only if time allows |
| Models (core) | 3–4 light open-weight instruct models on Colab, spanning sizes, e.g. SmolLM2-1.7B, Qwen2.5-1.5B/7B, Llama-3.2-3B, Gemma-2-2B, Phi-3.5-mini. One forward pass per item; read next-token logits for "Yes"/"No". No generation needed |
| Reference (optional) | gpt-4o-mini via API, `logprobs=true`, temperature 0 |
| Novelty check | Read Jin et al.'s results on the variants; state what is new relative to them (light models, P(Yes), theoretical account) |
| Scoring | Extract the answer before scoring; count parse failures and errors separately; record P(Yes) |
| Analysis | Accuracy by variant × rung with 95% CIs; yes-rate per variant; mean P(correct answer) per variant; breakdown by topology (graph_id) |
| Record | Model name/digest, temperature, max tokens, dataset file hash |

## Section plan (12 pages)

| # | Section | Pages | Core content | Sources | Editor comment addressed |
|---|---------|-------|--------------|---------|--------------------------|
| 1 | Introduction | 1.25 | Non-identifiability → background knowledge → LLMs as a stand-in for experts → risk that their "knowledge" is word plausibility | spirtes2016, glymour2019, kiciman2023, long2023, verma2025, butkus2025 | Add distributional routes (LiNGAM/FASK) |
| 2 | Background | 2.0 | Markov equivalence; constraint-based search; LiNGAM (non-Gaussian noise, ICA) and FASK (skewness); LLM priors as another orientation source; prior LLM causal evaluations | shimizu2006, Sanchez-Romero et al. 2019 *Network Neuroscience* (add to bib, verify DOI), verma1990/2013, zevcevic2023, willig2022, jin2023, chen2024, li2023, hobbhahn2022 | LiNGAM/FASK |
| 3 | Theoretical framework | 2.0 | Pearl's ladder; Rosen's reactive vs anticipatory systems; Astorga & Letelier Level 0/1/2 (Level 1 = conditional probability matrix ≈ Pearl's L1; LLMs as "statistical compressions of training data" with an Umwelt "derived from others' Umwelten"); Korbak/FEP (a generative model learned by acting) as contrast; architectural vs constitutive claim; Markov/faithfulness bridge | pearl2009, pearl2018theoretical, rosen2012, astorga2026, korbak2021 | "Can it work without Rosen?"; Markov/faithfulness |
| 4 | Method | 1.5 | CLadder; define query type ("subtype") and graph_id ("topology", 10 graphs); the three variants; models; prompt; logprobs; scoring; sampling and CIs | jin2023 | Define subtype/topology |
| 5 | Results | 2.0 | Variant × rung accuracy; P(Yes) and yes-bias; topology breakdown; toy failure-graph figure | own data | Failure-DAG figure |
| 6 | Discussion and limitations | 1.75 | Implications for LLM priors in discovery; limitations (model scale, prompt sensitivity, easy vs balanced set, sample size, the graph is given in the prompt); human comparison as future work | — | Limitations and challenges |
| 7 | Conclusion | 0.5 | Take-home + future work | — | — |
| | References | ~1 | Check whether CADIS counts references toward the 12 pages | | |

## Schedule (revised)

| Date | Writing | Experiments |
|------|---------|-------------|
| Wed 24 | §3 Framework | Fix parser; build variant samples; Colab notebook; start open-model runs |
| Thu 25 | §2 Background + §4 Method | Runs finish; rescore SmolLM2 |
| Fri 26 | §5 Results | Tables, CIs, P(Yes) plots, failure-graph figure |
| Sat 27 | §6 Discussion, §1 Intro, §7 Conclusion, Abstract | — |
| Sun 28 | Buffer, full read, references check, submit | — |

## Open question

- **Q5.** Which specific result would count against the word-priors claim? Candidate from your own prediction: no accuracy gap (or no P(Yes) shift) between commonsense and anticommonsense items. Decide before the runs return, and state it in §4 Method.

## Stress-test outcome → where it goes in the paper

- The ">85% means the dataset is too easy" point belongs in §6 Limitations as a scope condition (CLadder gives the graph and the numbers in the prompt), not as a way to protect the claim.
- The falsification criterion (Q5) goes in §4 as a pre-stated prediction.
