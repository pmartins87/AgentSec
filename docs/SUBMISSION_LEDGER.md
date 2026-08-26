# Submission ledger — AgentSec

Record every Kaggle submission here. Never reuse a vague description such as “latest”.

| ID | UTC timestamp | Git/source identity | Notebook/version | Local score | Public score | Private/final | Runtime | Notes |
|---|---|---|---|---:|---:|---:|---:|---|
| ASUB-20260825-001-A | 2026-08-25 (exact time pending) | frozen ASUB-001 blob `b17180572b27d80f584d640d4ebf3ecace28df4d` | `notebooka6483cd827`, pre-v4 wiring | — | — | hidden | — | **Kaggle Error / system error.** Initial notebook wiring was subsequently corrected; Kaggle also had contemporaneous system-error reports. Do not interpret as strategy failure. |
| ASUB-20260825-001-B | 2026-08-26 (exact time pending) | same frozen ASUB-001 source; wrapper Version 4 | `notebooka6483cd827` Version 4 | — | pending | hidden | running | Clean commit; internet-off eligibility had been addressed; output contained both `attack.py` and `submission.csv`. Submitted once intentionally. |
| ASUB-20260825-001-C | 2026-08-26 (exact time pending) | byte-identical Version 4 duplicate | `notebooka6483cd827` Version 4 | — | pending | hidden | running | Accidental duplicate submission. Preserve as a free evaluator-variance replicate; do not submit a third copy while these are running. |

## Current interpretation

- Competition entry/join state is confirmed by successful access to the submission flow; R0 eligibility gate is therefore closed.
- The first failed attempt was classified by Kaggle as a system error, not a scorer result.
- The two Version 4 reruns are byte-identical and can reveal evaluator/runtime variance if their outcomes differ.
- Until they finish, preserve the remaining daily submission slots.

## Required notes per submission

- exact code/config source
- major strategy family
- expected improvement vs prior submission
- any evaluator/runtime anomaly
- post-result interpretation
- whether the submission remains a final candidate

When a pending run terminates, replace `pending/running` and the approximate timestamp with the exact Kaggle values if visible.
