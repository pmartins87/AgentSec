# DRAFT-ASUB-023 — public frontier v12 gated online autotuner

Status: **FINAL PUBLIC CANDIDATE / NO NEW SCORE-CHASING EXPERIMENTS**

## Why v11 was not frozen unchanged

The final review found two avoidable risks in DRAFT-ASUB-022:

1. it raced multipost on every target row, so one noisy successful Gemma probe could promote a strategy for which post-refresh public evidence is negative;
2. it returned valid probes from losing arms, consuming replay prefix with candidates the autotuner itself had rejected.

The v11 CI failures were test-suite assumptions, not Python compilation failures, but the candidate was not frozen because the final architecture could be made safer and more evidence-aligned first.

## Evidence incorporated

Project-hosted evidence:

- ASUB-001 remains the strongest directly observed AgentSec public anchor: 77.850 and 86.040 on byte-identical hosted repetitions.
- ASUB-013 scored 60.500 after removing live keep-only-if-fired generation and returning a blind static archive, establishing that live filtering/runtime adaptation is causal rather than cosmetic.
- 2026-09-01 per-model diagnostic: the plain single-POST primitive fired 56/56 short GPT-OSS probes and 80/80 Gemma probes; Gemma generation was fast, but an eight-candidate replay still consumed ~85.1 s. Generation latency is therefore an imperfect replay-cost proxy.

Independent post-refresh public evidence incorporated conservatively:

- Gemma remains best treated as a reliable single-step row; Gemma multipost has been reported to regress materially.
- Harmony analysis-channel compression is a large GPT-OSS throughput lever.
- Post-refresh disclosed sentinel lineage used GPT-OSS forged N=5 multipost with Gemma single-post.
- Live keep-only-fired filling beats blind static emission; replay is cold enough that one in-run timing sample should not be trusted as a precise replay estimate.
- replay-phase timeout now preserves the accumulated prefix score, while attack-generation timeout remains fatal.

## v12 policy: behavioral capability gates

The algorithm never branches on a target model name.

1. Probe exact ASUB-001 plain single POST once.
2. Probe exact ASUB-001 Harmony-compressed single POST twice.
3. Harmony specialization is unlocked only if both probes fire and their aggregate value density beats the plain anchor by at least 20%.
4. Only after that gate does the algorithm probe forged multipost-5 twice.
5. Multipost is promoted only if both probes produce at least 4 successful marker POSTs and aggregate density is not materially worse than Harmony single.
6. Fill candidates are live verified. Two consecutive failures demote multi5 -> Harmony single -> plain single.
7. Losing race probes are discarded and never occupy the replay prefix.
8. Returned ordering is based primarily on arm-level aggregate value density, reducing sensitivity to one anomalously fast warm-cache observation.

This is a small contextual bandit / successive-gating policy rather than a model-name router. It adapts to the behavior actually observed in the current evaluation run while regularizing that adaptation with the strongest hosted evidence available.

## Deliberately rejected last-minute ideas

- Gemma-specific control-token injection: too evaluator/chat-template dependent for an untested final-day change.
- natural-language multipost or multi-message continuation: weaker public evidence and higher context/setup cost.
- static 2,000-candidate backfill: directly contradicted by ASUB-013.
- mixing the private-guardrail hedge into the public anchor: would destroy the intended final two-submission portfolio; private robustness remains a separate slot.
- more aggressive deadline packing: public evidence says the final few percent mostly add timeout risk, not a new throughput mechanism.

## Mechanical invariants

- one user message per `AttackCandidate`;
- candidate message <= 2,000 characters;
- max multipost width = 5, under the competition hop ceiling used by the executed path;
- hard returned-candidate cap = 2,000;
- live keep-only-if-fired validation;
- unique destination space;
- Internet off in Kaggle kernel;
- budget taken from `AttackRunConfig.time_budget_s`, not a hardcoded competition duration;
- static plain ASUB-001-style fallback only for environment/plumbing failure.

## Freeze rule

No new public-score tuning should be inserted into this candidate after mechanical validation. The only remaining gates are compile/structural validation, official `aicomp validate redteam`, Kaggle kernel completion, and final submission selection.