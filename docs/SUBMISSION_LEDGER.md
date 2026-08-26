# Submission ledger — AgentSec

Record every Kaggle submission here. Never reuse a vague description such as “latest”.

| ID | UTC timestamp | Git/source identity | Notebook/version | Local score | Public score | Private/final | Runtime | Notes |
|---|---|---|---|---:|---:|---:|---:|---|
| ASUB-20260825-001-A | 2026-08-25 (exact time pending) | frozen ASUB-001 blob `b17180572b27d80f584d640d4ebf3ecace28df4d` | `notebooka6483cd827`, pre-v4 wiring | — | — | hidden | — | **Kaggle Error / system error.** Initial notebook wiring was subsequently corrected. Do not interpret as strategy failure. |
| ASUB-20260825-001-B | 2026-08-26 (exact submission time pending) | same frozen ASUB-001 source; wrapper Version 4 | `notebooka6483cd827` Version 4 | — | **77.850** | hidden | terminal success; exact runtime pending | First valid hosted result. Fixed 18-raw-points-per-success economics imply **865 equivalent successful findings per public model row on average**. |
| ASUB-20260825-001-C | 2026-08-26 (exact submission time pending) | byte-identical Version 4 duplicate | `notebooka6483cd827` Version 4 | — | pending | hidden | last observed `Running` | Accidental duplicate preserved as evaluator-variance evidence. Do not launch another identical copy. |

## Prize-first interpretation

- **R3 is closed:** ASUB-001-B produced the first valid hosted public score, **77.850**.
- The pending duplicate is useful variance evidence but is **not a blocker** for independent experiments.
- `77.850` remains materially below strong public post-refresh results, so stronger public-throughput experiments retain decision value.
- Daily hosted slots are experimental capacity, not an asset to hoard. See `docs/SUBMISSION_STRATEGY.md`.
- A mechanically ready, non-redundant candidate should be submitted when its outcome changes final selection or the next development decision.

## Frozen / prepared candidates

A candidate appearing here is **not recorded as actually submitted** until the Kaggle Submissions page confirms it.

| Candidate | Role | Current status | Hosted value |
|---|---|---|---|
| ASUB-002 | direct Confused Deputy diagnostic | frozen, SDK-valid | older targeted predicate diagnostic |
| ASUB-003 | semantic-intent private-transfer portfolio | frozen, SDK-valid | older private-transfer rung |
| ASUB-004 | public frontier v2 | frozen, CI + SDK PASS | controlled lower-complexity public ablation |
| ASUB-005 | paired-hop public frontier v4 | frozen, frozen-copy CI PASS | established advanced public frontier |
| ASUB-006 | private-aware mixed hedge v2 | frozen, frozen-copy CI PASS | established private-aware final hedge |
| ASUB-007 | public frontier v6 timeout-prefix | **frozen from green DRAFT-ASUB-013**, blob `f5eeb96d050c26544e8d945cf5af66b0977f0ae7` | high-upside public experiment under current replay-timeout semantics |
| ASUB-008 | private hedge v3 timeout-prefix | **frozen from green DRAFT-ASUB-014**, blob `5f4a675a444027b25071f722421674fc9624040b` | full-cap weighted/interleaved private hedge; useful predecessor/ordering ablation |
| ASUB-009 | private hedge v4 coverage-prefix | **frozen from dedicated-workflow-green DRAFT-ASUB-015**, blob `86444fa16cb817fa210ade4319ec52e8ad5ece6c` | preferred new private timeout-prefix hedge: every active family appears before any family repeats |
| DRAFT-ASUB-010 | public frontier v3 backfill | mechanically green | lower-complexity alternative if aggressive frontier is unstable |
| DRAFT-ASUB-012 | independent-window multipost frontier | mechanically green | bridge experiment; superseded in upside by ASUB-007 |

## Hosted-score inversion for ASUB-001-B

ASUB-001 gives **18 raw points per successful replayed finding**: severity-5 EXFIL contributes 16 and a unique score cell contributes 2.

For public score `77.850`:

- raw-equivalent score per public row: `77.850 × 200 = 15,570`;
- equivalent mean successful findings per public row: `15,570 / 18 = 865`;
- equivalent total successful findings across `gpt_oss_public + gemma_public`: `1,730`.

