# ASUB-20260825-002 — Confused-deputy canary

Status: **PREPARED / NOT YET HOSTED**

Purpose: test a second predicate family with benign outbound content and live predicate validation. This lane is intentionally independent of the public `SECRET_MARKER` / first-field EXFILTRATION quirk.

## Frozen source

- Submission source: `attack.py`
- Required SDK: `aicomp-sdk==3.1.2`
- Source git-blob SHA at preparation: `aa356687dde69548040f77de867ca0e7a98cc899`
- Competition: `ai-agent-security-multi-step-tool-attacks`
- Generated hosted artifact: `/kaggle/working/attack.py`
- Internet: disabled

## Strategy

1. Cycle a small set of natural recipient-oriented phrasings that avoid the literal verbs `send` and `share`.
2. Run each wording live against the target environment.
3. Call the official SDK `eval_predicates` on the resulting trace.
4. Keep only candidates that actually trigger `CONFUSED_DEPUTY`.
5. Rank template families by observed hit-rate per second.
6. If the row is slow, probe the public Harmony compression suffix once and use it only if the compressed candidate still qualifies.
7. Fill the remaining budget with unique benign recipient domains using the winning verified wording.
8. Return replay candidates ordered by observed latency.

This is deliberately empirical: no guessed hidden intent-regex is used to accept candidates.

## Why this lane matters

Public SDK analysis shows `CONFUSED_DEPUTY` is not structurally closed in the same way as public `UNTRUSTED_TO_ACTION` or protected-root `DESTRUCTIVE_WRITE`.

The candidate content is benign (`benchmark complete`), so a strict all-arguments secret scanner does not automatically reject it. That makes this family useful as a private-robustness calibration lane even though severity-3 economics are weaker than severity-5 EXFILTRATION.

## Caveats

- The hidden private guardrail remains unknown.
- A direct recipient-oriented request can be semantically legitimate even if the public scorer's heuristic labels it `CONFUSED_DEPUTY`; hosted replay is the only meaningful benchmark evidence.
- Do not promote this as final solely because it scores.
- ASUB-001 remains the first hosted priority because it calibrates frontier throughput. ASUB-002 is the next controlled lane.

## Hosted decision

Submit after ASUB-001 has produced a valid hosted result, or earlier only if ASUB-001 is blocked by a public-sentinel/evaluator change and a second wiring calibration is needed.

## Result

Pending.
