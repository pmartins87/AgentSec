# STATUS — AgentSec

Last updated: 2026-08-26 after timeout-prefix optimization wave

## Mission

**Phase: R0-R3 PASS / R4-R7 optimization active / R8 candidate-pair selection active / R9 active**

Primary objective: maximize the probability of a prize-eligible final result in Kaggle **AI Agent Security – Multi-Step Tool Attacks**. Public score is development telemetry; final private-leaderboard performance is the objective.

Submission policy is prize-first: use hosted slots when a mechanically ready run has material expected score gain or decision value. Do not hoard slots, and do not spend them on redundant runs without a question.

## Hosted evidence

### ASUB-001 baseline

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

- first pre-v4 attempt: Kaggle system error;
- corrected Version 4 first copy: **Succeeded / Public Score 77.850**;
- byte-identical Version 4 replicate: last user-observed state still Running;
- 77.850 corresponds to about **865 equivalent 18-raw EXFIL findings per public model row on average**.

The duplicate remains useful as hosted-variance evidence, but it is not a blocker for independent submissions.

## Frozen hosted candidates

### ASUB-004 — controlled public frontier v2

`submissions/ASUB-20260826-004-public-frontier-v2/attack.py`

Frozen, CI/SDK green. Lower-complexity controlled public successor.

### ASUB-005 — paired-hop public frontier v4

`submissions/ASUB-20260826-005-public-frontier-v4-paired-hops/attack.py`

Frozen, frozen-copy CI PASS. Separates one-hop generation timing from full-hop replay calibration and uses live full/one-hop timing evidence.

### ASUB-006 — private hedge v2

`submissions/ASUB-20260826-006-private-hedge-v2/attack.py`

Frozen, frozen-copy CI PASS. 360-candidate mixed portfolio spanning public EXFIL, direct confused deputy and semantic source→action families. Two-message laundering evidence requires the target action during the first interaction while explicit authorization is current.

### ASUB-007 — timeout-prefix public frontier v6

`submissions/ASUB-20260826-007-public-frontier-v6-timeout-prefix/attack.py`

Frozen from mechanically green DRAFT-ASUB-013. Blob SHA `f5eeb96d050c26544e8d945cf5af66b0977f0ae7`.

New evaluator-aware design:

- tiny generation calibration;
- fast row stays plain single-post;
- slow row races plain/Harmony/forged 2..5-post arms by observed public raw score per full-hop second;
- non-plain winner must be confirmed by at least two positive observations and beat the plain anchor by a margin;
- returns the full legal **2,000-candidate** archive from the confirmed arm;
- deliberately does not shorten the archive to an estimated replay cap because the updated evaluator preserves score accumulated before replay timeout.

This is currently the highest-upside public research hypothesis. It remains a distinct experiment from ASUB-005 rather than silently replacing it.

### ASUB-008 — timeout-prefix private hedge v3

`submissions/ASUB-20260826-008-private-hedge-v3-timeout-prefix/attack.py`

Frozen from mechanically green DRAFT-ASUB-014. Blob SHA `5f4a675a444027b25071f722421674fc9624040b`.

It preserves the ASUB-006 private-hypothesis weights but scales the portfolio to the full **2,000 findings** and interleaves families so replay truncation does not discard an entire private hypothesis at the tail. Hidden private behavior remains unknown; this is deliberate uncertainty coverage, not a claim about the secret guardrail.

## Evaluator update and strategic consequence

Kaggle staff announced that public/private **replay timeouts preserve score accumulated before timeout**, while attack-generation timeout remains terminal. This changes the runtime optimization problem.

Earlier strategy: estimate replay capacity conservatively and stop before timeout.

Current timeout-prefix strategy: keep generation safely bounded, identify high-value replay mechanisms, return a value-ordered or robustly interleaved full legal archive, and allow replay truncation to remove only the tail.

Research record: `research/20260826_REPLAY_TIMEOUT_PREFIX.md`.

The Overview currently states 18,000 seconds per target model, while older host discussion described independent phase budgets differently. Runtime code therefore uses live `AttackRunConfig.time_budget_s` and does not hard-code either documentation number.

## New public research ladder

- DRAFT-ASUB-012: independent generation/replay windows + live multi-post arm race + conservative primary/backfill sizing.
- DRAFT-ASUB-013: full timeout-prefix archive; frozen as ASUB-007 after confirmation hardening.
- ASUB-007 is the preferred next-generation public experiment once hosted capacity and current results make it valuable.

## New private research ladder

- ASUB-006: 360-candidate private hedge baseline.
- DRAFT-ASUB-014: same hypothesis mix scaled/interleaved to 2,000 under prefix-preserving replay semantics.
- ASUB-008: frozen copy of DRAFT-ASUB-014 for future hosted use.

## Final two-submission selection

Added `src/final_pair_selector.py` and `scripts/plan_final_pair.py`.

The selector treats the two final Kaggle slots as a **pair**, not as two independent public-LB maxima. Given explicit scenario projections, it minimizes maximum regret relative to the best candidate in each scenario, then maximizes worst-case and weighted-mean pair performance.

All private scenario inputs remain explicit stress assumptions until real evidence exists. The tool does not pretend to know the hidden guardrail.

## CI state

CI run 110 completed **SUCCESS** after the newest DRAFT-ASUB-012/013/014 logic, confirmation tests, final-pair selector tests, SDK validations, deterministic smoke and Gym plumbing checks were present on main.

ASUB-007 and ASUB-008 are exact blob copies of the green DRAFT-ASUB-013 and DRAFT-ASUB-014 sources respectively. Their freeze commit triggered a subsequent CI run; the workflow at that freeze commit still gates the corresponding draft blobs rather than listing the new frozen paths explicitly.

## Current hosted priority

Subject to what is already queued/running in Kaggle:

1. preserve all terminal scores/errors and notebook versions in the ledger;
2. ASUB-005 remains the established advanced public candidate if not already submitted;
3. ASUB-006 remains the established private-aware hedge if not already submitted;
4. ASUB-007 is the next high-upside public experiment based on the new replay-timeout contract;
5. ASUB-008 is the next private-aware timeout-prefix experiment;
6. ASUB-004 remains a valuable controlled public ablation if more hosted evidence is needed.

Do not infer that a lower public score automatically rejects a private-aware candidate.

## Working Note

The Working Note evidence base now includes:

- public-generation/private-replay asymmetry;
- scorer/guardrail authorization-context mismatch;
- first-turn intent laundering tests;
- public throughput vs private robustness;
- hosted evaluator variance;
- first valid public score 77.850;
- one-hop/full-hop calibration;
- multi-post value/time trade-offs;
- **timeout semantics change the optimal archive-sizing policy**: zero-on-timeout favors conservative sizing, prefix-preserving replay timeout favors value-ordered oversubscription.

## Promotion gates

- **R0 PASS:** rules, eligibility, repository and benchmark inventory.
- **R1 PASS:** SDK-aligned baseline/contracts.
- **R2 PASS:** deterministic replay/trace plumbing.
- **R3 PASS:** first valid hosted score = 77.850.
- **R4 active:** predicate-directed reproducible lanes.
- **R5 active:** diversity/coverage engine.
- **R6 active:** runtime allocation, candidate ordering and timeout-prefix optimization.
- **R7 active:** multiple plausible private-guardrail stress models.
- **R8 active:** complementary final-pair selection and hosted evidence gathering.
- **R9 active:** Working Note evidence architecture and finalization.
