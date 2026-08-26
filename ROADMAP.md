# ROADMAP — AgentSec

## Objective

Maximize the probability of a prize-eligible final result by combining strong leaderboard performance with replay robustness and coverage of diverse security predicates/tool-call signatures.

## R0 — Intake and freeze official facts

- Capture competition rules, timeline, scoring formula, runtime constraints, submission interface, starter notebook, SDK version, and evaluator notes.
- Record any organizer evaluator changes with dates.
- Freeze copies/hashes of official assets where permitted.

**Exit:** all competition-critical facts are reproducible from repository notes.

## R1 — Baseline reproduction

- Run official starter end-to-end.
- Confirm `AttackAlgorithm` contract and candidate serialization.
- Confirm deterministic reset/replay behavior.
- Log baseline runtime, candidate count, predicate mix, diversity cells, score.

**Exit:** repeatable baseline and smoke tests.

## R2 — Local evaluator and trace laboratory

- Build trace capture and canonicalization.
- Classify successful/failed tool calls and predicate triggers.
- Add replay verification before accepting any candidate.
- Create seed/scenario fixtures and regression tests.

**Exit:** local experiment results can be trusted enough to drive search.

## R3 — First competitive submission

- Produce a valid Kaggle notebook with internet disabled.
- Submit an intentionally simple, auditable searcher.
- Reconcile local metrics with hosted evaluation.

**Exit:** first scored submission and documented local↔Kaggle deltas.

## R4 — Predicate-directed search

Search separately for:

1. EXFILTRATION
2. UNTRUSTED_TO_ACTION
3. DESTRUCTIVE_WRITE
4. CONFUSED_DEPUTY

Candidate methods: state-space exploration, trace-guided mutation, heuristic search, novelty search, evolutionary mutation, archive/Go-Explore-style retention, and carefully budgeted model-assisted generation if allowed/offline-compatible.

**Exit:** reproducible nontrivial findings in multiple predicate families.

## R5 — Diversity and archive engine

- Canonicalize tool-call signatures/cells.
- Reward novel cells in addition to severity.
- Deduplicate semantically equivalent candidates.
- Maintain elite archive by predicate, scenario, tool sequence, depth, model, and replay rate.

**Exit:** robust gain over R3/R4 under fixed compute.

## R6 — Budget optimization

- Estimate expected score gain per unit runtime.
- Allocate search between GPT-OSS and Gemma characteristics without assuming identical behavior.
- Early-stop dead branches and prioritize promising traces.
- Tune breadth/depth/mutation schedules.

**Exit:** stable score gain per evaluation budget.

## R7 — Private-guardrail robustness

- Avoid strategies dependent on quirks unique to `OptimalGuardrail`.
- Maintain **multiple conflicting private hypotheses**, not one guessed guardrail.
- Stress payload-sensitive actions with an all-arguments/DLP proxy.
- Stress provenance dependence with a pessimistic web/email-taint proxy.
- Test the semantic-authorization hypothesis: scorer literal intent words may disagree with a stricter semantic guardrail.
- Keep a direct confused-deputy hedge that does not require untrusted provenance.
- Order mixed portfolios so replay timeout still preserves cross-family coverage.
- Prefer severe, explicit, replay-stable tool actions over harness-only tricks.
- Hold out scenarios for final selection.

**Exit:** final candidate set has evidence across more than one plausible private-defense model and is not dominated by the public sentinel route.

## R8 — Final freeze

- Reproduce final notebook from clean environment.
- Confirm internet-off execution, runtime ceiling, `attack.py` output path, no hidden local dependency.
- Freeze source, configuration, hashes, experiment references, and Kaggle submission ID.
- Select up to the competition-allowed final submissions based on complementary private-transfer hypotheses, not a single noisy public score.
- Preserve at least one public-throughput anchor and one private-robust/mixed portfolio unless evidence strongly rejects a lane.

**Exit:** final submission accepted before 2026-09-01 23:59 UTC.

## R9 — Working Note

- Explain method, reproducibility, benchmark-specific security insight, ablations, failures, and lessons.
- Keep discussion confined to the authorized benchmark and responsible communication.

**Exit:** optional Working Note submitted before 2026-09-08 23:59 UTC when quality threshold is met.
