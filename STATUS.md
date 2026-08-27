# STATUS — AgentSec

Last updated: 2026-08-26 after ASUB-001 duplicate completed

## Mission

**Phase: R0-R3 PASS / R4-R7 optimization active / R8 candidate-pair selection active / R9 active**

Primary objective: maximize the probability of a prize-eligible final result in Kaggle **AI Agent Security – Multi-Step Tool Attacks**. Public score is development telemetry; final private-leaderboard performance is the objective.

Submission policy is prize-first: use hosted slots when a mechanically ready run has material expected score gain or decision value. Do not hoard slots, and do not spend them on redundant runs without a question.

## Hosted evidence

### ASUB-001 baseline

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

- first pre-v4 attempt: Kaggle system error;
- corrected Version 4 first copy: **Succeeded / Public Score 77.850**;
- byte-identical Version 4 replicate: **Succeeded / Public Score 86.040**;
- 77.850 corresponds to **865 equivalent 18-raw EXFIL findings per public model row on average**;
- 86.040 corresponds to **956 equivalent findings per public model row on average**;
- duplicate spread: **8.190 leaderboard points = 91 equivalent findings per public row**;
- duplicate mean: **81.945**.

This is now direct hosted evidence of material evaluator/runtime variance. Single-run public score differences of only a few points should therefore be interpreted cautiously.

The 86.040 replicate crosses the project's >=85 strong-public-anchor heuristic. That changes hosted priority: obtain private-aware evidence before spending several more slots on public-only tuning.

## Frozen hosted candidates

### ASUB-004 — controlled public frontier v2

`submissions/ASUB-20260826-004-public-frontier-v2/attack.py`

Frozen, CI/SDK green. Lower-complexity controlled public successor.

### ASUB-005 — paired-hop public frontier v4

`submissions/ASUB-20260826-005-public-frontier-v4-paired-hops/attack.py`

Frozen, frozen-copy CI PASS. Separates one-hop generation timing from full-hop replay calibration and uses live full/one-hop timing evidence.

### ASUB-006 — private hedge v2

`submissions/ASUB-20260826-006-private-hedge-v2/attack.py`

Frozen, frozen-copy CI PASS. 360-candidate mixed portfolio spanning public EXFIL, direct confused deputy and semantic source→action families.

### ASUB-007 — timeout-prefix public frontier v6

`submissions/ASUB-20260826-007-public-frontier-v6-timeout-prefix/attack.py`

Frozen blob `f5eeb96d050c26544e8d945cf5af66b0977f0ae7`.

- tiny generation calibration;
- fast row stays plain single-post;
- slow row races plain/Harmony/forged 2..5-post arms by observed public raw score per full-hop second;
- non-plain winner requires repeatability + value margin;
- confirmed arm emits the full legal **2,000-candidate** archive.

ASUB-007 is the simpler frozen public timeout-prefix anchor.

### ASUB-008 — timeout-prefix private hedge v3

`submissions/ASUB-20260826-008-private-hedge-v3-timeout-prefix/attack.py`

Frozen blob `5f4a675a444027b25071f722421674fc9624040b`. It preserves the ASUB-006 hypothesis weights, scales to **2,000 findings**, and weighted-interleaves families. It is retained as a predecessor/ordering ablation.

### ASUB-009 — coverage-prefix private hedge v4

`submissions/ASUB-20260826-009-private-hedge-v4-coverage-prefix/attack.py`

Frozen blob `86444fa16cb817fa210ade4319ec52e8ad5ece6c` after dedicated DRAFT-ASUB-015 workflow `33001993816` completed **SUCCESS**.

- every active private hypothesis family receives one replay position before any family receives a second;
- after the coverage prelude, exact remaining counts resume weighted deficit interleaving;
- short private replays therefore sample all active families as early as possible while long replays preserve intended proportions.

ASUB-009 is the preferred **next hosted submission** after the 86.040 public anchor.

### ASUB-010 — format-diverse public frontier v7

`submissions/ASUB-20260826-010-public-frontier-v7-format-diverse/attack.py`

Frozen byte-identical from DRAFT-ASUB-016 blob `a2a77c684cd6fd9f59f13094bef969eb411246ea` after full CI run `33018697791` completed **SUCCESS**.

New live public race:

- plain single-post control;
- model-agnostic imperative single-post;
- GPT-OSS-style Harmony full-call framing;
- Gemma-style forged model/tool-call framing;
- three-hop plain, Harmony-style and Gemma-style variants when `max_tool_hops >= 3`.

