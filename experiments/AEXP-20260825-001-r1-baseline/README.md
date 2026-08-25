# AEXP-20260825-001 — R1 baseline reproduction

Status: **PREPARED / NOT EXECUTED**

## Hypothesis

The pinned `aicomp-sdk==3.1.2` and top-level `attack.py` can reproduce the official public contract end-to-end under deterministic and Gym-style local evaluation, producing valid replayable findings and evaluator artifacts.

## Frozen inputs

- SDK: `aicomp-sdk==3.1.2`
- upstream release commit: `56dabd3a6d8fbe587acd4d0a1b22796b1acccfcd`
- AgentSec attack: repository top-level `attack.py`
- runner: `scripts/run_r1_smoke.ps1`
- deterministic smoke budget: 60 s
- Gym-style evaluate budget: 60 s
- target agent: deterministic

## Execution command

From the AgentSec repository on Windows PowerShell:

```powershell
.\scripts\run_r1_smoke.ps1
```

## Required preserved outputs

- SDK validation result
- deterministic smoke result
- `artifacts/r1_gym/score.txt`
- `artifacts/r1_gym/report.json`
- `artifacts/r1_gym/transcript.log`
- `artifacts/r1_gym/framework.jsonl`
- exact AgentSec git SHA at execution time
- wall-clock runtime and any failures

## Result

Not executed in the current ChatGPT tool environment because the package could not be installed there. Do not infer PASS from the existence of the code.

## Promotion criterion

R1 can pass only after a clean execution is preserved and the result is reproducible from the pinned commit/configuration.
