#!/usr/bin/env python3
"""Report the robust split between direct confused-deputy mechanisms."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.direct_cd_split import DEFAULT_STRESSES, default_direct_cd_split  # noqa: E402


def main() -> None:
    split = default_direct_cd_split()
    print("Synthetic stress planner only; hidden private guardrail remains unknown.")
    print()
    print("Direct-CD quota: 60")
    print(f"  synonym one-turn: {split.synonym}")
    print(f"  explicit+neutral: {split.launder}")
    print(f"  worst relative ratio: {split.min_ratio:.4f}")
    print(f"  mean relative ratio:  {split.mean_ratio:.4f}")
    print()
    print("Stress ratios:")
    for stress in DEFAULT_STRESSES:
        print(f"  {stress.name:32s} {split.scenario_ratios[stress.name]:.4f}")


if __name__ == "__main__":
    main()
