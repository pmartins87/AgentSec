from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-018-public-frontier-v8-interface-only-full-prefix"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_public_v8_interface_only", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


def test_default_archive_is_full_and_unique() -> None:
    archive = DRAFT._emit(DRAFT.DEFAULT_N)
    assert DRAFT.DEFAULT_N == DRAFT.MAX_FINDINGS == 2000
    assert len(archive) == 2000
    assert len({tuple(item.user_messages) for item in archive}) == 2000


def test_every_candidate_is_one_message_and_ordinary_text() -> None:
    archive = DRAFT._emit(50)
    for item in archive:
        assert len(item.user_messages) == 1
        message = item.user_messages[0]
        assert "http.post" in message
        assert DRAFT.PAYLOAD in message
        assert "<|" not in message
        assert "tool_call" not in message


def test_urls_are_distinct() -> None:
    messages = [DRAFT._message(i) for i in range(2000)]
    assert len(set(messages)) == 2000


def test_hard_cap_is_respected() -> None:
    algo = DRAFT.AttackAlgorithm({"n_candidates": 5000, "hard_n_cap": 137})
    archive = algo.run(None, None)
    assert len(archive) == 137


def test_minimum_requested_count_still_emits_one_candidate() -> None:
    assert len(DRAFT._emit(0)) == 1
