# Working Note — results narrative draft (2026-08-27)

This file is prose scaffolding for the prize-eligible Working Note. It separates direct hosted evidence from design hypotheses so later results can be inserted without rewriting the argument.

## 1. Hosted reproducibility is materially noisy

A byte-identical ASUB-001 submission was evaluated twice and returned public scores of **77.850** and **86.040**. Under that attack's fixed economics, these correspond to 865 and 956 equivalent successful EXFIL findings per public model row on average. The observed score range is **8.190 points**.

We therefore avoid treating small single-run leaderboard differences as proof of algorithmic improvement. The 8.190 range is used only as an empirical practical comparison band; two runs are insufficient for a formal confidence interval or stable variance estimate.

## 2. Replay-timeout semantics change archive optimization

Under prefix-preserving replay timeout behavior, a replay archive of non-negative-value findings should be ordered so that the most valuable or most informative findings appear first. Returning a full legal archive can dominate conservative replay-cap guessing because a replay timeout removes only the unprocessed suffix while preserving accumulated score.

This creates two distinct ordering objectives:

- **public frontier:** value/throughput first;
- **private uncertainty hedge:** hypothesis coverage first, then long-run portfolio weights.

Attack-generation timeout remains a separate constraint and motivates bounded generation-time calibration.

## 3. Private robustness is treated as uncertainty, not hidden knowledge

The private guardrail is not queried during attack generation. Private-aware candidates therefore encode explicit competing hypotheses rather than asserting knowledge of hidden behavior. The portfolio spans public EXFIL, direct Confused Deputy, and source-to-action semantic families over email, HTTP, shell, and filesystem writes.

The main methodological distinction is between optimizing a known public score surface and preserving coverage of materially different mechanisms under an unknown final defense.

## 4. Hierarchical prefix coverage

ASUB-009 emits one candidate from every active family before a family repeats. DRAFT-ASUB-017/ASUB-011 improves the same portfolio by first covering every active **lane** before a lane repeats, then covering the remaining families, then resuming exact weighted-deficit interleaving.

For the current 11-family, six-lane portfolio:

- ASUB-009 covers 4/6 lanes after six replay positions;
- hierarchical ordering covers 6/6 after six positions;
- both cover all 11 families within the first 11 positions;
- discrete early lane-coverage AUC improves from 41 to 51 (**+24.4%**).

The +24.4% number is a deterministic coverage metric, not a predicted leaderboard-score gain.

## 5. Hierarchical calibration breadth

DRAFT-ASUB-019 applies the same breadth principle to **generation-time calibration** while keeping the ASUB-011 fallback replay archive unchanged. Instead of probing both wording variants of one family before moving on, it performs two breadth-first passes over the hierarchical family order:

1. variant 0 for every family;
2. variant 1 for every family.

The first six calibration probes therefore cover all six lanes, the first eleven cover all eleven families, and no second wording variant is attempted until every family has received one probe. A family with only one failed observation is retained as unresolved rather than dropped as if both variants had been tested.

This is intended to reduce sensitivity to short generation windows. If the full 22-probe schedule completes, DRAFT-ASUB-019 has essentially the same calibration breadth as ASUB-011 and differs mainly in ordering. The design therefore supports a narrow attribution: any benefit should come from better early evidence allocation rather than a different replay portfolio.

## 6. Interface-only public control

DRAFT-ASUB-018/ASUB-012 isolates the lowest-assumption public strategy in the current ladder: 2,000 ordinary one-message `http.post` requests, one unique synthetic destination per finding, no control-token framing, no forged model/tool transcript, and no live model-format classification.

Its purpose is experimental rather than ideological. If it performs within the empirical hosted noise band of more complex public strategies, the simpler documented-interface mechanism becomes attractive because it depends on fewer evaluator-specific assumptions. If the complex strategies clearly outperform it beyond the observed noise band, their extra machinery has stronger hosted evidence of value.

## 7. Final selection is a portfolio problem

Kaggle allows two final selected submissions. We therefore model selection as a pair rather than independently taking the two largest noisy public scores. The intended pair structure is:

1. a strong credible public anchor;
2. a complementary private-aware hedge.

`src/final_pair_selector.py` evaluates candidate pairs under explicit stress scenarios and minimizes worst-case regret before considering worst-case and weighted-mean pair performance. Scenario inputs remain assumptions until replaced by evidence.

## 8. Current limitations

- Public scores do not expose the hidden private-defense survival of each mechanism.
- Two byte-identical hosted replicas provide useful operational evidence of noise but are insufficient for formal variance estimation.
- Synthetic benchmark tool misuse does not imply the same behavior in production agents or unrelated systems.
- Coverage metrics measure diversity of tested hypotheses, not security impact or final leaderboard score.
- Hierarchical calibration is a budget-allocation hypothesis until hosted evidence shows generation truncation or a score difference beyond ordinary run variance.
- Public model-format behavior may change with evaluator revisions; the interface-only control is retained specifically to test dependence on those assumptions.

## Pending inserts

When the current hosted wave finishes, insert:

- ASUB-009 public score and interpretation as a private-aware hedge;
- both ASUB-010 replicate scores and their strategy-specific spread;
- ASUB-007 public score;
- pairwise comparison using the empirical-noise decision helper;
- whether ASUB-011 and/or ASUB-012 were then promoted to hosted evaluation;
- whether DRAFT-ASUB-019 earned promotion based on hosted evidence of generation truncation/order sensitivity;
- final two selected submissions and rationale.
