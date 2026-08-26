#!/usr/bin/env python3
"""Compare the original and expanded AgentSec private-robust portfolio plans."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.portfolio_optimizer import (  # noqa: E402
    competition_lanes,
    illustrative_stress_scenarios,
    optimize_minimax_ratio,
)
from src.private_scenario_overlay import (  # noqa: E402
    expanded_private_stress_scenarios,
    plan_expanded_private_portfolio,
)


def _base_plan():
    lanes = competition_lanes()
    floors = {lane.name: 12 for lane in lanes}
    return optimize_minimax_ratio(
        lanes,
        illustrative_stress_scenarios(),
        360,
        quantum=12,
        min_counts=floors,
    )


def _print_plan(title: str, plan) -> None:
    print(title)
    for name, count in plan.counts.items():
        print(f"  {name:20s} {count:4d}")
    print(f"  worst_relative_ratio {plan.min_ratio:.4f}")
    print(f"  mean_relative_ratio  {plan.mean_ratio:.4f}")
    print()


def main() -> None:
    base = _base_plan()
    expanded = plan_expanded_private_portfolio()

    print("Synthetic stress planning only; hidden guardrail remains unknown.\n")
    _print_plan("Original scenario set:", base)
    _print_plan("Expanded set (+ private_authority_strict):", expanded)

    print("Allocation delta (expanded - original):")
    for name in base.counts:
        delta = expanded.counts[name] - base.counts[name]
        print(f"  {name:20s} {delta:+4d}")

    print("\nExpanded scenario ratios:")
    for scenario in expanded_private_stress_scenarios():
        print(
            f"  {scenario.name:28s} "
            f"ratio={expanded.scenario_ratios[scenario.name]:.4f}"
        )


if __name__ == "__main__":
    main()
