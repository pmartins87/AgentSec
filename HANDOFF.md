# HANDOFF — AgentSec

Use this file as the first read in a dedicated AgentSec chat.

## Mission

Compete seriously for a prize in Kaggle's **AI Agent Security – Multi-Step Tool Attacks**. Entry deadline: 2026-08-25 23:59 UTC. Final deadline: 2026-09-01 23:59 UTC. Optional Working Note: 2026-09-08 23:59 UTC.

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

Then inspect the current repository tree and latest commits before changing anything.

## Working rules

- Never optimize from memory when an official competition artifact can be checked.
- Separate verified competition facts from hypotheses.
- Record every leaderboard submission and the exact code/config that produced it.
- Require replayability before promoting a discovered finding.
- Maintain hold-out tests against public-leaderboard overfitting.
- Keep all security experimentation strictly within the competition's authorized offline benchmark.
- Advance as far as possible without unnecessary user micromanagement; surface only meaningful blockers, decisions, or results.

## Current project state

**R0 active / R1 baseline prepared.**

Completed:

- official SDK frozen at `aicomp-sdk==3.1.2`, upstream commit `56dabd3a6d8fbe587acd4d0a1b22796b1acccfcd`;
- package/source hashes recorded in `docs/OFFICIAL_ARTIFACTS.md`;
- R1 baseline implemented at top-level `attack.py`;
- Windows smoke runner added at `scripts/run_r1_smoke.ps1`;
- public guardrail/scorer reachability checks added at `tests/test_public_surface.py`;
- public attack-surface research preserved in `research/20260825_PUBLIC_ATTACK_SURFACE.md`.

Source inspection indicates a strong public `EXFILTRATION` sentinel route, structural public closure of `UNTRUSTED_TO_ACTION` and protected-root `DESTRUCTIVE_WRITE`, and a still-testable `CONFUSED_DEPUTY` lane. Do not assume those public conclusions transfer to the private guardrail.

## Immediate handoff queue

1. Confirm Kaggle competition rules/entry are accepted before the 2026-08-25 23:59 UTC entry deadline.
2. Download/freeze the current authenticated competition data/starter assets and their SHA256 hashes.
3. Run `scripts/run_r1_smoke.ps1` and preserve evaluator artifacts.
4. Record `AEXP-20260825-001-r1-baseline` with the exact run results.
5. Package and make the first valid hosted Kaggle baseline submission.
6. After the first score, branch into public throughput optimization and private-robustness stress testing.

See `STATUS.md` for the live detailed queue and promotion gates.
