# AgentSec

Competition workspace for **AI Agent Security – Multi-Step Tool Attacks** (Kaggle, 2026).

## Mission

Build a prize-contending attack-search algorithm for the official deterministic, offline benchmark. The project is limited to the competition sandbox and its authorized evaluation environment.

## Competition snapshot

- Host: OpenAI (competition page also credits Google and IEEE)
- Prize pool: **US$50,000**
- Entry deadline: **2026-08-25 23:59 UTC**
- Final submission deadline: **2026-09-01 23:59 UTC**
- Optional Working Note deadline: **2026-09-08 23:59 UTC**
- Main prizes: US$15k / 10k / 8k / 7k / 5k
- Working Note awards: 2 × US$2.5k
- Submission: Kaggle notebook producing `/kaggle/working/attack.py`
- Core interface: `AttackAlgorithm.run(env) -> list[AttackCandidate]`
- Score: severity + diversity of replay-validated findings, normalized to 0–1000

## Repository map

- `STATUS.md` — current state and immediate next actions
- `ROADMAP.md` — milestone-based route to final submission
- `HANDOFF.md` — starting point for a dedicated project chat
- `docs/COMPETITION.md` — rules, metric, constraints, deadlines
- `docs/EXPERIMENT_PROTOCOL.md` — reproducible experiment discipline
- `docs/SUBMISSION_LEDGER.md` — submission/result log
- `research/README.md` — hypotheses and research notes
- `src/README.md` — implementation architecture
- `experiments/README.md` — experiment artifacts and naming
- `submissions/README.md` — frozen submission packages

## Operating principle

Every meaningful change should be traceable to a hypothesis, experiment, measured result, or competition requirement. Public-leaderboard gains are useful, but the final design must also be robust to replay validation and the private guardrail.

Official competition: https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks
