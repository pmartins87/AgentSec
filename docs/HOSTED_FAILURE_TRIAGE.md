# Hosted evaluator failure triage — AgentSec

Last updated: 2026-08-26

## Why this exists

The AgentSec attack strategy and the Kaggle evaluation infrastructure can fail in
very different ways. Treating every terminal error as evidence about the attack
would contaminate the research ledger and waste scarce hosted submission slots.

Public competition discussions document all of the following:

- long-running submissions and inconsistent published runtime descriptions,
  acknowledged by the competition host;
- byte-identical or equivalent submissions producing materially different runtime
  and public score outcomes;
- `Submission Format Error` being used for multiple classes of failure in
  community reports, including replay/runtime exhaustion;
- periods where participants report repeated `A system error` across otherwise
  valid or previously scoring notebooks;
- evaluator/parser updates and leaderboard refreshes during the competition.

Operationally, AgentSec therefore classifies the *failure mode first* and the
*attack quality second*.

## Public references

- Host runtime investigation / budget clarification:
  https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/708272
- Byte-identical replay/runtime variation report:
  https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/717155
- Submission-format-error discussion / community debugging observations:
  https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/718901
- Evaluator update / leaderboard refresh:
  https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/733058
- System-error / stuck-queue report:
  https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/732447

Community comments are evidence of observed symptoms, not authoritative evaluator
specification. Host/staff statements outrank participant inference.

## Terminal-state taxonomy

### H0 — valid score

Evidence:

- submission reaches a scored/complete terminal state;
- public score is numeric;
- no format/system error.

Action:

1. Record score, submission ref, notebook version and wall runtime.
2. Run `scripts/interpret_hosted_score.py` for the applicable attack family.
3. If a byte-identical duplicate exists, wait for both before changing replay
   margins unless the decision is urgent.
4. Strategy conclusions are allowed, with hosted-variance caveat.

### H1 — Kaggle/system error

Typical UI wording: `Kaggle Error`, `A system error`, or equivalent platform
failure without a usable score.

Action:

1. Record screenshot/ref/time and whether output bytes/details are available.
2. Do **not** infer attack fire rate or guardrail behavior.
3. Verify the committed notebook still produced both `/kaggle/working/attack.py`
   and `/kaggle/working/submission.csv`.
4. If a byte-identical duplicate is still running, wait for it.
5. If multiple clean duplicates fail H1, escalate as infrastructure/evaluator
   evidence before changing attack logic.

### H2 — Submission Format Error

This label is ambiguous in public reports.

Action:

1. Check the notebook-selection contract first: placeholder `submission.csv`
   existed before the scored rerun.
2. Re-run official `aicomp validate redteam attack.py` on the frozen exact source.
3. Check finding/message limits and serialization contract.
4. Check replay-budget sizing and candidate count; format error can be a runtime
   symptom in community reports.
5. Do not change prompt strategy until mechanical causes are excluded.

### H3 — blank / missing score after completion

Action:

1. Treat as evaluator/output ambiguity, not as zero attack quality.
2. Inspect available submission details for timeout/parser/output clues.
3. Preserve the exact source and notebook version.
4. Prefer a diagnostic canary or support escalation over speculative strategy
   mutation.

### H4 — explicit attack-generation timeout

Action:

1. This is a real algorithm/runtime failure.
2. Reduce generation probing or increase headroom.
3. Keep public/private replay economics separate from generation wall time.
4. Preserve a static fallback path.

### H5 — replay truncation with partial numeric score

After the evaluator update, accumulated replay score can survive a replay timeout.

Action:

1. Numeric score remains useful evidence.
2. Interpret candidate ordering and completion as a prefix-selection problem.
3. Prefer value/time or fastest-first ordering according to the attack family's
   per-candidate economics.
4. Avoid assuming the missing tail would have had the same hit rate as the prefix.

## ASUB-001 Version 4 decision table

There are two byte-identical corrected Version 4 runs in flight.

| Run A | Run B | Interpretation | Next action |
|---|---|---|---|
| H0 | H0 | strongest calibration; duplicate variance measurable | compare scores as equivalent finding counts |
| H0 | H1/H2/H3 | infrastructure/runtime variance proven by identical source | trust numeric run for strategy, preserve failure evidence |
| H1 | H1 | likely infrastructure/evaluator class after wrapper was mechanically corrected | diagnose platform before spending another slot |
| H2 | H2 | inspect serialization/replay sizing before strategy | do not submit a new attack family yet |
| running | any | information still pending | spend no additional slot |

## Evidence capture checklist

For every hosted submission preserve:

- Kaggle submission reference if visible;
- notebook slug and version;
- attack source hash/blob SHA;
- submission description;
- start/terminal timestamps or best available wall-runtime estimate;
- exact terminal label;
- numeric public score if present;
- screenshot of details for any error;
- whether `/kaggle/working/attack.py` and `submission.csv` were present in the
  committed notebook output;
- whether the source was byte-identical to another run.

This evidence belongs in `docs/SUBMISSION_LEDGER.md` and the relevant ASUB folder.
