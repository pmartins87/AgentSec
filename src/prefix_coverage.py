"""Prefix-coverage diagnostics for mixed AgentSec private portfolios.

These helpers operate only on abstract family/lane labels. They are used to
compare replay orderings under the published prefix-preserving replay-timeout
semantics without making any claim about the hidden private guardrail.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class PrefixCoverage:
    prefix_size: int
    distinct_families: int
    distinct_lanes: int


def family_first_order(families: Sequence[str], counts: Mapping[str, int]) -> list[str]:
    """Emit one of every active family in declaration order."""
    return [name for name in families if int(counts.get(name, 0)) > 0]


def lane_first_order(
    families: Sequence[str],
    family_to_lane: Mapping[str, str],
    counts: Mapping[str, int],
) -> list[str]:
    """Cover every active lane before repeating a lane, then cover remaining families.

    Within a lane, family declaration order is preserved. Lanes inherit the order
    of their first active family, keeping the schedule deterministic.
    """

    lane_families: dict[str, list[str]] = defaultdict(list)
    lane_order: list[str] = []
    seen_lanes: set[str] = set()

    for family in families:
        if int(counts.get(family, 0)) <= 0:
            continue
        lane = str(family_to_lane[family])
        lane_families[lane].append(family)
        if lane not in seen_lanes:
            seen_lanes.add(lane)
            lane_order.append(lane)

    if not lane_order:
        return []

    out: list[str] = []
    depth = 0
    while True:
        emitted_this_round = False
        for lane in lane_order:
            rows = lane_families[lane]
            if depth < len(rows):
                out.append(rows[depth])
                emitted_this_round = True
        if not emitted_this_round:
            break
        depth += 1
    return out


def coverage_curve(
    order: Sequence[str],
    family_to_lane: Mapping[str, str],
) -> tuple[PrefixCoverage, ...]:
    seen_families: set[str] = set()
    seen_lanes: set[str] = set()
    rows: list[PrefixCoverage] = []
    for index, family in enumerate(order, start=1):
        seen_families.add(family)
        seen_lanes.add(str(family_to_lane[family]))
        rows.append(
            PrefixCoverage(
                prefix_size=index,
                distinct_families=len(seen_families),
                distinct_lanes=len(seen_lanes),
            )
        )
    return tuple(rows)


def lane_coverage_auc(curve: Sequence[PrefixCoverage]) -> int:
    """Discrete area under distinct-lane-vs-prefix curve; larger is better."""
    return sum(row.distinct_lanes for row in curve)
