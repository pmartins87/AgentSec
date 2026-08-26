from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-011-public-frontier-v4-paired-hops"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_public_frontier_v4", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
ASUB011 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ASUB011
SPEC.loader.exec_module(ASUB011)


def test_static_archive_is_unique_and_replay_bounded() -> None:
    archive = ASUB011._emit_static(2_500)
    assert len(archive) == ASUB011.HARD_N_CAP == 2_000
    chains = [tuple(candidate.user_messages) for candidate in archive]
    assert len(set(chains)) == len(chains)
    assert all(len(chain) == 1 for chain in chains)
    assert all(len(chain[0]) <= 2_000 for chain in chains)


def test_live_ratio_uses_medians_and_safety_multiplier() -> None:
    scale = ASUB011._calibrated_replay_scale(
        [4.0, 5.0, 6.0],
        [6.0, 6.5, 7.0],
        min_fires=2,
        safety_mult=1.10,
        floor=1.0,
        ceiling=3.0,
    )
    # median(full)/median(one) = 6.5/5 = 1.3; *1.10 = 1.43
    assert scale is not None
    assert abs(scale - 1.43) < 1e-9


def test_ratio_requires_positive_evidence_in_both_hop_groups() -> None:
    assert ASUB011._calibrated_replay_scale([4.0], [6.0, 7.0], min_fires=2) is None
    assert ASUB011._calibrated_replay_scale([4.0, 5.0], [6.0], min_fires=2) is None


def test_ratio_is_clamped_to_conservative_floor_and_ceiling() -> None:
    low = ASUB011._calibrated_replay_scale(
        [5.0, 5.0],
        [5.0, 5.0],
        min_fires=2,
        safety_mult=1.0,
        floor=1.15,
        ceiling=2.0,
    )
    high = ASUB011._calibrated_replay_scale(
        [2.0, 2.0],
        [10.0, 10.0],
        min_fires=2,
        safety_mult=1.10,
        floor=1.15,
        ceiling=2.0,
    )
    assert low == 1.15
    assert high == 2.0


def test_two_stage_budget_and_ratio_defaults_are_conservative() -> None:
    assert 0 < ASUB011.PRIMARY_REPLAY_FRAC < ASUB011.BACKFILL_REPLAY_FRAC < 1
    assert 0 < ASUB011.PRIMARY_WALL_FRAC < ASUB011.BACKFILL_WALL_FRAC < 1
    assert ASUB011.RATIO_SAFETY_MULT >= 1.0
    assert 1.0 <= ASUB011.RATIO_FLOOR <= ASUB011.RATIO_CEILING
    assert ASUB011.PAIR_ONE_HOP_N >= ASUB011.PAIR_MIN_FIRES
    assert ASUB011.PAIR_FULL_HOP_N >= ASUB011.PAIR_MIN_FIRES


def test_unique_domains_cover_full_replay_cap() -> None:
    urls = [ASUB011._url(index) for index in range(ASUB011.HARD_N_CAP)]
    assert len(set(urls)) == ASUB011.HARD_N_CAP
