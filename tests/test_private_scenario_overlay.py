from __future__ import annotations

from src.private_scenario_overlay import (
    PRIVATE_AUTHORITY_STRICT,
    expanded_private_stress_scenarios,
    plan_expanded_private_portfolio,
)


def test_authority_strict_closes_direct_cd_relative_to_semantic_lanes() -> None:
    rates = PRIVATE_AUTHORITY_STRICT.effective_hit_rate
    assert rates["direct_cd"] < rates["semantic_email"]
    assert rates["direct_cd"] < rates["semantic_http"]
    assert rates["direct_cd"] < rates["semantic_shell"]
    assert rates["direct_cd"] < rates["semantic_write"]


def test_expanded_scenario_set_is_additive_not_a_rewrite() -> None:
    scenarios = expanded_private_stress_scenarios()
    names = [scenario.name for scenario in scenarios]
    assert names[-1] == "private_authority_strict"
    assert len(names) == len(set(names))
    assert "private_provenance_strict" in names
    assert "private_semantic_auth" in names


def test_expanded_minimax_plan_shifts_some_cd_budget_to_semantic_email() -> None:
    plan = plan_expanded_private_portfolio()
    assert sum(plan.counts.values()) == 360
    assert all(value >= 12 for value in plan.counts.values())

    # Deterministic coarse optimum for the explicitly frozen synthetic stress
    # assumptions. This is a planning regression, not a claim about private LB.
    assert plan.counts == {
        "public_exfil": 144,
        "direct_cd": 60,
        "semantic_email": 120,
        "semantic_http": 12,
        "semantic_shell": 12,
        "semantic_write": 12,
    }
    assert 0.0 < plan.min_ratio <= plan.mean_ratio <= 1.0
