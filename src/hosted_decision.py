"""Decision helpers for noisy hosted public scores.

These helpers deliberately avoid claiming a statistical confidence interval from
only a handful of duplicate runs.  Instead they use an *empirical practical
noise band*: the observed score range of byte-identical hosted replicas.

A new candidate must clear that band before a single hosted result is treated as
strong evidence of a real public-frontier improvement.  Scores inside the band
remain useful telemetry but are treated as practically unresolved.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import fmean
from typing import Sequence


@dataclass(frozen=True)
class NoiseBand:
    replicate_scores: tuple[float, ...]
    score_min: float
    score_max: float
    score_mean: float
    empirical_range: float


@dataclass(frozen=True)
class HostedComparison:
    candidate: str
    candidate_score: float
    anchor: str
    anchor_score: float
    score_delta: float
    empirical_noise_range: float
    conservative_advantage: float
    relation: str


def empirical_noise_band(scores: Sequence[float]) -> NoiseBand:
    values = tuple(float(value) for value in scores)
    if len(values) < 2:
        raise ValueError("at least two byte-identical replicate scores are required")
    if any(value < 0 for value in values):
        raise ValueError("scores must be non-negative")
    return NoiseBand(
        replicate_scores=values,
        score_min=min(values),
        score_max=max(values),
        score_mean=fmean(values),
        empirical_range=max(values) - min(values),
    )


def compare_with_noise_band(
    *,
    candidate: str,
    candidate_score: float,
    anchor: str,
    anchor_score: float,
    replicate_scores: Sequence[float],
) -> HostedComparison:
    """Compare one hosted score to an anchor using the empirical replica range.

    relation values:
    - ``clear_improvement``: candidate beats anchor by more than the observed
      byte-identical replica range;
    - ``clear_regression``: candidate trails anchor by more than that range;
    - ``noise_band_overlap``: the single-run difference is no larger than the
      empirical range and should not be treated as decisive by itself.
    """

    band = empirical_noise_band(replicate_scores)
    candidate_value = float(candidate_score)
    anchor_value = float(anchor_score)
    delta = candidate_value - anchor_value
    margin = abs(delta) - band.empirical_range
    if delta > band.empirical_range:
        relation = "clear_improvement"
        conservative_advantage = margin
    elif delta < -band.empirical_range:
        relation = "clear_regression"
        conservative_advantage = -margin
    else:
        relation = "noise_band_overlap"
        conservative_advantage = 0.0
    return HostedComparison(
        candidate=str(candidate),
        candidate_score=candidate_value,
        anchor=str(anchor),
        anchor_score=anchor_value,
        score_delta=delta,
        empirical_noise_range=band.empirical_range,
        conservative_advantage=conservative_advantage,
        relation=relation,
    )
