# STATUS — AgentSec

Last updated: 2026-08-27 after ASUB-011/012 freeze and DRAFT-ASUB-019 validation

## Mission

**Phase: R0-R3 PASS / R4-R7 optimization active / R8 candidate-pair selection active / R9 Working Note active**

Primary objective: maximize the probability of a prize-eligible final result in Kaggle **AI Agent Security – Multi-Step Tool Attacks**. Public score is development telemetry; final private-leaderboard performance is the objective.

Submission policy is prize-first: spend hosted slots when a mechanically ready candidate has material expected score gain or decision value. Do not spend a slot merely because a draft is green.

## Hosted evidence

### ASUB-001 baseline and evaluator variance

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

- first pre-v4 attempt: Kaggle system error;
- corrected Version 4 first copy: **Succeeded / Public Score 77.850**;
- byte-identical Version 4 replicate: **Succeeded / Public Score 86.040**;
- duplicate spread: **8.190 leaderboard points**;
- duplicate mean: **81.945**.

The 8.190 spread is direct evidence that byte-identical hosted executions can differ materially. It is used as a practical empirical comparison band only, not as a confidence interval or stable variance estimate.

Current terminal public anchor: **86.040**.

At the last user-visible Kaggle check, the current hosted wave contained ASUB-009, ASUB-010, a byte-identical ASUB-010 duplicate, and ASUB-007 in `Running`. This is a **last-observed state only** and must not be presented as current without a new Kaggle screenshot.

## Frozen public candidates

### ASUB-007 — timeout-prefix public frontier v6

`submissions/ASUB-20260826-007-public-frontier-v6-timeout-prefix/attack.py`

Frozen blob `f5eeb96d050c26544e8d945cf5af66b0977f0ae7`.

Simpler public timeout-prefix anchor. It performs bounded live calibration and returns the full legal 2,000-candidate archive ordered so replay truncation removes only the suffix.

### ASUB-010 — format-diverse public frontier v7

`submissions/ASUB-20260826-010-public-frontier-v7-format-diverse/attack.py`

Frozen from green DRAFT-ASUB-016 blob `a2a77c684cd6fd9f59f13094bef969eb411246ea`.

It races plain and bounded alternative model-format arms, but non-plain promotion requires repeatable positive evidence and a value/time margin over the plain anchor. Unsupported or inert arms fall back to plain.

### ASUB-012 — interface-only public frontier v8

`submissions/ASUB-20260827-012-public-frontier-v8-interface-only-full-prefix/attack.py`

Frozen from green DRAFT-ASUB-018 blob `698a5f0eaa64b4203ca9d8e2b104e0802800bb39`.

ASUB-012 is the lowest-assumption public control in the current ladder:

- 2,000 ordinary one-message `http.post` candidates;
- one unique synthetic destination per finding;
- no forged model/tool transcript;
- no Harmony/control-token framing;
- no live model-format classification.

Its main value is attribution: if it lands inside the empirical hosted noise band of more complex public candidates, the simpler documented-interface mechanism becomes preferable on robustness grounds; if the complex candidates beat it clearly beyond ordinary run variation, their extra machinery has stronger evidence of value.

## Frozen private-aware candidates

### ASUB-009 — coverage-prefix private hedge v4

`submissions/ASUB-20260826-009-private-hedge-v4-coverage-prefix/attack.py`

Frozen blob `86444fa16cb817fa210ade4319ec52e8ad5ece6c`.

It preserves the private-hypothesis portfolio while giving every active family one replay position before any family repeats. This is the current hosted private-aware reference.

### ASUB-011 — hierarchical replay-prefix private hedge v5

`submissions/ASUB-20260827-011-private-hedge-v5-hierarchical-prefix/attack.py`

Frozen byte-identical from green DRAFT-ASUB-017 blob `5ef4d9ba9f100176d14a3968359ca019d1d14992`.

ASUB-011 keeps ASUB-009's long-run family weights but improves the prefix hierarchy:

- first six replay positions cover all **6/6 active lanes**;
- first eleven positions cover all **11/11 active families**;
- weighted-deficit interleaving then resumes with exact remaining counts.

This is a clean replay-ordering ablation rather than a new private hypothesis set.

## Green reserve — DRAFT-ASUB-019

`submissions/DRAFT-ASUB-019-private-hedge-v6-hierarchical-calibration/attack.py`

Green blob: `02fc8a021a72942abc885e0bade61f597affaeec`.

Dedicated workflow `33038715155`: **SUCCESS** for compile, structural tests, and official `aicomp validate redteam`.

DRAFT-ASUB-019 leaves the ASUB-011 fallback replay archive message-for-message unchanged and changes **generation-time calibration order only**.

ASUB-011-style calibration probes both variants of one family before moving to the next. DRAFT-ASUB-019 instead uses two breadth-first passes over hierarchical family order:

