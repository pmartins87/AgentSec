# Kaggle CLI-first workflow — AgentSec

Preferred operational workflow from 2026-09-01 onward.

## Principle

Use the official Kaggle CLI/API path by default for notebook creation/push, kernel status, outputs, submissions, and leaderboard telemetry. Use the browser UI mainly for visual inspection, one-off debugging, and final manual checks.

This reduces copy/paste errors, stale-notebook-state errors, accidental resubmission of an older version, and unnecessary screenshot-driven micropasses.

## Local working directory

Keep AgentSec Kaggle artifacts under a dedicated project directory, for example:

`%USERPROFILE%\Competicoes\AgentSec\kaggle`

Do not store project artifacts under unrelated project folders.

The Kaggle CLI installation and OAuth credentials are user-level and are not tied to the current working directory.

## Authentication

```powershell
py -m pip install -U kaggle
kaggle auth login
```

Never commit Kaggle credentials/tokens to GitHub.

## Push a prepared diagnostic/submission notebook

```powershell
kaggle kernels push -p <folder-containing-kernel-metadata.json>
```

Use `kernel-metadata.json` to declare competition, dataset and model sources, privacy, Internet setting and accelerator.

## Check status

```powershell
kaggle kernels status paulomartins87/<kernel-slug>
```

## Pull outputs after completion

```powershell
kaggle kernels output paulomartins87/<kernel-slug> -p <local-output-folder>
```

## Competition telemetry

```powershell
kaggle competitions submissions ai-agent-security-multi-step-tool-attacks -v
kaggle competitions leaderboard ai-agent-security-multi-step-tool-attacks --show -v
```

Repository helper:

```powershell
python scripts/kaggle_snapshot.py --download-leaderboard
```

## Browser fallback

Use the browser only when CLI/API does not expose the needed operation or when a visual inspection is genuinely useful. When browser steps are necessary, always provide the exact notebook/kernel URL and exact identifiers rather than vague instructions such as “open the same notebook”.
