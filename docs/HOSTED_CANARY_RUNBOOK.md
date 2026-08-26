# Hosted canary runbook — AgentSec

Date: 2026-08-25  
Target: `ASUB-20260825-001-frontier-canary`

This runbook is intentionally short. The goal is to get one valid hosted calibration result quickly and preserve enough evidence to interpret it.

## 0. Eligibility gate

Before spending runtime, open the competition page while signed in and verify that the account is actually entered / rules are accepted.

Trusted Access security verification was completed by the user on 2026-08-25. Trusted Access and competition-rule acceptance are separate gates, so the competition page itself is the final check.

Entry deadline: **2026-08-25 23:59 UTC**.

## 1. Source to use

Use exactly:

`submissions/ASUB-20260825-001-frontier-canary/attack.py`

Frozen source git-blob SHA:

`b17180572b27d80f584d640d4ebf3ecace28df4d`

Do not edit the source in Kaggle. If a change is required, create a new AgentSec submission ID first.

## 2. Kaggle notebook/script settings

- Competition source: `ai-agent-security-multi-step-tool-attacks`
- Internet: **OFF**
- Code file: `attack.py`
- Output must include `/kaggle/working/attack.py`
- The script itself has no external model/runtime dependency beyond the competition gateway/SDK mounted by Kaggle.
- Keep the official competition environment/runtime settings unless the current starter notebook explicitly requires a specific accelerator.

The repository's example metadata is:

`submissions/ASUB-20260825-001-frontier-canary/kernel-metadata.example.json`

## 3. Pre-submit mechanical check

Local/offline:

```bash
python scripts/preflight_frontier_canary.py
```

Expected result contains:

```json
{"status":"PASS","static_candidates":2000,"unique_urls":2000}
```

This is only a packaging/mechanical check. If the pinned SDK is available, also run:

```bash
aicomp validate redteam submissions/ASUB-20260825-001-frontier-canary/attack.py
```

## 4. Hosted execution sanity checks

During/after the Kaggle run, verify:

1. the script starts without import errors;
2. it prints `attack.py written: /kaggle/working/attack.py`;
3. it prints `placeholder submission.csv written: ...`;
4. the competition inference server starts;
5. the notebook completes within the allowed runtime;
6. `/kaggle/working/attack.py` is present in the notebook output;
7. Kaggle allows the notebook version to be submitted to the competition.

A failure in any item above is a packaging/runtime failure, not a strategy result.

## 5. What to record immediately

Capture:

- UTC timestamp
- AgentSec git commit SHA
- Kaggle notebook slug
- Kaggle notebook version number
- notebook total runtime
- whether `/kaggle/working/attack.py` exists
- submission ID/reference
- public score
- any visible public/private row detail
- timeout/parser/evaluator warning
- screenshot or copied log excerpt if the result is abnormal

Enter the result in:

`docs/SUBMISSION_LEDGER.md`

and:

`experiments/AEXP-20260825-003-frontier-canary/README.md`

## 6. Interpretation rule

### If submission is invalid / crashes

Fix only the hosted wiring defect. Preserve ASUB-001 and create a new submission package if source changes.

### If public score is far below the contemporary public frontier

Investigate in this order:

1. live candidate fire rate;
2. GPT-OSS/Gemma latency/template choice;
3. replay truncation;
4. under-fill from conservative replay fractions;
5. evaluator/parser changes.

### If public score is competitive

Freeze it as the public-throughput champion and stop chasing tiny public gains. Move compute/research time to the private-robust lane.

### If private score is weak

Treat this as expected evidence that the public sentinel route overfits the public guardrail. Prioritize multi-step and confused-deputy/private-proxy work.

## 7. Preserve immutability

`ASUB-20260825-001` is frozen.

Any parameter change, prompt change, fallback change, or gateway change becomes:

- a new `ASUB-*` directory;
- a new `AEXP-*` record;
- a new exact source hash.

## 8. Reproducible UI wrapper used for Version 4

When the frozen `attack.py` is attached to a Kaggle notebook as a private Dataset input, the notebook cell must do more than copy/compile it: execute the file's `__main__` entrypoint so the placeholder CSV and competition gateway are started.

The clean Version 4 wrapper used:

```python
from pathlib import Path
import shutil
import py_compile
import runpy

filename = "ASUB-20260825-001-frontier-canary_attack.py"
matches = list(Path("/kaggle/input/datasets").rglob(filename))
assert len(matches) == 1

source = matches[0]
destination = Path("/kaggle/working/attack.py")
shutil.copy2(source, destination)
py_compile.compile(str(destination), doraise=True)

runpy.run_path(str(destination), run_name="__main__")
```

Expected notebook output before submission includes both:

- `/kaggle/working/attack.py`
- `/kaggle/working/submission.csv`

The `submission.csv` contains placeholder zeros before private rerun; that is normal for this competition flow. The evaluator reruns the notebook/attack and produces the scored rows.

Observed history: the first pre-v4 attempt returned Kaggle `system error`; Version 4 was then submitted twice and both copies entered `Notebook Running`. Do not infer strategy failure from the earlier system-error class.
