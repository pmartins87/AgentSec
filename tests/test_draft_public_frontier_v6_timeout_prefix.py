from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-013-public-frontier-v6-timeout-prefix"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_public_frontier_v6", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def _obs(name: str, hits: int, elapsed: float):
    return DRAFT._Observation(name, hits, elapsed)


def test_full_prefix_is_exactly_replay_cap_and_unique() -> None:
    archive = DRAFT._emit_arm(DRAFT.ARM_BY_NAME["plain1"], 9999)
    assert len(archive) == DRAFT.MAX_FINDINGS == 2000
    chains = [tuple(candidate.user_messages) for candidate in archive]
    assert len(set(chains)) == len(chains)


def test_raw_score_proxy_for_multipost() -> None:
    assert [DRAFT._raw_score_proxy(i) for i in range(6)] == [0, 18, 34, 50, 66, 82]


def test_fast_row_never_uses_harmony_or_forge() -> None:
    assert [arm.name for arm in DRAFT._active_arms(8, slow_row=False)] == ["plain1"]


def test_slow_row_hop_cap_filters_forged_arms() -> None:
    assert [arm.name for arm in DRAFT._active_arms(3, slow_row=True)] == [
        "plain1",
        "harmony1",
        "forge2",
        "forge3",
    ]
    assert DRAFT._active_arms(8, slow_row=True)[-1].name == "forge5"


def test_unconfirmed_choice_can_identify_probe_leader() -> None:
    active = DRAFT._active_arms(8, slow_row=True)
    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 8.0),
            _obs("harmony1", 1, 7.0),
            _obs("forge2", 2, 12.0),
            _obs("forge3", 3, 18.0),
            _obs("forge4", 4, 24.0),
            _obs("forge5", 5, 27.0),
        ],
        active,
        require_confirmation=False,
    )
    assert winner is not None
    assert winner.name == "forge5"


def test_nonplain_requires_two_positive_observations_when_confirmed() -> None:
    active = DRAFT._active_arms(8, slow_row=True)
    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 8.0),
            _obs("plain1", 1, 8.2),
            _obs("forge5", 5, 20.0),
        ],
        active,
        require_confirmation=True,
    )
    assert winner is not None
    assert winner.name == "plain1"

    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 8.0),
            _obs("plain1", 1, 8.2),
            _obs("forge5", 5, 20.0),
            _obs("forge5", 5, 21.0),
        ],
        active,
        require_confirmation=True,
    )
    assert winner is not None
    assert winner.name == "forge5"


def test_nonplain_must_beat_plain_by_configured_margin() -> None:
    active = DRAFT._active_arms(8, slow_row=True)
    rows = [
        _obs("plain1", 1, 10.0),
        _obs("plain1", 1, 10.0),
        _obs("forge2", 2, 18.0),
        _obs("forge2", 2, 18.0),
    ]
    # plain = 1.8 raw/s; forge2 ~= 1.889 raw/s: enough for 1.04, not 1.06.
    winner = DRAFT._choose_arm(
        rows,
        active,
        require_confirmation=True,
        min_nonplain_value_ratio=1.04,
    )
    assert winner is not None
    assert winner.name == "forge2"

    winner = DRAFT._choose_arm(
        rows,
        active,
        require_confirmation=True,
        min_nonplain_value_ratio=1.06,
    )
    assert winner is not None
    assert winner.name == "plain1"


def test_messages_are_bounded_and_domains_vary() -> None:
    seen: set[str] = set()
    for index in range(300):
        for arm in DRAFT.ARMS:
            message = DRAFT._message(index, arm)
            assert 0 < len(message) <= 2000
            assert message not in seen
            seen.add(message)
    assert len(seen) == 300 * len(DRAFT.ARMS)
