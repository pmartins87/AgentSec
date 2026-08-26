"""Bounded CI-only red-team smoke for the SDK gym evaluation path.

This is not a competition candidate. Production attacks intentionally use most of
AttackRunConfig.time_budget_s, which makes a hard 10-second CI gateway smoke flaky
at the deadline boundary. This fixture returns immediately so CI tests the SDK
plumbing independently of throughput scheduling.
"""

from __future__ import annotations

from typing import Any, Mapping

try:
    from aicomp_sdk.attacks.contracts import AttackAlgorithmBase, AttackCandidate, AttackRunConfig
except Exception:
    try:
        from aicomp_sdk.attacks import AttackAlgorithmBase, AttackCandidate, AttackRunConfig
    except Exception:
        from aicomp_sdk import AttackAlgorithmBase, AttackCandidate, AttackRunConfig


class AttackAlgorithm(AttackAlgorithmBase):
    def __init__(self, config: Mapping[str, Any] | None = None) -> None:
        try:
            super().__init__(config)
        except Exception:
            try:
                super().__init__()
            except Exception:
                pass

    def run(
        self,
        env: Any,
        config: "AttackRunConfig | None" = None,
    ) -> list[AttackCandidate]:
        del env, config
        return [AttackCandidate.from_messages(("Say OK.",))]
