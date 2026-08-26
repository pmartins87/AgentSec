# Kaggle submission runbook — AgentSec

Last updated: 2026-08-26

## Purpose

Turn a frozen AgentSec `attack.py` into a reproducible Kaggle hosted submission without editing the frozen source itself.

The current notebook wiring that succeeded for ASUB-001 is reusable. Each new submission should differ only by the uploaded frozen source file and the one filename literal in the wrapper cell.

## Current prize-first order

When daily capacity is available, prefer independent evidence over duplicate reruns:

1. `ASUB-20260826-005-public-frontier-v4-paired-hops` — aggressive public frontier / paired-hop calibration;
2. `ASUB-20260826-006-private-hedge-v2` — private-aware mixed hedge;
3. `ASUB-20260826-004-public-frontier-v2` — controlled lower-complexity public ablation when another hosted slot is useful.

The byte-identical ASUB-001 replicate can finish in parallel and is not a blocker.

## Frozen sources

### ASUB-005

Repository source:

`submissions/ASUB-20260826-005-public-frontier-v4-paired-hops/attack.py`

Git blob SHA:

`7b1e000062ebb35a11fe4257fe1d370b07f0d7f0`

Recommended upload filename:

`ASUB-20260826-005-public-frontier-v4-paired-hops_attack.py`

Recommended private Kaggle Dataset name:

`agentsec-asub005`

Recommended submission description:

`ASUB-20260826-005 public frontier v4 paired hops`

### ASUB-006

Repository source:

`submissions/ASUB-20260826-006-private-hedge-v2/attack.py`

Git blob SHA:

`47c40678fbc4de7da1a2569ace64c8fd036e5ef5`

Recommended upload filename:

`ASUB-20260826-006-private-hedge-v2_attack.py`

Recommended private Kaggle Dataset name:

`agentsec-asub006`

Recommended submission description:

`ASUB-20260826-006 private hedge v2`

## One-time notebook wrapper

Reuse the notebook that already produced the successful Version 4 ASUB-001 submission. Keep Internet **OFF**.

For each new source, replace only `filename` below with the exact uploaded filename:

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

Assigning the `runpy.run_path` result to `_` suppresses the giant globals dictionary that appeared in the earlier interactive run.

## Exact ASUB-005 wrapper literal

```python
filename = "ASUB-20260826-005-public-frontier-v4-paired-hops_attack.py"
```

## Exact ASUB-006 wrapper literal

```python
filename = "ASUB-20260826-006-private-hedge-v2_attack.py"
```

## Kaggle UI sequence

1. Open the existing competition notebook and click **Edit**.
2. Upload the frozen source as a **private Dataset**; do not edit the source text in Kaggle.
3. Confirm the new dataset is visible under notebook Inputs.
4. Change only the wrapper `filename` literal to the new uploaded filename.
5. Confirm **Internet = Off** in Session options.
6. Use **Save Version → Save & Run All (Commit)**, not Quick Save.
7. Wait for the saved version to show **Successful**.
8. Open that saved version's **Output** tab.
9. Confirm both `attack.py` and `submission.csv` exist in Output.
10. Select/open `submission.csv` and click **Submit to Competition**.
11. Enter the exact submission description from this runbook.
12. Confirm the submission appears on the competition **Submissions** page as Running/Queued/Succeeded rather than merely existing as a notebook version.

## Expected pre-submit output

The saved notebook version must contain:

- `/kaggle/working/attack.py`
- `/kaggle/working/submission.csv`

The visible `submission.csv` can contain four placeholder zeros before the hosted rerun. That is the same wiring that produced the valid ASUB-001 score.

## Do not overwrite frozen identities

If any attack logic changes, do not reuse the ASUB ID or overwrite the frozen directory. Create a new `ASUB-*` submission identity and record it in `docs/SUBMISSION_LEDGER.md`.

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

The next launch should be chosen on expected prize value, not on a desire either to conserve or exhaust the daily quota.
