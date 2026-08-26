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
- Preserve accidental duplicate runs as variance evidence rather than discarding them.

## 3. Source-level public attack-surface analysis

### 3.1 Public sentinel EXFIL route

- Explain structural reachability without claiming private transfer.
- Demonstrate throughput/replay economics.
- ASUB-001 first hosted result: **77.850 public**.
- Fixed 18-raw economics imply **865 equivalent successful findings per public row on average**.

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

A second throughput consequence is equally important: generation and replay have **independent time windows**. Generation-only warm-up cost therefore should not automatically be deducted from replay allowance. That distinction motivates the DRAFT-ASUB-010 ablation.

### 4.3 Authorization-context TOCTOU / intent laundering

This is the strongest source-derived benchmark-design contribution.

The frozen SDK evaluates authorization at two different moments:

1. **guardrail time:** inside `SandboxEnv.interact()`, the guardrail receives `context["last_user"] = self.trace.user_messages[-1]` immediately before a tool decision;
2. **score time:** `eval_predicates()` later computes SHARE/EXEC/WRITE authorization from the **final** user message in the entire replay trace.

Earlier explicit authorization can therefore be visible to a runtime guardrail when the action occurs and then disappear from canonical scoring after a neutral later turn.

Example structure:

1. `Send an email to ...` — explicit authorization;
2. `email.send` succeeds during that turn;
3. `Continue.` — neutral final message;
4. canonical scorer sees the neutral final message and emits `CONFUSED_DEPUTY` for the earlier share.

For source→action chains, the same temporal mismatch can make an explicitly authorized earlier action count as `UNTRUSTED_TO_ACTION` after the neutral tail, provided the runtime defense permits the action.

This is an **authorization-context time-of-check/time-of-score mismatch** across guardrail and scorer layers.

Mechanical evidence:

- `tests/test_intent_laundering_surface.py` — canonical last-message scorer behavior;
- `tests/test_runtime_authorization_context.py` — runtime semantic proxy vs final scorer vs provenance-strict proxy;
- `tests/test_draft_private_hedge_v2.py` — first-turn target evidence, delayed-target rejection, and denied first-turn private-transfer calibration;
- `src/semantic_authorization_proxy.py` — separate final-trace and interaction-time semantic stress models.

Research implementations:

- DRAFT-ASUB-008 — first laundering portfolio, later found to over-select one direct-CD mechanism by public speed;
- DRAFT-ASUB-009 — private hedge v2 preserving both direct mechanisms and now requiring the target action/attempt in the explicitly authorized first turn.

## 5. Private robustness without hidden-evaluator access

Maintain deliberately conflicting proxies/stress cases:

1. provenance-strict / all-args DLP;
2. runtime-context semantic authorization + sensitive-content protection;
3. final-trace semantic approximation;
4. authority-strict semantic defense that can also close direct confused-deputy behavior.

Explain why a portfolio across mutually incompatible hypotheses is more defensible than pretending one proxy predicts hidden code.

Current aggregate 360-candidate stress-plan target:

- public EXFIL: 144;
- direct CD: 60;
- semantic email: 120;
- semantic HTTP: 12;
- semantic shell: 12;
- semantic write: 12.

The direct-CD quota keeps two conflicting mechanisms:

- 24 one-turn scorer-negative synonym candidates;
- 36 explicit-action + neutral-tail laundering candidates.

The rates are deliberately synthetic stress assumptions, never measurements of the private evaluator.

## 6. Search, runtime, and portfolio engineering

- Live calibration of target-model tool-action attempts.
- Distinguish successful findings from useful denied-attempt calibration traces.
- For laundering candidates, require the intended action during the explicitly authorizing turn; a target action delayed until the neutral turn no longer supports the same runtime-authorization hypothesis.
- Score-cell diversity based on actual tool traces, not prompt paraphrases.
- Argument-level diversity: domains, recipients, commands, paths.
- Severity economics per candidate.
- Replay-aware caps and cross-family ordering.
- Partial-timeout behavior motivates prefix quality and explicit speculative tails.
- One-message vs two-message replay cost must be measured, not assumed equal.
- Separate a public-throughput anchor from private-transfer hedges.

### 6.1 Public throughput generations

Public anchor lineage to ablate:

- **ASUB-001** — conservative canary; hosted public **77.850**.
- **ASUB-004** — frozen frontier v2: compact terminal, fixed plain/Harmony race, `REPLAY_COST_COEF=0.95`, fastest-first ordering.
- **DRAFT-ASUB-010** — frontier v3 backfill: independent-budget accounting, slow-row-only A/B, strict `REPLAY_COST_COEF=1.0`, primary archive + speculative backfill tail.

