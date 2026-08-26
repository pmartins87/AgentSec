from __future__ import annotations

import pytest

from src.hosted_evidence import (
    ASUB001_RAW_PER_HIT,
    ASUB002_RAW_PER_HIT,
    compare_duplicate_scores,
    infer_asub001,
    infer_asub002,
    minimum_hits_for_score_cap,
    raw_to_normalized,
)


def test_asub001_score_inversion_recovers_exact_hit_count() -> None:
    hits = 137
    score = raw_to_normalized(hits * ASUB001_RAW_PER_HIT)
    result = infer_asub001(score, candidate_count=200)
    assert result.hit_count_estimate == pytest.approx(hits)
    assert result.nearest_integer_hits == hits
    assert result.completion_ratio == pytest.approx(hits / 200)
    assert result.score_residual == pytest.approx(0.0)
    assert result.capped is False


def test_asub002_score_inversion_recovers_exact_hit_count() -> None:
    hits = 40
    score = raw_to_normalized(hits * ASUB002_RAW_PER_HIT)
    result = infer_asub002(score)
    assert result.hit_count_estimate == pytest.approx(hits)
    assert result.nearest_integer_hits == hits


def test_duplicate_variance_converts_to_hit_variance() -> None:
    score_a = raw_to_normalized(100 * ASUB001_RAW_PER_HIT)
    score_b = raw_to_normalized(125 * ASUB001_RAW_PER_HIT)
    result = compare_duplicate_scores((score_a, score_b))
    assert result.hit_range == pytest.approx(25)
    assert result.hit_mean == pytest.approx(112.5)


def test_score_cap_is_marked_ambiguous() -> None:
    result = infer_asub001(1000.0)
    assert result.capped is True
    assert result.raw_score_estimate == 200_000.0
    assert minimum_hits_for_score_cap(ASUB001_RAW_PER_HIT) == 11_112


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError):
        infer_asub001(-0.1)
    with pytest.raises(ValueError):
        compare_duplicate_scores((1.0,))
