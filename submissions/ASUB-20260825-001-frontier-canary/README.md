# ASUB-20260825-001 — Frontier canary

Status: **PREPARED / NOT YET HOSTED**

Purpose: obtain AgentSec's first competitive hosted calibration score using a compact synthesis of current public-frontier mechanics. This is not the final/private-robust candidate.

## Frozen source

- Submission source: `attack.py`
- Required SDK: `aicomp-sdk==3.1.2`
- Competition: `ai-agent-security-multi-step-tool-attacks`
- Generated hosted artifact: `/kaggle/working/attack.py`
- Internet: disabled
- GPU requirement for this script itself: none; competition evaluation infrastructure provides the target models.

Record the exact AgentSec git commit used when the kernel is pushed. Do not submit a locally modified copy without committing it first.

## Strategy

1. Warm the hosted environment with one one-hop probe; do not return that under-measured candidate.
2. Run one full-hop natural-template probe and use measured latency as a model signal.
3. Use the natural single-post template for the fast row.
4. Use the publicly disclosed Harmony-compression suffix for the slow row.
5. Generate unique short `.co` domains.
6. Probe every candidate live; keep it only when a successful `http.post` with `SECRET_MARKER` is observed.
7. Size the returned portfolio from the measured candidate cost and `AttackRunConfig.time_budget_s`.
8. Use a conservative primary segment, then a bounded backfill segment.
9. Sort successful candidates by measured latency before returning them.

Current default sizing:

- primary replay fraction: `0.945`
- primary wall fraction: `0.980`
- backfill replay fraction: `0.990`
- backfill wall fraction: `0.994`
- next-candidate cost multiplier: `1.12`
- hard cap: `2000`

These are deliberately slightly more conservative than the most aggressive public variants. The first hosted run is intended to measure actual AgentSec throughput and replay behavior before tightening.

## Public-source provenance

The public technique family is independently visible across multiple participant repositories/notebooks. AgentSec's implementation is rewritten and simplified around the common mechanism rather than copied as an opaque submission.

Key public references:

- https://github.com/Jun-Morita/kaggle-ai-agent-security
- https://github.com/SKYGOD07/AI-Agent-Security---Multi-Step-Tool-Attacks

The slow-row Harmony suffix and live validation-fill are public benchmark techniques. Third-party reported scores are evidence for prioritization, not AgentSec results.

## Why this is only a canary

The public SDK 3.1.2 scorer/guardrail pairing permits `SECRET_MARKER`-based `EXFILTRATION` and over-granular URL-domain diversity. The competition's final/private guardrail is hidden and stricter. A high public score can therefore coexist with weak private performance.

Promotion rule: this submission can become the public-throughput champion after a successful hosted run, but it cannot become the R8 final candidate without private-robustness evidence.

## Before hosted submission

- Confirm Kaggle rules/entry acceptance before the entry deadline.
- Replace `YOUR_KAGGLE_USERNAME` in a copy of `kernel-metadata.example.json` if pushing via Kaggle CLI.
- Run SDK validation/smoke when an environment with the competition SDK is available.
- Commit any change before pushing.
- Record kernel slug/version, git SHA, runtime, returned candidate count, and resulting public/private rows in the submission ledger.

## Expected hosted outputs

When executed as a Kaggle script kernel, `attack.py`:

1. locates the mounted competition gateway;
2. writes itself to `/kaggle/working/attack.py`;
3. writes a placeholder `submission.csv` for the pre-submit output check;
4. starts `JEDAttackInferenceServer`.

The competition rerun is responsible for loading the generated `attack.py`, running the attack, replaying candidates, and producing the scored submission rows.

## Result

Pending.