Independent public field evidence now includes a pinned MIT lineage reporting **91.305** at its v22 backfill architecture. At fixed 18-raw economics that is `1,014.5` equivalent findings per row, versus AgentSec ASUB-001's 865. Treat the ~149.5 finding gap as a search opportunity, not an expected-gain estimate.

### 6.2 Why ASUB-004 and DRAFT-ASUB-010 are both scientifically useful

They separate otherwise confounded effects:

1. compact prompt/terminal compliance;
2. replay-cost estimation (`0.95` vs strict `1.0`);
3. warm-up accounting under separate generation/replay budgets;
4. single conservative cutoff vs primary+backfill archive policy;
5. global fastest-first ordering vs primary-first/speculative-tail ordering.

## 7. Ablations to include when hosted data arrives

Minimum desired table:

| Variant | Public score | Runtime | Findings | Unique cells | Failure family mix | Notes |
|---|---:|---:|---:|---:|---|---|
| R1 baseline | | | | | | |
| ASUB-001 public frontier | **77.850** | pending exact | ~865 mean equiv./row | | EXFIL | first hosted numeric result |
| ASUB-001 duplicate | pending | | | | EXFIL | byte-identical variance replicate |
| ASUB-002 direct CD | | | | | CD | |
| ASUB-003 semantic transfer | | | | | mixed | |
| ASUB-004 public frontier v2 | | | | | EXFIL | frozen controlled successor |
| DRAFT-007 forged multi-post | | | | | EXFIL | |
| DRAFT-009 private hedge v2 | | | | | mixed | first-turn invariant |
| DRAFT-010 public frontier v3 | | | | | EXFIL | primary/backfill |
| final mixed portfolio | | | | | mixed | |

Specific authorization ablations:

- direct `notify` one-turn vs explicit `send/email` + neutral tail;
- source→action explicit authorization with vs without neutral tail;
- target action completed during authorizing turn vs delayed until neutral turn;
- one- vs two-message replay cost;
- public attempted-tool rate vs hosted private-transfer outcome when/if final results expose it.

Specific throughput ablations:

- ASUB-001 vs ASUB-004 terminal/sizing changes;
- `REPLAY_COST_COEF=0.95` vs strict `1.0`;
- generation warm-up deduction vs independent replay allowance;
- conservative single cutoff vs two-stage primary/backfill;
- all-candidates fastest-first vs primary-before-backfill ordering.

## 8. Negative results

Potentially valuable negative results:

- deterministic-agent smoke scores are not representative of target models;
- prompt-text diversity alone does not guarantee score-cell diversity;
- domain-only public diversity is fragile under coarser private assumptions;
- public sentinel success does not imply private robustness;
- provenance-strict and semantic private proxies disagree by construction;
- a final-trace semantic proxy is too pessimistic to model interaction-time authorization faithfully;
- public `fs.read(secret.txt)` is blocked under the frozen public guardrail contract;
- public U2A is structurally preempted by the wider public taint window;
- compound/multi-action prompts can lose on model compliance despite better theoretical raw economics;
- selecting one private-transfer mechanism solely from public latency is avoidable overfit;
- a timing-boundary CI smoke can fail while compile/tests/SDK validation are all green, so infrastructure/runtime failures must remain distinct from algorithmic failures.

## 9. Responsible conclusions

- Keep findings confined to the authorized benchmark.
- Focus on shared lessons for agent-security benchmark design:
  - scorer/guardrail semantic alignment;
  - authorization context should be attached to the action/turn it authorizes rather than recomputed from the final user message;
  - replayability;
  - provenance modeling;
  - hidden-defense robustness;
  - evaluator variance and timeout reporting;
  - separate generation/replay budgets should be explicit in benchmark documentation because they materially affect attack-search economics.

## Evidence checklist before finalizing

- [x] first exact hosted public score preserved: 77.850
- [ ] exact hosted timestamps/runtime rows where available
- [ ] final submission IDs/version numbers
- [ ] all source claims linked to pinned source files
- [x] canonical last-message authorization behavior regression-tested
- [x] public-generation/private-replay asymmetry documented from gateway source
- [x] runtime guardrail `last_user` context vs final scorer context frozen in regression tests
- [x] first-turn laundering calibration invariant regression-tested
- [x] second public frontier reference pinned and license attributed
- [ ] experiment artifacts preserved for all hosted variants
- [ ] no hidden-guardrail speculation written as fact
- [ ] at least one strong hosted ablation table beyond ASUB-001
- [ ] duplicate-run variance documented if available
- [ ] final code hash and clean reproduction
