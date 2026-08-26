"""Mechanical regressions for the unfrozen DRAFT-ASUB-004 robust mix."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "submissions" / "DRAFT-ASUB-004-robust-mix" / "attack.py"
SPEC = importlib.util.spec_from_file_location("agentsec_draft_asub004", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def test_fallback_portfolio_is_exact_unique_and_bounded() -> None:
    attack = DRAFT.AttackAlgorithm()
    candidates = attack.run(None, None)
    assert len(candidates) == DRAFT.DEFAULT_N
    chains = [tuple(candidate.user_messages) for candidate in candidates]
    assert len(set(chains)) == DRAFT.DEFAULT_N
    assert all(1 <= len(chain) <= 2 for chain in chains)
    assert all(0 < len(message) <= 2_000 for chain in chains for message in chain)
    defaults = {family.name: family.default_count for family in DRAFT.FAMILIES}
    assert sum(defaults.values()) == DRAFT.DEFAULT_N
    assert DRAFT._scaled_counts(tuple(defaults), DRAFT.DEFAULT_N) == defaults


def test_timeout_interleave_frontloads_every_subfamily() -> None:
    counts = {family.name: family.default_count for family in DRAFT.FAMILIES}
    order = DRAFT._interleave(counts)
    assert len(order) == DRAFT.DEFAULT_N
    assert set(order[:60]) == set(counts)
    assert {name: order.count(name) for name in counts} == counts


@pytest.mark.parametrize("chain_style", ("one", "two"))
def test_semantic_families_preserve_literal_authorization_gap(chain_style: str) -> None:
    for family in DRAFT.FAMILIES:
        if family.source is None and chain_style == "two":
            continue
        for variant in range(len(family.action_variants)):
            messages = DRAFT._build_messages(family, 100 + variant, variant, chain_style)
            last = messages[-1].casefold()
            assert not any(word in last for word in family.block_words)
            assert all(0 < len(message) <= 2_000 for message in messages)


def test_public_exfil_arguments_remain_unique_at_replay_scale() -> None:
    family = DRAFT.FAMILY_BY_NAME["public_exfil"]
    messages = [DRAFT._build_messages(family, index, index % len(family.action_variants), "one") for index in range(DRAFT.MAX_FINDINGS)]
    assert len(set(messages)) == DRAFT.MAX_FINDINGS
    assert all(DRAFT.PAYLOAD in chain[0] for chain in messages)


def test_scaled_counts_reallocate_when_a_family_is_dropped() -> None:
    active = tuple(family.name for family in DRAFT.FAMILIES if family.name != "public_exfil")
    counts = DRAFT._scaled_counts(active, DRAFT.DEFAULT_N)
    assert "public_exfil" not in counts
    assert sum(counts.values()) == DRAFT.DEFAULT_N
    assert all(count > 0 for count in counts.values())
