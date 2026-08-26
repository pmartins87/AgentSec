# AEXP-20260826-008 — ASUB-005 hosted public-frontier test

## Candidate

`submissions/ASUB-20260826-005-public-frontier-v4-paired-hops/attack.py`

Git blob SHA: `7b1e000062ebb35a11fe4257fe1d370b07f0d7f0`

## Baseline

ASUB-001 valid hosted public score: `77.850`.

Equivalent ASUB-001 public economics: 865 successful 18-raw findings per public row on average.

## Question

Does live one-hop/full-hop paired calibration recover enough generation throughput while conservatively estimating full-hop replay cost to materially outperform the 77.850 baseline?

## Primary success gates

- `>=85`: strong public anchor candidate; prioritize private-aware evidence after recording variance;
- `80–85`: useful improvement; compare against ASUB-004 and evaluator variance;
- `77.850–80`: weak positive result; paired-hop complexity may not justify itself unless replicate variance is large;
- `<77.850`: regression/underfill signal; inspect hop-ratio fallback, replay scale, and fill wall projections;
- error/blank: classify infrastructure vs source mechanics before strategy conclusions.

These are operational decision thresholds, not statistical confidence intervals.

## What must be recorded

- Kaggle notebook version;
- exact submission description;
- terminal status;
- public score;
- visible runtime/age;
- ASUB-001 duplicate state at time of result;
- whether paired-hop remains the preferred public anchor.

## Next decision

A high ASUB-005 score does not remove the need for ASUB-006. Public throughput and private-guardrail robustness are separate prize risks.
