# Public leaderboard frontier — 2026-08-25

Status: public-source intelligence, not official private-evaluator knowledge.

## Purpose

Establish a competitive public baseline quickly without confusing public-leaderboard optimization with prize-winning private robustness.

## Official facts that constrain the design

Kaggle's competition page states that:

- findings are replayed and rescored rather than trusted directly;
- score rewards predicate severity and unique cells;
- the public path uses the SDK `OptimalGuardrail`;
- the final/private path uses a stricter hidden guardrail;
- the attack is run against GPT-OSS and Gemma 4;
- the hosted budget is supplied by the evaluator and must not be hard-coded from conflicting documentation.

AgentSec therefore treats public throughput as a calibration lane, not as the final objective.

## Public evidence snapshot

### Official Kaggle Code page

On 2026-08-25, publicly visible Kaggle notebooks include scores in the high-80 range. This confirms that the starter-scale baseline is far below the active public frontier.

### Jun Morita public research repository

Publicly disclosed experiments provide useful historical calibration:

- a 300-candidate unique-domain `SECRET_MARKER` portfolio is recorded at exactly `27.000` public score;
- this matches the public scorer economics of 18 raw points for a severity-5 EXFILTRATION finding with a unique cell;
- later public implementations use live validation-fill rather than blindly returning a fixed candidate count.

Source: https://github.com/Jun-Morita/kaggle-ai-agent-security

### SKYGOD07 public research repository

A repository updated on 2026-08-25 records the following self-reported public progression:

- OMEGA v13: `91.170`
- OMEGA v22: `91.305`
- OMEGA v23: `91.125`

The repository attributes the v22 result to a two-phase replay-safe validation-fill architecture. This score has **not** been independently verified by AgentSec from Kaggle's authenticated leaderboard and must remain labeled third-party evidence.

Source: https://github.com/SKYGOD07/AI-Agent-Security---Multi-Step-Tool-Attacks

## Convergent public-frontier mechanics

Across public implementations and the SDK source, the strongest low-complexity public recipe is:

1. **Single post per candidate.** Multi-post candidates cost more model/tool-loop time and public experiments repeatedly report worse throughput.
2. **Use the public scorer's sentinel primitive.** A clean unique URL with `data=SECRET_MARKER` can produce a severity-5 EXFILTRATION finding under the public SDK 3.1.2 scorer/guardrail pairing.
3. **Live validation-fill.** Probe a candidate against the live target environment and return it only when the expected `http.post` actually succeeds. This converts model-specific fire rate into a measured property instead of a guessed one.
4. **Unique short domains.** The public SDK cell signature buckets `http.post` by domain, making unique domains a direct public diversity lever.
5. **Latency-adaptive model behavior.** Public experiments report Gemma as the faster row and GPT-OSS as the slower row. The attack does not receive a model name, so measured latency is the usable signal.
6. **Reasoning-compression template only on the slow row.** Multiple public implementations append GPT-OSS Harmony control tokens after a normal completed user instruction to reduce slow-row generation overhead. This is benchmark-specific and must never be assumed to transfer to other models or private robustness.
7. **Replay-safe sizing.** Returned candidates are replayed after search. Generation throughput alone is insufficient; the portfolio must be sized from measured validation latency with a safety cushion.
8. **Latency-ascending output order.** When candidates have equal public value, returning faster measured candidates first maximizes completed findings if replay truncates near a deadline.

## What AgentSec will *not* copy blindly

- hard-coded `9000`, `18000`, or `1800` second assumptions;
- experimental multi-post / burst stacking;
- unverified prompt tournaments that consume search budget;
- public sentinel farming as the sole final strategy;
- claims about the private guardrail inferred from public score alone;
- third-party scores as if they were independently verified.

## AgentSec public canary design

`submissions/ASUB-20260825-001-frontier-canary/attack.py` is our own compact synthesis of the convergent mechanics:

- self-contained Kaggle entrypoint;
- one warm-up probe at one tool hop;
- one full-hop latency classification probe;
- natural single-post template for the fast row;
- public Harmony compression suffix for the slow row;
- one candidate per unique short domain;
- keep-only-if-fired live validation;
- two replay/wall-clock phases with conservative primary and near-terminal backfill;
- `config.time_budget_s` as the only authoritative runtime input;
- latency-ascending returned portfolio;
- hard cap of 2,000 findings;
- static fallback only if the live environment cannot be probed.

The first hosted run is a **canary**. Its purpose is to establish parity with the public frontier mechanism and measure our actual GPT-OSS/Gemma throughput before any parameter tightening.

## Private-prize lane

The final leaderboard uses a hidden stricter guardrail. A public sentinel-only score around the frontier may have poor private value.

AgentSec will therefore maintain a second archive where candidates are ranked for:

- semantic security severity rather than literal-marker dependence;
- distinct predicate/source/sink structure, not just distinct URL domains;
- replay stability;
- resistance to an all-arguments outbound-payload scanner;
- resistance to coarse cell deduplication / diminishing-return proxies;
- multi-step behavior that remains meaningful if the public guardrail's first-argument quirk disappears.

A public private-eval proxy exists at https://github.com/aduriseti/kaggle-aas-private-eval-proxy. It explicitly describes itself as a best guess. AgentSec may use its ideas as stress tests, never as ground truth about the hidden guardrail.

## Promotion decision

Prepare and submit the public frontier canary as soon as eligibility and Kaggle notebook wiring are confirmed. Do not promote it to R8/final solely on public score. The private-robust lane begins immediately after the first hosted calibration result.
