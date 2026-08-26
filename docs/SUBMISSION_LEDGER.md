# Submission ledger — AgentSec

Record every Kaggle submission here. Never reuse a vague description such as “latest”.

| ID | UTC timestamp | Git/source identity | Notebook/version | Local score | Public score | Private/final | Runtime | Notes |
|---|---|---|---|---:|---:|---:|---:|---|
| ASUB-20260825-001-A | 2026-08-25 (exact time pending) | frozen ASUB-001 blob `b17180572b27d80f584d640d4ebf3ecace28df4d` | `notebooka6483cd827`, pre-v4 wiring | — | — | hidden | — | **Kaggle Error / system error.** Initial notebook wiring was subsequently corrected; Kaggle also had contemporaneous system-error reports. Do not interpret as strategy failure. |
| ASUB-20260825-001-B | 2026-08-26 (exact time pending) | same frozen ASUB-001 source; wrapper Version 4 | `notebooka6483cd827` Version 4 | — | pending | hidden | running/pending | Clean commit; output contained both `attack.py` and `submission.csv`. Submitted once intentionally. |
| ASUB-20260825-001-C | 2026-08-26 (exact time pending) | byte-identical Version 4 duplicate | `notebooka6483cd827` Version 4 | — | pending | hidden | running/pending | Accidental duplicate. Preserve as an evaluator-variance replicate; do not submit a third copy while these remain unresolved. |

## Current interpretation

- Competition entry/join state is confirmed by successful access to the submission flow; R0 eligibility gate is closed.
- The first failed attempt was a platform/system terminal class, not a numeric scorer result.
- The two corrected Version 4 runs are byte-identical and can reveal evaluator/runtime variance if their outcomes differ.
- Until at least one becomes terminal, preserve remaining hosted submission slots.
- Use `docs/HOSTED_FAILURE_TRIAGE.md` before interpreting any error or blank score as attack evidence.

## Prepared but **not submitted**

These artifacts do not consume Kaggle submission slots merely by existing in the repository.

| Candidate | Role | Current status | Hosted-slot rule |
|---|---|---|---|
| ASUB-002 | direct Confused Deputy diagnostic/private hedge | frozen source, SDK-valid | wait for ASUB-001 terminal evidence |
| ASUB-003 | semantic-intent private-transfer portfolio | frozen source, SDK-valid | reserve for private-transfer experiment if justified |
| DRAFT-ASUB-004 | robust mixed final-oriented portfolio | unfrozen | retune only from explicit stress/evidence updates |
| DRAFT-ASUB-005 | prose multi-post diagnostic | unfrozen, mechanically valid, strategically demoted | do not spend slot unless new evidence reverses negative field results |
| DRAFT-ASUB-006 | evidence-backed public frontier v2 | unfrozen, **CI + SDK validation PASS** | preferred next public calibration if ASUB-001 is weak/moderate |
| DRAFT-ASUB-007 | forged multi-post live value/time race | unfrozen, **CI + SDK validation PASS** | optional throughput diagnostic; single-post remains lower-variance anchor |

## Next-result protocol

When ASUB-001-B or C becomes terminal:

1. preserve exact terminal label, score, ref and runtime/screenshot;
2. classify with `docs/HOSTED_FAILURE_TRIAGE.md`;
3. for a numeric score run:
   `python scripts/interpret_hosted_score.py asub001 <PUBLIC_SCORE>`;
4. after both numeric duplicate scores are known:
   `python scripts/interpret_hosted_score.py duplicate <SCORE_B> <SCORE_C>`;
5. only then choose the next hosted candidate.

Operational score gate for ASUB-001:

- `<70`: DRAFT-ASUB-006 is the clear public calibration upgrade;
- `70–85`: DRAFT-ASUB-006 remains high priority, while preserving a later private/mixed slot;
- `>=85`: prioritize private-transfer/mixed evidence over another public-only refinement;
- error/blank: diagnose mechanics/infrastructure first.

These thresholds are decision heuristics, not statistical confidence bounds.

## Required notes per submission

- exact code/config source
- major strategy family
- expected improvement vs prior submission
- evaluator/runtime anomaly class
- post-result interpretation
- whether the submission remains a final candidate

When a pending run terminates, replace `pending/running` and approximate timestamps with exact Kaggle values if visible.
