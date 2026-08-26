from __future__ import annotations

from collections import Counter

import pytest

from src.portfolio_optimizer import (
    Lane,
    Scenario,
    competition_lanes,
    illustrative_stress_scenarios,
    optimize_minimax_ratio,
    robust_interleave,
    score_allocation,
)


def test_score_allocation_is_linear_and_scenario_specific() -> None:
    lanes = (Lane("a", 10.0), Lane("b", 4.0))
    scenario = Scenario("s", {"a": 0.5, "b": 1.0})
    assert score_allocation({"a": 2, "b": 3}, lanes, scenario) == 22.0


def test_minimax_ratio_diversifies_across_orthogonal_scenarios() -> None:
    lanes = (Lane("a", 10.0), Lane("b", 10.0), Lane("c", 10.0))
    scenarios = (
        Scenario("only_a", {"a": 1.0}),
        Scenario("only_b", {"b": 1.0}),
        Scenario("only_c", {"c": 1.0}),
    )
    plan = optimize_minimax_ratio(lanes, scenarios, 30, quantum=10)
    assert plan.counts == {"a": 10, "b": 10, "c": 10}
    assert plan.min_ratio == pytest.approx(1 / 3)


def test_bounds_preserve_explicit_family_coverage() -> None:
    lanes = competition_lanes()
    floors = {lane.name: 12 for lane in lanes}
    plan = optimize_minimax_ratio(
        lanes,
        illustrative_stress_scenarios(),
        360,
        quantum=12,
        min_counts=floors,
    )
    assert sum(plan.counts.values()) == 360
    assert all(plan.counts[name] >= 12 for name in floors)
    assert 0.0 < plan.min_ratio <= plan.mean_ratio <= 1.0


def test_interleave_preserves_exact_counts_and_frontloads_mix() -> None:
    counts = {"a": 12, "b": 6, "c": 3, "d": 3}
    order = robust_interleave(counts, priority=("a", "b", "c", "d"))
    assert Counter(order) == Counter(counts)
    assert len(order) == sum(counts.values())

    # The first half should already contain every non-trivial lane, rather than
    # exhausting one family before moving to the next.
    first_half = order[: len(order) // 2]
    assert set(first_half) == set(counts)


def test_interleave_rejects_negative_counts() -> None:
    with pytest.raises(ValueError):
        robust_interleave({"a": 1, "b": -1})


def test_optimizer_rejects_unknown_scenario_lane() -> None:
    with pytest.raises(ValueError):
        optimize_minimax_ratio(
            (Lane("a", 1.0),),
            (Scenario("bad", {"missing": 1.0}),),
            12,
            quantum=12,
        )


def test_optimizer_requires_exact_quantum_divisor() -> None:
    with pytest.raises(ValueError):
        optimize_minimax_ratio(
            (Lane("a", 1.0),),
            (Scenario("ok", {"a": 1.0}),),
            10,
            quantum=6,
        )
