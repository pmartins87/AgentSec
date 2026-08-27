from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_PATH = (
    ROOT
    / "submissions"
    / "DRAFT-ASUB-019-private-hedge-v6-hierarchical-calibration"
    / "attack.py"
)
BASE_PATH = (
    ROOT
    / "submissions"
    / "DRAFT-ASUB-017-private-hedge-v5-hierarchical-prefix"
    / "attack.py"
)


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


DRAFT = _load("agentsec_private_hedge_v6", NEW_PATH)
BASE = _load("agentsec_private_hedge_v5_base", BASE_PATH)


def test_default_archive_is_full_unique_and_replay_identical_to_v5() -> None:
    archive = DRAFT._emit_portfolio(DRAFT._fallback_winners(), DRAFT.DEFAULT_N)
    base = BASE._emit_portfolio(BASE._fallback_winners(), BASE.DEFAULT_N)
    assert DRAFT.DEFAULT_N == DRAFT.MAX_FINDINGS == 2000
    assert len(archive) == 2000
    assert len({tuple(item.user_messages) for item in archive}) == 2000
    assert [tuple(item.user_messages) for item in archive] == [tuple(item.user_messages) for item in base]


def test_calibration_first_six_probes_cover_all_six_lanes() -> None:
    schedule = DRAFT._calibration_schedule()
    lane_by_name = {family.name: family.lane for family in DRAFT.FAMILIES}
    first_six = schedule[:6]
    assert all(variant == 0 for _, variant in first_six)
    assert len({lane_by_name[name] for name, _ in first_six}) == 6


def test_calibration_first_pass_covers_every_family_before_variant_one() -> None:
    schedule = DRAFT._calibration_schedule()
    family_names = [family.name for family in DRAFT.FAMILIES]
    first_pass = schedule[: len(family_names)]
    second_pass = schedule[len(family_names):]
    assert len(schedule) == 2 * len(family_names) == 22
    assert [variant for _, variant in first_pass] == [0] * len(family_names)
    assert [variant for _, variant in second_pass] == [1] * len(family_names)
    assert {name for name, _ in first_pass} == set(family_names)
    assert {name for name, _ in second_pass} == set(family_names)


def test_replay_prefix_still_covers_every_lane_then_every_family() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    order = DRAFT._interleave(counts)
    lane_by_name = {family.name: family.lane for family in DRAFT.FAMILIES}
    assert len({lane_by_name[name] for name in order[:6]}) == 6
    assert set(order[: len(active)]) == set(active)
    assert Counter(order) == Counter(counts)


def test_neutral_tail_remains_authorization_token_free() -> None:
    for family in DRAFT.FAMILIES:
        messages = DRAFT._build_messages(family, 123, 0)
        if len(messages) == 2:
            last = messages[-1].casefold()
            assert not any(word in last for word in DRAFT.ALL_AUTH_WORDS)
