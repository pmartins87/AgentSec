# HANDOFF — AgentSec

Use this file as the first read in a dedicated AgentSec chat.

## Mission

Compete seriously for a prize in Kaggle's **AI Agent Security – Multi-Step Tool Attacks**. Entry/Trusted Access were completed before the entry deadline. Final submission deadline: 2026-09-01 23:59 UTC. Optional Working Note deadline: 2026-09-08 23:59 UTC.

## Source of truth

This repository is authoritative for project state, decisions, code, experiments, submissions, frozen artifacts, and Working Note evidence.

## Required first reads

1. `STATUS.md`
2. `ROADMAP.md`
3. `docs/SUBMISSION_LEDGER.md`
4. `docs/NEXT_SUBMISSIONS_20260827.md`
5. `docs/KAGGLE_SUBMISSION_RUNBOOK.md`
6. `docs/WORKING_NOTE_RESULTS_20260827.md`
7. `research/20260826_REPLAY_TIMEOUT_PREFIX.md`
8. `research/20260826_MODEL_FORMAT_DIVERSITY.md`
9. `research/20260827_HIERARCHICAL_CALIBRATION.md`
10. `docs/COMPETITION.md`
11. `docs/OFFICIAL_ARTIFACTS.md`
12. `docs/EXPERIMENT_PROTOCOL.md`

Then inspect the current repository tree and latest commits before changing anything.

## Working rules

- Never optimize from memory when an official competition artifact can be checked.
- Separate verified competition facts, hosted evidence, public-field evidence, and private-evaluator hypotheses.
- Record every actual Kaggle submission and exact code/config that produced it.
- A frozen/prepared ASUB is **not** an actual hosted submission until the Kaggle Submissions page confirms it.
- Require replayability before promoting a discovered finding.
- Maintain stress tests against public-leaderboard overfitting.
- Keep all security experimentation strictly within the competition's authorized offline benchmark.
- Advance as far as possible without unnecessary user micromanagement; surface only meaningful blockers, decisions, or results.

## Current project state

**R0-R3 PASS / R4-R7 optimization active / R8 final-pair selection active / R9 Working Note active.**

### Hosted evidence

- ASUB-001 frozen blob: `b17180572b27d80f584d640d4ebf3ecace28df4d`.
- Kaggle notebook `notebooka6483cd827` Version 4 produced valid `attack.py` + `submission.csv` wiring.
- Byte-identical ASUB-001 hosted results: **77.850** and **86.040**.
- Observed duplicate spread: **8.190 points**; use only as a practical empirical noise band, not a formal confidence interval.
- Current terminal public anchor: **86.040**.

At the last user-visible Kaggle check, the hosted wave contained ASUB-009, ASUB-010, a byte-identical ASUB-010 duplicate, and ASUB-007 in `Running`. Treat this as last-observed state only; do not claim it is still current without a new Kaggle screenshot.

### Frozen public candidates

- **ASUB-004** — controlled public frontier v2.
- **ASUB-005** — paired-hop public frontier v4.
- **ASUB-007** — simpler public timeout-prefix anchor; blob `f5eeb96d050c26544e8d945cf5af66b0977f0ae7`.
- **ASUB-010** — format-diverse public frontier v7; green parent blob `a2a77c684cd6fd9f59f13094bef969eb411246ea`.
- **ASUB-012** — interface-only public frontier v8; green parent blob `698a5f0eaa64b4203ca9d8e2b104e0802800bb39`.

ASUB-012 is the lowest-assumption control: 2,000 ordinary single-message `http.post` candidates with unique synthetic destinations and no model-format framing/search.

### Frozen private-aware candidates

- **ASUB-006** — 360-candidate private hedge v2.
- **ASUB-008** — 2,000-candidate weighted/interleaved timeout-prefix hedge; blob `5f4a675a444027b25071f722421674fc9624040b`.
- **ASUB-009** — 2,000-candidate coverage-first private hedge v4; blob `86444fa16cb817fa210ade4319ec52e8ad5ece6c`.
- **ASUB-011** — hierarchical replay-prefix private hedge v5; frozen from green DRAFT-ASUB-017 blob `5ef4d9ba9f100176d14a3968359ca019d1d14992`.

ASUB-011 preserves ASUB-009 long-run weights but covers all six active hypothesis lanes in the first six replay positions and all eleven families in the first eleven.

### Green reserve experiment

**DRAFT-ASUB-019 — private hedge v6 hierarchical calibration**

`submissions/DRAFT-ASUB-019-private-hedge-v6-hierarchical-calibration/attack.py`

- green blob: `02fc8a021a72942abc885e0bade61f597affaeec`;
- dedicated workflow `33038715155`: **SUCCESS**;
- fallback replay archive is message-for-message identical to DRAFT-ASUB-017/ASUB-011;
- first six calibration probes cover 6/6 lanes versus 2/6 for ASUB-011-style family-local calibration;
- first eleven probes cover 11/11 families versus 6/11;
- first-six lane-coverage AUC: 10 → 21 (+110%);
- first-eleven lane-coverage AUC: 26 → 51 (+96.2%).

Do not freeze/promote DRAFT-ASUB-019 just because it is green. It earns a hosted slot only if private-aware evidence remains strategically relevant and generation-calibration truncation/order sensitivity is plausible.

### Core benchmark-design findings

1. **Public generation/private replay asymmetry:** generation measures public model compliance/latency but cannot observe hidden private survival.
2. **Authorization-context TOCTOU:** runtime guardrail intent can use the current `last_user`, while canonical scorer authorization is recomputed from the final user message.
3. **Replay-timeout semantics:** prefix-preserving replay timeout shifts the optimum from guessed conservative sizing toward full legal archives with value-first or coverage-first prefix ordering.
4. **Model-format diversity:** broad bounded live search can be separated from narrow archive commitment; unsupported format-specific arms fall back to plain.
5. **Private uncertainty:** final selection should preserve mutually conflicting private hypotheses rather than optimize only the public route.
6. **Calibration-prefix robustness:** breadth-first calibration preserves more hypothesis coverage when attack generation is cut off early.

## Immediate handoff queue

1. As soon as any current Kaggle run becomes terminal, update `docs/SUBMISSION_LEDGER.md` with notebook version, actual code identity, exact description, score/error, visible runtime, and interpretation.
2. Use `docs/NEXT_SUBMISSIONS_20260827.md` rather than a fixed submission order. ASUB-011 and ASUB-012 are mechanically ready; their priority depends on the current wave.
3. Do not promote DRAFT-ASUB-019 unless the current hosted evidence makes calibration-order sensitivity decision-relevant.
4. Use `scripts/compare_hosted_candidates.py` for differences relative to the 77.850–86.040 ASUB-001 duplicate band.
5. Use `scripts/plan_final_pair.py` after enough hosted evidence exists; do not choose the final two solely by public score.
6. Continue R9 in parallel: convert confirmed findings, negative results, variance observations, and design ablations into evidence-backed Working Note sections.

See `STATUS.md` for the broader project ledger and `docs/SUBMISSION_LEDGER.md` for hosted history.
