#!/usr/bin/env python3
"""Compare ASUB-009 family-first coverage with lane-first hierarchical coverage."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.prefix_coverage import coverage_curve, family_first_order, lane_coverage_auc, lane_first_order


FAMILIES = (
    "public_exfil",
    "direct_synonym",
    "direct_launder",
    "web_email",
    "inbox_email",
    "web_http",
    "inbox_http",
    "web_shell",
    "inbox_shell",
    "web_write",
    "inbox_write",
)
FAMILY_TO_LANE = {
    "public_exfil": "public_exfil",
    "direct_synonym": "direct_cd",
    "direct_launder": "direct_cd",
    "web_email": "semantic_email",
    "inbox_email": "semantic_email",
    "web_http": "semantic_http",
    "inbox_http": "semantic_http",
    "web_shell": "semantic_shell",
    "inbox_shell": "semantic_shell",
    "web_write": "semantic_write",
    "inbox_write": "semantic_write",
}
COUNTS = {
    "public_exfil": 800,
    "direct_synonym": 133,
    "direct_launder": 200,
    "web_email": 334,
    "inbox_email": 333,
    "web_http": 34,
    "inbox_http": 33,
    "web_shell": 34,
    "inbox_shell": 33,
    "web_write": 33,
    "inbox_write": 33,
}


def main() -> None:
    family_order = family_first_order(FAMILIES, COUNTS)
    lane_order = lane_first_order(FAMILIES, FAMILY_TO_LANE, COUNTS)
    family_curve = coverage_curve(family_order, FAMILY_TO_LANE)
    lane_curve = coverage_curve(lane_order, FAMILY_TO_LANE)

    print("ASUB-009 family-first prelude:")
    print("  " + ", ".join(family_order))
    print("Lane-first hierarchical prelude:")
    print("  " + ", ".join(lane_order))
    print()
    print("prefix | family-first lanes | lane-first lanes")
    for left, right in zip(family_curve, lane_curve, strict=True):
        print(f"{left.prefix_size:>6} | {left.distinct_lanes:>18} | {right.distinct_lanes:>16}")
    print()
    print(f"family-first lane-coverage AUC: {lane_coverage_auc(family_curve)}")
    print(f"lane-first   lane-coverage AUC: {lane_coverage_auc(lane_curve)}")


if __name__ == "__main__":
    main()
