# Replay-timeout prefix strategy

Date: 2026-08-26

## Trigger

Kaggle staff announced an evaluator change that preserves score accumulated before a **public or private replay timeout**. Attack-generation (`attack.py`) timeout remains terminal. Public discussion:

- https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/733058

A separate public discussion records the host clarification that attack generation, public replay and private replay are separately budgeted phases (participants commonly quote 9,000 s/phase from that clarification even though the Overview currently displays 18,000 s/model). The attack code must use the live `AttackRunConfig.time_budget_s` rather than hard-code either documentation number:

- https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/709285

## Consequence

Before partial-score preservation, oversizing the returned archive risked turning a good run into zero at replay timeout. That justified conservative replay-budget estimation.

After the evaluator update, a replay timeout is a **prefix truncation** rather than a total-score failure. For a returned archive whose candidates have non-negative score contribution, adding more candidates to the tail cannot reduce already accumulated score. Therefore:

1. keep attack-generation safely inside its own deadline;
2. calibrate only enough to identify a high-value replay mechanism;
3. return the largest legal archive (`<= 2,000` findings);
4. order candidates by expected score/replay-second or interleave private-hedge families so any prefix remains useful;
5. let replay timeout truncate the tail if necessary.

This argument does **not** imply that malformed candidates or submission-format failures are harmless. The strategy applies only to valid replayable candidates under the documented interface.

## Public implementation ladder

### DRAFT-ASUB-012 — independent-window measured fill

`submissions/DRAFT-ASUB-012-public-frontier-v5-multipost-independent/attack.py`

- fixes generation/replay window conflation;
- races single-post and forged 2..5-post mechanisms;
- full-hop live validates fill candidates;
- keeps a conservative primary + aggressive backfill replay estimate.

Purpose: controlled bridge from earlier replay-sized code.

### DRAFT-ASUB-013 — timeout-prefix full archive

`submissions/DRAFT-ASUB-013-public-frontier-v6-timeout-prefix/attack.py`

- tiny live calibration only;
- fast row uses plain single-post to avoid known Gemma Harmony-format risk;
- slow row races plain/Harmony/forge2..forge5 by observed public raw/sec;
- returns the full 2,000-candidate legal archive from the winning mechanism;
- makes no replay-cap estimate because replay timeout preserves the prefix.

This is the highest-upside public experiment currently under mechanical validation. It should not displace a private-aware final candidate merely because it has a stronger public score.

## Private implication

The same replay-timeout change also suggests that a private-aware mixed hedge should eventually be tested with an **oversubscribed, interleaved archive** rather than an arbitrarily short 360-candidate list. Interleaving is important: if private replay truncates early, the prefix must still contain multiple distinct private hypotheses instead of placing an entire family in an unevaluated tail.

Do not mutate frozen ASUB-006 in place. Any 2,000-candidate private-prefix variant must receive a new ASUB identity after mechanical tests.

## Working Note value

This evaluator change creates a clean methodological lesson: runtime optimization depends on timeout semantics. Under zero-on-timeout, conservative sizing is rational; under prefix-preserving timeout, value-ordered oversubscription is rational. The attack algorithm should adapt to the evaluator contract rather than treat candidate count as a fixed hyperparameter.
