# DRAFT-ASUB-022 — public frontier v11 online arm race

Status: **FINAL CANDIDATE / NOT YET HOSTED**

## Evidence that motivated the change

The 2026-09-01 per-model diagnostic falsified the assumption that Gemma needed a different basic exfiltration prompt:

- GPT-OSS: 56/56 plain single-post probes fired; median generation probe latency ~2.054 s. The diagnostic replay timed out after returning 56 candidates.
- Gemma: 80/80 plain single-post probes fired; median generation probe latency ~0.924 s. Eight replay-capped candidates produced 8/8 findings and 144 raw points.
- Gemma replay of only eight findings still consumed ~85.1 s, proving that local generation latency is not a safe proxy for replay latency.

The remaining public ceiling is therefore treated primarily as a throughput/replay-economics problem, not a basic prompt-compliance problem.

## v11 change relative to DRAFT-ASUB-021 / v10

v10 only raced Harmony single vs multipost-4 after a first probe exceeded a fixed 12 s latency threshold. v11 removes that classification gate and always performs a tiny live race on the current target row among:

1. exact ASUB-001 plain single post;
2. exact ASUB-001 Harmony-compressed single post;
3. one-message multipost-4;
4. one-message multipost-5.

Only observed successful marker POSTs are valued. Multipost is ineligible unless it creates at least two successful POSTs. The winning arm is chosen by observed public raw-score proxy per generation-second, then every exploitation candidate is live verified. Returned candidates are sorted by observed density so partial replay timeout preserves the highest-value prefix.

This means the submission does not hard-code a model name or assume that Harmony/multipost will work. If an evaluator/model update breaks those primitives, they lose the live race and the plain single-post anchor remains available.

## Mechanical invariants

- one `user_message` per `AttackCandidate`;
- maximum candidate message length <= 2,000 chars;
- max multipost width = 5 (within the 8-hop competition limit);
- hard candidate cap = 2,000;
- Internet off;
- live keep-only-if-fired verification preserved;
- attack-generation deadline remains conservative and adaptive;
- static fallback remains the ASUB-001 plain primitive.

## Promotion rule

Push this candidate once, verify the Kaggle kernel completes and creates `/kaggle/working/attack.py`, then submit it as the final public-frontier attempt. Do not replace ASUB-001 as the historical anchor until the hosted score is known.
