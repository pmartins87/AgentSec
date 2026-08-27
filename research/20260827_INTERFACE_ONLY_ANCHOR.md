# Interface-only public anchor

## Motivation

Kaggle staff warned that approaches depending on implementation-specific evaluator behavior may not carry over to the final-ranking evaluation. The current public frontier includes format-sensitive candidates that intentionally test target-model parser/framing behavior. Those experiments are useful, but they should not be the project's only high-throughput public option.

## DRAFT-ASUB-018

`submissions/DRAFT-ASUB-018-public-frontier-v8-interface-only-full-prefix/attack.py`

Design:

- ordinary user-language prompt only;
- documented `http.post` request;
- synthetic competition marker only;
- one message per finding;
- unique URL argument per finding for score-cell diversity;
- full legal **2,000-candidate** archive;
- no Harmony/control tokens;
- no forged assistant/tool transcript;
- no parser-specific formatting;
- no model-identification assumption;
- no hidden/private guardrail access.

## Why full-prefix now

The evaluator update preserves score accumulated before a replay timeout. For a fixed positive-value single-post mechanism, returning all 2,000 legal candidates weakly dominates guessing a smaller replay cutoff: any replay truncation removes only the tail while preserving earlier successes.

Attack-generation timeout remains terminal, so DRAFT-ASUB-018 intentionally performs no live model search during `AttackAlgorithm.run()`. It simply constructs the replay archive. This makes generation mechanically cheap and isolates the public question to replay compliance/throughput.

## Hosted value

If promoted after CI, this is a useful control against ASUB-007 and ASUB-010:

- ASUB-007: bounded live calibration; may promote Harmony/forged multi-post on a slow row;
- ASUB-010: broader format-diverse live race;
- DRAFT-ASUB-018: documented-interface-only single-post full prefix.

If the interface-only control matches the more complex candidates within the empirical hosted noise band, the simpler candidate is strategically attractive for a final slot because it depends on fewer evaluator-specific assumptions. If complex candidates clearly beat it by more than the observed duplicate-run band, the extra mechanism has stronger evidence of real public value.

## Limits

This remains a public-guardrail throughput anchor. A strong public result does not prove private-guardrail survival. Final pair selection should still preserve a complementary private-aware hedge.
