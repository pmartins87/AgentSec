from __future__ import annotations

import pytest

from src.hosted_evidence import (
    ASUB001_RAW_PER_HIT,
    ASUB002_RAW_PER_HIT,
    compare_duplicate_scores,
    infer_asub001,
    infer_asub001_row,
    infer_asub002,
    minimum_hits_for_row_score_cap,
    raw_to_normalized,
)


def test_asub001_public_lb_inversion_recovers_mean_and_total_hits() -> None:
    gpt_hits = 100
    gemma_hits = 150
    public_score = (
        raw_to_normalized(gpt_hits * ASUB001_RAW_PER_HIT)
        + raw_to_normalized(gemma_hits * ASUB001_RAW_PER_HIT)
    ) / 2
    result = infer_asub001(public_score)
    assert result.equivalent_mean_hits_per_public_row == pytest.approx(125)
    assert result.equivalent_total_hits_across_public_rows == pytest.approx(250)
    assert result.nearest_half_mean_hits == 125
    assert result.score_residual == pytest.approx(0.0)


def test_asub002_public_lb_inversion_recovers_mean_hits() -> None:
    gpt_hits = 30
    gemma_hits = 50
    public_score = (
        raw_to_normalized(gpt_hits * ASUB002_RAW_PER_HIT)
        + raw_to_normalized(gemma_hits * ASUB002_RAW_PER_HIT)
    ) / 2
    result = infer_asub002(public_score)
    assert result.equivalent_mean_hits_per_public_row == pytest.approx(40)


def test_row_inference_remains_available_when_per_model_score_is_known() -> None:
    hits = 137
    row_score = raw_to_normalized(hits * ASUB001_RAW_PER_HIT)
    result = infer_asub001_row(row_score, candidate_count=200)
    assert result.hit_count_estimate == pytest.approx(hits)
    assert result.nearest_integer_hits == hits
    assert result.completion_ratio == pytest.approx(hits / 200)


def test_duplicate_variance_converts_to_mean_hit_variance() -> None:
    score_a = raw_to_normalized(100 * ASUB001_RAW_PER_HIT)
    score_b = raw_to_normalized(125 * ASUB001_RAW_PER_HIT)
    result = compare_duplicate_scores((score_a, score_b))
    assert result.equivalent_mean_hit_range == pytest.approx(25)
    assert result.equivalent_mean_hit_mean == pytest.approx(112.5)


def test_score_cap_is_marked_ambiguous() -> None:
    result = infer_asub001(1000.0)
    assert result.capped is True
    assert minimum_hits_for_row_score_cap(ASUB001_RAW_PER_HIT) == 11_112


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError):
        infer_asub001(-0.1)
    with pytest.raises(ValueError):
        compare_duplicate_scores((1.0,))
