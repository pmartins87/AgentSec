from __future__ import annotations

from src.hosted_wave import decide_hosted_wave


def test_waits_when_wave_is_incomplete_and_no_rule_is_decisive() -> None:
    result = decide_hosted_wave({"ASUB-007": 88.0})
    assert result.next_candidate is None
    assert result.decision == "wait_for_more_terminal_evidence"


def test_clear_public_improvement_prioritizes_private_complement() -> None:
    result = decide_hosted_wave({"ASUB-007": 95.0})
    assert result.next_candidate == "ASUB-011"
    assert result.decision == "prioritize_private_complement"


def test_competitive_private_telemetry_prioritizes_clean_private_ablation() -> None:
    result = decide_hosted_wave({"ASUB-009": 82.0})
    assert result.next_candidate == "ASUB-011"
    assert result.decision == "test_hierarchical_private_prefix"


def test_all_public_inside_anchor_band_selects_interface_control() -> None:
    result = decide_hosted_wave(
        {
            "ASUB-007": 84.0,
            "ASUB-010-A": 89.0,
            "ASUB-010-B": 87.0,
        }
    )
    assert result.next_candidate == "ASUB-012"
    assert result.decision == "test_interface_only_control"
    assert result.asub010_spread == 2.0


def test_large_asub010_replicate_spread_is_reported() -> None:
    result = decide_hosted_wave(
        {
            "ASUB-007": 70.0,
            "ASUB-009": 70.0,
            "ASUB-010-A": 75.0,
            "ASUB-010-B": 90.0,
        }
    )
    assert result.asub010_spread == 15.0
    assert any("unusually large hosted variance" in line for line in result.rationale)
