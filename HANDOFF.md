# HANDOFF — AgentSec

Use this file as the first read in a dedicated AgentSec chat.

## Mission

Compete seriously for a prize in Kaggle's **AI Agent Security – Multi-Step Tool Attacks**. Entry/Trusted Access were completed before the entry deadline. Final submission deadline: 2026-09-01 23:59 UTC. Optional Working Note deadline: 2026-09-08 23:59 UTC.

## Source of truth

This repository is authoritative for project state, decisions, code, experiments, submissions, and frozen artifacts.

## Required first reads

1. `STATUS.md`
2. `ROADMAP.md`
3. `docs/SUBMISSION_LEDGER.md`
4. `docs/KAGGLE_SUBMISSION_RUNBOOK.md`
5. `docs/WORKING_NOTE_OUTLINE.md`
6. `research/20260826_REPLAY_TIMEOUT_PREFIX.md`
7. `research/20260826_MODEL_FORMAT_DIVERSITY.md`
8. `docs/COMPETITION.md`
9. `docs/OFFICIAL_ARTIFACTS.md`
10. `docs/EXPERIMENT_PROTOCOL.md`

Then inspect the current repository tree and latest commits before changing anything.

## Working rules

- Never optimize from memory when an official competition artifact can be checked.
- Separate verified competition facts, public-field evidence, and private-evaluator hypotheses.
- Record every actual Kaggle submission and exact code/config that produced it.
- A frozen/prepared ASUB is **not** an actual hosted submission until the Kaggle Submissions page confirms it.
- Require replayability before promoting a discovered finding.
- Maintain hold-out/stress tests against public-leaderboard overfitting.
- Keep all security experimentation strictly within the competition's authorized offline benchmark.
- Advance as far as possible without unnecessary user micromanagement; surface only meaningful blockers, decisions, or results.

## Current project state

**R0-R3 PASS / R4-R7 optimization active / R8 final-pair selection active / R9 active.**

### Hosted evidence

- ASUB-001 frozen blob: `b17180572b27d80f584d640d4ebf3ecace28df4d`.
- Kaggle notebook `notebooka6483cd827` Version 4 produced valid `attack.py` + `submission.csv` wiring.
- First valid hosted public result: **77.850**.
- A byte-identical ASUB-001 replicate was last recorded as pending/running and is retained as variance evidence.
- Do not infer the current Kaggle queue from repository state alone; inspect the latest user screenshot before claiming which newer ASUBs are already submitted/running.

### Frozen public candidates

- **ASUB-004** — controlled public frontier v2.
- **ASUB-005** — paired-hop public frontier v4.
- **ASUB-007** — simpler public timeout-prefix anchor; blob `f5eeb96d050c26544e8d945cf5af66b0977f0ae7`.
- **ASUB-010** — newest format-diverse public frontier; exact green DRAFT-ASUB-016 blob `a2a77c684cd6fd9f59f13094bef969eb411246ea`.

ASUB-010 live-races plain, imperative, GPT-OSS-style Harmony, Gemma-style tool-call and bounded three-hop variants. A non-plain arm needs two positive observations and a raw-score-per-second margin over the positive plain anchor before it may own the 2,000-item archive. Full CI run `33018697791` passed before freeze.

### Frozen private-aware candidates

- **ASUB-006** — 360-candidate private hedge v2.
- **ASUB-008** — 2,000-candidate weighted/interleaved timeout-prefix hedge; blob `5f4a675a444027b25071f722421674fc9624040b`.
- **ASUB-009** — preferred new private hedge v4 coverage-prefix; blob `86444fa16cb817fa210ade4319ec52e8ad5ece6c`; every active family appears before any family repeats, then weighted interleaving resumes.

DRAFT-ASUB-015, the research parent of ASUB-009, passed dedicated workflow `33001993816` before freeze.

### Core benchmark-design findings

1. **Public generation/private replay asymmetry:** generation measures public model compliance/latency but cannot observe hidden private survival.
2. **Authorization-context TOCTOU:** runtime guardrail intent can use the current `last_user`, while canonical scorer authorization is recomputed from the final user message.
3. **Replay-timeout semantics:** prefix-preserving replay timeout shifts the optimum from guessed conservative sizing toward full legal archives with value-first or coverage-first prefix ordering.
4. **Model-format diversity:** broad bounded live search can be separated from narrow archive commitment; unsupported format-specific arms fall back to plain.
5. **Private uncertainty:** final selection should preserve mutually conflicting private hypotheses rather than optimize only the public route.

## Immediate handoff queue

1. Verify the freeze-commit CI that directly compiles/SDK-validates ASUB-010 and locks its byte identity to green DRAFT-ASUB-016.
2. As soon as any Kaggle run becomes terminal, update `docs/SUBMISSION_LEDGER.md` with notebook version, exact description, score/error, visible runtime, and interpretation.
3. For a new public hosted slot, compare **ASUB-010** (format-diverse, highest information value) with **ASUB-007** (simpler timeout-prefix anchor) based on what is already queued.
4. Prefer **ASUB-009** over ASUB-008 for a new private timeout-prefix slot; if ASUB-008 is already queued, retain it as a clean ordering ablation.
5. Use `scripts/plan_final_pair.py` after enough hosted evidence exists; do not choose the final two submissions solely by public score.
6. Continue R9 in parallel: convert confirmed findings and negative results into evidence-backed Working Note sections.

See `STATUS.md` for live details and `docs/SUBMISSION_LEDGER.md` for hosted history.
