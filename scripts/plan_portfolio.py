"""Print the current illustrative AgentSec robust-portfolio plan.

The scenario rates are synthetic stress assumptions.  This is a planning aid,
not a hidden-evaluator predictor.  Replace the assumptions after hosted evidence.
"""

from __future__ import annotations

from collections import Counter

from src.portfolio_optimizer import (
    competition_lanes,
    illustrative_stress_scenarios,
    optimize_minimax_ratio,
    robust_interleave,
)


def main() -> None:
    lanes = competition_lanes()
    scenarios = illustrative_stress_scenarios()
    floors = {lane.name: 12 for lane in lanes}

    plan = optimize_minimax_ratio(
        lanes,
        scenarios,
        360,
        quantum=12,
        min_counts=floors,
    )
    order = robust_interleave(
        plan.counts,
        priority=tuple(lane.name for lane in lanes),
    )

    print("Illustrative stress-plan only; hidden guardrail remains unknown.")
    print("\nAllocation:")
    for lane in lanes:
        print(f"  {lane.name:20s} {plan.counts[lane.name]:4d}")

    print(f"\nWorst relative scenario ratio: {plan.min_ratio:.4f}")
    print(f"Mean relative scenario ratio:  {plan.mean_ratio:.4f}")
    print("\nScenario scores / relative optima:")
    for scenario in scenarios:
        print(
            f"  {scenario.name:28s} "
            f"{plan.scenario_scores[scenario.name]:9.2f} "
            f"ratio={plan.scenario_ratios[scenario.name]:.4f}"
        )

    prefix = order[:30]
    print("\nFirst 30 replay slots:")
    print("  " + ", ".join(prefix))
    print("\nFirst-30 family counts:")
    for name, count in sorted(Counter(prefix).items()):
        print(f"  {name:20s} {count:2d}")


if __name__ == "__main__":
    main()
