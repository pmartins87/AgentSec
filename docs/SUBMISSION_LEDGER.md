# Submission ledger — AgentSec

Record every Kaggle submission here. Never reuse a vague description such as “latest”.

| ID | UTC timestamp | Git/source identity | Notebook/version | Local score | Public score | Private/final | Runtime | Notes |
|---|---|---|---|---:|---:|---:|---:|---|
| ASUB-20260825-001-A | 2026-08-25 (exact time pending) | frozen ASUB-001 blob `b17180572b27d80f584d640d4ebf3ecace28df4d` | `notebooka6483cd827`, pre-v4 wiring | — | — | hidden | — | **Kaggle Error / system error.** Initial notebook wiring was subsequently corrected; Kaggle also had contemporaneous system-error reports. Do not interpret as strategy failure. |
| ASUB-20260825-001-B | 2026-08-26 (exact submission time pending) | same frozen ASUB-001 source; wrapper Version 4 | `notebooka6483cd827` Version 4 | — | **77.850** | hidden | terminal success; exact runtime pending | First valid hosted numeric result. Screenshot observed 2026-08-26 08:03 America/Rio_Branco; Kaggle UI showed `Succeeded · 13h ago`. Under the fixed 18-raw-points-per-success ASUB-001 lane, 77.850 corresponds exactly to **865 equivalent successful findings per public model row on average** (1,730 across the two public rows). |
| ASUB-20260825-001-C | 2026-08-26 (exact submission time pending) | byte-identical Version 4 duplicate | `notebooka6483cd827` Version 4 | — | pending | hidden | `Running` when observed | Accidental duplicate. Screenshot observed 2026-08-26 08:03 America/Rio_Branco; Kaggle UI showed `Running · 11h ago`. Preserve as an evaluator-variance replicate. |

## Current interpretation

- **R3 is now closed:** ASUB-001-B produced the first valid hosted public score, **77.850**.
- The first failed attempt was a platform/system terminal class, not a numeric scorer result.
- ASUB-001-B and C are byte-identical; if C also scores, their spread becomes direct evidence of hosted evaluator/runtime variance.
- `77.850` lies in the precommitted `70–85` decision band: **DRAFT-ASUB-006 remains the preferred next public calibration**, while at least one later slot should be preserved for private-transfer/mixed evidence.
- Do not submit another byte-identical ASUB-001 copy.
- Because ASUB-001-C is already consuming no additional decision effort and can finish soon, prefer waiting for its terminal result before changing replay margins or finalizing the exact next hosted variant.
- Use `docs/HOSTED_FAILURE_TRIAGE.md` before interpreting any future error or blank score as attack evidence.

## Prepared but **not submitted**

These artifacts do not consume Kaggle submission slots merely by existing in the repository.

| Candidate | Role | Current status | Hosted-slot rule |
|---|---|---|---|
| ASUB-002 | direct Confused Deputy diagnostic/private hedge | frozen source, SDK-valid | preserve as targeted predicate diagnostic; public economics weaker than EXFIL |
| ASUB-003 | semantic-intent private-transfer portfolio | frozen source, SDK-valid | reserve for private-transfer experiment if justified |
| DRAFT-ASUB-004 | robust mixed final-oriented portfolio | unfrozen | retained as earlier robust-mix rung |
| DRAFT-ASUB-005 | prose multi-post diagnostic | unfrozen, mechanically valid, strategically demoted | do not spend slot unless new evidence reverses negative field results |
| DRAFT-ASUB-006 | evidence-backed public frontier v2 | unfrozen, **CI + SDK validation PASS** | **preferred next public calibration after duplicate variance is known or waiting becomes strategically costly** |
| DRAFT-ASUB-007 | forged multi-post live value/time race | unfrozen, **CI + SDK validation PASS** | optional throughput diagnostic; single-post remains lower-variance anchor |
| DRAFT-ASUB-008 | intent-laundering mixed portfolio | unfrozen, CI/SDK-valid research rung | superseded for private-hedge purposes by DRAFT-ASUB-009 |
| DRAFT-ASUB-009 | private hedge v2 | unfrozen, **latest CI + SDK validation PASS** | preserve both direct-CD mechanisms; candidate for later private/mixed slot after first-turn calibration invariant is tightened |

## Hosted-score inversion for ASUB-001-B

The ASUB-001 canary gives a fixed public raw value of **18 points per successful replayed finding**: severity-5 EXFIL contributes 16 and a unique score cell contributes 2.

For a public leaderboard score of `77.850`:

- raw-equivalent score per public row: `77.850 × 200 = 15,570`;
- equivalent mean successful findings per public row: `15,570 / 18 = 865`;
- equivalent total successful findings across `gpt_oss_public + gemma_public`: `1,730`.

This inversion identifies the **mean** public-row success volume. It does not reveal the individual GPT-OSS vs Gemma split, the number of candidates returned per model, or private-guardrail survival.

## Next-result protocol

When ASUB-001-C becomes terminal:

1. preserve exact terminal label, score/error, visible age/runtime and screenshot;
2. if numeric, run the duplicate interpretation using `77.850` and the new score;
3. convert the score spread into equivalent mean successful-finding variance;
4. decide whether DRAFT-ASUB-006's replay safety margin should remain at the current setting or become more conservative;
5. then spend the next scarce hosted slot.

Operational score gate for ASUB-001 remains:

- `<70`: DRAFT-ASUB-006 is the clear public calibration upgrade;
- `70–85`: **current branch** — DRAFT-ASUB-006 remains high priority, while preserving a later private/mixed slot;
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

When the pending duplicate terminates, replace approximate timing with exact Kaggle values if visible.
