from __future__ import annotations

from src.direct_cd_split import DEFAULT_STRESSES, default_direct_cd_split


def main() -> None:
    split = default_direct_cd_split()
    print("Synthetic stress planner only; hidden private guardrail remains unknown.")
    print()
    print("Direct-CD quota: 60")
    print(f"  synonym one-turn: {split.synonym}")
    print(f"  explicit+neutral: {split.launder}")
    print(f"  worst relative ratio: {split.min_ratio:.4f}")
    print(f"  mean relative ratio:  {split.mean_ratio:.4f}")
    print()
    print("Stress ratios:")
    for stress in DEFAULT_STRESSES:
        print(f"  {stress.name:32s} {split.scenario_ratios[stress.name]:.4f}")


if __name__ == "__main__":
    main()
