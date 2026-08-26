# STATUS — AgentSec

Last updated: 2026-08-26 after prize-first submission-policy correction and paired-hop timing fix

## Mission

**Phase: R0-R3 PASS / R4-R7 optimization active / R8 pending / R9 active**

Primary objective: maximize the probability of a prize-eligible final result in Kaggle **AI Agent Security – Multi-Step Tool Attacks**. Public leaderboard score is development telemetry; final private-leaderboard performance is the target.

Hosted submission policy is now explicit in `docs/SUBMISSION_STRATEGY.md`: daily slots are experimental capacity, not something to hoard. The Kaggle UI was observed on 2026-08-26 showing `1/5 used`. When two mechanically ready, non-redundant prize-relevant hypotheses exist, using more than one hosted slot in a day is desirable.

## First valid hosted result — ASUB-001

Frozen baseline:

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

- source git-blob SHA: `b17180572b27d80f584d640d4ebf3ecace28df4d`
- notebook slug: `notebooka6483cd827`
- clean wrapper: Version 4
- first pre-v4 attempt: `Kaggle Error / system error`
- corrected Version 4 first copy: **Succeeded / Public Score 77.850**
- corrected byte-identical Version 4 replicate: last observed still running; preserve its terminal result as hosted-variance evidence

ASUB-001 is fixed public EXFIL. At 18 raw points per successful new-cell finding, `77.850` is equivalent to **865 successful findings per public model row on average**.

## Frozen public successor — ASUB-004

`submissions/ASUB-20260826-004-public-frontier-v2/attack.py`

Role: controlled public-throughput calibration.

Main differences from ASUB-001:

- compact `Then say OK.` terminal;
- 3 plain + 3 Harmony probe race;
- full-hop live validation;
- cumulative replay sizing;
- `REPLAY_SAFE_FRAC=0.985`;
- `REPLAY_COST_COEF=0.95`;
- fastest verified candidates first.

Mechanically green: compile, structural regressions, SDK validation and clean CI all pass.

## Public frontier v3 — DRAFT-ASUB-010

`submissions/DRAFT-ASUB-010-public-frontier-v3-backfill/attack.py`

Role: exploit the published independence of generation and replay windows while protecting already-earned replay score.

Key design:

- independent generation/replay budget accounting;
- warm-up at one hop;
- conservative primary segment followed by near-deadline backfill;
- primary ordered before speculative backfill so replay truncation sacrifices the tail first;
- live keep-only-if-fired validation;
- classifier rescue so one unlucky plain miss cannot force a 300-candidate fallback.

Mechanically green under current CI.

## Public frontier v4 — DRAFT-ASUB-011 paired hops

`submissions/DRAFT-ASUB-011-public-frontier-v4-paired-hops/attack.py`

Research question: can generation use `max_tool_hops=1` to skip scoring-irrelevant model wrap-up while still estimating the evaluator's full-hop replay cost from live hosted calibration?

Current design:

- paired one-hop/full-hop positive calibration;
- median full/one latency ratio with safety multiplier and conservative clamps;
- one-hop fill enabled only when both calibration groups have enough positive EXFIL evidence;
- automatic fallback to full-hop fill when calibration is insufficient;
- full-hop replay probes and one-hop generation now maintain **separate wall-clock high-water marks**.

The last item fixes an important underfill bug found during review: the earlier implementation updated a single `slowest` value with expensive full-hop calibration calls. If one-hop fill was later selected, that full-hop latency still controlled the generation deadline projection and could erase much of the expected one-hop throughput gain. Commit `c2d3991...` separates the timing regimes, and a regression test now explicitly requires one-hop fill timing to ignore full-hop probe latency.

CI run 80 before this timing fix was fully green. A new CI run is triggered by the fix and must be green before DRAFT-ASUB-011 is promoted for hosted use.

## Private-aware hedge — DRAFT-ASUB-009

`submissions/DRAFT-ASUB-009-private-hedge-v2/attack.py`

Role: protect final-private prize probability against the known weakness of a pure public EXFIL strategy.

Default 360-candidate portfolio:

