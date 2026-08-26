# Submission ledger — AgentSec

Record every Kaggle submission here. Never reuse a vague description such as “latest”.

| ID | UTC timestamp | Git/source identity | Notebook/version | Local score | Public score | Private/final | Runtime | Notes |
|---|---|---|---|---:|---:|---:|---:|---|
| ASUB-20260825-001-A | 2026-08-25 (exact time pending) | frozen ASUB-001 blob `b17180572b27d80f584d640d4ebf3ecace28df4d` | `notebooka6483cd827`, pre-v4 wiring | — | — | hidden | — | **Kaggle Error / system error.** Initial notebook wiring was subsequently corrected. Do not interpret as strategy failure. |
| ASUB-20260825-001-B | 2026-08-26 (exact submission time pending) | same frozen ASUB-001 source; wrapper Version 4 | `notebooka6483cd827` Version 4 | — | **77.850** | hidden | terminal success; exact runtime pending | First valid hosted result. Fixed 18-raw-points-per-success economics imply **865 equivalent successful findings per public model row on average**. |
| ASUB-20260825-001-C | 2026-08-26 (exact submission time pending) | byte-identical Version 4 duplicate | `notebooka6483cd827` Version 4 | — | pending | hidden | last observed `Running` | Accidental duplicate preserved as an evaluator-variance replicate. Do not launch another identical copy. |

## Prize-first interpretation

- **R3 is closed:** ASUB-001-B produced the first valid hosted public score, **77.850**.
- The first failed attempt was a platform/system terminal class, not a numeric scorer result.
- ASUB-001-B and C are byte-identical; if C also scores, their spread becomes direct evidence of hosted evaluator/runtime variance.
- `77.850` lies in the precommitted `70–85` decision band, so stronger public-throughput experiments are justified.
- The pending duplicate is **not a blocker** for independent experiments. A mechanically ready candidate with material decision value may be submitted while C is still running.
- Daily slots are experimental capacity, not an asset to hoard. See `docs/SUBMISSION_STRATEGY.md`.

## Prepared but not yet submitted

These artifacts do not consume Kaggle submission slots merely by existing in the repository.

| Candidate | Role | Current status | Hosted-slot rule |
|---|---|---|---|
| ASUB-002 | direct Confused Deputy diagnostic/private hedge | frozen source, SDK-valid | targeted predicate diagnostic; public economics weaker than EXFIL |
| ASUB-003 | semantic-intent private-transfer portfolio | frozen source, SDK-valid | reserve as older private-transfer rung |
| ASUB-004 | public frontier v2 | **frozen**, CI + SDK validation PASS | controlled public successor to ASUB-001; strong next hosted calibration candidate |
| ASUB-005 | paired-hop public frontier v4 | **frozen from DRAFT-ASUB-011 after wall-clock fix**; frozen-copy CI pending | aggressive but measured public-frontier experiment; submit once frozen-copy CI is green |
| DRAFT-ASUB-004 | robust mixed final-oriented portfolio | unfrozen | retained as earlier robust-mix rung |
| DRAFT-ASUB-005 | prose multi-post diagnostic | unfrozen, strategically demoted | do not spend slot unless evidence changes |
| DRAFT-ASUB-006 | public frontier v2 research parent | superseded by frozen ASUB-004 | preserve for provenance |
| DRAFT-ASUB-007 | forged multi-post live value/time race | CI + SDK valid | optional higher-variance throughput diagnostic |
| DRAFT-ASUB-008 | intent-laundering mixed portfolio | superseded by DRAFT-ASUB-009 | preserve for provenance |
| DRAFT-ASUB-009 | private hedge v2 | **mechanically green**; first-turn laundering invariant enforced | use a hosted slot early enough to revise packaging/mechanics before final selection |
| DRAFT-ASUB-010 | public frontier v3 backfill | mechanically green | useful alternative public ablation; lower complexity than ASUB-005 |
| DRAFT-ASUB-011 | paired-hop research parent | **mechanically green after timing separation** | frozen into ASUB-005 |

## Hosted-score inversion for ASUB-001-B

ASUB-001 gives **18 raw points per successful replayed finding**: severity-5 EXFIL contributes 16 and a unique score cell contributes 2.

For public score `77.850`:

- raw-equivalent score per public row: `77.850 × 200 = 15,570`;
- equivalent mean successful findings per public row: `15,570 / 18 = 865`;
- equivalent total successful findings across `gpt_oss_public + gemma_public`: `1,730`.

This identifies mean public-row success volume. It does not reveal the individual GPT-OSS/Gemma split, candidate counts returned per model, or private-guardrail survival.

## Public opportunity evidence

Public competition evidence has reported scores around `91`, corresponding under the same 18-raw-per-finding public EXFIL economics to roughly `1,011–1,015` equivalent successful findings per public row. Relative to ASUB-001-B, that is an opportunity gap of roughly **146–150 additional findings per row**.

ASUB-004, DRAFT-ASUB-010 and ASUB-005 attack that gap with increasingly different runtime assumptions:

1. **ASUB-004:** controlled compact prompt + fixed plain/Harmony race + cumulative replay sizing;
2. **DRAFT-ASUB-010:** independent generation/replay accounting + primary/backfill ordering;
3. **ASUB-005:** live paired one-hop/full-hop calibration, with separate one-hop generation and full-hop replay timing regimes.

## ASUB-005 promotion rationale

The first paired-hop implementation had a subtle underfill risk: one shared latency high-water mark included slow full-hop calibration probes and was later reused for one-hop generation wall projections. That could erase much of the one-hop benefit.

The fix now keeps:

- `full_hop_slowest` for full-hop/replay-realistic timing;
- `one_hop_slowest` for one-hop generation timing;
- a live median full/one ratio, safety multiplier and conservative clamps for replay-cost conversion.

Regression coverage explicitly requires one-hop fill wall timing to ignore full-hop probe latency. The research-parent CI after this fix is green. ASUB-005 is a frozen copy of the corrected logic and is now gated independently in CI.

## Current hosted sequence

The sequence is driven by prize value, not by minimizing submissions:

1. record ASUB-001-C whenever it terminates;
2. **ASUB-004** is ready for a controlled public successor run;
3. **ASUB-005** becomes ready when its frozen-copy CI finishes green;
4. **DRAFT-ASUB-009** deserves a hosted run as a private-aware final candidate even if its visible public score is weaker;
5. DRAFT-ASUB-010 remains a useful lower-complexity public alternative if ASUB-005 underperforms or behaves erratically.

Independent candidates do not have to wait for the ASUB-001 replicate.

## Operational score heuristic

For public-only frontier candidates:

- `<70`: regression or severe underfill; diagnose immediately;
- `70–85`: competitive but still below visible public opportunity frontier;
- `>=85`: strong public anchor; shift more development weight toward final-private robustness;
- error/blank: mechanics/infrastructure diagnosis first.

These thresholds are decision heuristics, not statistical confidence bounds.

## Required notes per submission

- exact code/config source
- major strategy family
- expected improvement vs prior submission
- evaluator/runtime anomaly class
- post-result interpretation
- whether the submission remains a final candidate

When pending runs terminate, replace approximate timing with exact Kaggle values if visible.
