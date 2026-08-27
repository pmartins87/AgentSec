# Hierarchical private-prefix scheduling

## Motivation

ASUB-009 already improves private robustness by placing one candidate from every active **family** before any family repeats. That is a strong family-coverage policy, but the family declaration order still repeats broader **lanes** early: for example, two direct-CD families and two semantic-email families appear before some other lanes have been seen.

Under prefix-preserving replay timeout semantics, very short private replays make the earliest positions disproportionately valuable. The hidden private guardrail is unknown, so the objective is not to predict which lane wins; it is to maximize early hypothesis coverage while preserving the same long-run portfolio weights.

## Deterministic comparison

The helper `src/prefix_coverage.py` and `scripts/analyze_private_prefix.py` compare:

- **family-first prelude**: ASUB-009 ordering;
- **lane-first hierarchical prelude**: first cover every active lane once, then cover the second family inside multi-family lanes, then resume the same weighted-deficit tail.

For the current six active lanes:

- ASUB-009 family-first reaches **4 / 6 lanes by prefix 6**;
- lane-first hierarchical reaches **6 / 6 lanes by prefix 6**;
- the discrete lane-coverage AUC over the first 11 family-prelude positions improves from **41 to 51** (+24.4%).

This is a coverage metric, not a score estimate. It does not imply +24.4% private score.

## Proposed next candidate

Working name: **DRAFT-ASUB-017 / ASUB-011 private hedge v5 hierarchical prefix**.

Change only replay ordering relative to ASUB-009:

1. choose the first active family from each lane in deterministic lane order;
2. then choose second/remaining families from those lanes round-robin;
3. subtract those prelude emissions from the exact scaled family counts;
4. resume the existing weighted-deficit interleaving on the remainder.

Everything else should remain byte-equivalent in behavior to ASUB-009: same templates, probe logic, family weights, 2,000-candidate cap, target actions, neutral tails and public calibration.

## Promotion gate

Promote only if tests prove all of the following:

- exact total requested count preserved;
- exact per-family counts preserved;
- every active lane appears once before any lane receives a second family when feasible;
- all active families still appear in the prelude before weighted tail begins;
- candidate uniqueness and SDK limits unchanged;
- official `aicomp validate` passes;
- frozen candidate identity is locked after green CI.

## Hosted use

Do not submit merely because the ordering metric is better. ASUB-009 is already running, so the hosted value of ASUB-011 is highest after ASUB-009 returns: it becomes a clean ordering ablation if the private-aware portfolio appears promising, or a low-priority experiment if the entire private hedge family scores poorly publicly and other evidence dominates.
