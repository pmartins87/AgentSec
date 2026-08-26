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
- **R6 ACTIVE** — one-hop/full-hop timing, multi-post value, timeout-prefix ordering and model-format-diverse calibration under development.
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

Search separately for:

1. EXFILTRATION
2. UNTRUSTED_TO_ACTION
3. DESTRUCTIVE_WRITE
4. CONFUSED_DEPUTY

Candidate methods: state-space exploration, trace-guided mutation, heuristic search, novelty search, evolutionary mutation, archive/Go-Explore-style retention, and carefully budgeted model-assisted generation if allowed/offline-compatible.

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
- Tune breadth/depth/mutation schedules.
- Treat attack-generation timeout and replay-timeout semantics separately.
- Exploit prefix-preserving replay timeout with full legal archives when tail value is non-negative.
- Live-test model-format-diverse arms instead of hard-coding a format assumption.

Current lineage:

- ASUB-005: paired one-hop/full-hop calibration;
- DRAFT-ASUB-012: independent-window multipost bridge;
- ASUB-007: confirmed-arm 2,000-item timeout-prefix public archive;
- DRAFT-ASUB-016: plain/imperative/Harmony/Gemma-format + three-hop live race with confirmation gates.

**Exit:** stable score gain per evaluation budget. **ACTIVE**

## R7 — Private-guardrail robustness

- Avoid strategies dependent only on quirks unique to `OptimalGuardrail`.
- Maintain **multiple conflicting private hypotheses**, not one guessed guardrail.
- Stress payload-sensitive actions with an all-arguments/DLP proxy.
- Stress provenance dependence with a pessimistic web/email-taint proxy.
- Test semantic-authorization hypotheses where scorer literal intent words may disagree with a stricter semantic guardrail.
- Keep a direct confused-deputy hedge that does not require untrusted provenance.
- Order mixed portfolios so replay timeout preserves cross-family coverage.
- Prefer severe, explicit, replay-stable tool actions over unsupported hidden-evaluator speculation.
- Hold out scenarios for final selection.

Current private ladder:

- ASUB-006: 360-candidate baseline mix;
- ASUB-008: 2,000-candidate weighted/interleaved timeout-prefix mix;
- ASUB-009: 2,000-candidate coverage-first timeout-prefix mix, current preferred new private candidate.

**Exit:** final candidate set has evidence across more than one plausible private-defense model and is not dominated by the public sentinel route. **ACTIVE**

## R8 — Final freeze

- Reproduce final notebook from clean environment.
- Confirm internet-off execution, runtime ceiling, `attack.py` output path, no hidden local dependency.
- Freeze source, configuration, hashes, experiment references, and Kaggle submission ID.
- Select up to the competition-allowed final submissions based on complementary private-transfer hypotheses, not a single noisy public score.
- Preserve at least one public-throughput anchor and one private-robust/mixed portfolio unless evidence strongly rejects a lane.
- Use `scripts/plan_final_pair.py` as an explicit decision aid after hosted evidence is populated.

Current candidate structure already supports a public-anchor/private-hedge pair, but hosted comparisons are still incomplete.

**Exit:** final submission accepted before 2026-09-01 23:59 UTC. **ACTIVE**

## R9 — Working Note

- Explain method, reproducibility, benchmark-specific security insight, ablations, failures, and lessons.
- Include authorization-context TOCTOU, public/private staging, timeout semantics, coverage-first ordering, model-format diversity, hosted variance, and negative results.
- Keep discussion confined to the authorized benchmark and responsible communication.

**Exit:** optional Working Note submitted before 2026-09-08 23:59 UTC when quality threshold is met. **ACTIVE**

## Immediate prize-first queue

1. Keep all queued Kaggle experiments running; capture terminal results without launching redundant duplicates.
2. Get DRAFT-ASUB-016 mechanically green; promote/freeze only after CI + official SDK validation.
3. Use ASUB-007 as the strongest current frozen public timeout-prefix hypothesis unless hosted evidence rejects it.
4. Use ASUB-009 as the preferred *new* private timeout-prefix hedge; retain ASUB-008 only as an existing run or deliberate ordering ablation.
5. Feed hosted results into the final-pair scenario table and freeze the final two before the competition deadline.
6. Continue the Working Note in parallel so the writing deadline does not become a post-competition bottleneck.
