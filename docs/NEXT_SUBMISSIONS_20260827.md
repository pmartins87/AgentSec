# Next hosted submissions — 2026-08-27

Prize-first decision sheet for the current hosted wave.

## Current wave already in Kaggle

| Kaggle version | Actual code | Role | State at last UI check |
|---|---|---|---|
| Version 5 | ASUB-009 | private hedge v4 coverage-prefix | Running |
| Version 6 | ASUB-010 | public frontier v7 format-diverse | Running |
| Version 6 duplicate | ASUB-010 | byte-identical hosted replicate; description was misleading | Running |
| Version 8 | ASUB-007 | public frontier v6 timeout-prefix | Running |

Do not infer code identity from the submission description alone. The failed Version 7 caused one submission with an ASUB-007-looking description to reuse the last successful Version 6, so it is actually ASUB-010.

Current terminal public anchor: ASUB-001 Version 4 replicate, **86.040**. Byte-identical ASUB-001 duplicate range: **8.190** points (77.850–86.040).

## Newly frozen candidates

### ASUB-011 — private hedge v5 hierarchical prefix

Source:
`submissions/ASUB-20260827-011-private-hedge-v5-hierarchical-prefix/attack.py`

Frozen byte-identical from green DRAFT-ASUB-017 blob:
`5ef4d9ba9f100176d14a3968359ca019d1d14992`

Kaggle upload filename:
`ASUB-20260827-011-private-hedge-v5-hierarchical-prefix_attack.py`

Suggested private dataset:
`agentsec-asub011`

Suggested submission description:
`ASUB-20260827-011 private hedge v5 hierarchical prefix`

Decision value: ordering-only successor to ASUB-009. It covers all six active hypothesis lanes in the first six replay positions while preserving the same long-run portfolio counts. Prefer it when ASUB-009 evidence suggests the private hedge remains worth a final/hosted slot and early-prefix robustness is valuable.

### ASUB-012 — public frontier v8 interface-only full prefix

Source:
`submissions/ASUB-20260827-012-public-frontier-v8-interface-only-full-prefix/attack.py`

Frozen byte-identical from green DRAFT-ASUB-018 blob:
`698a5f0eaa64b4203ca9d8e2b104e0802800bb39`

Kaggle upload filename:
`ASUB-20260827-012-public-frontier-v8-interface-only-full-prefix_attack.py`

Suggested private dataset:
`agentsec-asub012`

Suggested submission description:
`ASUB-20260827-012 public frontier v8 interface only full prefix`

Decision value: documented-interface-only public control. It emits 2,000 ordinary single-post candidates with unique URLs and performs no live model-format search. It is the lowest-assumption public comparator to ASUB-007 and ASUB-010.

## Green reserve experiment

### DRAFT-ASUB-019 — private hedge v6 hierarchical calibration

Source:
`submissions/DRAFT-ASUB-019-private-hedge-v6-hierarchical-calibration/attack.py`

Green draft blob:
`02fc8a021a72942abc885e0bade61f597affaeec`

Dedicated workflow `33038715155`: **SUCCESS** for compile, structural tests, and official SDK validation.

DRAFT-ASUB-019 keeps the ASUB-011 replay archive unchanged and changes calibration order only. It probes one variant from every family before any second variant, using lane-first family ordering. At a six-probe cutoff it covers all 6 lanes versus 2/6 for the ASUB-011-style family-local calibration schedule; at eleven probes it covers all 11 families versus 6/11.

Do **not** freeze/promote it automatically. Its hosted value appears only if private-aware evidence remains competitive and generation-time truncation/order sensitivity is plausible enough to justify another ablation.

## Result-driven next-slot rule

When the current wave lands, use the result rather than a fixed calendar order:

- **ASUB-010 or ASUB-007 clearly > 94.230:** public improvement exceeds the current 8.190 empirical duplicate range relative to the 86.040 anchor. Preserve that candidate as a new public leader and prioritize a private-complement slot next.
- **ASUB-007 and ASUB-010 both inside 77.850–94.230:** one-run differences are within the practical duplicate band. ASUB-012 gains high information value because it tests whether the complex formatting/calibration is needed at all.
- **ASUB-010 duplicates disagree materially:** use their own spread as the strategy-specific variance signal before attributing a modest difference versus ASUB-007 to code quality.
- **ASUB-009 has a surprisingly competitive public score:** keep the private-aware lane alive and ASUB-011 becomes a high-value clean replay-ordering ablation.
- **ASUB-009/ASUB-011 evidence plus logs indicate generation calibration is being cut short:** DRAFT-ASUB-019 becomes eligible for freeze because it materially improves early calibration breadth without changing the fallback replay archive.
- **ASUB-009 public score is low:** do not automatically reject the private lane. Public score is not private survival. Use the mechanism role and final-pair stress model; ASUB-011 or DRAFT-ASUB-019 should be submitted only if the ordering experiment still changes final selection.
- **Any run errors:** classify mechanics/infrastructure first. Do not interpret a system/format error as strategy performance.

## Final two selections

Do not select the final two checkboxes yet. The intended final structure remains a complementary pair unless hosted evidence strongly contradicts it:

1. strongest credible public anchor;
2. strongest credible private-aware hedge or complementary mechanism.

Use `src/final_pair_selector.py` and explicit stress scenarios once the current wave has terminal results.
