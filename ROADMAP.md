# ROADMAP — AgentSec

## Objective

Maximize the probability of a prize-eligible final result by combining strong leaderboard performance with replay robustness and coverage of diverse security predicates/tool-call signatures.

## Current milestone position — 2026-08-26

- **R0 PASS** — competition facts, rules, deadlines, scorer and evaluator architecture frozen.
- **R1 PASS** — SDK-aligned attack contract and CI validation established.
- **R2 PASS** — trace/scorer/proxy regression laboratory established.
- **R3 PASS** — first valid hosted result: ASUB-001 public **77.850**.
- **R4 ACTIVE** — predicate-directed lanes implemented; several public-negative surfaces documented.
- **R5 ACTIVE** — diversity, deduplication and mixed-family archives implemented.
- **R6 ACTIVE** — one-hop/full-hop timing, multi-post value, timeout-prefix ordering and model-format-diverse calibration implemented in frozen/draft candidates.
- **R7 ACTIVE** — conflicting private stress models plus mixed public/private hedges; ASUB-009 is current coverage-first private candidate.
- **R8 ACTIVE** — frozen candidates exist on both public-anchor and private-hedge sides; final-pair selector implemented; hosted evidence still needed before final freeze.
- **R9 ACTIVE** — Working Note outline/evidence base is being written in parallel.

## R0 — Intake and freeze official facts

- Capture competition rules, timeline, scoring formula, runtime constraints, submission interface, starter notebook, SDK version, and evaluator notes.
- Record organizer evaluator changes with dates.
- Freeze copies/hashes of official assets where permitted.

**Exit:** all competition-critical facts are reproducible from repository notes. **PASS**

## R1 — Baseline reproduction

- Run official starter end-to-end.
- Confirm `AttackAlgorithm` contract and candidate serialization.
- Confirm deterministic reset/replay behavior.
- Log baseline runtime, candidate count, predicate mix, diversity cells, score.

**Exit:** repeatable baseline and smoke tests. **PASS**

## R2 — Local evaluator and trace laboratory

- Build trace capture and canonicalization.
- Classify successful/failed tool calls and predicate triggers.
- Add replay verification before accepting any candidate.
- Create seed/scenario fixtures and regression tests.

**Exit:** local experiment results can be trusted enough to drive search. **PASS**

## R3 — First competitive submission

- Produce a valid Kaggle notebook with internet disabled.
- Submit an intentionally simple, auditable searcher.
- Reconcile local metrics with hosted evaluation.

**Exit:** first scored submission and documented local↔Kaggle deltas. **PASS — ASUB-001 = 77.850 public**

## R4 — Predicate-directed search

Search separately for EXFILTRATION, UNTRUSTED_TO_ACTION, DESTRUCTIVE_WRITE and CONFUSED_DEPUTY. Candidate methods include state-space exploration, trace-guided mutation, heuristic/novelty search, evolutionary mutation and replay-validated archive retention.

Current evidence includes public EXFIL reachability, direct confused-deputy constructions, semantic source→action hypotheses, protected-root/write negatives, and public U2A structural limitations.

**Exit:** reproducible nontrivial findings in multiple predicate families. **ACTIVE**

## R5 — Diversity and archive engine

- Canonicalize tool-call signatures/cells.
- Reward novel cells in addition to severity.
- Deduplicate semantically equivalent candidates.
- Maintain elite archive by predicate, scenario, tool sequence, depth, model, and replay rate.
- Preserve cross-family coverage near the beginning of timeout-truncated private archives.

Current implementation includes argument-level diversity, weighted deficit interleaving, and ASUB-009's coverage-first prelude.

**Exit:** robust gain over R3/R4 under fixed compute. **ACTIVE**

## R6 — Budget optimization

- Estimate expected score gain per unit runtime.
- Allocate search between GPT-OSS and Gemma characteristics without assuming identical behavior.
- Early-stop dead branches and prioritize promising traces.
- Treat attack-generation timeout and replay-timeout semantics separately.
- Exploit prefix-preserving replay timeout with full legal archives when tail value is non-negative.
- Live-test model-format-diverse arms instead of hard-coding a format assumption.

Current lineage:

- ASUB-005: paired one-hop/full-hop calibration;
- DRAFT-ASUB-012: independent-window multipost bridge;
- ASUB-007: confirmed-arm 2,000-item timeout-prefix public archive;
- DRAFT-ASUB-016: green format-diverse research parent;
- **ASUB-010:** frozen format-diverse public frontier, same green blob as DRAFT-ASUB-016.

**Exit:** stable score gain per evaluation budget. **ACTIVE**

## R7 — Private-guardrail robustness

- Maintain **multiple conflicting private hypotheses**, not one guessed guardrail.
- Stress payload-sensitive actions, provenance dependence, semantic authorization and direct confused-deputy behavior.
- Order mixed portfolios so replay timeout preserves cross-family coverage.
- Prefer severe, explicit, replay-stable tool actions over unsupported hidden-evaluator speculation.
- Hold out scenarios for final selection.

Current private ladder:

- ASUB-006: 360-candidate baseline mix;
- ASUB-008: 2,000-candidate weighted/interleaved timeout-prefix mix;
- **ASUB-009:** 2,000-candidate coverage-first timeout-prefix mix, current preferred new private candidate.

**Exit:** final candidate set has evidence across more than one plausible private-defense model and is not dominated by the public sentinel route. **ACTIVE**

## R8 — Final freeze

- Reproduce final notebook from clean environment.
- Confirm internet-off execution, runtime ceiling, `attack.py` output path, no hidden local dependency.
- Freeze source, configuration, hashes, experiment references, and Kaggle submission ID.
- Select the final submissions based on complementary private-transfer hypotheses, not a single noisy public score.
- Preserve at least one public-throughput anchor and one private-robust/mixed portfolio unless evidence strongly rejects a lane.
- Use `scripts/plan_final_pair.py` as an explicit decision aid after hosted evidence is populated.

Current candidate structure:

- public side: ASUB-007 simple timeout-prefix anchor, ASUB-010 format-diverse timeout-prefix challenger, plus older ASUB-004/005 controls;
- private side: ASUB-009 preferred coverage-first hedge, ASUB-008 weighted-only ablation, ASUB-006 baseline mix.

**Exit:** final submission accepted before 2026-09-01 23:59 UTC. **ACTIVE**

## R9 — Working Note

- Explain method, reproducibility, benchmark-specific security insight, ablations, failures, and lessons.
- Include authorization-context TOCTOU, public/private staging, timeout semantics, coverage-first ordering, model-format diversity, hosted variance, and negative results.
- Keep discussion confined to the authorized benchmark and responsible communication.

**Exit:** optional Working Note submitted before 2026-09-08 23:59 UTC when quality threshold is met. **ACTIVE**

## Immediate prize-first queue

1. Keep all queued Kaggle experiments running; capture terminal results without launching redundant duplicates.
2. Verify the freeze-commit CI for ASUB-010 and its exact draft↔frozen identity.
3. Use hosted capacity on independent questions, with ASUB-010/ASUB-007 representing different public hypotheses and ASUB-009 the preferred new private hedge.
4. Feed hosted results into the final-pair scenario table and freeze the final two before the competition deadline.
5. Continue the Working Note in parallel so the writing deadline does not become a post-competition bottleneck.
