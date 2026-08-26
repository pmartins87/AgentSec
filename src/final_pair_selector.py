"""Robust selector for the two Kaggle final-submission slots.

The final leaderboard is determined from a limited set of selected submissions.
Because the hidden private guardrail is unknown, the two selected candidates
should be evaluated as a *pair*: in each plausible private scenario, the useful
outcome is the stronger of the two submissions.

This module is deliberately generic.  It consumes scenario score projections that
come from experiments/stress models; it does not embed claims about the hidden
Kaggle guardrail.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Mapping, Sequence


@dataclass(frozen=True)
class CandidateProfile:
    name: str
    scenario_scores: Mapping[str, float]


@dataclass(frozen=True)
class PairPlan:
    first: str
    second: str
    max_regret: float
    worst_case_best: float
    mean_best: float
    scenario_best: Mapping[str, float]


def _scenario_names(candidates: Sequence[CandidateProfile]) -> tuple[str, ...]:
    names: set[str] = set()
    for candidate in candidates:
        names.update(str(name) for name in candidate.scenario_scores)
    if not names:
        raise ValueError("at least one scenario score is required")
    return tuple(sorted(names))


def _score(candidate: CandidateProfile, scenario: str) -> float:
    if scenario not in candidate.scenario_scores:
        raise ValueError(f"candidate {candidate.name!r} missing scenario {scenario!r}")
    return float(candidate.scenario_scores[scenario])


def choose_final_pair(
    candidates: Sequence[CandidateProfile],
    *,
    scenario_weights: Mapping[str, float] | None = None,
) -> PairPlan:
    """Choose two candidates by minimax regret, then robustness and mean score.

    For every scenario, the pair receives the better of its two candidate scores.
    Regret is measured relative to the best single candidate available in that
    scenario.  The chosen pair minimizes maximum regret; ties maximize the
    pair's worst-case best score, then weighted mean best score.
    """

    profiles = list(candidates)
    if len(profiles) < 2:
        raise ValueError("at least two candidate profiles are required")
    scenarios = _scenario_names(profiles)

    weights = {scenario: 1.0 for scenario in scenarios}
    if scenario_weights is not None:
        for scenario in scenarios:
            weights[scenario] = max(0.0, float(scenario_weights.get(scenario, 0.0)))
    weight_total = sum(weights.values())
    if weight_total <= 0:
        raise ValueError("scenario weights must contain positive mass")

    oracle = {
        scenario: max(_score(candidate, scenario) for candidate in profiles)
        for scenario in scenarios
    }

    best_plan: PairPlan | None = None
    best_key: tuple[float, float, float, str, str] | None = None

    for left, right in combinations(profiles, 2):
        scenario_best = {
            scenario: max(_score(left, scenario), _score(right, scenario))
            for scenario in scenarios
        }
        regrets = {
            scenario: oracle[scenario] - scenario_best[scenario]
            for scenario in scenarios
        }
        max_regret = max(regrets.values())
        worst_case_best = min(scenario_best.values())
        mean_best = sum(
            scenario_best[scenario] * weights[scenario]
            for scenario in scenarios
        ) / weight_total

        names = tuple(sorted((left.name, right.name)))
        plan = PairPlan(
            first=names[0],
            second=names[1],
            max_regret=float(max_regret),
            worst_case_best=float(worst_case_best),
            mean_best=float(mean_best),
            scenario_best=scenario_best,
        )
        # Lower regret is better; then larger worst/mean are better.  Final name
        # tie-break keeps results deterministic across Python versions.
        key = (-max_regret, worst_case_best, mean_best, names[0], names[1])
        if best_key is None or key > best_key:
            best_key = key
            best_plan = plan

    assert best_plan is not None
    return best_plan
