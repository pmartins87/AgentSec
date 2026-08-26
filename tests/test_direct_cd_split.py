from __future__ import annotations

import pytest

from src.direct_cd_split import (
    DirectCDStress,
    DEFAULT_STRESSES,
    default_direct_cd_split,
    optimize_direct_cd_split,
)


def test_default_split_preserves_both_shapes_and_exact_quota() -> None:
    split = default_direct_cd_split()
    assert split.synonym == 24
    assert split.launder == 36
    assert split.synonym + split.launder == 60
    assert split.min_ratio == pytest.approx(0.70)
    assert split.mean_ratio > split.min_ratio


def test_default_split_beats_both_pure_extremes_on_worst_case_ratio() -> None:
    split = default_direct_cd_split()
    pure_syn = optimize_direct_cd_split(
        60,
        quantum=60,
        stresses=DEFAULT_STRESSES,
    )
    # quantum=60 considers only the two pure endpoints and picks the better one.
    assert split.min_ratio > pure_syn.min_ratio


def test_symmetric_conflict_prefers_even_split() -> None:
    stresses = (
        DirectCDStress("syn", 1.0, 0.0),
        DirectCDStress("launder", 0.0, 1.0),
    )
    split = optimize_direct_cd_split(60, quantum=6, stresses=stresses)
    assert split.synonym == 30
    assert split.launder == 30
    assert split.min_ratio == pytest.approx(0.5)


def test_rejects_invalid_rate() -> None:
    with pytest.raises(ValueError):
        optimize_direct_cd_split(
            60,
            stresses=(DirectCDStress("bad", 1.1, 0.1),),
        )


def test_rejects_non_dividing_quantum() -> None:
    with pytest.raises(ValueError):
        optimize_direct_cd_split(60, quantum=7)