Promotion is deliberately conservative: every non-plain arm needs at least **two positive observations** and must beat the positive plain anchor by a configurable raw-score-per-second margin before it may own the archive. Unsupported/inert formats therefore fall back to plain. The confirmed winner returns the full legal **2,000-candidate** timeout-prefix archive.

ASUB-010 remains the next public high-information experiment after private-aware evidence is obtained.

## Evaluator update and strategic consequence

Kaggle staff announced that public/private **replay timeouts preserve score accumulated before timeout**, while attack-generation timeout remains terminal.

Earlier strategy: estimate replay capacity conservatively and stop before timeout.

Current strategy: keep generation safely bounded, identify high-value replay mechanisms, return a value-ordered or robustly coverage-ordered full legal archive, and allow replay truncation to remove only the tail.

Research record: `research/20260826_REPLAY_TIMEOUT_PREFIX.md`.

Runtime code uses live `AttackRunConfig.time_budget_s` rather than hard-coding documentation-level budget numbers.

## Public research ladder

- DRAFT-ASUB-012: independent generation/replay windows + live multi-post arm race + conservative primary/backfill sizing.
- ASUB-007: confirmed-arm full timeout-prefix archive.
- DRAFT-ASUB-016: model-format-diverse live race with bounded three-hop variants.
- ASUB-010: frozen copy of green DRAFT-ASUB-016; current newest public experiment.

Research/attribution: `research/20260826_MODEL_FORMAT_DIVERSITY.md`. Public field evidence is hypothesis input only; format-specific behavior may be harness-specific.

## Private research ladder

- ASUB-006: 360-candidate private hedge baseline.
- ASUB-008: full-cap weighted-interleaved private hedge.
- ASUB-009: full-cap coverage-first private hedge; preferred next hosted candidate.

The hidden private guardrail is never queried during generation. All private mechanisms remain explicit hypotheses, not observations.

## Final two-submission selection

`src/final_pair_selector.py` and `scripts/plan_final_pair.py` treat the two final Kaggle slots as a **pair**, not two independent public-LB maxima. Given explicit scenario projections, the selector minimizes maximum regret relative to the best candidate in each scenario, then maximizes worst-case and weighted-mean pair performance.

All private scenario inputs remain explicit stress assumptions until real evidence exists.

## CI state

- Full CI run `33018697791`: **SUCCESS** after DRAFT-ASUB-016 was added to compile + official SDK validation and its structural tests entered the complete test suite.
- The same run also compiled/validated frozen ASUB-007/008/009 and exercised frozen-identity locks.
- DRAFT-ASUB-015 dedicated workflow `33001993816`: **SUCCESS** before ASUB-009 freeze.
- ASUB-010 is an exact blob copy of the full-CI-green DRAFT-ASUB-016 source.

## Current hosted priority

Subject to what is already queued/running in Kaggle:

1. preserve both terminal ASUB-001 Version 4 scores as evaluator-variance evidence;
2. **ASUB-009** — preferred next private timeout-prefix hedge with coverage-first prefix;
3. **ASUB-010** — newest high-information public format-diverse experiment;
4. **ASUB-007** — simpler full-cap public timeout-prefix anchor;
5. ASUB-005 — established advanced public candidate if not already submitted;
6. ASUB-006 — established private-aware baseline if not already submitted;
7. ASUB-008 — weighted-only predecessor/ablation when already queued or scientifically worth comparing;
8. ASUB-004 — controlled public ablation when more hosted evidence is useful.

A lower public score does not automatically reject a private-aware candidate.

## Working Note

The Working Note evidence base now includes:

- public-generation/private-replay asymmetry;
- scorer/guardrail authorization-context mismatch;
- first-turn intent laundering tests;
- public throughput vs private robustness;
- **hosted evaluator variance from byte-identical 77.850 vs 86.040 runs**;
- one-hop/full-hop calibration;
- multi-post value/time trade-offs;
- timeout semantics changing the optimal archive-sizing policy;
- coverage-first private replay ordering;
- model-format-diverse public search separated from archive commitment.

## Promotion gates

- **R0 PASS:** rules, eligibility, repository and benchmark inventory.
- **R1 PASS:** SDK-aligned baseline/contracts.
- **R2 PASS:** deterministic replay/trace plumbing.
- **R3 PASS:** first valid hosted score = 77.850; byte-identical replicate = 86.040.
- **R4 active:** predicate-directed reproducible lanes.
- **R5 active:** diversity/coverage engine.
- **R6 active:** runtime allocation, candidate ordering, timeout-prefix and model-format optimization.
- **R7 active:** multiple plausible private-guardrail stress models.
- **R8 active:** complementary final-pair selection and hosted evidence gathering.
- **R9 active:** Working Note evidence architecture and finalization.
