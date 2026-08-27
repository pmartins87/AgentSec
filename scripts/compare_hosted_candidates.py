#!/usr/bin/env python3
"""Compare hosted scores against an anchor using an empirical duplicate-run band."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.hosted_decision import compare_with_noise_band, empirical_noise_band


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    parser.add_argument("candidate_score", type=float)
    parser.add_argument("--anchor", default="ASUB-001 best")
    parser.add_argument("--anchor-score", type=float, default=86.040)
    parser.add_argument("--replicate", type=float, action="append", default=None)
    args = parser.parse_args()

    replicates = tuple(args.replicate or (77.850, 86.040))
    band = empirical_noise_band(replicates)
    result = compare_with_noise_band(
        candidate=args.candidate,
        candidate_score=args.candidate_score,
        anchor=args.anchor,
        anchor_score=args.anchor_score,
        replicate_scores=replicates,
    )

    print(f"empirical duplicate band: {band.score_min:.3f}..{band.score_max:.3f}")
    print(f"empirical range: {band.empirical_range:.3f}")
    print(f"candidate: {result.candidate} = {result.candidate_score:.3f}")
    print(f"anchor: {result.anchor} = {result.anchor_score:.3f}")
    print(f"delta: {result.score_delta:+.3f}")
    print(f"relation: {result.relation}")
    print(f"conservative advantage beyond band: {result.conservative_advantage:+.3f}")


if __name__ == "__main__":
    main()