1. variant 0 for every family;
2. variant 1 for every family.

Deterministic early-cutoff comparison:

| Calibration cutoff | ASUB-011-style | DRAFT-ASUB-019 |
|---|---:|---:|
| 6 probes | 3 families / 2 lanes | **6 families / 6 lanes** |
| 11 probes | 6 families / 4 lanes | **11 families / 6 lanes** |

Coverage AUC improvements:

- first-six lane AUC: **10 → 21 (+110%)**;
- first-eleven lane AUC: **26 → 51 (+96.2%)**;
- first-eleven family AUC: **36 → 66 (+83.3%)**.

These are deterministic scheduling metrics, not predicted leaderboard gains.

DRAFT-ASUB-019 must **not** be frozen/promoted automatically. A hosted slot is justified only if private-aware evidence remains strategically relevant and generation-calibration truncation/order sensitivity becomes plausible enough to affect final selection.

Research record: `research/20260827_HIERARCHICAL_CALIBRATION.md`.

## Core benchmark-design findings

1. **Public generation/private replay asymmetry:** generation can measure public compliance/latency but cannot observe hidden private survival.
2. **Authorization-context mismatch:** runtime guardrail intent and canonical scoring authorization can depend on different user-message context.
3. **Replay-timeout semantics:** prefix-preserving replay timeout makes value-first or coverage-first full legal archives attractive because truncation removes only the unprocessed suffix.
4. **Model-format diversity:** broad bounded live search can be separated from narrow archive commitment; unsupported arms can fall back to plain.
5. **Private uncertainty:** final selection should preserve materially different private hypotheses rather than maximize only noisy public score.
6. **Hierarchical replay coverage:** lane-first then family-first prefix ordering improves diversity under short private replays without changing long-run counts.
7. **Hierarchical calibration breadth:** breadth-first generation probes preserve substantially more hypothesis coverage if attack generation is cut short.

## Hosted decision rule

Use `docs/NEXT_SUBMISSIONS_20260827.md` rather than a fixed submission calendar.

With 86.040 as the current anchor and 8.190 as the observed byte-identical spread:

- a candidate above **94.230** exceeds the full current duplicate band relative to the anchor and is stronger one-run evidence of public improvement;
- a candidate below **77.850** is stronger one-run evidence of regression;
- scores between **77.850 and 94.230** should not be over-interpreted without mechanism, replicate, or complementary evidence.

If ASUB-009 remains strategically credible, ASUB-011 is the clean replay-ordering successor. If public candidates cluster inside the practical noise band, ASUB-012 has high decision value as the interface-only control. DRAFT-ASUB-019 becomes eligible only if calibration-order sensitivity is itself decision-relevant.

## Final two-submission selection

Kaggle allows two final selected submissions. `src/final_pair_selector.py` and `scripts/plan_final_pair.py` therefore treat final selection as a **pair** rather than two independent public-leaderboard maxima.

Default intended structure, unless hosted evidence strongly contradicts it:

1. strongest credible public anchor;
2. strongest credible complementary/private-aware hedge.

All private scenario projections remain explicit stress assumptions until supported by evidence.

## CI state

Confirmed green evidence:

- full CI run `33037614910`: **SUCCESS** across compile, structural tests, planners, official SDK validation, deterministic smoke, and Gym smoke;
- DRAFT-ASUB-019 dedicated run `33038715155`: **SUCCESS**;
- ASUB-011 and ASUB-012 were frozen from dedicated green draft blobs.

The latest documentation commits retriggered the repository workflows. Their transient `in_progress` state is not strategy evidence and should not be confused with hosted Kaggle evaluation.

## Working Note

`docs/WORKING_NOTE_RESULTS_20260827.md` now contains evidence-backed prose scaffolding for:

- byte-identical hosted variance;
- replay-timeout archive economics;
- private uncertainty and explicit hypothesis hedging;
- hierarchical replay coverage;
- hierarchical generation-time calibration;
- interface-only public control;
- complementary final-pair selection;
- limitations and responsible interpretation.

Pending inserts are the terminal results of the current hosted wave and the final pair decision.

## Promotion gates

- **R0 PASS:** rules, eligibility, repository and benchmark inventory.
- **R1 PASS:** SDK-aligned baseline/contracts.
- **R2 PASS:** deterministic replay/trace plumbing.
- **R3 PASS:** valid hosted score and byte-identical replicate evidence.
- **R4 active:** predicate-directed reproducible lanes.
- **R5 active:** diversity/coverage engine.
- **R6 active:** runtime allocation, candidate ordering, timeout-prefix, model-format and calibration-prefix optimization.
- **R7 active:** multiple plausible private-guardrail stress models.
- **R8 active:** complementary final-pair selection and hosted evidence gathering.
- **R9 active:** Working Note evidence architecture and finalization.
