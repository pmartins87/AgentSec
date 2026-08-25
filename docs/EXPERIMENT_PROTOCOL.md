# Experiment protocol — AgentSec

## Purpose

Prevent leaderboard chasing, irreproducible findings, and accidental loss of strong candidates.

## Every experiment must record

- experiment ID and timestamp
- git commit SHA
- SDK/evaluator version or hash
- target model(s)
- scenario/fixture set
- search configuration and budget
- random seeds, if any
- candidate count
- replay success rate
- predicate counts by severity
- unique cell/signature count
- raw/normalized local score when available
- runtime and failure modes
- comparison against current champion

## Experiment IDs

Use `AEXP-YYYYMMDD-NNN-short-name`.

Example: `AEXP-20260826-003-novelty-archive`.

## Promotion rule

A change may replace the champion only when:

1. it is reproducible from a clean run;
2. replay success is verified;
3. gain survives repeated runs or deterministic replication;
4. it does not materially collapse predicate or diversity coverage;
5. it is within hosted runtime/memory constraints;
6. evidence is preserved under `experiments/`.

## Hold-out discipline

Maintain scenarios/configurations not used to tune search parameters. Use them before final freeze to estimate generalization beyond public-evaluator quirks.

## Failure logging

Negative results are first-class artifacts. Record failed hypotheses briefly so later chats do not repeat expensive dead ends.
