# Hierarchical calibration under short hosted budgets

Date: 2026-08-27

## Question

Does breadth-first calibration improve private-hedge robustness when the hosted generation budget ends before every family/template pair can be tested?

## Baseline

ASUB-011 / DRAFT-ASUB-017 already uses hierarchical **replay** ordering:

1. one family from each active lane appears before a lane repeats;
2. every family appears once before weighted-deficit replay resumes;
3. long-run family counts are unchanged.

Its live calibration still probes both template variants for one family before moving to the next family. Under a short generation window, this can spend early probes on repeated variants while entire hypothesis lanes remain unseen.

## DRAFT-ASUB-019 change

DRAFT-ASUB-019 keeps the ASUB-011 replay archive unchanged and changes only calibration scheduling.

Calibration order is now two passes over the hierarchical family order:

- pass 1: variant 0 for every family;
- pass 2: variant 1 for every family.

The hierarchical family order itself covers all six lanes in the first six probes and all eleven families in the first eleven probes. The second template variant starts only after every family has received one probe.

This is deliberately a narrow ablation. Default weights, candidate construction, neutral-tail policy, 2,000-finding cap, replay prefix and weighted tail remain unchanged.

## Expected benefit

If hosted generation is truncated early, the calibration evidence should span more distinct private hypotheses. The algorithm can still retain partially observed families rather than incorrectly dropping them after only one failed template.

If the full 22-probe schedule completes, the set of observations is equivalent in breadth to ASUB-011; only probe order changes. Any hosted difference should therefore be interpreted primarily as a budget/order effect rather than a portfolio-content effect.

## Structural gates

DRAFT-ASUB-019 must satisfy all of the following before promotion:

- 2,000 unique fallback candidates;
- fallback replay archive byte-for-message identical to DRAFT-ASUB-017;
- first six calibration probes cover all six lanes;
- first eleven calibration probes cover all eleven families with variant 0;
- second eleven probes cover all eleven families with variant 1;
- hierarchical replay count preservation remains exact;
- neutral tails remain authorization-token free;
- official `aicomp validate redteam` passes.

## Hosted promotion rule

Do not spend a hosted slot on DRAFT-ASUB-019 merely because it is mechanically green. Promote only if:

1. ASUB-009/011 evidence suggests private-hedge ordering matters; or
2. hosted logs/score behavior imply generation calibration is materially truncated; or
3. a slot remains where this ablation has more decision value than the interface-only public anchor.

The private guardrail remains hidden throughout. This experiment changes search ordering under uncertainty; it does not infer or probe hidden guardrail rules.
