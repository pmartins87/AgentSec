from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-014-private-hedge-v3-timeout-prefix"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_private_hedge_v3", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def test_default_archive_uses_full_replay_cap() -> None:
    archive = DRAFT._emit_portfolio(DRAFT._fallback_winners(), DRAFT.DEFAULT_N)
    assert DRAFT.DEFAULT_N == DRAFT.MAX_FINDINGS == 2000
    assert len(archive) == 2000
    assert len({tuple(item.user_messages) for item in archive}) == 2000


def test_weight_total_remains_original_360_plan() -> None:
    assert DRAFT.PORTFOLIO_WEIGHT_TOTAL == 360
    assert sum(family.default_count for family in DRAFT.FAMILIES) == 360


def test_scaled_counts_fill_exact_target() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    assert sum(counts.values()) == 2000
    assert counts["public_exfil"] > counts["direct_synonym"]
    assert counts["web_email"] == counts["inbox_email"]


def test_interleaving_keeps_every_family_in_early_prefix() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    order = DRAFT._interleave(DRAFT._scaled_counts(active, 2000))
    prefix = set(order[:120])
    assert prefix == set(active)


def test_neutral_tail_stays_authorization_token_free() -> None:
    for family in DRAFT.FAMILIES:
        messages = DRAFT._build_messages(family, 123, 0)
        if len(messages) == 2:
            last = messages[-1].casefold()
            assert not any(word in last for word in DRAFT.ALL_AUTH_WORDS)
