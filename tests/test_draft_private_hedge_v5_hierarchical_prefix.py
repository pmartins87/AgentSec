from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-017-private-hedge-v5-hierarchical-prefix"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_private_hedge_v5", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def test_default_archive_is_full_and_unique() -> None:
    archive = DRAFT._emit_portfolio(DRAFT._fallback_winners(), DRAFT.DEFAULT_N)
    assert DRAFT.DEFAULT_N == DRAFT.MAX_FINDINGS == 2000
    assert len(archive) == 2000
    assert len({tuple(item.user_messages) for item in archive}) == 2000


def test_first_six_positions_cover_all_six_active_lanes() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    order = DRAFT._interleave(counts)
    lane_by_name = {family.name: family.lane for family in DRAFT.FAMILIES}
    assert len({lane_by_name[name] for name in order[:6]}) == 6


def test_first_eleven_positions_cover_every_active_family_once() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    order = DRAFT._interleave(counts)
    prelude = order[: len(active)]
    assert set(prelude) == set(active)
    assert len(set(prelude)) == len(active)


def test_hierarchical_interleave_preserves_exact_scaled_counts() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    order = DRAFT._interleave(counts)
    assert len(order) == 2000
    assert Counter(order) == Counter(counts)


def test_hierarchical_prefix_handles_dropped_family() -> None:
    active = [
        "public_exfil",
        "direct_launder",
        "web_email",
        "web_http",
        "web_shell",
        "web_write",
    ]
    counts = DRAFT._scaled_counts(active, 137)
    order = DRAFT._interleave(counts)
    lane_by_name = {family.name: family.lane for family in DRAFT.FAMILIES}
    assert len({lane_by_name[name] for name in order[:6]}) == 6
    assert Counter(order) == Counter(counts)


def test_neutral_tail_remains_authorization_token_free() -> None:
    for family in DRAFT.FAMILIES:
        messages = DRAFT._build_messages(family, 123, 0)
        if len(messages) == 2:
            last = messages[-1].casefold()
            assert not any(word in last for word in DRAFT.ALL_AUTH_WORDS)
