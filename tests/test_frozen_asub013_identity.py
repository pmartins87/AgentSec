from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = (
    ROOT
    / "submissions"
    / "DRAFT-ASUB-020-public-frontier-v9-baseline-exact-full-prefix"
    / "attack.py"
)
FROZEN = (
    ROOT
    / "submissions"
    / "ASUB-20260829-013-public-frontier-v9-baseline-exact-full-prefix"
    / "attack.py"
)


def test_frozen_asub013_is_byte_identical_to_green_draft020() -> None:
    assert FROZEN.read_bytes() == DRAFT.read_bytes()
