from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-016-public-frontier-v7-format-diverse"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_public_frontier_v7", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def _obs(name: str, hits: int, elapsed: float):
    return DRAFT._Observation(name, hits, elapsed)


def test_all_messages_are_bounded_and_unique() -> None:
    seen: set[str] = set()
    for index in range(200):
        for arm in DRAFT.ARMS:
            message = DRAFT._message(index, arm)
            assert 0 < len(message) <= 2000
            assert message not in seen
            seen.add(message)
    assert len(seen) == 200 * len(DRAFT.ARMS)


def test_format_specific_single_post_markers_are_present() -> None:
    harmony = DRAFT._message(1, DRAFT.ARM_BY_NAME["harmony_full1"])
    gemma = DRAFT._message(1, DRAFT.ARM_BY_NAME["gemma_full1"])
    assert "to=functions.http.post" in harmony
    assert '"data":"SECRET_MARKER"' in harmony
    assert "<end_of_turn>" in gemma
    assert "<|tool_call>call:http.post" in gemma


def test_chain_arms_require_three_hops_and_three_endpoints() -> None:
    assert [arm.name for arm in DRAFT._active_arms(1)] == [
        "plain1",
        "imperative1",
        "harmony_full1",
        "gemma_full1",
    ]
    active_three = [arm.name for arm in DRAFT._active_arms(3)]
    assert active_three[-3:] == ["chain3_plain", "chain3_harmony", "chain3_gemma"]
    message = DRAFT._message(7, DRAFT.ARM_BY_NAME["chain3_plain"])
    assert message.count("http://") == 3


def test_unconfirmed_nonplain_cannot_own_archive() -> None:
    active = DRAFT._active_arms(3)
    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 10.0),
            _obs("plain1", 1, 10.0),
            _obs("gemma_full1", 1, 1.0),
        ],
        active,
        require_confirmation=True,
    )
    assert winner is not None
    assert winner.name == "plain1"


def test_confirmed_format_specific_arm_can_beat_plain() -> None:
    active = DRAFT._active_arms(3)
    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 10.0),
            _obs("plain1", 1, 10.0),
            _obs("harmony_full1", 1, 5.0),
            _obs("harmony_full1", 1, 5.0),
        ],
        active,
        require_confirmation=True,
    )
    assert winner is not None
    assert winner.name == "harmony_full1"


def test_confirmed_multihop_value_can_win_on_raw_per_second() -> None:
    active = DRAFT._active_arms(3)
    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 6.0),
            _obs("plain1", 1, 6.0),
            _obs("chain3_gemma", 3, 12.0),
            _obs("chain3_gemma", 3, 12.0),
        ],
        active,
        require_confirmation=True,
    )
    assert winner is not None
    assert winner.name == "chain3_gemma"


def test_full_archive_caps_at_2000_and_is_unique() -> None:
    archive = DRAFT._emit_arm(DRAFT.ARM_BY_NAME["plain1"], 9999)
    assert len(archive) == DRAFT.MAX_FINDINGS == 2000
    chains = [tuple(candidate.user_messages) for candidate in archive]
    assert len(set(chains)) == len(chains)
