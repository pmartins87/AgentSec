# Hosted variance and final-candidate selection

## Direct evidence

ASUB-001 Version 4 was submitted twice with byte-identical attack code and returned two different public scores:

- **77.850**
- **86.040**

Observed range: **8.190 leaderboard points**.

Under ASUB-001's fixed 18-raw-points-per-success lane, those scores correspond to 865 vs 956 equivalent successful findings per public model row on average, a difference of 91 findings per row.

This is direct hosted evidence that a single public score is noisy enough that small score differences between different strategies should not be over-interpreted.

## Decision rule

AgentSec now uses the observed duplicate range as an **empirical practical noise band**, not as a formal confidence interval.

For a one-off candidate compared with the current 86.040 public anchor:

- improvement greater than 8.190: strong single-run evidence of a real public-frontier gain;
- regression greater than 8.190: strong single-run evidence of a real public-frontier loss;
- absolute difference at or below 8.190: unresolved by one run; use mechanism evidence, complementary-role value, or a replicate before treating the score difference as decisive.

Implementation: `src/hosted_decision.py` and `scripts/compare_hosted_candidates.py`.

## Why this matters for the current hosted wave

The current wave contains:

- ASUB-009 private hedge;
- ASUB-010 format-diverse public frontier, accidentally replicated twice;
- ASUB-007 simpler timeout-prefix public frontier.

The accidental ASUB-010 duplicate is therefore useful rather than wasted: it gives a second strategy-specific variance estimate. Once both ASUB-010 runs finish, compare their internal spread with the 8.190 ASUB-001 range before attributing a modest ASUB-007/ASUB-010 difference to strategy quality.

## Final-pair implication

The two final Kaggle selections should not be chosen by sorting noisy public scores alone. Public score is one signal. Private-mechanism complementarity, robustness under explicit hidden-defense stress scenarios, and observed hosted variance should all enter the decision.

This supports the existing robust pair selector in `src/final_pair_selector.py`: one slot can preserve the strongest public anchor while the second covers a materially different private hypothesis, even if its single public score is lower.

## Limits

Two duplicate scores are insufficient for a statistical variance estimate. The 8.190 range is therefore a conservative operational yardstick only. It must not be presented as a confidence interval, standard error, or stable property of the Kaggle evaluator.
