from __future__ import annotations

import pytest

from src.hosted_decision import compare_with_noise_band, empirical_noise_band


def test_empirical_noise_band_matches_asub001_duplicate_range() -> None:
    band = empirical_noise_band((77.850, 86.040))
    assert band.score_min == pytest.approx(77.850)
    assert band.score_max == pytest.approx(86.040)
    assert band.score_mean == pytest.approx(81.945)
    assert band.empirical_range == pytest.approx(8.190)


def test_small_single_run_gain_is_not_declared_decisive() -> None:
    result = compare_with_noise_band(
        candidate="new",
        candidate_score=90.0,
        anchor="ASUB-001",
        anchor_score=86.040,
        replicate_scores=(77.850, 86.040),
    )
    assert result.relation == "noise_band_overlap"
    assert result.conservative_advantage == 0.0


def test_gain_larger_than_replica_range_is_clear_improvement() -> None:
    result = compare_with_noise_band(
        candidate="new",
        candidate_score=95.0,
        anchor="ASUB-001",
        anchor_score=86.040,
        replicate_scores=(77.850, 86.040),
    )
    assert result.relation == "clear_improvement"
    assert result.conservative_advantage == pytest.approx((95.0 - 86.040) - 8.190)


def test_loss_larger_than_replica_range_is_clear_regression() -> None:
    result = compare_with_noise_band(
        candidate="new",
        candidate_score=70.0,
        anchor="ASUB-001",
        anchor_score=86.040,
        replicate_scores=(77.850, 86.040),
    )
    assert result.relation == "clear_regression"


def test_noise_band_requires_true_replicates() -> None:
    with pytest.raises(ValueError):
        empirical_noise_band((86.040,))
