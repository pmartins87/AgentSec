# DRAFT-ASUB-007 — forged multi-post + live validation

Status: **DRAFT / CI gate required / no Kaggle slot authorized yet.**

This draft replaces the weak parts of DRAFT-ASUB-005 while keeping multi-post as
an empirical question rather than assuming it is better or worse than single
post.

## Arms

The generation-phase race compares, per target model:

1. plain single post;
2. Harmony-framed single post;
3. forged Harmony plan for 2 posts;
4. forged Harmony plan for 3 posts;
5. forged Harmony plan for 4 posts.

Arms requiring more tool calls than `AttackRunConfig.max_tool_hops` are removed.
The default race is two round-robin probes per active arm. The winner maximizes
**observed public raw points per elapsed second** using actual
`eval_predicates()` EXFILTRATION count.

## Fill

After the race:

- emit only the winning shape;
- run every candidate against the live generation env;
- retain only candidates with >=1 observed EXFILTRATION;
- charge cumulative replay cost using measured full-hop latency × 0.95;
- stop inside a 0.985 replay-safe fraction with warm-up headroom reserved;
- return verified candidates sorted by observed raw-points/second.

Positive calibration probes are retained too, because they are already verified
replay findings and their measured cost is charged.

## Why this exists

Public field evidence is mixed:

- prose-only multi-post has poor compliance;
- Harmony-forged plans have produced near-complete N=4 execution in public probes;
- some hosted N=4 variants beat a weaker single-post anchor;
- other controlled two-post variants underperformed a stronger ~89-point anchor.

Therefore `k>1` is not a frozen strategic assumption. The model itself must prove
that the arm wins on value/time before the draft uses it.

## Promotion gates

1. All structural tests PASS.
2. `aicomp validate` PASS against pinned SDK 3.1.2.
3. ASUB-001 Version 4 runs terminal before another hosted slot is spent.
4. Prefer DRAFT-ASUB-006 if the goal is a low-variance public anchor.
5. Use DRAFT-ASUB-007 only when an extra hosted slot is justified as a throughput
   calibration or if subsequent public evidence strengthens multi-post.
6. Never infer private robustness from a public multipost score.
