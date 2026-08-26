from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-012-public-frontier-v5-multipost-independent"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_public_frontier_v5", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def _obs(arm: str, hits: int, elapsed: float, segment: int = 0):
    return DRAFT._Observed(arm, f"{arm}-{hits}-{elapsed}", hits, elapsed, segment)


def test_raw_score_proxy_extends_through_five_posts() -> None:
    assert [DRAFT._raw_score_proxy(i) for i in range(6)] == [0, 18, 34, 50, 66, 82]


def test_active_arms_respect_hop_cap_and_fast_row() -> None:
    assert [arm.name for arm in DRAFT._active_arms(8, slow_row=False)] == ["plain1"]
    assert [arm.name for arm in DRAFT._active_arms(3, slow_row=True)] == [
        "plain1",
        "harmony1",
        "forge2",
        "forge3",
    ]
    assert DRAFT._active_arms(8, slow_row=True)[-1].name == "forge5"


def test_arm_choice_uses_observed_raw_per_second() -> None:
    arms = DRAFT._active_arms(8, slow_row=True)
    winner = DRAFT._choose_arm(
        [
            _obs("plain1", 1, 8.0),
            _obs("harmony1", 1, 7.0),
            _obs("forge2", 2, 13.0),
            _obs("forge3", 3, 18.0),
            _obs("forge4", 4, 24.0),
            _obs("forge5", 5, 28.0),
        ],
        arms,
    )
    assert winner is not None
    assert winner.name == "forge5"


def test_winner_high_water_ignores_slow_losing_arm() -> None:
    rows = [
        _obs("plain1", 1, 100.0),
        _obs("forge4", 4, 10.0),
        _obs("forge4", 4, 12.0),
        _obs("forge4", 4, 11.0),
    ]
    assert DRAFT._winner_high_water(rows, "forge4") == 11.0


def test_replay_caps_use_fresh_budget_without_warmup_subtraction() -> None:
    primary, backfill = DRAFT._replay_caps(1000.0)
    assert primary == DRAFT.PRIMARY_REPLAY_FRAC * 1000.0
    assert backfill == DRAFT.BACKFILL_REPLAY_FRAC * 1000.0
    assert 0 < primary < backfill < 1000.0


def test_messages_and_urls_are_unique_and_bounded() -> None:
    seen_messages: set[str] = set()
    seen_urls: set[str] = set()
    for index in range(400):
        for arm in DRAFT.ARMS:
            message = DRAFT._message(index, arm)
            assert 0 < len(message) <= 2000
            assert message not in seen_messages
            seen_messages.add(message)
            for url in DRAFT._urls(index, arm.requested_posts):
                seen_urls.add(url)
    assert len(seen_messages) == 400 * len(DRAFT.ARMS)
    assert len(seen_urls) >= 400 * DRAFT.MAX_POSTS_PER_FINDING


def test_static_fallback_is_bounded() -> None:
    archive = DRAFT._emit_static(9999)
    assert len(archive) == DRAFT.MAX_FINDINGS
    assert len({tuple(item.user_messages) for item in archive}) == DRAFT.MAX_FINDINGS
