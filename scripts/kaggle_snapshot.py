#!/usr/bin/env python3
"""Capture AgentSec Kaggle competition telemetry via the official Kaggle CLI.

This helper intentionally reads only public/account-visible Kaggle telemetry:
submissions, leaderboard, and kernel status. It does not attempt to infer or
access the hidden private leaderboard/guardrail.

Prerequisites:
  pip install -U kaggle
  kaggle auth login

Usage:
  python scripts/kaggle_snapshot.py
  python scripts/kaggle_snapshot.py --download-leaderboard
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

COMPETITION = "ai-agent-security-multi-step-tool-attacks"
KERNEL = "paulomartins87/notebooka6483cd827"


def _run(*args: str) -> dict[str, object]:
    proc = subprocess.run(
        list(args),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "command": list(args),
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/kaggle_snapshot.json")
    parser.add_argument("--download-leaderboard", action="store_true")
    args = parser.parse_args()

    if shutil.which("kaggle") is None:
        print("Kaggle CLI not found. Run: pip install -U kaggle", file=sys.stderr)
        return 2

    snapshot: dict[str, object] = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "competition": COMPETITION,
        "kernel": KERNEL,
        "submissions": _run(
            "kaggle", "competitions", "submissions", COMPETITION, "-v"
        ),
        "leaderboard_top": _run(
            "kaggle", "competitions", "leaderboard", COMPETITION, "--show", "-v"
        ),
        "kernel_status": _run("kaggle", "kernels", "status", KERNEL),
    }

    if args.download_leaderboard:
        lb_dir = Path("artifacts/kaggle_leaderboard")
        lb_dir.mkdir(parents=True, exist_ok=True)
        snapshot["leaderboard_download"] = _run(
            "kaggle",
            "competitions",
            "leaderboard",
            COMPETITION,
            "--download",
            "-p",
            str(lb_dir),
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
    print(out)

    # A failed authenticated read is important and should surface to callers.
    submissions = snapshot["submissions"]
    assert isinstance(submissions, dict)
    return 0 if submissions.get("returncode") == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
