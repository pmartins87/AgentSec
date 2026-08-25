# AEXP-20260825-003 — Public frontier canary

Status: **PREPARED / NOT HOSTED**

## Hypothesis

A replay-first single-post validation-fill portfolio should move AgentSec from starter-scale public performance into the current public-frontier regime while providing model-specific throughput measurements that can guide later budget tuning.

## Submission under test

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

Source blob SHA at preparation: `b17180572b27d80f584d640d4ebf3ecace28df4d`

## Independent variables

Initial canary configuration is deliberately conservative:

- `PRIMARY_REPLAY_FRAC = 0.945`
- `PRIMARY_WALL_FRAC = 0.980`
- `BACKFILL_REPLAY_FRAC = 0.990`
- `BACKFILL_WALL_FRAC = 0.994`
- `NEXT_COST_MULT = 1.12`
- one full-hop latency classifier
- threshold `12.0 s`
- one post per candidate
- `SECRET_MARKER` payload
- unique short `.co` domains
- hard cap `2000`

The actual hosted attack budget is not fixed here; the algorithm consumes `AttackRunConfig.time_budget_s` from the evaluator.

## Metrics to capture

For each target model / leaderboard row where available:

- attack-generation runtime
- returned candidate count
- successful replay count, if exposed
- unique cell count, if exposed
- public score
- private score
- timeout/truncation behavior
- Kaggle total runtime
- kernel slug/version
- submission reference
- exact AgentSec git SHA
- evaluator update epoch / submission timestamp

Derived metrics:

- public score per returned candidate
- estimated public replay completion ratio
- score per model-second
- public/private ratio
- candidate-count asymmetry between GPT-OSS and Gemma, if observable

## Expected interpretation

A public score near the contemporary public single-post frontier would validate the mechanics and hosted wiring, not the final prize strategy.

A substantially lower score should be decomposed into:

1. candidate fire-rate failure;
2. model latency/template misclassification;
3. conservative under-fill;
4. replay truncation;
5. evaluator/parser changes;
6. gateway/format errors.

Private score is the most important signal for the prize track. If it is much lower than public, the project should avoid further sentinel-only tuning and prioritize the private-robust archive.

## Promotion criterion

- Hosted run completes with a valid scored submission.
- Results are entered in `docs/SUBMISSION_LEDGER.md`.
- No undocumented source/config drift.
- Any parameter tightening is a new experiment/submission, not an in-place edit of this frozen canary.

## Result

Pending.
