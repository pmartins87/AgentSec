#!/usr/bin/env python3
"""Select two complementary final submissions from explicit scenario projections.

Input JSON schema:
{
  "candidates": {
    "ASUB-005": {"scenario_a": 90.0, "scenario_b": 10.0},
    "ASUB-006": {"scenario_a": 55.0, "scenario_b": 65.0}
  },
  "weights": {"scenario_a": 1.0, "scenario_b": 1.0}
}

Scenario scores may be raw score, normalized score, or another common utility
scale as long as every candidate uses the same scale. They are planning inputs,
not claims about the hidden Kaggle evaluator.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.final_pair_selector import CandidateProfile, choose_final_pair


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    raw_candidates = payload.get("candidates")
    if not isinstance(raw_candidates, dict) or len(raw_candidates) < 2:
        raise SystemExit("input must contain at least two candidate profiles")

    candidates = [
        CandidateProfile(str(name), dict(scores))
        for name, scores in raw_candidates.items()
    ]
    weights = payload.get("weights")
    plan = choose_final_pair(
        candidates,
        scenario_weights=dict(weights) if isinstance(weights, dict) else None,
    )

    print(
        json.dumps(
            {
                "first": plan.first,
                "second": plan.second,
                "max_regret": plan.max_regret,
                "worst_case_best": plan.worst_case_best,
                "mean_best": plan.mean_best,
                "scenario_best": dict(plan.scenario_best),
            },
            sort_keys=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
