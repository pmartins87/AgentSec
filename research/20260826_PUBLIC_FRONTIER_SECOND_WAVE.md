# Public frontier second wave — hosted 77.850 vs public 91.305 evidence

Date: 2026-08-26

## Trigger

AgentSec ASUB-001 produced the first valid hosted public score:

- public leaderboard score: **77.850**
- fixed ASUB-001 economics: 18 raw points per successful new-cell EXFIL finding
- equivalent mean successful findings per public model row: **865.0**
- equivalent total across the two public rows: **1,730.0**

This closes R3 (hosted evaluation works) and gives a real throughput baseline.

## New independent public reference

A second public MIT-licensed competition repository was inspected:

- `SKYGOD07/AI-Agent-Security---Multi-Step-Tool-Attacks`
- pinned commit: `204d6d2eeb2752607b04100987216e7440c011ef`
- repository license: MIT
- commit history records hosted public results:
  - v21: 80.870
  - **v22: 91.305 peak**
  - v23: 91.125
- v22 implementation: `our_work/versions/v52/omega_v22_attack.py`

The v22 score corresponds to **1,014.5 equivalent 18-raw findings per public row**, or about 149.5 more completed findings per row than AgentSec ASUB-001. The score gap is 13.455 public points, about 17.3% relative to ASUB-001.

This is field evidence, not a guarantee that the same architecture will reproduce under our run variance.

## Why the v22 architecture matters to AgentSec

The public source reinforces two facts we independently derived from the published evaluator gateway:

1. **generation and replay have independent time windows**;
2. **replay truncation preserves points already completed**.

That makes some ASUB-004/DRAFT-006 safety accounting unnecessarily conservative. In particular, DRAFT-006 subtracts warm-up generation wall time from its replay allowance, even though the published gateway resets the replay deadline after generation. The warm-up is useful for model initialization, but its wall time does not consume the later replay budget.

The public v22 architecture also uses a two-stage fill:

- conservative primary archive;
- near-full-budget backfill;
- replay ordering designed so the speculative/backfill tail is exposed first to truncation.

This is a materially different risk shape from simply lowering a replay-cost coefficient.

## AgentSec response: DRAFT-ASUB-010

`submissions/DRAFT-ASUB-010-public-frontier-v3-backfill/attack.py`

Independent implementation choices:

- one synthetic `http.post` EXFIL action per candidate;
- unique domains;
- live keep-only-if-fired validation;
- unreturned `hops=1` warm-up for model initialization;
- warm-up wall time **not subtracted from replay allowance**;
- one post-warm-up plain sample to classify fast/slow behavior;
- plain-vs-Harmony A/B only on slow rows, reducing calibration tax on fast rows;
- `REPLAY_COST_COEF=1.0` rather than optimistic `0.95`;
- primary replay cap `0.945` and wall cap `0.985`;
- backfill replay cap `0.995` and wall cap `0.997`;
- primary candidates sorted by latency first;
- backfill candidates sorted separately and appended after the primary archive.

The separate ordering is deliberate: if replay ends early, backfill findings are the first economic material at risk. The conservative primary segment is kept ahead of them even when an individual backfill candidate happened to validate faster.

## Relationship to ASUB-004

ASUB-004 remains frozen and reproducible. Do not rewrite it in place.

Its current role:

- direct successor precommitted for the 70–85 ASUB-001 score band;
- lower conceptual distance from our first hosted run;
- useful controlled ablation against ASUB-001.

DRAFT-ASUB-010 is the next public-throughput research rung. It should not replace ASUB-004 automatically before:

1. structural tests pass;
2. SDK validation passes;
3. CI is green;
4. the byte-identical ASUB-001 duplicate finishes, so we have a direct hosted variance estimate;
5. we decide whether the next scarce Kaggle slot is better spent on a controlled public ablation or on private-transfer evidence.

## Working-note value

This creates a clean ablation story:

- ASUB-001: conservative canary, hosted 77.850;
- ASUB-004: compact terminal + fixed A/B + `0.95` replay coefficient;
- DRAFT-ASUB-010: independent-budget accounting + two-stage backfill + strict `1.0` replay coefficient.

The comparison separates three effects that are otherwise easy to confound:

1. prompt/terminal compliance;
2. replay-cost estimation;
3. archive fill policy near the evaluator deadline.

## Evidence discipline

- 77.850 is our hosted measurement.
- 91.305 is a public third-party hosted measurement at a pinned public commit.
- hidden/private transfer remains unknown.
- the 17.3% gap is an opportunity estimate, not an expected improvement claim.
