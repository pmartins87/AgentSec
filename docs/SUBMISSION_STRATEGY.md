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

Examples:

- ASUB-001 baseline;
- ASUB-004 controlled public successor;
- DRAFT-ASUB-010 primary/backfill accounting;
- DRAFT-ASUB-011 paired one-hop/full-hop calibration.

### 2. Private-transfer hedge

Question: does a structurally different family have enough public model compliance and replay validity to justify one of the final private-leaderboard selections?

Example:

- DRAFT-ASUB-009 mixed private-aware portfolio.

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

The competition uses the private leaderboard for final standings, and Kaggle competitions of this form allow selection of a limited number of final submissions. Final choices should therefore be complementary rather than merely the two highest noisy public scores.

Preferred final structure unless hosted evidence strongly argues otherwise:

- one **high-throughput public anchor** with the strongest plausible transfer to the private guardrail;
- one **private-aware mixed/hedge candidate** covering mechanisms the public anchor does not.

The public leaderboard is development telemetry, not the objective function.

## Current intended sequence

Subject to live results and CI:

1. record the pending ASUB-001 replicate when it terminates;
2. submit a controlled public successor rather than another ASUB-001 duplicate;
3. submit the strongest mechanically ready paired-hop/backfill frontier candidate when its latest CI is green;
4. allocate a hosted slot to the private-aware mixed hedge early enough that a failure still leaves time for revision;
5. use remaining daily capacity for evidence-driven follow-ups, not automatic repetition.

## Rule of thumb

**A submission slot is worth spending when its expected information or expected final-score gain is greater than the value of waiting.**

The project optimizes for prize probability, not submission frugality.
