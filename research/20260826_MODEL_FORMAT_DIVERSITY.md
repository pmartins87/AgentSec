# Model-format diversity as a live public frontier

Date: 2026-08-26

## Scope

Authorized Kaggle AI Agent Security – Multi-Step Tool Attacks sandbox only. This note concerns synthetic fixture-backed tools and benchmark payloads.

## Motivation

The hosted evaluator runs the same attack algorithm separately against GPT-OSS and Gemma. Public field evidence shows that a prompt format which is fast/reliable on one target may be inert or expensive on the other. That makes a single hard-coded control-token format a fragile public-throughput strategy.

A useful public reference is the Apache-2.0 repository `COK-ZhangZiliang/AI-Agent-Security`. Its documented lineage reports a large improvement when the adaptive search combined a GPT-OSS Harmony-format arm with a Gemma-specific tool-call-format arm, selected live by observed firing/latency rather than by guessing the model identity. The implementation in AgentSec is independently written and uses the reference only as external evidence for the research hypothesis.

Reference:

- https://github.com/COK-ZhangZiliang/AI-Agent-Security

## Hypothesis

A bounded live race across **model-agnostic + model-format-specific** arms should weakly improve the chance of finding a high-value public replay mechanism, provided format-specific promotion has a strict repeatability gate.

The important distinction is between:

1. **search diversity** — it is cheap to test several prompt formats during the public generation phase;
2. **archive commitment** — it is expensive to extrapolate one lucky format to a 2,000-candidate replay archive.

Therefore DRAFT-ASUB-016 separates the two: broad first/second-pass probing, narrow confirmed winner.

## DRAFT-ASUB-016 arms

Single-post controls:

- `plain1` — conservative baseline;
- `imperative1` — model-agnostic immediate-tool wording;
- `harmony_full1` — GPT-OSS-style full tool-call exemplar;
- `gemma_full1` — Gemma-style forged model/tool-call exemplar.

Three-hop candidates:

- `chain3_plain`;
- `chain3_harmony`;
- `chain3_gemma`.

The three-hop arms target the structural possibility that multiple successful EXFIL events inside one finding improve raw score per replayed candidate. They are not assumed to work: their live predicate count is measured and priced into raw-score-per-second.

## Promotion gate

A non-plain arm may own the archive only when:

- it has at least two positive live observations;
- its aggregate public raw-score-per-second exceeds the positive plain anchor by at least the configured margin (default 3%);
- its required hop count is supported by the live `AttackRunConfig.max_tool_hops`;
- the bounded probe wall remains inside the generation budget.

If those conditions are not met, the algorithm falls back to plain single-post.

## Timeout-prefix interaction

The evaluator update that preserves score accumulated before replay timeout changes archive economics. Once a positive mechanism is selected, DRAFT-ASUB-016 returns the full legal 2,000 findings rather than shortening the archive to a guessed replay count. The highest-confidence mechanism occupies the entire prefix; a timeout simply truncates its tail.

## Private-leaderboard caution

This is a **public frontier experiment**. Format-specific public compliance does not imply private-guardrail survival. It should therefore compete for the public-anchor side of the final pair, while ASUB-009 remains the deliberately heterogeneous private hedge.

## Decision rule after hosted evidence

- If DRAFT-ASUB-016 materially beats ASUB-007 and is mechanically stable, freeze a successor ASUB identity.
- If it ties ASUB-007, prefer the simpler/less format-dependent candidate for final transfer unless row-level evidence favors the diversified arm.
- If it underperforms or errors, retain the result as evidence that current harness-specific format injection does not justify archive commitment.
