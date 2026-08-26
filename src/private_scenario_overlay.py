"""Expanded private-evaluator stress scenarios for AgentSec final planning.

This module deliberately sits *on top* of ``portfolio_optimizer`` rather than
rewriting its original illustrative scenarios. The extra scenario encodes an
important opposite failure mode: a semantic authority guard may recognize and
block direct confused-deputy behavior even while allowing some benign-looking
source→action chains that the literal public scorer still rewards.

All rates are synthetic stress assumptions. They are not estimates of the hidden
Kaggle guardrail and must never be described as measured private behavior.
"""

from __future__ import annotations

from src.portfolio_optimizer import (
    PortfolioPlan,
    Scenario,
    competition_lanes,
    illustrative_stress_scenarios,
    optimize_minimax_ratio,
)


PRIVATE_AUTHORITY_STRICT = Scenario(
    "private_authority_strict",
    {
        # Marker EXFIL may be blocked by payload-aware policy.
        "public_exfil": 0.08,
        # A semantic authority judge can catch ambient-authority email misuse.
        "direct_cd": 0.10,
        # Benign semantically authorized actions can still survive if the private
        # policy reasons about intent more than raw source provenance.
        "semantic_email": 0.55,
        "semantic_http": 0.60,
        "semantic_shell": 0.50,
        "semantic_write": 0.60,
    },
)


def expanded_private_stress_scenarios() -> tuple[Scenario, ...]:
    """Base stress set plus an explicit direct-CD-closing semantic guard case."""

    return illustrative_stress_scenarios() + (PRIVATE_AUTHORITY_STRICT,)


def plan_expanded_private_portfolio(
    total_candidates: int = 360,
    *,
    quantum: int = 12,
    floor_per_lane: int = 12,
) -> PortfolioPlan:
    """Return the deterministic minimax plan under the expanded stress set."""

    lanes = competition_lanes()
    floors = {lane.name: int(floor_per_lane) for lane in lanes}
    return optimize_minimax_ratio(
        lanes,
        expanded_private_stress_scenarios(),
        int(total_candidates),
        quantum=int(quantum),
        min_counts=floors,
    )