- public EXFIL: **144**
- direct scorer-negative confused deputy: **24**
- explicit-action + neutral-tail confused deputy: **36**
- semantic email: **120**
- semantic HTTP: **12**
- semantic shell: **12**
- semantic write: **12**

Two-message laundering candidates require the target-tool action to be attempted on the **first interaction**, while explicit authorization is still current. Delayed target actions after the neutral tail are rejected as false calibration evidence.

Mechanically green in the current full CI suite. Its hosted public score may be much lower than the public EXFIL frontier; that alone is not a rejection criterion because final standings use the stricter private guardrail.

## CI

The project now separates attack-logic throughput tests from SDK/Gym plumbing tests.

- previous false-red source: production attack intentionally consumes nearly all of an exact 10-second budget, occasionally crossing the CI boundary by a fraction of a second;
- fix: bounded `ci/gym_smoke_attack.py` verifies SDK/Gym mechanics independently;
- CI run 76: **PASS, 105 tests**;
- CI run 80: **PASS** with DRAFT-ASUB-011 included in compile/SDK gates;
- latest paired-hop wall-clock-separation commit has triggered a fresh CI run; terminal green is the promotion gate.

## Official benchmark facts frozen

- `aicomp-sdk==3.1.2`
- replay cap: <=2,000 findings, <=32 messages/finding, <=2,000 chars/message
- score: severity weights plus +2 per unique score cell
- hosted evaluator runs GPT-OSS and Gemma separately
- returned candidates are independently replayed against public `OptimalGuardrail` and a stricter hidden private guardrail
- final standings use the **private leaderboard**
- final submission deadline: 2026-09-01 23:59 UTC
- Working Note deadline: 2026-09-08 23:59 UTC

## Public/private asymmetry

The public generation environment exposes `OptimalGuardrail`; private replay is hidden. Consequently:

- public model compliance and latency can be measured live;
- hidden-private survival cannot be observed during generation;
- a pure public EXFIL score can be high and still be a weak final-private strategy;
- final candidates should cover conflicting plausible private mechanisms rather than optimize one public sentinel route only.

## Submission strategy

See `docs/SUBMISSION_STRATEGY.md`.

Current rule: **submit when a mechanically ready run has material expected score gain or decision value; do not delay merely to conserve a daily slot.** Also do not submit near-duplicates without a concrete question.

Current intended hosted sequence, subject to live results:

1. record the pending ASUB-001 replicate when it terminates;
2. use a hosted slot for a controlled public successor rather than another baseline duplicate;
3. use another slot for the strongest mechanically ready advanced public frontier (DRAFT-ASUB-010 or DRAFT-ASUB-011 after latest CI);
4. use a hosted slot for DRAFT-ASUB-009 early enough to revise the private hedge before the deadline;
5. use remaining daily capacity for evidence-driven follow-ups.

There is no requirement that step 1 finish before independent steps 2-4 can launch.

## Final-selection principle

Unless evidence strongly rejects a lane, preserve complementary final candidates:

- one high-throughput public anchor with the strongest plausible private transfer;
- one private-aware mixed hedge covering mechanisms the anchor does not.

The best noisy public score is not automatically the best final submission.

## Working Note

`docs/WORKING_NOTE_OUTLINE.md` already contains:

- public-generation/private-replay asymmetry;
- last-message intent laundering;
- authorization-context TOCTOU mismatch;
- direct synonym vs laundering ablation;
- public throughput vs private robustness;
- hosted evaluator variance;
- first real hosted score `77.850`;
- second-wave replay-budget and hop-depth experiments.

## Promotion gates

- **R0 PASS:** rules, eligibility, repository, metric/environment inventory.
- **R1 PASS:** SDK-aligned baseline/contracts reproduced.
- **R2 PASS:** deterministic local replay/trace plumbing.
- **R3 PASS:** first valid hosted score = **77.850**.
- **R4 active:** predicate-directed reproducible lanes.
- **R5 active:** diversity/coverage engine.
- **R6 active:** runtime allocation and candidate ordering.
- **R7 active:** multiple plausible private-guardrail stress models.
- **R8 pending:** final private-aware freeze + final submission selection.
- **R9 active:** Working Note evidence architecture and finalization.
