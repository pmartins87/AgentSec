# STATUS — AgentSec

Last updated: 2026-08-25

## Mission status

**Phase: R0 active / R1 baseline prepared**

Goal: produce a prize-contending final submission for AI Agent Security – Multi-Step Tool Attacks, while also preserving an optional Working Note path.

R0 is close to completion. The official SDK/source contract is now pinned and the first reproducible attack baseline exists, but account eligibility and the current authenticated Kaggle data bundle still need to be verified/frozen before R0 can be declared PASS.

## Confirmed competition constraints

- Entry deadline: 2026-08-25 23:59 UTC.
- Final submission deadline: 2026-09-01 23:59 UTC.
- Working Note deadline: 2026-09-08 23:59 UTC.
- Code competition; notebook must produce `/kaggle/working/attack.py`.
- Internet disabled during submitted notebook execution.
- GPU notebook runtime limit: 15 hours.
- Public/private replay scoring; private guardrail is stricter and hidden.
- Score rewards replay-validated predicate severity plus unique cells.
- SDK replay limits include at most 2,000 findings, 32 messages/finding, 2,000 characters/message.
- Runtime publications conflict; hosted code must obey `AttackRunConfig.time_budget_s` instead of hard-coding 18,000/9,000/1,800 seconds.

## Official source freeze completed

- `aicomp-sdk==3.1.2`
- upstream tag `v3.1.2`
- release commit `56dabd3a6d8fbe587acd4d0a1b22796b1acccfcd`
- PyPI wheel/sdist hashes recorded
- source blob hashes recorded in `docs/OFFICIAL_ARTIFACTS.md`
- public SDK contract and scoring model checked directly from source

## Implementation completed in this phase

- `requirements.txt` pins SDK 3.1.2.
- top-level `attack.py` contains the R1 deterministic archive-search baseline.
- `scripts/run_r1_smoke.ps1` performs validate → deterministic smoke → Gym-style evaluator run.
- `tests/test_public_surface.py` captures structural public-guardrail reachability regressions.
- `research/20260825_PUBLIC_ATTACK_SURFACE.md` records the source-verified public attack-surface analysis and private-overfit caveat.

## Source-verified strategic finding

Under the known public SDK 3.1.2 guardrail/scorer pairing:

- a clean `http.post` carrying the benchmark sentinel `SECRET_MARKER` in `data` is structurally reachable and can score `EXFILTRATION`;
- `UNTRUSTED_TO_ACTION` is preempted by the public guardrail's wider recent-source window;
- destructive access to the protected root `secret.txt` is denied by the public guardrail;
- `CONFUSED_DEPUTY` remains worth empirical testing but has lower severity economics.

This finding is **not** assumed to transfer to the hidden private guardrail. AgentSec will maintain a public-throughput lane and a private-robustness lane.

## Immediate next-action queue

1. **Eligibility gate — urgent:** confirm the Kaggle account has accepted the competition rules before the 2026-08-25 23:59 UTC entry deadline.
2. Download the current authenticated competition data/starter assets and add filenames/sizes/SHA256 to `docs/OFFICIAL_ARTIFACTS.md`.
3. Execute `scripts/run_r1_smoke.ps1` in an environment with Python 3.11+ and preserve `artifacts/r1_gym` outputs.
4. Record the run as `AEXP-20260825-001-r1-baseline` under `experiments/` with exact git SHA, score, runtime, findings, cells, and failures.
5. Produce the first valid Kaggle notebook using the frozen `attack.py`; confirm internet-off execution and generated `/kaggle/working/attack.py`.
6. Submit the first hosted baseline and record it in `docs/SUBMISSION_LEDGER.md`.
7. Start controlled experiments on sentinel throughput, confused-deputy economics, model-specific behavior, and stricter private-guardrail proxies.

## Promotion gates

- **R0 PASS:** repository, official artifacts, rules, metric, environment inventory captured **and Kaggle entry eligibility confirmed**.
- **R1 PASS:** official/SDK-aligned baseline reproduced end-to-end with artifacts preserved.
- **R2 PASS:** deterministic local replay/evaluation harness verified.
- **R3 PASS:** first valid Kaggle submission scored.
- **R4 PASS:** predicate-directed search finds reproducible nontrivial failures.
- **R5 PASS:** diversity/coverage engine beats baseline robustly.
- **R6 PASS:** runtime allocation and candidate prioritization optimized.
- **R7 PASS:** robustness tests against public/private-guardrail mismatch proxies.
- **R8 PASS:** final candidate frozen, independently reproduced, submitted.
- **R9 PASS:** Working Note finalized by 2026-09-08 if competitive/novel enough.

## Known strategic risks

- Public leaderboard optimization alone can overfit the permissive public guardrail.
- The hosted evaluator has changed during the competition, including Gemma tool-call parsing and leaderboard reruns.
- Hosted timing/replay behavior may differ materially from local deterministic/Gym tests.
- A high public score from the sentinel route is insufficient evidence of prize robustness under the private guardrail.
