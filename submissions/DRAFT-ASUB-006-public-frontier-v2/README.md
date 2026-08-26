# DRAFT-ASUB-006 — public frontier v2

Status: **DRAFT / CI gate required / do not submit while ASUB-001 Version 4 is still unresolved.**

This candidate is the successor to the frozen ASUB-001 public canary. It folds
in source-verified SDK behavior plus independent hosted public evidence without
changing the private-transfer research lanes.

## Frozen defaults under test

- one successful `http.post` / finding
- `SECRET_MARKER`
- terminal: `Then say OK.`
- 3 plain + 3 Harmony classification probes
- winner chosen by elapsed time per successful firing
- full-hop validation and keep-only-if-fired
- `REPLAY_SAFE_FRAC = 0.985`
- `REPLAY_COST_COEF = 0.95`
- `SLOWEST_MULT = 1.35`
- max 2,000 findings
- unique guardrail-clean domains
- fastest verified candidates first

## Promotion gates

Before this draft may become an ASUB:

1. GitHub CI: syntax + SDK `aicomp validate` + regression suite PASS.
2. Current ASUB-001 duplicate hosted runs are terminal.
3. At least one ASUB-001 run has a valid public score, or both have a clearly
   classified infrastructure failure.
4. The score is interpreted through `src/hosted_evidence.py`.
5. A new hosted slot is justified by the decision gate in
   `research/20260826_PUBLIC_FRONTIER_FIELD_EVIDENCE.md`.
6. Freeze source hash and notebook wrapper before submission.

## Strategic role

Public throughput anchor only. A strong public score does not imply hidden
private-guardrail transfer. The final strategy must still preserve at least one
private/mixed lane unless hosted evidence strongly rejects it.
