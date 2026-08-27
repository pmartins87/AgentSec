# AEXP-20260826-006 — Hosted queue: ASUB-009 + ASUB-010

Observed from Kaggle Submissions UI on 2026-08-26 (local user time around 23:00 -03:00):

- `notebooka6483cd827` Version 5 — `ASUB-20260826-009 private hedge v4 coverage prefix` — **Notebook Running**.
- `notebooka6483cd827` Version 6 — `ASUB-20260826-010 public frontier v7 format diverse` — **Notebook Running**.
- ASUB-001 Version 4 terminal controls remain **86.040** and **77.850** public.
- Final-selection UI remains `0/2`; no final candidates selected yet.

Interpretation:

- ASUB-009 is the current private-aware coverage-prefix experiment.
- ASUB-010 is the current high-information public-format experiment.
- They are independent enough to run concurrently; neither result is required for the other to execute.
- Next hosted candidate, if daily quota remains available, is ASUB-007 as the simpler full-cap public timeout-prefix anchor. This provides a clean complexity-vs-throughput comparison against ASUB-010 and a direct comparison against the 86.040 ASUB-001 anchor.

Decision rule after terminal results:

- ASUB-010 >= 86.040 by a margin materially larger than observed run-to-run noise: promote as public anchor candidate.
- ASUB-010 near 86.040: treat as inconclusive unless ASUB-007 helps isolate complexity cost.
- ASUB-010 materially below the ASUB-001 duplicate band: prefer simpler public anchor and diagnose format/probe overhead.
- ASUB-009 public score is telemetry only; a lower public score does not automatically reject it because its purpose is private-guardrail robustness.

Do not select final `0/2` slots yet.
