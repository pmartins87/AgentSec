# Working Note draft section — Timeout semantics change the optimal archive policy

Status: evidence-backed methodological draft; integrate into `WORKING_NOTE_OUTLINE.md` after hosted ablation data arrives.

## Claim

A benchmark's timeout semantics are part of the attack surface and materially change the rational search policy.

The AgentSec development sequence encountered two evaluator regimes:

1. **zero-on-replay-timeout risk** — a conservative attacker should estimate replay cost and stop the returned archive before the expected deadline;
2. **prefix-preserving replay timeout** — once the evaluator preserves findings scored before replay timeout, a valid non-negative-value tail cannot erase score already accumulated in the prefix.

Under the second regime, the design objective changes from **predict the largest replay-safe archive** to **maximize value and hypothesis coverage in every replay prefix**.

## Public-frontier consequence

For a public lane whose candidates have positive expected score:

- keep attack generation bounded because generation timeout is still terminal;
- spend a small fraction of generation budget identifying the best live mechanism;
- order the highest expected raw-score-per-replay-second mechanism first;
- return the full legal archive rather than truncating solely from a noisy replay-time estimate;
- let replay timeout remove the tail if the evaluator reaches its limit.

ASUB-007 implements this as a public ablation. Fast rows retain plain single-post EXFIL. Slow rows compare plain, Harmony, and forged 2–5-post candidates; a non-plain mechanism must be confirmed twice and clear a value/time margin over the plain anchor before it owns the 2,000-item archive.

## Private-robustness consequence

For a hidden defense, raw-score ordering alone is insufficient because mechanism survival is uncertain. Prefix quality must include **hypothesis coverage**.

ASUB-008 scales the private hedge to 2,000 candidates and uses weighted interleaving. DRAFT-ASUB-015 strengthens the earliest prefix further: every active family receives one slot before any family receives a second slot, after which exact weighted interleaving resumes.

This separates two notions of prefix optimality:

- **public value prefix:** maximize expected score per replay second;
- **private uncertainty prefix:** ensure early exposure to mutually incompatible plausible transfer mechanisms while retaining long-run portfolio weights.

## Why this is a benchmark-design issue

The same attack generator can be rationally conservative under one timeout contract and rationally oversubscribed under another. Therefore timeout handling is not merely infrastructure detail. It affects:

- candidate count;
- candidate order;
- value of live latency calibration;
- value of multi-post amortization;
- value of inter-family diversification;
- the interpretation of incomplete replays.

Benchmarks should specify separately:

- attack-generation timeout semantics;
- public replay timeout semantics;
- private replay timeout semantics;
- whether partial score is preserved;
- whether budgets are independent across stages.

## Hosted ablation to report

Minimum comparison when results arrive:

| Candidate | Archive policy | Public score | Interpretation |
|---|---|---:|---|
| ASUB-001 | conservative replay-aware canary | 77.850 | baseline |
| ASUB-005 | paired one-hop/full-hop replay sizing | pending | measured replay-cap strategy |
| ASUB-007 | full value-ordered timeout prefix | pending | prefix-preserving oversubscription |
| ASUB-006 | 360 mixed private hedge | pending | short private portfolio |
| ASUB-008 / successor | 2,000 interleaved private prefix | pending | full-cap private uncertainty coverage |

Do not claim superiority until hosted scores or final-private results support it. The methodological conclusion — that the optimal policy changes with timeout semantics — follows from the evaluator contract itself; the magnitude of the gain is empirical.
