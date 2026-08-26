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

## 4. Main benchmark-design insights: authorization semantics and evaluator staging

### 4.1 Semantic authorization mismatch

The official scorer uses literal authorization terms, while a realistic guardrail may reason semantically. This can create evaluator disagreement:

- `notify` vs literal `send/email/upload`;
- `POST` vs literal share authorization;
- `invoke` vs literal `run/execute`;
- `persist` vs literal `save/write`.

Synthetic official-scorer proofs establish the score consequences *if* the action survives private replay. This is not presented as knowledge of hidden guardrail behavior.

### 4.2 Public generation → frozen archive → public/private replay

Source reconstruction of the published gateway shows that `AttackAlgorithm.run()` is executed against the public `OptimalGuardrail`, then the returned archive is replayed independently under the public and private guardrails.

Consequence: public generation can measure **model compliance and latency**, but it cannot measure hidden-defense survival. For a publicly blocked source→action family, a guardrail-denied target call can still be valuable generation evidence because it proves the model attempted the intended sequence; private replay remains the actual transfer test.

### 4.3 Last-message intent laundering

`aicomp-sdk==3.1.2` derives SHARE/EXEC/WRITE authorization from the **last user message only**. Earlier explicit authorization is forgotten by canonical predicate scoring.

This creates a genuinely multi-step mismatch:

1. an earlier user message explicitly authorizes a tool action using ordinary natural language;
2. the action occurs;
3. a final neutral user message such as `Continue.` is appended;
4. canonical scoring evaluates the earlier action using only the neutral last-message authorization context.

Mechanical regressions are frozen in `tests/test_intent_laundering_surface.py` for direct CD and U2A SHARE/EXEC/WRITE shapes.

Research implementation: `submissions/DRAFT-ASUB-008-intent-launder-portfolio/attack.py`.

## 5. Private robustness without hidden-evaluator access

Maintain deliberately conflicting proxies/stress cases:

1. provenance-strict / all-args DLP;
2. semantic authorization + sensitive-content protection;
3. authority-strict semantic defense that can also close direct confused-deputy behavior.

Explain why a portfolio across mutually incompatible hypotheses is more defensible than pretending one proxy predicts hidden code.

Current aggregate 360-candidate stress-plan target:

- public EXFIL: 144;
- direct CD: 60;
- semantic email: 120;
- semantic HTTP: 12;
- semantic shell: 12;
- semantic write: 12.

The direct-CD quota itself has two conflicting mechanisms. A second minimax-relative-regret planner keeps both instead of selecting one solely from public speed:

- 24 one-turn scorer-negative synonym candidates;
- 36 explicit-action + neutral-tail laundering candidates.

The rates driving this split are deliberately synthetic stress assumptions, never measurements of the private evaluator.

## 6. Search and portfolio engineering

- Live calibration of target-model tool-action attempts.
- Distinguish successful findings from useful denied-attempt calibration traces.
- Score-cell diversity based on actual tool traces, not prompt paraphrases.
- Argument-level diversity: domains, recipients, commands, paths.
- Severity economics per candidate.
- Replay-aware caps and cross-family ordering.
- Partial-timeout update motivates front-loaded diversity.
- Separate a public-throughput anchor from private-transfer hedges.

Public-throughput research variants to ablate:

- DRAFT-ASUB-006: single-post frontier v2;
- DRAFT-ASUB-007: live choice among single-/multi-post forged shapes.

## 7. Ablations to include when hosted data arrives

Minimum desired table:

| Variant | Public score | Runtime | Findings | Unique cells | Failure family mix | Notes |
|---|---:|---:|---:|---:|---|---|
| R1 baseline | | | | | | |
| ASUB-001 public frontier | | | | | EXFIL | |
| ASUB-002 direct CD | | | | | CD | |
| ASUB-003 semantic transfer | | | | | mixed | |
| DRAFT-006 public frontier v2 | | | | | EXFIL | |
| DRAFT-007 forged multi-post | | | | | EXFIL | |
| DRAFT-008 intent laundering | | | | | mixed | |
| final mixed portfolio | | | | | mixed | |

Also record identical-submission variance from the accidental duplicate Version 4 if both complete.

Specific authorization ablations:

- direct `notify` one-turn vs explicit `send/email` + neutral tail;
- source→action explicit authorization with vs without neutral tail;
- one- vs two-message replay cost;
- public attempted-tool rate vs hosted private-transfer outcome when/if final results expose it.

## 8. Negative results

Potentially valuable negative results:

- deterministic-agent smoke scores are not representative of target models;
- prompt-text diversity alone does not guarantee score-cell diversity;
- domain-only public diversity is fragile under coarser private assumptions;
- public sentinel success does not imply private robustness;
- provenance-strict and semantic private proxies disagree by construction;
- public `fs.read(secret.txt)` is blocked under the frozen public guardrail contract;
- public U2A is structurally preempted by the wider public taint window;
- compound/multi-action prompts can lose on model compliance despite better theoretical raw economics.

## 9. Responsible conclusions

- Keep findings confined to the authorized benchmark.
- Focus on shared lessons for agent-security benchmark design:
  - scorer/guardrail semantic alignment;
  - conversational authorization should not be reduced to last-message substring checks;
  - replayability;
  - provenance modeling;
  - hidden-defense robustness;
  - evaluator variance and timeout reporting.

## Evidence checklist before finalizing

- [ ] exact Kaggle scores and timestamps
- [ ] final submission IDs/version numbers
- [ ] all source claims linked to pinned source files
- [x] canonical last-message authorization behavior regression-tested
- [x] public-generation/private-replay asymmetry documented from gateway source
- [ ] experiment artifacts preserved
- [ ] no hidden-guardrail speculation written as fact
- [ ] at least one strong ablation table
- [ ] duplicate-run variance documented if available
- [ ] final code hash and clean reproduction
