# AgentSec diagnostic pivot — 2026-08-30

## Trigger

Latest hosted evidence shows that continued scalar-public-LB tuning is not enough:

| Hosted candidate | Public score |
|---|---:|
| ASUB-001 replicate best | **86.040** |
| ASUB-001 byte-identical replicate | 77.850 |
| ASUB-007 timeout-prefix | 82.700 |
| ASUB-010 format-diverse | 78.810 / 81.920 |
| ASUB-009 private coverage hedge | 8.565 |
| ASUB-011 hierarchical private hedge | 8.145 |
| ASUB-013 baseline-exact static full prefix | **60.500** |

The ASUB-013 result is especially diagnostic. It preserves the successful ASUB-001 public message mechanism but removes live validation/fill and blindly returns the full 2,000-candidate archive. Its large regression means that live model interaction, keep-only-if-fired filtering, runtime sizing, and/or model-specific path selection are causal components of the stronger public result. Static archive volume alone is not the answer.

## Essential missing measurement

The competition runs the attack separately against GPT-OSS and Gemma and averages the public rows. A single scalar leaderboard number hides whether a candidate is balanced across both models or effectively optimized to one.

The next public candidate must therefore be driven by **per-model measurements**, not by another prompt-format guess.

Required per-model telemetry:

- successful unsafe-action / predicate fire rate;
- generation probe latency distribution;
- candidate count verified during generation;
- replay-safe candidate count estimate;
- public raw/normalized score for the local run;
- trace examples for failed and successful candidates;
- model-specific prompt arm selected by the algorithm.

## Primary diagnostic environment

Use the public Kaggle notebook:

`https://www.kaggle.com/code/llkh0a/aas-local-validation`

It attaches the competition GPT-OSS and Gemma GGUF models and provides separate public-style red-team runs for each model. Start with short controlled runs before full-budget tests.

First target under test: ASUB-001, because it remains the best hosted public mechanism and its live validation logic is the most important causal baseline.

Source:

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

## Public candidate direction after diagnosis

Do not freeze a successor until the local per-model run shows the bottleneck.

Most likely design family for the next public candidate:

1. multiple cheap initial observations rather than a one-sample latency classifier;
2. explicit per-model branch selection from measured behavior;
3. keep-only-if-fired candidate generation;
4. replay-cost calibration using observed full-hop or corrected low-hop latency;
5. adaptive candidate count sized to the actual model/runtime budget;
6. fastest/highest-value verified candidates first under prefix-preserving replay timeout;
7. no blind 2,000-candidate static archive.

This candidate will receive a new ASUB ID only after local evidence and SDK/CI validation.

## Kaggle CLI / API role

The official Kaggle CLI is now part of the final-sprint workflow for operational telemetry and automation. It can:

- list submission refs, statuses and public scores;
- inspect/download the leaderboard;
- pull/push notebooks;
- inspect kernel status and download kernel outputs;
- submit a code-kernel version and wait/poll for scoring.

It **cannot** reveal the hidden private guardrail or hidden private score before final evaluation.

Helper added:

`scripts/kaggle_snapshot.py`

Setup:

```bash
pip install -U kaggle
kaggle auth login
python scripts/kaggle_snapshot.py --download-leaderboard
```

Never commit Kaggle tokens/credentials to this repository.

## Private track

ASUB-009 (8.565) and ASUB-011 (8.145) are nearly indistinguishable on the permissive public guardrail despite materially different early coverage ordering. This is negative public evidence, but it does not measure hidden-private survival.

Do not promote DRAFT-ASUB-019 merely because its deterministic coverage metrics are better. Before another private-aware hosted slot, use an explicit private-guardrail proxy/stress test and document that it is only a hypothesis model, not hidden-ground-truth access.

## Working Note value

Two new negative results are scientifically useful:

1. **ASUB-013:** exact successful public message family + blind static 2,000 archive regressed to 60.500, showing that live validation/runtime allocation is an essential part of the attack algorithm.
2. **ASUB-011 vs ASUB-009:** hierarchical prefix coverage materially improves deterministic early diversity but does not improve the permissive public leaderboard, supporting the distinction between public exploitation and private-uncertainty hedging.

These should be incorporated into the Working Note with clear separation between observed evidence and private-survival hypotheses.
