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

## 8. Hosted public complexity did not beat the simple baseline

The next hosted wave produced the following public scores:

- **ASUB-007:** 82.700;
- **ASUB-010:** 78.810;
- an accidental duplicate of the same ASUB-010 notebook version, submitted under an incorrect ASUB-007 description: 81.920;
- **ASUB-009:** 8.565.

The two ASUB-010 results differ by 3.110 points. This is directionally consistent with the earlier observation that hosted evaluation is noisy, although it should not be combined mechanically with the ASUB-001 spread because the samples are sparse and candidate/runtime conditions differ.

The key negative result is that neither the timeout-prefix public frontier nor the format-diverse public frontier exceeded the best simple ASUB-001 replicate at 86.040. Added selection logic, format diversity, and generation-time calibration therefore did not produce hosted evidence of a better public mechanism in this wave.

This negative result changes the next public experiment. Rather than adding another prompt format, DRAFT-ASUB-020 / frozen ASUB-013 holds the exact successful ASUB-001 FAST_TEMPLATE and URL generator fixed, removes live generation probing, and emits the full 2,000-candidate archive. This is a controlled throughput ablation: the main changed variable is generation overhead, not attack wording.

## 9. Broad private hedging has a severe visible public cost

ASUB-009 scored **8.565** publicly, far below the public-only candidates. This is direct evidence that a broad hedge over semantically different attack families imposes a large cost on the known public score surface.

It is not direct evidence that the same portfolio fails under the hidden private guardrail. The result instead strengthens the case for treating Kaggle's two final submission slots as a complementary portfolio: a public anchor can carry the known public mechanism while a second candidate spends score budget on hidden-defense uncertainty.

ASUB-011 is the cleaner follow-up private experiment because it preserves the same broad hypothesis portfolio while improving early lane coverage from 4/6 to 6/6 in the first six replay positions. Its hosted public score remains pending at the time of this insert.

## 10. Baseline-exact full-prefix throughput ablation

DRAFT-ASUB-020 was validated mechanically and through the official SDK before being frozen byte-identically as ASUB-013. It preserves the exact ASUB-001 fast prompt and destination generator but removes the live warm-up/probe loop and returns the legal maximum of 2,000 candidates immediately.

This experiment is intentionally narrow. If ASUB-013 materially exceeds the ASUB-001 hosted region, the result supports the interpretation that generation-time calibration overhead, rather than insufficient archive depth, was limiting the simple public mechanism. If it remains inside the observed ASUB-001 duplicate range or regresses, then full-prefix static emission alone is not enough to move the public frontier.

The 8.190-point ASUB-001 duplicate range is used only as an operational comparison band. In particular, a single ASUB-013 score above **94.230** would exceed the current 86.040 anchor by more than the entire observed identical-run range and would therefore be substantially stronger evidence of public improvement than a one- or two-point gain.

## 11. Current limitations

- Public scores do not expose the hidden private-defense survival of each mechanism.
- Two byte-identical hosted replicas provide useful operational evidence of noise but are insufficient for formal variance estimation.
- Synthetic benchmark tool misuse does not imply the same behavior in production agents or unrelated systems.
- Coverage metrics measure diversity of tested hypotheses, not security impact or final leaderboard score.
- Hierarchical calibration is a budget-allocation hypothesis until hosted evidence shows generation truncation or a score difference beyond ordinary run variance.
- Public model-format behavior may change with evaluator revisions; the interface-only control is retained specifically to test dependence on those assumptions.
- ASUB-009's low public score cannot by itself establish private value; final private behavior remains unobserved until Kaggle's hidden evaluation.
- ASUB-007/010 negative public results establish that those specific added mechanisms failed to improve this hosted wave, not that all richer strategies are intrinsically worse.

## Pending inserts

Before final Working Note submission, insert:

- ASUB-011 terminal public score and interpretation;
- ASUB-013 terminal public score and comparison against the 77.850–86.040 ASUB-001 replicate region;
- whether ASUB-012 and/or DRAFT-ASUB-019 earned hosted slots after those results;
- final two selected submissions and scenario-based rationale;
- final leaderboard/private outcome if available before the Working Note deadline.
