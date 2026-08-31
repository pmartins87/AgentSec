# Working Note — results narrative draft (2026-08-27)

This file is prose scaffolding for the prize-eligible Working Note. It separates direct hosted evidence from design hypotheses so later results can be inserted without rewriting the argument.

## 1. Hosted reproducibility is materially noisy

A byte-identical ASUB-001 submission was evaluated twice and returned public scores of **77.850** and **86.040**. Under that attack's fixed economics, these correspond to 865 and 956 equivalent successful EXFIL findings per public model row on average. The observed score range is **8.190 points**.

We therefore avoid treating small single-run leaderboard differences as proof of algorithmic improvement. The 8.190 range is used only as an empirical practical comparison band; two runs are insufficient for a formal confidence interval or stable variance estimate.

## 2. Replay-timeout semantics change archive optimization

Under prefix-preserving replay timeout behavior, a replay archive of non-negative-value findings should be ordered so that the most valuable or most informative findings appear first. Returning a full legal archive can dominate conservative replay-cap guessing only when the archive itself contains replayable positive-value candidates. The ASUB-013 result below shows that blind archive depth cannot substitute for live candidate validation.

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

Hosted evidence now shows ASUB-011 at **8.145** versus ASUB-009 at **8.565**. The hierarchical ordering therefore did not improve the permissive public leaderboard. This is useful negative evidence: deterministic early diversity and public exploit throughput are different objectives. It remains unknown whether the ordering changes survival under the hidden private guardrail.

## 5. Hierarchical calibration breadth

DRAFT-ASUB-019 applies the same breadth principle to **generation-time calibration** while keeping the ASUB-011 fallback replay archive unchanged. Instead of probing both wording variants of one family before moving on, it performs two breadth-first passes over the hierarchical family order:

1. variant 0 for every family;
2. variant 1 for every family.

The first six calibration probes therefore cover all six lanes, the first eleven cover all eleven families, and no second wording variant is attempted until every family has received one probe. A family with only one failed observation is retained as unresolved rather than dropped as if both variants had been tested.

This is intended to reduce sensitivity to short generation windows. If the full 22-probe schedule completes, DRAFT-ASUB-019 has essentially the same calibration breadth as ASUB-011 and differs mainly in ordering. The design therefore supports a narrow attribution: any benefit should come from better early evidence allocation rather than a different replay portfolio.

ASUB-011's public result does not justify promoting DRAFT-ASUB-019 on public-score grounds. Any hosted promotion must instead be motivated by explicit private-uncertainty stress evidence or generation-truncation evidence.

## 6. Interface-only public control

DRAFT-ASUB-018/ASUB-012 isolates the lowest-assumption public strategy in the current ladder: 2,000 ordinary one-message `http.post` requests, one unique synthetic destination per finding, no control-token framing, no forged model/tool transcript, and no live model-format classification.

Its purpose is experimental rather than ideological. If it performs within the empirical hosted noise band of more complex public strategies, the simpler documented-interface mechanism becomes attractive because it depends on fewer evaluator-specific assumptions. If the complex strategies clearly outperform it beyond the observed noise band, their extra machinery has stronger hosted evidence of value.

The ASUB-013 result makes blind static archive emission substantially less attractive, so ASUB-012 should not be promoted merely as another 2,000-item static control without a new decision-relevant reason.

## 7. Final selection is a portfolio problem

Kaggle allows two final selected submissions. We therefore model selection as a pair rather than independently taking the two largest noisy public scores. The intended pair structure is:

1. a strong credible public anchor;
2. a complementary private-aware hedge.

`src/final_pair_selector.py` evaluates candidate pairs under explicit stress scenarios and minimizes worst-case regret before considering worst-case and weighted-mean pair performance. Scenario inputs remain assumptions until replaced by evidence.

## 8. Hosted public complexity did not beat the simple baseline

The hosted public wave produced:

- **ASUB-007:** 82.700;
- **ASUB-010:** 78.810;
- an accidental duplicate of the same ASUB-010 notebook version, submitted under an incorrect ASUB-007 description: 81.920;
- **ASUB-009:** 8.565;
- **ASUB-011:** 8.145;
- **ASUB-013:** 60.500.

The two ASUB-010 results differ by 3.110 points. This is directionally consistent with the earlier observation that hosted evaluation is noisy, although it should not be combined mechanically with the ASUB-001 spread because the samples are sparse and candidate/runtime conditions differ.

The key negative result is that neither timeout-prefix public logic nor format-diverse public logic exceeded the best simple ASUB-001 replicate at 86.040. Added selection logic and prompt-format diversity therefore did not produce hosted evidence of a better public mechanism in this wave.

## 9. Broad private hedging has a severe visible public cost

ASUB-009 scored **8.565** publicly and ASUB-011 scored **8.145**, far below the public-only candidates. This is direct evidence that the broad private-hypothesis portfolio pays a severe cost on the known permissive public score surface.

It is not direct evidence that the same portfolio fails under the hidden private guardrail. The near-equality of ASUB-009 and ASUB-011 instead shows that improved hierarchical ordering is essentially invisible to the current public score. This supports treating private-aware design as an uncertainty/stress-testing problem rather than a public-LB optimization problem.

## 10. Live validation is a causal component of the strongest public path

ASUB-013 is the most informative public negative result so far. It preserved the exact successful ASUB-001 `FAST_TEMPLATE` and destination generator but removed live generation probing and emitted the legal maximum of 2,000 candidates immediately. It scored only **60.500**, well below both byte-identical ASUB-001 hosted scores (77.850 and 86.040).

This falsifies the simple hypothesis that the ASUB-001 message mechanism was already sufficient and that eliminating generation overhead plus maximizing archive depth would improve throughput. In this evaluator, blind candidate volume is not enough.

The causal bundle removed from ASUB-001 includes:

- live model interaction;
- keep-only-if-fired filtering;
- latency/model-path selection;
- runtime-adaptive replay sizing;
- latency-based candidate ordering.

The next experiment must decompose that bundle with **per-model measurements** rather than another scalar leaderboard guess. Because the competition evaluates GPT-OSS and Gemma separately and averages their public rows, a single leaderboard score can conceal a strategy that works well on one model and poorly on the other.

## 11. Current limitations

- Public scores do not expose the hidden private-defense survival of each mechanism.
- Two byte-identical hosted replicas provide useful operational evidence of noise but are insufficient for formal variance estimation.
- The public scalar leaderboard does not expose per-model contribution, so model imbalance must be diagnosed locally or through controlled per-model experiments.
- Synthetic benchmark tool misuse does not imply the same behavior in production agents or unrelated systems.
- Coverage metrics measure diversity of tested hypotheses, not security impact or final leaderboard score.
- Hierarchical calibration is a budget-allocation hypothesis until hosted/private-proxy evidence makes it decision-relevant.
- Public model-format behavior may change with evaluator revisions.
- ASUB-009/011 low public scores cannot by themselves establish private value; final private behavior remains unobserved until Kaggle's hidden evaluation.
- ASUB-007/010/013 negative public results establish that those specific mechanisms failed to improve this hosted wave, not that all richer strategies are intrinsically worse.

## Next evidence inserts

Before final Working Note submission, insert:

- per-model local-validation telemetry for ASUB-001 and its next controlled successor;
- whether the main 86-point ceiling was caused by GPT-OSS/Gemma imbalance, latency, fire-rate, replay sizing, or another measured factor;
- any explicit private-guardrail proxy/stress-test evidence, clearly labeled as a proxy rather than hidden-ground-truth access;
- final two selected submissions and scenario-based rationale;
- final leaderboard/private outcome if available before the Working Note deadline.
