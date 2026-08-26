from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_asub007_is_exact_frozen_copy_of_green_draft() -> None:
    draft = ROOT / "submissions" / "DRAFT-ASUB-013-public-frontier-v6-timeout-prefix" / "attack.py"
    frozen = ROOT / "submissions" / "ASUB-20260826-007-public-frontier-v6-timeout-prefix" / "attack.py"
    assert frozen.read_bytes() == draft.read_bytes()


def test_asub008_is_exact_frozen_copy_of_green_draft() -> None:
    draft = ROOT / "submissions" / "DRAFT-ASUB-014-private-hedge-v3-timeout-prefix" / "attack.py"
    frozen = ROOT / "submissions" / "ASUB-20260826-008-private-hedge-v3-timeout-prefix" / "attack.py"
    assert frozen.read_bytes() == draft.read_bytes()


def test_asub009_is_exact_frozen_copy_of_green_draft() -> None:
    draft = ROOT / "submissions" / "DRAFT-ASUB-015-private-hedge-v4-coverage-prefix" / "attack.py"
    frozen = ROOT / "submissions" / "ASUB-20260826-009-private-hedge-v4-coverage-prefix" / "attack.py"
    assert frozen.read_bytes() == draft.read_bytes()


def test_asub010_is_exact_frozen_copy_of_green_draft() -> None:
    draft = ROOT / "submissions" / "DRAFT-ASUB-016-public-frontier-v7-format-diverse" / "attack.py"
    frozen = ROOT / "submissions" / "ASUB-20260826-010-public-frontier-v7-format-diverse" / "attack.py"
    assert frozen.read_bytes() == draft.read_bytes()
