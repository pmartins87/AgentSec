$ErrorActionPreference = "Stop"

# AgentSec R1 local smoke test for Windows / PowerShell.
# Requires Python 3.11+ and internet only for the one-time SDK install.

if (-not (Test-Path ".venv")) {
    py -3.11 -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

& .\.venv\Scripts\aicomp.exe validate redteam attack.py
& .\.venv\Scripts\aicomp.exe test redteam attack.py --budget-s 60 --agent deterministic
& .\.venv\Scripts\aicomp.exe evaluate redteam attack.py --budget-s 60 --agent deterministic --env gym --artifacts-dir artifacts/r1_gym --save-transcript --save-framework-events

Write-Host "R1 smoke completed. Preserve artifacts/r1_gym report.json, score.txt, transcript.log and framework.jsonl."
