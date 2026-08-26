"""Interpret an AgentSec hosted public canary score.

Examples:
  python scripts/interpret_hosted_score.py asub001 4.50
  python scripts/interpret_hosted_score.py asub002 1.20 --candidates 40
  python scripts/interpret_hosted_score.py duplicate 4.50 5.40
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.hosted_evidence import compare_duplicate_scores, infer_asub001, infer_asub002  # noqa: E402


def _print_lane(result) -> None:
    print(result.submission)
    print(f"normalized_score:       {result.normalized_score:.6f}")
    print(f"raw_score_estimate:     {result.raw_score_estimate:.3f}")
    print(f"hit_count_estimate:     {result.hit_count_estimate:.3f}")
    print(f"nearest_integer_hits:   {result.nearest_integer_hits}")
    print(f"nearest_integer_score:  {result.score_if_nearest_integer:.6f}")
    print(f"display_rounding_delta: {result.score_residual:+.6f}")
    if result.completion_ratio is not None:
        print(f"candidate_completion:   {result.completion_ratio:.2%}")
    if result.capped:
        print("note: score is capped at 1000; raw/hit counts are lower bounds.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lane", choices=("asub001", "asub002", "duplicate"))
    parser.add_argument("scores", nargs="+", type=float)
    parser.add_argument("--candidates", type=int, default=None)
    args = parser.parse_args()
    if args.lane == "asub001":
        if len(args.scores) != 1:
            parser.error("asub001 requires exactly one score")
        _print_lane(infer_asub001(args.scores[0], candidate_count=args.candidates))
        return
    if args.lane == "asub002":
        if len(args.scores) != 1:
            parser.error("asub002 requires exactly one score")
        _print_lane(infer_asub002(args.scores[0], candidate_count=args.candidates))
        return
    result = compare_duplicate_scores(args.scores)
    print(result.submission)
    print("scores:                 " + ", ".join(f"{value:.6f}" for value in result.scores))
    print("inferred_hits:          " + ", ".join(f"{value:.3f}" for value in result.inferred_hits))
    print(f"score_range:            {result.score_range:.6f}")
    print(f"equivalent_hit_range:   {result.hit_range:.3f}")
    print(f"score_mean:             {result.score_mean:.6f}")
    print(f"hit_mean:               {result.hit_mean:.3f}")


if __name__ == "__main__":
    main()
