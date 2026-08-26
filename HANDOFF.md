# HANDOFF — AgentSec

Use this file as the first read in a dedicated AgentSec chat.

## Mission

Compete seriously for a prize in Kaggle's **AI Agent Security – Multi-Step Tool Attacks**. Entry was completed before the 2026-08-25 deadline. Final deadline: 2026-09-01 23:59 UTC. Optional Working Note: 2026-09-08 23:59 UTC.

## Source of truth

This repository is authoritative for project state, decisions, code, experiments, submissions, and frozen artifacts.

## Required first reads

1. `STATUS.md`
2. `ROADMAP.md`
3. `docs/COMPETITION.md`
4. `docs/OFFICIAL_ARTIFACTS.md`
5. `docs/EXPERIMENT_PROTOCOL.md`
6. `docs/SUBMISSION_LEDGER.md`
7. `research/20260825_PUBLIC_ATTACK_SURFACE.md`
8. `research/20260825_SEMANTIC_AUTHORIZATION_GAP.md`

Then inspect the current repository tree and latest commits before changing anything.

## Working rules

- Never optimize from memory when an official competition artifact can be checked.
- Separate verified competition facts from hypotheses.
- Record every leaderboard submission and exact code/config that produced it.
- Require replayability before promoting a discovered finding.
- Maintain hold-out/stress tests against public-leaderboard overfitting.
- Keep all security experimentation strictly within the competition's authorized offline benchmark.
- Advance as far as possible without unnecessary user micromanagement; surface only meaningful blockers, decisions, or results.

## Current project state

**R0 PASS / R3 hosted evaluation in flight / R7 private-transfer research active.**

Hosted state:

- user completed Trusted Access and competition entry;
- frozen `ASUB-20260825-001-frontier-canary` source blob remains `b17180572b27d80f584d640d4ebf3ecace28df4d`;
- Kaggle notebook `notebooka6483cd827` Version 4 is a clean successful commit that produced both `attack.py` and `submission.csv`;
- first earlier submission ended in `Kaggle Error`;
- Version 4 was subsequently submitted twice; both identical copies were `Notebook Running` at last observation;
- do not submit another copy while those runs are active.

Three lanes exist:

1. **ASUB-001** — public `SECRET_MARKER` EXFIL throughput canary.
2. **ASUB-002** — direct benign `CONFUSED_DEPUTY` synonym canary.
3. **ASUB-003** — semantic-intent transfer portfolio for hidden private guardrail hypotheses.

ASUB-003 is the major new result. The official scorer uses literal authorization words, while a realistic hidden guardrail may reason semantically. The submission calibrates public *attempted* shapes and emits a 360-candidate portfolio across web/inbox→email/http/shell/write plus a direct-email hedge. It deliberately avoids marker-only dependence and Harmony forging.

Two private stress proxies now intentionally disagree:

- provenance-strict: `src/private_guardrail_proxy.py`;
- semantic-authorization: `src/semantic_authorization_proxy.py`.

This is deliberate portfolio engineering, not a claim that either proxy matches hidden code.

## Immediate handoff queue

1. Wait for the two identical ASUB-001 Version 4 Kaggle runs to finish; record both outcomes and variance.
2. Run/inspect GitHub CI for ASUB-003 and the expanded regression suite.
3. If the first valid ASUB-001 score arrives, spend the next hosted slot only after comparing the value of ASUB-002 vs ASUB-003.
4. Preserve remaining daily slots; repeated identical submissions are useful only as variance evidence, not as the default strategy.
5. Continue R7 toward a mixed final portfolio covering public throughput, direct CD, semantic U2A transfer, and stricter private stress assumptions.
6. Maintain Working Note evidence as results land.

See `STATUS.md` for live details and `docs/SUBMISSION_LEDGER.md` for hosted history.
