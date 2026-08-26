"""Interpret AgentSec hosted public scores.

Public leaderboard mode assumes the empirically documented Kaggle aggregation:
mean(gpt_oss_public, gemma_public).

Examples:
  python scripts/interpret_hosted_score.py asub001 56.60
  python scripts/interpret_hosted_score.py asub002 1.20
  python scripts/interpret_hosted_score.py duplicate 49.77 56.60
  python scripts/interpret_hosted_score.py asub001-row 12.33 --candidates 180
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.hosted_evidence import (  # noqa: E402
    compare_duplicate_scores,
    infer_asub001,
    infer_asub001_row,
    infer_asub002,
    infer_asub002_row,
)


def _print_lb(result) -> None:
    print(result.submission)
    print(f"public_lb_score:                   {result.public_lb_score:.6f}")
    print(f"raw_per_successful_hit:            {result.raw_per_hit:.3f}")
    print(f"equiv_mean_hits_per_public_row:   {result.equivalent_mean_hits_per_public_row:.3f}")
    print(f"equiv_total_hits_two_public_rows: {result.equivalent_total_hits_across_public_rows:.3f}")
    print(f"nearest_half_mean_hits:            {result.nearest_half_mean_hits:.1f}")
    print(f"score_if_nearest_half:             {result.score_if_nearest_half:.6f}")
    print(f"display_rounding_delta:            {result.score_residual:+.6f}")
    if result.capped:
        print("note: public score is capped; implied hit volumes are lower bounds.")


def _print_row(result) -> None:
    print(result.submission)
    print(f"row_score:               {result.row_score:.6f}")
    print(f"raw_score_estimate:      {result.raw_score_estimate:.3f}")
    print(f"hit_count_estimate:      {result.hit_count_estimate:.3f}")
    print(f"nearest_integer_hits:    {result.nearest_integer_hits}")
    print(f"nearest_integer_score:   {result.score_if_nearest_integer:.6f}")
    print(f"display_rounding_delta:  {result.score_residual:+.6f}")
    if result.completion_ratio is not None:
        print(f"candidate_completion:    {result.completion_ratio:.2%}")
    if result.capped:
        print("note: row score is capped; raw/hit counts are lower bounds.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "lane",
        choices=("asub001", "asub002", "duplicate", "asub001-row", "asub002-row"),
    )
    parser.add_argument("scores", nargs="+", type=float)
    parser.add_argument("--candidates", type=int, default=None)
    args = parser.parse_args()

    if args.lane == "asub001":
        if len(args.scores) != 1:
            parser.error("asub001 requires exactly one public leaderboard score")
        _print_lb(infer_asub001(args.scores[0]))
        return
    if args.lane == "asub002":
        if len(args.scores) != 1:
            parser.error("asub002 requires exactly one public leaderboard score")
        _print_lb(infer_asub002(args.scores[0]))
        return
    if args.lane == "asub001-row":
        if len(args.scores) != 1:
            parser.error("asub001-row requires exactly one row score")
        _print_row(infer_asub001_row(args.scores[0], candidate_count=args.candidates))
        return
    if args.lane == "asub002-row":
        if len(args.scores) != 1:
            parser.error("asub002-row requires exactly one row score")
        _print_row(infer_asub002_row(args.scores[0], candidate_count=args.candidates))
        return

    result = compare_duplicate_scores(args.scores)
    print(result.submission)
    print("scores:                         " + ", ".join(f"{value:.6f}" for value in result.scores))
    print("equiv_mean_hits:                " + ", ".join(f"{value:.3f}" for value in result.equivalent_mean_hits))
    print(f"score_range:                    {result.score_range:.6f}")
    print(f"equiv_mean_hit_range:           {result.equivalent_mean_hit_range:.3f}")
    print(f"score_mean:                     {result.score_mean:.6f}")
    print(f"equiv_mean_hit_mean:            {result.equivalent_mean_hit_mean:.3f}")


if __name__ == "__main__":
    main()
