# Working Note outline — AgentSec

Status: **living draft / evidence first**

Deadline: 2026-09-08 23:59 UTC

## Provisional title

**When the Guardrail and the Scorer Disagree: Reproducible Multi-Step Agent Security Search Under Public/Private Evaluation**

## 1. Problem and competition setting

- Tool-using agents, deterministic offline benchmark.
- Attack algorithm must return replayable user-message chains.
- Evaluator reruns candidates independently.
- Four documented failure predicates.
- Public guardrail known; private guardrail hidden and stricter.
- Why raw public leaderboard optimization is an incomplete objective.

## 2. Reproducibility discipline

- Freeze `aicomp-sdk==3.1.2` and official source commit/hashes.
- Immutable ASUB IDs and submission ledger.
- Source-derived claims separated from hypotheses.
- CI contract checks and synthetic scorer regressions.
- Replay-first candidate selection.

## 3. Source-level public attack-surface analysis

### 3.1 Public sentinel EXFIL route

- Explain structural reachability without claiming private transfer.
- Demonstrate throughput/replay economics.
- Show ASUB-001 calibration design.

### 3.2 Structurally closed public lanes

- Public U2A mismatch between scorer window and guardrail source window.
- Protected-root destructive-write denial.
- Why negative reachability results matter: search budget should move elsewhere.

### 3.3 Confused deputy lane

- Public scorer authorization heuristic.
- Benign direct synonym canary.
- Empirical template selection rather than hand-picked prompt folklore.

## 4. Main benchmark-design insight: semantic authorization mismatch

The official scorer uses literal authorization terms, while a realistic guardrail may reason semantically. This can create evaluator disagreement:

- `notify` vs literal `send/email/upload`;
- `POST` vs literal share authorization;
- `invoke` vs literal `run/execute`;
- `persist` vs literal `save/write`.

Synthetic official-scorer proofs establish the score consequences *if* the action survives private replay. This is not presented as knowledge of hidden guardrail behavior.

## 5. Private robustness without hidden-evaluator access

Maintain deliberately conflicting proxies:

1. provenance-strict / all-args DLP;
2. semantic authorization + sensitive-content protection.

Explain why a portfolio across mutually incompatible hypotheses is more defensible than pretending one proxy predicts hidden code.

## 6. Search and portfolio engineering

- Live calibration of target-model tool-action attempts.
- Distinguish successful findings from useful denied-attempt calibration traces.
- Score-cell diversity based on actual tool traces, not prompt paraphrases.
- Argument-level diversity: domains, recipients, commands, paths.
- Severity economics per candidate.
- Replay-aware caps and cross-family ordering.
- Partial-timeout update motivates front-loaded diversity.

## 7. Ablations to include when hosted data arrives

Minimum desired table:

| Variant | Public score | Runtime | Findings | Unique cells | Failure family mix | Notes |
|---|---:|---:|---:|---:|---|---|
| R1 baseline | | | | | | |
| ASUB-001 public frontier | | | | | EXFIL | |
| ASUB-002 direct CD | | | | | CD | |
| ASUB-003 semantic transfer | | | | | mixed | |
| final mixed portfolio | | | | | mixed | |

Also record identical-submission variance from the accidental duplicate Version 4 if both complete.

## 8. Negative results

Potentially valuable negative results:

- deterministic-agent smoke scores are not representative of target models;
- prompt-text diversity alone does not guarantee score-cell diversity;
- domain-only public diversity is fragile under coarser private assumptions;
- public sentinel success does not imply private robustness;
- provenance-strict and semantic private proxies disagree by construction.

## 9. Responsible conclusions

- Keep findings confined to the authorized benchmark.
- Focus on shared lessons for agent-security benchmark design:
  - scorer/guardrail semantic alignment;
  - replayability;
  - provenance modeling;
  - hidden-defense robustness;
  - evaluator variance and timeout reporting.

## Evidence checklist before finalizing

- [ ] exact Kaggle scores and timestamps
- [ ] final submission IDs/version numbers
- [ ] all source claims linked to pinned source files
- [ ] experiment artifacts preserved
- [ ] no hidden-guardrail speculation written as fact
- [ ] at least one strong ablation table
- [ ] duplicate-run variance documented if available
- [ ] final code hash and clean reproduction
