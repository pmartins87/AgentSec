# HANDOFF — AgentSec

Use this file as the first read in a dedicated AgentSec chat.

## Mission

Compete seriously for a prize in Kaggle's **AI Agent Security – Multi-Step Tool Attacks**. Final deadline: 2026-09-01 23:59 UTC. Optional Working Note: 2026-09-08 23:59 UTC.

## Source of truth

This repository is authoritative for project state, decisions, code, experiments, submissions, and frozen artifacts.

## Required first reads

1. `STATUS.md`
2. `ROADMAP.md`
3. `docs/COMPETITION.md`
4. `docs/EXPERIMENT_PROTOCOL.md`
5. `docs/SUBMISSION_LEDGER.md`

Then inspect the current repository tree and latest commits before changing anything.

## Working rules

- Never optimize from memory when an official competition artifact can be checked.
- Separate verified competition facts from hypotheses.
- Record every leaderboard submission and the exact code/config that produced it.
- Require replayability before promoting a discovered finding.
- Maintain hold-out tests against public-leaderboard overfitting.
- Keep all security experimentation strictly within the competition's authorized offline benchmark.
- Advance as far as possible without unnecessary user micromanagement; surface only meaningful blockers, decisions, or results.

## Current starting phase

R0: competition intake and official artifact acquisition. See `STATUS.md` for the live next-action queue.
