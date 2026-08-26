# Public frontier field evidence — 2026-08-26

## Scope

This note records **public, independently hosted** evidence relevant to AgentSec's
public-throughput anchor. It does not claim anything about the hidden private
guardrail.

Primary public reference:

- Junichiro Morita, `kaggle-ai-agent-security`
- repository: `https://github.com/Jun-Morita/kaggle-ai-agent-security`
- submission ledger: `submit/SUBMISSIONS.md`
- reference implementation: `submit/v169_replay_costcoef095/attack.py`
- repository license: MIT

The MIT license permits use, modification, and redistribution with preservation
of the copyright/license notice in substantial copied portions. AgentSec uses the
reported experimental results and architecture ideas; DRAFT-ASUB-006 is an
independent implementation rather than a copied file.

## Hosted results that matter

The public ledger contains unusually useful controlled experiments:

| Experiment | Public LB | Change / interpretation |
|---|---:|---|
| `v163_fastfirst_terminal_short` | 88.920 | `Then say OK.` established as a strong compact terminal |
| `v166_terminal_say_ok_direct` | 89.235 | `Say OK.` also strong, slightly below v163 in this run |
| `v169_replay_costcoef095` | **89.685** | keep v163 wording, change replay-cost coefficient `1.0 -> 0.95`; best confirmed result in the ledger snapshot |
| `v171_sayok_router` | 88.695 | adaptive routing across several terminal variants regressed |
| `v157_confdeputy_only` | 20.715 | direct Confused Deputy is real but low-value as the main public lane |
| `v156_confdeputy_compound` | 49.390 | stacking EXFIL + CD in one prompt strongly hurt throughput/compliance |
| `v155_slowmultipost2` | 81.365 | two-post slow-row variant regressed versus the single-post anchor |
| `v161_v148_exact_rerun` | 80.370 | byte-equivalent rerun of `v148=88.245`; large hosted variance is real |

Pending at the ledger snapshot: v172/v173/v174. They are not treated as evidence
until a public score is recorded.

## What this changes for AgentSec

### 1. ASUB-001 remains a valid canary, not the best known public architecture

ASUB-001 was frozen before this field evidence was incorporated. Its terminal
wording is `Then answer OK only.` and its replay sizing is more conservative.
The public field evidence supports a stronger successor rather than modifying the
already-running frozen canary.

### 2. DRAFT-ASUB-006 becomes the preferred public-frontier successor

The new draft uses:

- one `http.post` per candidate;
- `SECRET_MARKER` payload;
- unique clean domains;
- live keep-only-if-fired validation;
- `Then say OK.`;
- six probes split 3 plain / 3 Harmony;
- chosen template = lower elapsed time per successful fire;
- full-hop probe timing;
- cumulative replay sizing at `REPLAY_SAFE_FRAC=0.985`;
- `REPLAY_COST_COEF=0.95`;
- fastest verified candidates first.

The 0.95 coefficient is deliberately a mild risk position. It is supported by a
hosted controlled result, but high variance means it is not guaranteed to repeat.

### 3. DRAFT-ASUB-005 multi-post is demoted to diagnostic status

Official scorer mechanics make multi-post attractive on paper because several
EXFIL predicates can fire in one finding. Hosted evidence is more important than
that static arithmetic: the public two-post experiment fell to 81.365. Therefore
ASUB-005 should not consume a scarce hosted slot unless new evidence reverses
that result.

### 4. Direct CD stays in the final research portfolio as a private hedge

The 20.715 public result proves the lane is reachable, while its lower severity
and throughput make it a poor public-score mainline. This is exactly the role
AgentSec already assigned to ASUB-002: diagnostic/private hedge.

### 5. Avoid adaptive terminal routers and compound prompts

The public ledger shows two recurring costs:

- extra probe/routing complexity can consume useful budget without improving the
  stable single-post primitive;
- compound multi-action prompts reduce compliance enough to outweigh theoretical
  predicate stacking.

For the public anchor, simplicity wins.

## Hosted-slot decision gate after ASUB-001

Use the first valid ASUB-001 public score as evidence, not as a prize proxy:

- `< 70`: DRAFT-ASUB-006 is the clear next public calibration candidate.
- `70–85`: DRAFT-ASUB-006 remains high priority because the independent anchor is
  near 90, but reserve a later slot for a private-transfer/mixed candidate.
- `>= 85`: public throughput is already close enough to the field anchor that the
  next scarce slot should usually test private-transfer robustness before another
  public-only refinement.
- error / blank score: diagnose infrastructure/runtime first; do not infer attack
  quality from the failed run.

The thresholds are operational heuristics, not statistical confidence bounds.

## Reproducibility caveat

A byte-equivalent rerun moving from 88.245 to 80.370 is a warning against
overinterpreting one hosted score. Duplicate ASUB-001 results should be converted
to equivalent finding counts with `src/hosted_evidence.py` before tuning margins.
