from __future__ import annotations

import pytest

from src.final_pair_selector import CandidateProfile, choose_final_pair


def test_complementary_pair_beats_two_similar_public_anchors() -> None:
    candidates = [
        CandidateProfile(
            "public_a",
            {"payload_open": 92, "payload_scan": 5, "semantic": 12},
        ),
        CandidateProfile(
            "public_b",
            {"payload_open": 90, "payload_scan": 6, "semantic": 11},
        ),
        CandidateProfile(
            "private_hedge",
            {"payload_open": 55, "payload_scan": 62, "semantic": 68},
        ),
    ]
    plan = choose_final_pair(candidates)
    assert {plan.first, plan.second} == {"public_a", "private_hedge"}
    assert plan.max_regret == 0
    assert plan.scenario_best["payload_open"] == 92
    assert plan.scenario_best["payload_scan"] == 62
    assert plan.scenario_best["semantic"] == 68


def test_weights_break_robustness_ties_by_weighted_mean() -> None:
    candidates = [
        CandidateProfile("a", {"s1": 10, "s2": 5, "s3": 5}),
        CandidateProfile("b", {"s1": 5, "s2": 10, "s3": 5}),
        CandidateProfile("c", {"s1": 5, "s2": 5, "s3": 10}),
    ]
    plan = choose_final_pair(candidates, scenario_weights={"s1": 10, "s2": 1, "s3": 1})
    assert "a" in {plan.first, plan.second}


def test_rejects_missing_scenario_scores() -> None:
    candidates = [
        CandidateProfile("a", {"s1": 1}),
        CandidateProfile("b", {"s2": 1}),
    ]
    with pytest.raises(ValueError):
        choose_final_pair(candidates)


def test_requires_two_candidates_and_positive_weight_mass() -> None:
    with pytest.raises(ValueError):
        choose_final_pair([CandidateProfile("a", {"s": 1})])

    with pytest.raises(ValueError):
        choose_final_pair(
            [CandidateProfile("a", {"s": 1}), CandidateProfile("b", {"s": 2})],
            scenario_weights={"s": 0},
        )
