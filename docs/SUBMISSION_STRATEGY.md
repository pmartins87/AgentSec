# Hosted Submission Strategy — Prize-First

Last updated: 2026-08-26

## Objective

Hosted Kaggle submissions are an experimental and competitive resource. The goal is **not** to minimize submission count; the goal is to maximize the probability of a prize-eligible final result.

The opposite failure modes are both costly:

- hoarding daily slots leaves expiring information-gathering capacity unused;
- submitting near-duplicates without a decision question consumes runtime without improving final selection.

The correct unit of value is **expected prize value**, combining expected private-leaderboard strength, information gained for later choices, mechanical reliability, and time remaining before the final deadline.

## Current observed quota

The Kaggle submission dialog was observed on 2026-08-26 showing `1/5 used`, i.e. **five hosted submissions available that day**. Treat the live Kaggle UI as authoritative because competition settings can change.

Daily capacity does not create a reason to wait merely to save a slot for a future day. When multiple mechanically valid, non-redundant hypotheses are ready, using more than one slot in a day is desirable.

## Submission roles

Every hosted run should have a declared role before launch.

### 1. Public frontier calibration

Question: does a throughput or replay-accounting change materially improve the public reachable lane?

Current rungs:

- ASUB-001 baseline;
- ASUB-004 controlled public successor;
- ASUB-005 paired one-hop/full-hop calibration;
- DRAFT-ASUB-010 primary/backfill accounting retained as a lower-complexity alternative.

### 2. Private-transfer hedge

Question: does a structurally different family have enough public model compliance and replay validity to justify one of the final private-leaderboard selections?

Current frozen candidate:

- ASUB-006 private-aware mixed hedge v2.

A lower public score is acceptable here if the candidate protects a plausible private-guardrail hypothesis that a pure public EXFIL strategy does not cover.

### 3. Variance / evaluator calibration

Question: how noisy is the hosted evaluator for byte-identical or behavior-identical code?

Use sparingly. One controlled replicate can be valuable; repeated duplicates after the variance scale is understood are usually dominated by new hypotheses.

### 4. Mechanical / infrastructure diagnosis

Use only when a submission is required to distinguish evaluator wiring from attack logic. Prefer CI and clean notebook commits for failures that can be resolved without a hosted scoring run.

## Prize-first launch gate

A candidate should be submitted when all of the following hold:

1. **mechanically ready** — compile, SDK validation, structural regressions and notebook packaging are green;
2. **non-redundant decision value** — the run tests a material change or a materially different private hypothesis;
3. **actionable outcome** — either a high or low result changes what we will freeze, tune, or select next;
4. **deadline value** — waiting is not expected to produce stronger evidence before the daily capacity would otherwise expire.

There is no rule to wait for another submission to finish when an independent candidate already satisfies these gates.

## Daily operating policy

With several days remaining and five slots observed in the live UI, the default posture is:

- use **at least two distinct hosted experiments in a day** when two prize-relevant, mechanically ready hypotheses exist;
- use additional slots when the result has clear decision value and queue/runtime permits;
- avoid filling the quota merely because it exists;
- do not sacrifice a private-aware experiment solely to chase a small public-LB increase.

This is a decision heuristic, not a rigid quota.

## Final-selection logic

The competition uses the private leaderboard for final standings, and the current competition UI allows selection of up to two final-counting submissions. Final choices should therefore be complementary rather than merely the two highest noisy public scores.

Preferred final structure unless hosted evidence strongly argues otherwise:

- one **high-throughput public anchor** with the strongest plausible transfer to the private guardrail;
- one **private-aware mixed/hedge candidate** covering mechanisms the public anchor does not.

The public leaderboard is development telemetry, not the objective function.

## Current intended sequence

All three current candidates are mechanically useful; order is driven by information diversity and expected prize value:

1. **ASUB-005** — submit first as the strongest current public-upside experiment;
2. **ASUB-006** — submit independently as the private-aware hedge; do not wait for ASUB-005 or the ASUB-001 duplicate to finish;
3. **ASUB-004** — use another hosted slot when a controlled lower-complexity public ablation is worth more than waiting for a newer hypothesis;
4. record the pending ASUB-001 byte-identical replicate whenever it terminates and use the spread as evaluator-variance evidence;
5. use remaining daily capacity for evidence-driven follow-ups, not automatic repetition.

## Operational UI runbook

The exact Kaggle notebook/upload workflow and frozen filenames are maintained in:

`docs/KAGGLE_SUBMISSION_RUNBOOK.md`

## Rule of thumb

**A submission slot is worth spending when its expected information or expected final-score gain is greater than the value of waiting.**

The project optimizes for prize probability, not submission frugality.
