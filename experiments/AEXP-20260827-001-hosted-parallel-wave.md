# AEXP-20260827-001 — Hosted parallel wave

## Purpose

Use remaining hosted-evaluation capacity for distinct, prize-relevant questions while preserving exact notebook/version identities.

## Observed Kaggle state at 2026-08-27 ~00:02 America/Sao_Paulo

Terminal baseline evidence:

- ASUB-001 Version 4 replicate A: Public Score **77.850**.
- ASUB-001 Version 4 replicate B: Public Score **86.040**.
- pre-v4 wiring attempt: Kaggle Error.

Currently running rows visible in the Kaggle UI:

1. **Version 8** — description `ASUB-20260826-007 public frontier v6 timeout prefix` — intended/correct ASUB-007 after attaching the missing input dataset.
2. **Version 6** — description `ASUB-20260826-007 public frontier v6 timeout prefix` — this row is operationally mislabeled; Version 6 source is the prior ASUB-010 notebook and therefore acts as an accidental byte-identical ASUB-010 replicate.
3. **Version 6** — description `ASUB-20260826-010 public frontier v7 format diverse` — intended ASUB-010.
4. **Version 5** — description `ASUB-20260826-009 private hedge v4 coverage prefix` — intended ASUB-009.

## Questions answered by this wave

- **ASUB-009:** does a private-aware mixed portfolio retain enough public telemetry to remain a plausible complementary final candidate?
- **ASUB-010 x2:** how much hosted variance does the format-diverse public frontier show, and does the format race improve the public anchor beyond the 86.040 baseline?
- **ASUB-007:** does the simpler timeout-prefix public frontier outperform the more complex format-diverse strategy?

## Interpretation discipline

- Do not infer private-leaderboard survival from public score alone.
- The two Version-6 rows should be interpreted as an accidental ASUB-010 replicate pair, despite one having an ASUB-007 description.
- Only Version 8 should be treated as the actual ASUB-007 hosted run.
- Public differences of only a few points should be interpreted against the already observed 8.190-point spread between byte-identical ASUB-001 runs.

## Next decision

Wait for terminal outcomes from this wave before choosing the next hosted experiment. Development continues in parallel on hierarchical private-prefix ordering (candidate ASUB-011) and final-pair selection. This is not slot-hoarding: three distinct strategy questions plus one useful replicate are already in flight.
