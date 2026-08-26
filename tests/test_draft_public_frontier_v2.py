"""Mechanical checks for DRAFT-ASUB-006 public-frontier v2."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from aicomp_sdk.attacks import AttackRunConfig


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "submissions"
    / "DRAFT-ASUB-006-public-frontier-v2"
    / "attack.py"
)
SPEC = importlib.util.spec_from_file_location("agentsec_draft_frontier_v2", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
DRAFT = importlib.util.module_from_spec(SPEC)
# Dataclasses resolves postponed annotations through sys.modules during class
# decoration. Register a dynamically loaded module exactly like a normal import.
sys.modules[SPEC.name] = DRAFT
SPEC.loader.exec_module(DRAFT)


class _FrameOnlyEnv:
    def __init__(self) -> None:
        self.last_message = ""
        self.messages: list[str] = []

    def reset(self) -> None:
        self.last_message = ""

    def interact(self, message: str, max_tool_hops: int | None = None) -> None:
        del max_tool_hops
        self.last_message = message
        self.messages.append(message)

    def export_trace_dict(self) -> dict:
        if DRAFT.HARMONY_SUFFIX not in self.last_message:
            return {"user_messages": [self.last_message], "tool_events": []}
        return {
            "user_messages": [self.last_message],
            "tool_events": [
                {
                    "name": "http.post",
                    "ok": True,
                    "args": {"url": "http://aa.co", "data": DRAFT.PAYLOAD},
                    "side_effect": "SHARE",
                    "scope": "external",
                    "source": "tool",
                    "output": "ok",
                    "error": "",
                }
            ],
        }


def test_static_portfolio_is_unique_and_within_limits() -> None:
    findings = DRAFT._emit_static(2_000)
    assert len(findings) == 2_000
    messages = [candidate.user_messages[0] for candidate in findings]
    assert len(set(messages)) == 2_000
    assert all(len(message) <= 2_000 for message in messages)

    urls = [DRAFT._url(index) for index in range(2_000)]
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


def test_public_terminal_wording_is_the_compact_anchor() -> None:
    message = DRAFT._message(0, DRAFT.PLAIN_TEMPLATE)
    assert message.endswith("Then say OK.")
    assert "answer OK only" not in message
    assert DRAFT.PAYLOAD in message
    assert "http.post" in message


def test_none_env_fallback_and_static_override() -> None:
    attack = DRAFT.AttackAlgorithm()
    fallback = attack.run(None, AttackRunConfig(time_budget_s=1.0, max_steps=1))
    assert len(fallback) == DRAFT.FALLBACK_N

    exact = DRAFT.AttackAlgorithm({"n_candidates": 7}).run(
        None,
        AttackRunConfig(time_budget_s=1.0, max_steps=1),
    )
    assert len(exact) == 7


def test_template_race_selects_frame_when_only_frame_fires() -> None:
    env = _FrameOnlyEnv()
    attack = DRAFT.AttackAlgorithm(
        {
            "slowest_seed_s": 0.001,
            "slowest_mult": 1.0,
            "replay_safe_frac": 0.99,
            "replay_cost_coef": 1.0,
        }
    )
    findings = attack.run(
        env,
        AttackRunConfig(time_budget_s=10.0, max_steps=7, max_tool_hops=8),
    )

    # One warm-up + 6 classifier probes + one main-fill probe.
    assert len(env.messages) == 8
    assert DRAFT.HARMONY_SUFFIX not in env.messages[1]
    assert DRAFT.HARMONY_SUFFIX in env.messages[4]
    assert DRAFT.HARMONY_SUFFIX in env.messages[-1]
    assert findings
    assert all(DRAFT.HARMONY_SUFFIX in candidate.user_messages[0] for candidate in findings)
