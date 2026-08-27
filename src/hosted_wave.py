"""Decision support for the ASUB-007/009/010 hosted wave.

The helper turns terminal public scores into an explicit next-experiment decision
without pretending that the tiny byte-identical replicate sample defines a formal
confidence interval.  It uses the observed ASUB-001 range as a practical noise
band and keeps public-frontier strength separate from private-hedge information
value.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import fmean
from typing import Mapping

from src.hosted_decision import compare_with_noise_band, empirical_noise_band

ANCHOR_NAME = "ASUB-001"
ANCHOR_SCORE = 86.040
ANCHOR_REPLICATES = (77.850, 86.040)
PUBLIC_NAMES = ("ASUB-007", "ASUB-010-A", "ASUB-010-B")
PRIVATE_NAME = "ASUB-009"


@dataclass(frozen=True)
class WaveDecision:
    terminal_scores: tuple[tuple[str, float], ...]
    public_best_name: str | None
    public_best_score: float | None
    asub010_spread: float | None
    next_candidate: str | None
    decision: str
    rationale: tuple[str, ...]


def _clean(scores: Mapping[str, float | None]) -> dict[str, float]:
    out: dict[str, float] = {}
    for name, value in scores.items():
        if value is None:
            continue
        numeric = float(value)
        if numeric < 0:
            raise ValueError(f"score for {name} must be non-negative")
        out[str(name)] = numeric
    return out


def decide_hosted_wave(scores: Mapping[str, float | None]) -> WaveDecision:
    """Recommend the next information-bearing candidate from terminal wave scores.

    Expected keys are ``ASUB-007``, ``ASUB-009``, ``ASUB-010-A`` and
    ``ASUB-010-B``. Missing/non-terminal rows should be omitted or set to None.
    """

    clean = _clean(scores)
    terminal = tuple(sorted(clean.items()))
    band = empirical_noise_band(ANCHOR_REPLICATES)

    public = {name: clean[name] for name in PUBLIC_NAMES if name in clean}
    if public:
        public_best_name, public_best_score = max(public.items(), key=lambda item: item[1])
    else:
        public_best_name = None
        public_best_score = None

    if "ASUB-010-A" in clean and "ASUB-010-B" in clean:
        asub010_spread = abs(clean["ASUB-010-A"] - clean["ASUB-010-B"])
    else:
        asub010_spread = None

    rationale: list[str] = []
    if asub010_spread is not None:
        rationale.append(
            f"ASUB-010 byte-identical spread={asub010_spread:.3f}; "
            f"ASUB-001 practical band={band.empirical_range:.3f}."
        )
        if asub010_spread > band.empirical_range:
            rationale.append("ASUB-010 itself shows unusually large hosted variance; modest public deltas are weak attribution evidence.")

    if public_best_name is not None and public_best_score is not None:
        comparison = compare_with_noise_band(
            candidate=public_best_name,
            candidate_score=public_best_score,
            anchor=ANCHOR_NAME,
            anchor_score=ANCHOR_SCORE,
            replicate_scores=ANCHOR_REPLICATES,
        )
        rationale.append(
            f"Best public row is {public_best_name}={public_best_score:.3f}: {comparison.relation} vs {ANCHOR_SCORE:.3f} anchor."
        )

        if comparison.relation == "clear_improvement":
            rationale.append("A stronger public anchor increases the marginal value of testing the complementary private-aware lane.")
            return WaveDecision(
                terminal,
                public_best_name,
                public_best_score,
                asub010_spread,
                "ASUB-011",
                "prioritize_private_complement",
                tuple(rationale),
            )

    private_score = clean.get(PRIVATE_NAME)
    if private_score is not None:
        private_comparison = compare_with_noise_band(
            candidate=PRIVATE_NAME,
            candidate_score=private_score,
            anchor=ANCHOR_NAME,
            anchor_score=ANCHOR_SCORE,
            replicate_scores=ANCHOR_REPLICATES,
        )
        rationale.append(f"ASUB-009 public telemetry={private_score:.3f}: {private_comparison.relation} vs anchor.")
        if private_comparison.relation != "clear_regression":
            rationale.append("The private-aware portfolio remains publicly competitive enough that the clean ASUB-011 replay-ordering ablation has high decision value.")
            return WaveDecision(
                terminal,
                public_best_name,
                public_best_score,
                asub010_spread,
                "ASUB-011",
                "test_hierarchical_private_prefix",
                tuple(rationale),
            )

    all_public_terminal = all(name in clean for name in PUBLIC_NAMES)
    if all_public_terminal:
        relations = [
            compare_with_noise_band(
                candidate=name,
                candidate_score=clean[name],
                anchor=ANCHOR_NAME,
                anchor_score=ANCHOR_SCORE,
                replicate_scores=ANCHOR_REPLICATES,
            ).relation
            for name in PUBLIC_NAMES
        ]
        if all(relation == "noise_band_overlap" for relation in relations):
            rationale.append("All public-wave runs overlap the practical anchor band; the interface-only control has maximum attribution value.")
            return WaveDecision(
                terminal,
                public_best_name,
                public_best_score,
                asub010_spread,
                "ASUB-012",
                "test_interface_only_control",
                tuple(rationale),
            )

    expected = {"ASUB-007", "ASUB-009", "ASUB-010-A", "ASUB-010-B"}
    missing = sorted(expected - clean.keys())
    if missing:
        rationale.append("Still missing terminal rows: " + ", ".join(missing) + ".")
        return WaveDecision(
            terminal,
            public_best_name,
            public_best_score,
            asub010_spread,
            None,
            "wait_for_more_terminal_evidence",
            tuple(rationale),
        )

    public_mean = fmean(clean[name] for name in PUBLIC_NAMES)
    rationale.append(f"Public-wave mean={public_mean:.3f}; no single rule dominates. Prefer the low-assumption public control for attribution.")
    return WaveDecision(
        terminal,
        public_best_name,
        public_best_score,
        asub010_spread,
        "ASUB-012",
        "default_to_interface_control",
        tuple(rationale),
    )
