# Kaggle submission runbook — AgentSec

Last updated: 2026-08-26

## Purpose

Turn a frozen AgentSec `attack.py` into a reproducible Kaggle hosted submission without editing the frozen source itself.

The notebook wiring that produced the valid ASUB-001 score is reusable. Each new submission should differ only by the uploaded frozen source file and the exact `filename` literal in the wrapper cell.

## Prize-first order

Use the live Kaggle queue/results to decide exact ordering. The current independent candidates are:

1. `ASUB-20260826-007-public-frontier-v6-timeout-prefix` — next-generation public experiment adapted to prefix-preserving replay timeouts;
2. `ASUB-20260826-009-private-hedge-v4-coverage-prefix` — preferred next-generation private hedge; full cap plus coverage-first prefix;
3. `ASUB-20260826-005-public-frontier-v4-paired-hops` — established advanced public frontier;
4. `ASUB-20260826-006-private-hedge-v2` — established private-aware mixed hedge;
5. `ASUB-20260826-008-private-hedge-v3-timeout-prefix` — useful predecessor/ablation for ASUB-009 if it is already queued or if a direct ordering ablation is worth a slot;
6. `ASUB-20260826-004-public-frontier-v2` — lower-complexity controlled public ablation.

Do not submit an additional ASUB-001 duplicate. Its existing byte-identical replicate can finish in parallel and is not a blocker.

ASUB-009 supersedes ASUB-008 for a *new* private timeout-prefix slot because it preserves the same hypothesis weights and calibration logic while guaranteeing one appearance of every active family before any family receives a second replay position. If ASUB-008 is already queued, preserve it as a clean ordering ablation rather than cancelling or duplicating it.

## Frozen sources

### ASUB-005

Repository source: `submissions/ASUB-20260826-005-public-frontier-v4-paired-hops/attack.py`  
Git blob SHA: `7b1e000062ebb35a11fe4257fe1d370b07f0d7f0`  
Upload filename: `ASUB-20260826-005-public-frontier-v4-paired-hops_attack.py`  
Private Dataset: `agentsec-asub005`  
Submission description: `ASUB-20260826-005 public frontier v4 paired hops`

### ASUB-006

Repository source: `submissions/ASUB-20260826-006-private-hedge-v2/attack.py`  
Git blob SHA: `47c40678fbc4de7da1a2569ace64c8fd036e5ef5`  
Upload filename: `ASUB-20260826-006-private-hedge-v2_attack.py`  
Private Dataset: `agentsec-asub006`  
Submission description: `ASUB-20260826-006 private hedge v2`

### ASUB-007

Repository source: `submissions/ASUB-20260826-007-public-frontier-v6-timeout-prefix/attack.py`  
Git blob SHA: `f5eeb96d050c26544e8d945cf5af66b0977f0ae7`  
Upload filename: `ASUB-20260826-007-public-frontier-v6-timeout-prefix_attack.py`  
Private Dataset: `agentsec-asub007`  
Submission description: `ASUB-20260826-007 public frontier v6 timeout prefix`

### ASUB-008

Repository source: `submissions/ASUB-20260826-008-private-hedge-v3-timeout-prefix/attack.py`  
Git blob SHA: `5f4a675a444027b25071f722421674fc9624040b`  
Upload filename: `ASUB-20260826-008-private-hedge-v3-timeout-prefix_attack.py`  
Private Dataset: `agentsec-asub008`  
Submission description: `ASUB-20260826-008 private hedge v3 timeout prefix`

### ASUB-009

Repository source: `submissions/ASUB-20260826-009-private-hedge-v4-coverage-prefix/attack.py`  
Git blob SHA: `86444fa16cb817fa210ade4319ec52e8ad5ece6c`  
Upload filename: `ASUB-20260826-009-private-hedge-v4-coverage-prefix_attack.py`  
Private Dataset: `agentsec-asub009`  
Submission description: `ASUB-20260826-009 private hedge v4 coverage prefix`

## Reusable notebook wrapper

Reuse the notebook that produced the successful Version 4 ASUB-001 submission. Keep Internet **OFF**.

For each new source, replace only `filename` with the exact uploaded filename:

```python
from pathlib import Path
import shutil
import py_compile
import runpy

filename = "REPLACE_WITH_EXACT_UPLOADED_FILENAME.py"

matches = list(Path("/kaggle/input/datasets").rglob(filename))
print("Matches:")
for path in matches:
    print(" -", path)

assert len(matches) == 1, (
    f"Expected exactly one {filename}, found {len(matches)}"
)

source = matches[0]
destination = Path("/kaggle/working/attack.py")

shutil.copy2(source, destination)
py_compile.compile(str(destination), doraise=True)

print("attack.py prepared:", destination)
print("Python syntax: OK")

_ = runpy.run_path(str(destination), run_name="__main__")
```

Assigning the `runpy.run_path` result to `_` suppresses the giant globals dictionary seen in the earlier interactive run.

Exact filename literals:

```python
# ASUB-005
filename = "ASUB-20260826-005-public-frontier-v4-paired-hops_attack.py"

# ASUB-006
filename = "ASUB-20260826-006-private-hedge-v2_attack.py"

# ASUB-007
filename = "ASUB-20260826-007-public-frontier-v6-timeout-prefix_attack.py"

# ASUB-008
filename = "ASUB-20260826-008-private-hedge-v3-timeout-prefix_attack.py"

# ASUB-009
filename = "ASUB-20260826-009-private-hedge-v4-coverage-prefix_attack.py"
```

## Kaggle UI sequence

1. Open the existing competition notebook and click **Edit**.
2. Upload the frozen source as a **private Dataset**; do not edit the source logic in Kaggle.
3. Confirm the new dataset appears under notebook Inputs.
4. Change only the wrapper `filename` literal to the exact uploaded filename.
5. Confirm **Internet = Off** in Session options.
6. Use **Save Version → Save & Run All (Commit)**, not Quick Save.
7. Wait for the saved version to show **Successful**.
8. Open that saved version's **Output** tab.
9. Confirm both `attack.py` and `submission.csv` exist.
10. Open/select `submission.csv` and click **Submit to Competition**.
11. Enter the exact submission description above.
12. Confirm the competition **Submissions** page shows the run as Running/Queued/Succeeded rather than merely a notebook version.

## Expected pre-submit output

The saved notebook version must contain:

- `/kaggle/working/attack.py`
- `/kaggle/working/submission.csv`

The visible `submission.csv` can contain four placeholder zeros before the hosted rerun. That is the same wiring that produced the valid ASUB-001 score.

## Immutability

If attack logic changes, do not reuse an existing ASUB ID or overwrite a frozen directory. Create a new `ASUB-*` identity and record it in `docs/SUBMISSION_LEDGER.md`.

## Result capture

As soon as a hosted run becomes terminal, record:

- ASUB ID;
- Kaggle notebook version;
- exact submission description;
- terminal status;
- public score;
- visible runtime/age;
- screenshot;
- whether the result changes the next submission decision.

The next launch is chosen by expected prize value, not by either conserving or exhausting the daily quota.
