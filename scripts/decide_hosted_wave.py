#!/usr/bin/env python3
"""Decide the next hosted AgentSec experiment from terminal wave scores."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.hosted_wave import decide_hosted_wave


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Decide the next AgentSec hosted experiment from terminal wave scores.")
    parser.add_argument("--asub007", type=float)
    parser.add_argument("--asub009", type=float)
    parser.add_argument("--asub010-a", dest="asub010_a", type=float)
    parser.add_argument("--asub010-b", dest="asub010_b", type=float)
    return parser


def main() -> None:
    args = _parser().parse_args()
    decision = decide_hosted_wave(
        {
            "ASUB-007": args.asub007,
            "ASUB-009": args.asub009,
            "ASUB-010-A": args.asub010_a,
            "ASUB-010-B": args.asub010_b,
        }
    )
    print(f"decision={decision.decision}")
    print(f"next_candidate={decision.next_candidate or 'NONE'}")
    if decision.public_best_name is not None:
        print(f"public_best={decision.public_best_name}:{decision.public_best_score:.3f}")
    if decision.asub010_spread is not None:
        print(f"asub010_spread={decision.asub010_spread:.3f}")
    for line in decision.rationale:
        print(f"- {line}")


if __name__ == "__main__":
    main()