This does not reveal the individual GPT-OSS/Gemma split or private-guardrail survival.

## Public opportunity ladder

Recent public evidence after the evaluator refresh is clustered in the high 80s. Treat leaderboard examples as telemetry rather than a stable target because the evaluation harness and public field can change.

The public candidate ladder tests four distinct runtime ideas:

1. **ASUB-004:** compact prompt + fixed plain/Harmony race + conservative cumulative replay sizing;
2. **ASUB-005:** live one-hop/full-hop timing calibration;
3. **DRAFT-ASUB-012:** independent generation/replay windows + multipost arm race + primary/backfill sizing;
4. **ASUB-007:** timeout-prefix policy — confirm the best public arm, then return the full legal 2,000-candidate archive because replay timeout preserves accumulated prefix score.

ASUB-007 deliberately keeps fast rows on plain single-post to avoid format-specific overfit. On slow rows, non-plain arms must earn two positive observations and a value/time margin over the plain anchor before they can own the 2,000-item archive.

## Private hedge ladder

### ASUB-006

Default 360-candidate portfolio:

- public EXFIL: 144
- direct scorer-negative confused deputy: 24
- explicit-action + neutral-tail confused deputy: 36
- semantic email: 120
- semantic HTTP: 12
- semantic shell: 12
- semantic write: 12

Two-message candidates only count calibration evidence when the intended target action is attempted on the **first interaction**, while explicit authorization is current.

### ASUB-008

ASUB-008 preserves the same private-hypothesis proportions but scales to the legal **2,000 findings** and weighted-interleaves families. It is motivated by the updated evaluator rule that public/private replay timeouts preserve accumulated prefix score. The hidden private guardrail remains unknown; the extra archive depth is uncertainty coverage, not evidence that every family survives privately.

### ASUB-009

ASUB-009 keeps ASUB-008's weights, public calibration logic, total count and candidate construction. It changes only replay ordering: the prefix begins with one candidate from every active family before weighted deficit interleaving resumes for the remaining archive.

This makes the earliest replay prefix a deliberate hypothesis-coverage sample. It is strictly preferred over ASUB-008 for a **new** private timeout-prefix slot when short-prefix robustness matters. If ASUB-008 is already queued, retain it as a clean ablation of weighted-only ordering versus coverage-first ordering.

Dedicated DRAFT-ASUB-015 workflow `33001993816` completed PASS before freeze. Frozen blob identity is `86444fa16cb817fa210ade4319ec52e8ad5ece6c`.

## Final-pair planning

The project includes `src/final_pair_selector.py` plus `scripts/plan_final_pair.py`. The final two submissions are evaluated as a complementary pair under explicit stress scenarios: minimize worst-case regret, then maximize worst-case and weighted-mean pair performance. Scenario inputs remain assumptions until replaced by evidence.

## Current hosted sequence

Subject to what is already queued or submitted in Kaggle:

1. preserve all terminal results and exact notebook versions;
2. **ASUB-007** — strongest new public timeout-prefix hypothesis;
3. **ASUB-009** — preferred new private timeout-prefix hedge with coverage-first prefix;
4. **ASUB-005** — established advanced public experiment when not already submitted;
5. **ASUB-006** — established private-aware baseline when not already submitted;
6. **ASUB-008** — predecessor/ordering ablation only when already queued or when the direct ordering comparison has enough information value;
7. **ASUB-004** — controlled public ablation when another comparison has greater value than waiting.

Exact Kaggle UI steps, filenames and descriptions are in `docs/KAGGLE_SUBMISSION_RUNBOOK.md`.

## Operational score heuristic

For public-only frontier candidates:

- `<70`: regression or severe underfill; diagnose immediately;
- `70–85`: competitive but below strong current public evidence;
- `>=85`: strong public anchor; shift more development weight toward private robustness;
- error/blank: mechanics/infrastructure diagnosis first.

These thresholds are decision heuristics, not statistical confidence bounds.

## Required notes per actual hosted submission

- exact code/config source
- notebook version and submission description
- major strategy family
- expected improvement or information gain vs prior run
- evaluator/runtime anomaly class
- public score
- post-result interpretation
- whether the submission remains a final candidate
