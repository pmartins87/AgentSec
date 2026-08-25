# STATUS — AgentSec

Last updated: 2026-08-25

## Mission status

**Phase: R0 — repository and competition intake**

Goal: produce a prize-contending final submission for AI Agent Security – Multi-Step Tool Attacks, while also preserving an optional Working Note path.

## Confirmed competition constraints

- Entry deadline: 2026-08-25 23:59 UTC.
- Final submission deadline: 2026-09-01 23:59 UTC.
- Working Note deadline: 2026-09-08 23:59 UTC.
- Code competition; submission must produce `attack.py`.
- Internet disabled during evaluation.
- GPU notebook runtime limit: 15 hours.
- Attack is evaluated sequentially against GPT-OSS and Gemma with independent 18,000-second budgets.
- Findings are replayed and scored against public and private guardrails.

## Immediate next actions

1. Confirm competition rules have been accepted and account is eligible to submit.
2. Acquire the official starter notebook / SDK / data and preserve their versions.
3. Reproduce the starter smoke test locally or in Kaggle.
4. Map the full action/state/trace API and all four security predicates.
5. Establish a zero-ambiguity local evaluator and replay harness.
6. Produce the first valid baseline submission.
7. Start systematic search over severity × diversity × replayability.
8. Track all leaderboard results in `docs/SUBMISSION_LEDGER.md`.

## Promotion gates

- **R0 PASS:** repository, official artifacts, rules, metric, environment inventory captured.
- **R1 PASS:** official baseline reproduced end-to-end.
- **R2 PASS:** deterministic local replay/evaluation harness verified.
- **R3 PASS:** first valid Kaggle submission scored.
- **R4 PASS:** predicate-directed search finds reproducible nontrivial failures.
- **R5 PASS:** diversity/coverage engine beats baseline robustly.
- **R6 PASS:** runtime allocation and candidate prioritization optimized.
- **R7 PASS:** robustness tests against public/private-guardrail mismatch proxies.
- **R8 PASS:** final candidate frozen, independently reproduced, submitted.
- **R9 PASS:** Working Note finalized by 2026-09-08 if competitive/novel enough.

## Known strategic risk

Public leaderboard optimization alone can overfit the permissive public guardrail. Promotion decisions must therefore reward replay stability, predicate coverage, diverse tool-call signatures, and robustness to stricter filtering.
