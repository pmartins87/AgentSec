from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-015-private-hedge-v4-coverage-prefix"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_private_hedge_v4", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def test_default_archive_is_full_and_unique() -> None:
    archive = DRAFT._emit_portfolio(DRAFT._fallback_winners(), DRAFT.DEFAULT_N)
    assert DRAFT.DEFAULT_N == DRAFT.MAX_FINDINGS == 2000
    assert len(archive) == 2000
    assert len({tuple(item.user_messages) for item in archive}) == 2000


def test_coverage_prelude_contains_every_active_family_before_repeat() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    order = DRAFT._interleave(counts)
    prelude = order[: len(active)]
    assert prelude == active
    assert len(set(prelude)) == len(active)


def test_coverage_first_interleave_preserves_exact_scaled_counts() -> None:
    active = [family.name for family in DRAFT.FAMILIES]
    counts = DRAFT._scaled_counts(active, 2000)
    order = DRAFT._interleave(counts)
    assert len(order) == 2000
    assert Counter(order) == Counter(counts)


def test_subset_coverage_prelude_handles_dropped_families() -> None:
    active = ["public_exfil", "direct_launder", "web_email", "inbox_write"]
    counts = DRAFT._scaled_counts(active, 137)
    order = DRAFT._interleave(counts)
    assert order[: len(active)] == active
    assert Counter(order) == Counter(counts)


def test_neutral_tail_remains_authorization_token_free() -> None:
    for family in DRAFT.FAMILIES:
        messages = DRAFT._build_messages(family, 123, 0)
        if len(messages) == 2:
            last = messages[-1].casefold()
            assert not any(word in last for word in DRAFT.ALL_AUTH_WORDS)
