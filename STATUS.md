# STATUS — AgentSec

Last updated: 2026-08-26 after ASUB-009 coverage-prefix promotion

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

Evaluator-aware design:

- tiny generation calibration;
- fast row stays plain single-post;
- slow row races plain/Harmony/forged 2..5-post arms by observed public raw score per full-hop second;
- non-plain winner must be confirmed by at least two positive observations and beat the plain anchor by a margin;
- returns the full legal **2,000-candidate** archive from the confirmed arm;
- does not shorten the archive to an estimated replay cap because the updated evaluator preserves score accumulated before replay timeout.

This remains the highest-upside frozen public research hypothesis.

### ASUB-008 — timeout-prefix private hedge v3

`submissions/ASUB-20260826-008-private-hedge-v3-timeout-prefix/attack.py`

Frozen from mechanically green DRAFT-ASUB-014. Blob SHA `5f4a675a444027b25071f722421674fc9624040b`.

It preserves the ASUB-006 private-hypothesis weights, scales to **2,000 findings**, and weighted-interleaves families. It is retained as a clean predecessor/ordering ablation.

### ASUB-009 — coverage-prefix private hedge v4

`submissions/ASUB-20260826-009-private-hedge-v4-coverage-prefix/attack.py`

Frozen from DRAFT-ASUB-015 after dedicated workflow `33001993816` completed **SUCCESS** with compile, structural tests and official SDK validation all green. Blob SHA `86444fa16cb817fa210ade4319ec52e8ad5ece6c`.

ASUB-009 preserves ASUB-008's weights, calibration logic, candidate construction and 2,000-item cap but changes the replay order:

- each active private hypothesis family receives one replay position before any family receives a second;
- after the coverage prelude, the exact remaining counts resume weighted deficit interleaving;
- therefore an unexpectedly short private replay samples all active families as early as possible while long replays preserve the intended portfolio proportions.

This is now the preferred **new** private timeout-prefix submission. ASUB-008 remains valuable if already queued or if a direct ordering ablation is worth a hosted slot.

## Evaluator update and strategic consequence

Kaggle staff announced that public/private **replay timeouts preserve score accumulated before timeout**, while attack-generation timeout remains terminal. This changes the runtime optimization problem.

Earlier strategy: estimate replay capacity conservatively and stop before timeout.

Current strategy: keep generation safely bounded, identify high-value replay mechanisms, return a value-ordered or robustly coverage-ordered full legal archive, and allow replay truncation to remove only the tail.

Research record: `research/20260826_REPLAY_TIMEOUT_PREFIX.md`.

Runtime code uses live `AttackRunConfig.time_budget_s` rather than hard-coding documentation-level budget numbers.

## Public research ladder

- DRAFT-ASUB-012: independent generation/replay windows + live multi-post arm race + conservative primary/backfill sizing.
- DRAFT-ASUB-013: full timeout-prefix archive; frozen as ASUB-007 after confirmation hardening.
- ASUB-007 is the preferred frozen public timeout-prefix experiment.
- Next public research should test **model-format-diverse live arms** only through bounded public calibration, keeping plain fallback and requiring confirmation before any format-specific arm owns the archive.

## Private research ladder

- ASUB-006: 360-candidate private hedge baseline.
- ASUB-008: full-cap weighted-interleaved private hedge.
- DRAFT-ASUB-015: coverage-first evolution of ASUB-008.
- ASUB-009: frozen coverage-first private hedge; preferred new private timeout-prefix candidate.

The hidden private guardrail is never queried during generation. All private mechanisms remain explicit hypotheses, not observations.

## Final two-submission selection

`src/final_pair_selector.py` and `scripts/plan_final_pair.py` treat the two final Kaggle slots as a **pair**, not two independent public-LB maxima. Given explicit scenario projections, the selector minimizes maximum regret relative to the best candidate in each scenario, then maximizes worst-case and weighted-mean pair performance.

All private scenario inputs remain explicit stress assumptions until real evidence exists.

## CI state

- CI run 110 completed **SUCCESS** with DRAFT-ASUB-012/013/014, final-pair selector, SDK validation, deterministic smoke and Gym plumbing.
- DRAFT-ASUB-015 dedicated workflow `33001993816` completed **SUCCESS** before ASUB-009 freeze.
- ASUB-009 is the exact DRAFT-ASUB-015 blob `86444fa16cb817fa210ade4319ec52e8ad5ece6c`.
- Main CI is being expanded to compile and officially validate frozen ASUB-007/008/009, compile DRAFT-ASUB-015, run the full structural suite, and lock draft↔frozen byte identity.

## Current hosted priority

Subject to what is already queued/running in Kaggle:

1. preserve all terminal scores/errors and notebook versions in the ledger;
2. **ASUB-007** — strongest new public timeout-prefix hypothesis;
3. **ASUB-009** — preferred new private timeout-prefix hedge;
4. ASUB-005 — established advanced public candidate if not already submitted;
5. ASUB-006 — established private-aware baseline if not already submitted;
6. ASUB-008 — weighted-only predecessor/ablation when already queued or scientifically worth comparing;
7. ASUB-004 — controlled public ablation when more hosted evidence is useful.

A lower public score does not automatically reject a private-aware candidate.

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
- **timeout semantics change the optimal archive-sizing policy**;
- **coverage-first private replay ordering** as a robust response when a prefix-preserving timeout can truncate an uncertain mixed portfolio.

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
