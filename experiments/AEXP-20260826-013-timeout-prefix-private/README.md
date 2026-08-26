# AEXP-20260826-013 — Timeout-prefix private hedge

Candidate: `ASUB-20260826-008-private-hedge-v3-timeout-prefix`

## Question

Given prefix-preserving replay timeouts, is a full-capacity, interleaved private-hypothesis archive a better final hedge than the 360-candidate ASUB-006 design?

## Mechanism

ASUB-008 preserves ASUB-006's hypothesis weights but scales them to 2,000 candidates and interleaves family order. Bounded public generation calibration can remove a family only when the target model fails both tested formulations; unprobed families remain uncertainty hedges.

The design intentionally covers mutually incompatible private-defense hypotheses rather than maximizing the public sentinel EXFIL lane.

## Precommitted interpretation

The visible public score is **not** the main acceptance metric for this candidate because the final target is the hidden private replay.

Hosted use is still informative:

- format/runtime error: fix mechanics and refreeze; do not infer strategy failure;
- extremely low public score with normal completion: inspect whether model-compliance calibration dropped too many families or whether two-message costs truncate the public prefix too early;
- moderate public score: acceptable if mechanical behavior is stable; preserve as a final-pair candidate because it covers private mechanisms absent from public-only anchors;
- public score unexpectedly close to the public frontier: especially valuable, because the hedge may carry less public opportunity cost than expected.

Do not reject ASUB-008 solely because ASUB-005/007 scores higher publicly.

## Final-pair decision

Before final submission selection, compare candidate pairs under explicit stress scenarios with `scripts/plan_final_pair.py`. Prefer complementary coverage unless evidence strongly collapses private uncertainty to one mechanism.

## Evidence to preserve

- exact source blob and notebook version;
- terminal status and public score;
- visible runtime/age;
- whether all expected output files existed;
- contemporary scores for ASUB-005/006/007;
- any evidence of replay truncation or parser behavior.
