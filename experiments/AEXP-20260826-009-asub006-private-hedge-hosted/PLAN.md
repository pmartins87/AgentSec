# AEXP-20260826-009 — ASUB-006 hosted private-aware hedge test

## Candidate

`submissions/ASUB-20260826-006-private-hedge-v2/attack.py`

Git blob SHA: `47c40678fbc4de7da1a2569ace64c8fd036e5ef5`

## Question

Can a mixed portfolio that preserves structurally distinct Confused Deputy and semantic authorization-context families remain mechanically stable enough to deserve one of the two final-counting submission slots, even if its visible public score is below the pure EXFIL frontier?

## Important interpretation constraint

The visible public leaderboard cannot directly reveal private-guardrail survival. Therefore a lower public score is not automatically a failure for this experiment.

The hosted run is valuable for:

- verifying model compliance under real GPT-OSS/Gemma generation;
- detecting runtime or archive-packaging failures that local structural tests cannot expose;
- measuring the public-score cost of keeping private-transfer diversity;
- establishing a final-candidate artifact early enough to revise before deadline.

## Result classes

### Mechanical failure

Error/blank/invalid output: fix packaging or runtime issue under a new frozen identity before interpreting strategy.

### Very low public score

Investigate whether probe budget, two-turn cost, or public-denied semantic families suppress too much of the public anchor. Consider increasing EXFIL weight only if private-family coverage remains meaningful.

### Moderate public score

Potentially desirable: confirms that the hedge preserves nontrivial public value while maintaining private-transfer diversity.

### Surprisingly high public score

Promote immediately to a strong final-candidate branch and inspect which families actually survived public generation.

## What must be recorded

- Kaggle notebook version;
- exact submission description;
- terminal status;
- public score;
- visible runtime/age;
- any evaluator error text;
- whether the candidate remains one of the two preferred final selections.

## Prize decision

Do not compare ASUB-006 with ASUB-005 solely by public score. The intended final pair is complementary: one throughput anchor plus one private-aware hedge unless later evidence rejects that structure.
