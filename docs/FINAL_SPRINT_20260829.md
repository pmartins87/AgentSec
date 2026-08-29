# AgentSec final sprint — 2026-08-29

## Objective

Maximize prize probability across three coupled tracks during the last competition days:

1. improve the public attack frontier without overfitting to the public harness;
2. preserve a complementary private-robust candidate for the hidden final guardrail;
3. finish a reproducible Working Note that turns both positive and negative hosted evidence into a clear security contribution.

Public leaderboard score is telemetry. The final two Kaggle selections should be treated as a portfolio, not simply the two highest public scores.

## Hosted evidence entering the sprint

| Candidate / run | Role | Public score | Interpretation |
|---|---|---:|---|
| ASUB-001 Version 4 replicate A | simple public EXFIL baseline | 77.850 | valid hosted baseline |
| ASUB-001 Version 4 replicate B | byte-identical baseline | **86.040** | current best public score |
| ASUB-007 Version 8 | timeout-prefix public frontier | 82.700 | more complex public policy did not beat ASUB-001 best |
| ASUB-010 Version 6 | format-diverse public frontier | 78.810 | format diversity did not beat ASUB-001 best |
| accidental ASUB-010 duplicate, mislabeled ASUB-007 | replicate telemetry | 81.920 | confirms material hosted run-to-run variability |
| ASUB-009 Version 5 | coverage-first private hedge | 8.565 | severe visible public cost; still not evidence about hidden-private survival |
| ASUB-011 Version 9 | hierarchical private hedge | running as of latest Kaggle screenshot | pending hosted evidence |

ASUB-001's two byte-identical runs span 8.190 leaderboard points. Treat that as an empirical practical noise band, not a statistical confidence interval.

## Immediate public experiment: ASUB-013

Frozen source:

`submissions/ASUB-20260829-013-public-frontier-v9-baseline-exact-full-prefix/attack.py`

Origin: byte-identical frozen copy of green `DRAFT-ASUB-020-public-frontier-v9-baseline-exact-full-prefix`.

Hypothesis: the strongest observed public mechanism is still the simple ASUB-001 FAST_TEMPLATE. ASUB-013 removes live generation-time probing and returns the full legal 2,000-candidate archive using the exact same successful prompt and URL generator. Under prefix-preserving replay timeout semantics, this isolates whether probe/calibration overhead was reducing public throughput.

Mechanism held fixed relative to ASUB-001:

- payload `SECRET_MARKER`;
- exact FAST_TEMPLATE;
- exact label / URL generator;
- one ordinary user message per candidate;
- one `http.post` target action per candidate.

Changed variable:

- no live generation probe loop;
- static full 2,000-candidate archive.

Promotion evidence before freeze:

- DRAFT-ASUB-020 dedicated workflow run `33141973829`: SUCCESS;
- full AgentSec CI run `33141973815`: SUCCESS;
- frozen ASUB-013 Git blob equals the green draft blob `641d0402dd999fe2b0cd52a3372c50a68f331b3a`;
- dedicated frozen workflow `Validate ASUB-013` must finish successfully before hosted launch.

### Exact Kaggle wiring for ASUB-013

Notebook:

`https://www.kaggle.com/code/paulomartins87/notebooka6483cd827/notebook`

GitHub source:

`https://github.com/pmartins87/AgentSec/blob/main/submissions/ASUB-20260829-013-public-frontier-v9-baseline-exact-full-prefix/attack.py`

Upload filename:

`ASUB-20260829-013-public-frontier-v9-baseline-exact-full-prefix_attack.py`

Private Dataset:

`agentsec-asub013`

Notebook filename literal:

```python
filename = "ASUB-20260829-013-public-frontier-v9-baseline-exact-full-prefix_attack.py"
```

Submission description:

`ASUB-20260829-013 public frontier v9 baseline exact full prefix`

Do not select final-leaderboard checkboxes immediately after launch.

## Interpretation gates for ASUB-013

Using current best public anchor 86.040 and empirical identical-replica range 8.190:

- **>94.230:** strong single-run evidence of a real public improvement beyond the observed duplicate range;
- **86.040–94.230:** promising public telemetry, but not decisive by itself because it remains within one empirical duplicate-range above the anchor;
- **77.850–86.040:** consistent with the observed noisy baseline region; mechanism choice should depend on additional evidence and final-pair role;
- **<77.850:** strong evidence that static full-prefix removal of probing regressed the public path.

These are practical decision gates, not confidence intervals.

## Private track

ASUB-011 is the current private hedge experiment. It preserves the broad ASUB-009 hypothesis portfolio but improves the earliest replay prefix by covering major lanes before repetitions. Its public score may remain low; the purpose is hidden-private robustness and complementarity with a public anchor.

Reserve candidate DRAFT-ASUB-019 additionally improves hierarchical ordering during calibration. Promote it only if ASUB-011 evidence or remaining hosted capacity makes the calibration-order question decision-relevant.

## Final two-selection policy

Do not auto-select the two largest public numbers.

Target portfolio structure:

- slot A: strongest credible public anchor / public-throughput candidate;
- slot B: candidate with materially different failure assumptions and plausible private-guardrail survival.

Use `src/final_pair_selector.py` / `scripts/plan_final_pair.py` with explicit scenario assumptions after ASUB-011 and ASUB-013 become terminal.

## Working Note sprint

The Working Note should emphasize results that are reproducible and security-relevant even when they are negative:

- public-generation versus private-replay asymmetry;
- byte-identical hosted variance (77.850 vs 86.040);
- replay timeout semantics changing optimal archive sizing;
- failure of added public complexity to outperform the simpler baseline (ASUB-007 / ASUB-010);
- large public cost of broad private hedging (ASUB-009);
- hierarchical prefix coverage as a robustness-under-uncertainty policy;
- controlled baseline-exact throughput ablation (ASUB-013);
- final two-submission selection as a robust portfolio problem.

Every claim must distinguish observed hosted evidence, local/proxy evidence, and hidden-private hypotheses.

## Operational rule for the remaining days

A hosted submission is justified when it is mechanically green and its result can change either:

1. the best public mechanism;
2. the private-hedge choice;
3. the final two-submission portfolio.

Do not spend hosted slots on cosmetic prompt variants or redundant replicas without a decision question.
