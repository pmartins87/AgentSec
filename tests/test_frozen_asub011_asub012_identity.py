from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_asub011_is_byte_identical_to_green_draft017() -> None:
    frozen = ROOT / "submissions" / "ASUB-20260827-011-private-hedge-v5-hierarchical-prefix" / "attack.py"
    draft = ROOT / "submissions" / "DRAFT-ASUB-017-private-hedge-v5-hierarchical-prefix" / "attack.py"
    assert frozen.read_bytes() == draft.read_bytes()


def test_asub012_is_byte_identical_to_green_draft018() -> None:
    frozen = ROOT / "submissions" / "ASUB-20260827-012-public-frontier-v8-interface-only-full-prefix" / "attack.py"
    draft = ROOT / "submissions" / "DRAFT-ASUB-018-public-frontier-v8-interface-only-full-prefix" / "attack.py"
    assert frozen.read_bytes() == draft.read_bytes()
