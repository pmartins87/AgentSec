# FINAL PUBLIC FREEZE — 2026-09-01

## Candidate

`DRAFT-ASUB-023-public-frontier-v12-gated-autotuner`

Attack commit frozen at:

`617dcbe5a623009171eeefbfa2c7042ed444f6e2`

Final attack.py SHA-256:

`6782882ea76a76a67c43380ef84031820ed58e8fa1441f43afc4da1bb158546a`

Final Kaggle package:

`agentsec_final_public_v12.zip`

Package SHA-256:

`68d26259399d0ef3f661a894a2f76f6a27626e8708f9835c5566aeac9fa29ba5`

Kernel slug:

`paulomartins87/agentsec-final-public-v12`

## Final review outcome

The previous v11 online arm race was not frozen unchanged. Two last-review issues were removed:

1. multipost was being explored on every row, allowing one noisy positive observation to promote a fragile strategy on a target where hosted/public evidence favors the single-post primitive;
2. successful probes from losing arms were still returned, wasting high-value replay-prefix positions.

V12 replaces that with a staged behavioral autotuner / contextual bandit:

- plain ASUB-001 single-post anchor first;
- two Harmony single-post confirmations;
- multipost-5 exploration only after a strong, repeated Harmony capability signal;
- two multipost confirmations, each requiring >=4 successful marker POSTs;
- live keep-only-if-fired fill;
- losing probes discarded from replay;
- every attempt, including failures, retained in arm history so fragile arms are penalized rather than benefiting from survivorship bias;
- two-failure circuit breaker: `multi5 -> harmony-single -> fast-single`;
- replay-prefix ordering by aggregate arm value density, then hit count/value;
- no model-name hardcoding.

## Validation gate

GitHub Actions run `33543920450` (`Validate DRAFT-ASUB-023`) completed SUCCESS on the frozen attack commit.

Passed steps:

- Python 3.11 setup;
- dependency install;
- `py_compile`;
- structural pytest suite;
- official `aicomp validate redteam`;
- cleanup/completion.

Local mechanical checks also passed before packaging, including both non-Harmony and Harmony/multipost simulated paths and a clean ZIP-content audit.

## Freeze rule

No more score-chasing strategy changes are authorized for the public candidate. From this point only deployment/submission handling may change. A code modification is justified only if the Kaggle kernel exposes a mechanical incompatibility that prevents execution; any such modification must be documented as a hotfix rather than a new strategy experiment.

The separate hidden/private-guardrail hedge remains a different final-submission portfolio slot and must not be mixed into this public-frontier anchor.