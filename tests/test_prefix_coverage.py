from __future__ import annotations

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
LANES = {
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
COUNTS = {name: 1 for name in FAMILIES}


def test_lane_first_covers_all_six_lanes_in_first_six_positions() -> None:
    order = lane_first_order(FAMILIES, LANES, COUNTS)
    curve = coverage_curve(order, LANES)
    assert curve[5].distinct_lanes == 6


def test_family_first_has_only_four_lanes_after_six_positions() -> None:
    order = family_first_order(FAMILIES, COUNTS)
    curve = coverage_curve(order, LANES)
    assert curve[5].distinct_lanes == 4


def test_lane_first_preserves_all_families_exactly_once() -> None:
    order = lane_first_order(FAMILIES, LANES, COUNTS)
    assert len(order) == len(FAMILIES)
    assert set(order) == set(FAMILIES)
    assert len(set(order)) == len(order)


def test_lane_first_improves_early_lane_coverage_auc() -> None:
    family_curve = coverage_curve(family_first_order(FAMILIES, COUNTS), LANES)
    lane_curve = coverage_curve(lane_first_order(FAMILIES, LANES, COUNTS), LANES)
    assert lane_coverage_auc(lane_curve) > lane_coverage_auc(family_curve)


def test_inactive_family_is_skipped_without_breaking_lane_rounds() -> None:
    counts = dict(COUNTS)
    counts["direct_synonym"] = 0
    order = lane_first_order(FAMILIES, LANES, counts)
    assert "direct_synonym" not in order
    assert "direct_launder" in order[:6]
    assert len({LANES[name] for name in order[:6]}) == 6
