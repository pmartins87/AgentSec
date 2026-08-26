# AEXP-20260826-012 — Timeout-prefix public frontier

Candidate: `ASUB-20260826-007-public-frontier-v6-timeout-prefix`

## Question

Does the updated prefix-preserving replay-timeout contract make a full 2,000-candidate, value-ordered archive outperform replay-cap-sized public frontier submissions?

## Mechanism

- generation remains bounded and must finish normally;
- fast row uses plain single-post EXFIL;
- slow row races plain/Harmony/forged 2..5-post arms using live full-hop score-per-second evidence;
- non-plain winner requires two positive observations plus a 5% value/time margin over plain when plain evidence exists;
- returned archive is always the full legal 2,000 candidates from the confirmed arm;
- replay timeout is allowed to truncate the tail because current evaluator semantics preserve the scored prefix.

## Precommitted interpretation

Use hosted public score as development telemetry, not private evidence.

- `<70`: reject as public anchor until diagnosed. Likely causes: arm extrapolation drift, formatting/tool parsing, poor slow/fast classification, or an incorrect assumption about timeout-prefix behavior.
- `70–80`: no clear public improvement over the 77.850 baseline once hosted variance is considered; preserve result for methodology but prefer simpler anchors unless another run reproduces gain.
- `80–85`: promising public improvement; compare against ASUB-005 and duplicate variance before promotion.
- `>=85`: strong public-anchor candidate and evidence that timeout-prefix oversubscription is useful.
- `>=90`: public frontier-class result; stop spending most effort on tiny public throughput gains and emphasize complementary private selection.

A single score does not estimate the hidden private guardrail.

## Failure diagnosis order

1. submission/format/runtime terminal class;
2. fast vs slow row classification;
3. selected arm and whether non-plain confirmation fired;
4. replay truncation behavior;
5. model-specific formatting drift, especially Gemma vs Harmony;
6. only then tune thresholds.

## Evidence to preserve

- notebook version and exact source blob;
- submission description;
- terminal status and public score;
- visible runtime/age;
- ASUB-001 duplicate status at the same time;
- ASUB-005 score if available;
- any Kaggle evaluator warning.
