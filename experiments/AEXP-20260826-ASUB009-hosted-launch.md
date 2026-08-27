# AEXP-20260826 — ASUB-009 hosted launch

## Purpose

Capture the first hosted launch of the private-aware coverage-prefix hedge so the Kaggle result can be reconciled against the exact frozen source and the ASUB-001 public anchor.

## Hosted launch

Observed from the Kaggle Submissions page on 2026-08-26:

- notebook: `notebooka6483cd827`
- notebook version: `Version 5`
- submission description: `ASUB-20260826-009 private hedge v4 coverage prefix`
- hosted state at observation: `Notebook Running`
- visible age at observation: about `36s`
- final-selection checkbox: not selected

## Frozen source

- candidate: `ASUB-20260826-009-private-hedge-v4-coverage-prefix`
- repository path: `submissions/ASUB-20260826-009-private-hedge-v4-coverage-prefix/attack.py`
- frozen Git blob: `86444fa16cb817fa210ade4319ec52e8ad5ece6c`
- role: private-aware mixed hedge with coverage-first replay prefix

## Baseline context

Byte-identical ASUB-001 Version 4 hosted results already observed:

- `77.850`
- `86.040`

The spread is direct evidence of material hosted variance. ASUB-009 should therefore be interpreted primarily for its strategic/private-robustness role; a public score below the ASUB-001 best does not by itself reject the candidate.

## Decision rule when terminal

Record exact terminal status and public score. Then:

- if error: inspect exact hosted error before changing attack logic;
- if valid score: compare against the 77.850/86.040 public-anchor distribution, while preserving the fact that private survival is unobserved;
- regardless of the ASUB-009 public score, proceed with the independent ASUB-010 format-diverse public experiment unless new evidence makes it redundant.

## Next hosted experiment

`ASUB-20260826-010-public-frontier-v7-format-diverse` is the next planned independent launch.
