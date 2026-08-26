# One-hop fill, replay-cost calibration, and public-score noise

Date: 2026-08-26

## Source

Public Kaggle Working Note / writeup:

- Xander (`canqiang`), **The Scored Attack Surface Collapses to a Single Predicate**
- URL: `https://www.kaggle.com/writeups/canqiang/the-scored-attack-surface-collapses-to-a-single-pr`
- revisions through 2026-08-04 were visible when reviewed.

This is public field evidence. It is not private-guardrail evidence and does not
replace source-level SDK proofs.

## Two findings that materially affect AgentSec R6

### 1. Public score is noisy enough that a peak is not a mechanism estimate

The writeup reports a 21-submission same-mechanism forged-Harmony lineage:

- minimum: **85.945**
- maximum: **91.030**
- mean: **88.69**
- range: **5.09**
- reported CV: about **1.2%**

The author explicitly describes 91.030 as the maximum draw, not a distinct
algorithmic gain.

Earlier same-configuration groups in the same note were much noisier, including a
three-draw group spanning 42.14–61.94. These groups are not controlled estimates
of one common variance distribution, but they establish that byte-identical or
same-mechanism hosted reruns can move materially.

### AgentSec consequence

The accidental ASUB-001 duplicate is scientifically valuable. Once its second
score arrives, treat the two-run spread as a direct local noise observation. Do
not infer a small algorithmic improvement from a single public score unless the
delta is large relative to observed rerun spread or supported by repeated runs.

The public 91-ish frontier should therefore be interpreted as a noisy upper tail.
A better comparison target for mechanism quality is the same-mechanism mean/band
when available.

### 2. One-hop generation can remove scoring-irrelevant wrap-up cost, but replay
cost must be calibrated separately

The writeup reports that the scored EXFIL event occurs on the first tool action and
that one-hop probing fired stably in local tests on both target-model classes. The
claimed benefit is generation throughput: `max_tool_hops=1` avoids an additional
model wrap-up turn that contributes no EXFIL score.

However, scored replay still runs with the evaluator's full hop allowance. A
one-hop generation latency therefore underestimates replay cost.

The same public lineage reports an important negative result:

- a local eight-hop/one-hop ratio near ~2.0 was used as a replay-cost multiplier;
- that build regressed from a public anchor around **85.500** to **53.550**;
- the author concluded hosted transfer suggested a ratio nearer ~1.25, with no
  reliable spare margin for an aggressive fixed multiplier.

This is exactly the kind of local→hosted timing mismatch AgentSec should avoid.

## Design decision

Do **not** hard-code a new AgentSec `REPLAY_COST_COEF=2.0` or any other local-only
one-hop multiplier.

If we promote a one-hop fill experiment, use **paired live calibration inside the
hosted generation environment**:

1. warm the model;
2. run several one-hop candidates and several full-hop candidates with the same
   chosen prompt family and equivalent unique targets;
3. require positive EXFIL evidence in both groups;
4. estimate a per-model full-hop / one-hop latency ratio from live observations;
5. charge every one-hop retained candidate using a conservative upper estimate of
   its expected full-hop replay cost;
6. keep a strict fallback to full-hop fill when the paired estimate is missing or
   unstable;
7. retain a primary/backfill archive split so any optimistic tail is replayed last.

This would be a **DRAFT-ASUB-011** research rung, not a direct mutation of frozen
ASUB-004 or DRAFT-ASUB-010.

## Why not implement blindly today

We already have two public-throughput candidates under active validation:

- frozen ASUB-004: controlled v2 successor;
- DRAFT-ASUB-010: independent-budget primary/backfill v3.

The byte-identical ASUB-001 duplicate is also still pending. That result gives us
the cleanest available hosted variance measurement. DRAFT-ASUB-011 should be built
only with explicit paired-calibration gates and should not consume a hosted slot
before the current public and variance evidence is interpreted.

## Working Note value

This adds a useful negative-result and methodology point:

> Throughput optimization is not just “make generation faster.” When generation
> and replay have different hop counts, latency must be modeled in the phase that
> actually consumes the scoring budget. Local timing ratios can transfer badly;
> live paired calibration plus truncation-aware ordering is a more defensible
> benchmark methodology.
