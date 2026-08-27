# AEXP-20260827-001 — Hierarchical private prefix

## Question

Can replay ordering improve robustness to an unexpectedly short private replay without changing the underlying private-hypothesis portfolio?

## Baseline

`ASUB-20260826-009-private-hedge-v4-coverage-prefix`

The baseline emits one candidate from every active family before any family repeats. With the current declaration order, some lanes repeat before all six active lanes have appeared.

## Candidate

`DRAFT-ASUB-017-private-hedge-v5-hierarchical-prefix`

The candidate changes the prelude only:

1. group active families by lane;
2. emit one family from every active lane before any lane repeats;
3. emit the second family from lanes that have one;
4. resume weighted-deficit interleaving over the exact remaining counts.

Generation, family weights, candidate templates, bounded calibration, 2,000-candidate cap, scorer checks, and neutral-tail constraints remain aligned with ASUB-009.

## Deterministic expectations

For the full 11-family portfolio:

- first 6 replay positions: **6/6 distinct lanes** under hierarchical ordering;
- ASUB-009 family-first ordering reaches only **4/6 lanes** after 6 positions;
- first 11 replay positions: all **11/11 families** exactly once;
- discrete lane-coverage AUC over the 11-position prelude: **51 vs 41** for family-first ordering, a **24.4% improvement in early lane coverage**;
- exact 2,000-candidate family counts must be unchanged.

The 24.4% figure is a coverage metric, not a projected leaderboard-score gain.

## Promotion gate

Promote to frozen ASUB-011 only if all of the following pass:

- Python compile;
- structural tests for uniqueness, exact counts and lane-first prefix;
- official `aicomp validate redteam`;
- no regression to neutral-tail authorization constraints;
- current ASUB-009 hosted evidence does not reveal a reason to prefer its original family-first order.

## Interpretation

This is an uncertainty-robustness ablation. The hidden private guardrail is never queried or inferred from the ordering itself. If ASUB-009 later scores strongly, DRAFT-ASUB-017 remains useful as a controlled ordering variant; if ASUB-009 underperforms, the result should guide whether to change weights/mechanisms rather than assuming ordering alone is the cause.
