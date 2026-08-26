# Authority-strict private stress scenario — 2026-08-26

## Problem found

The original robust optimizer had a hidden assumption inside its *synthetic*
scenario table: direct Confused Deputy survived every private-defense philosophy
at a relatively high rate, including `private_semantic_auth`.

That is too optimistic. A semantic authorization/authority guard is exactly the
kind of defense that may recognize “notify this recipient” as an ambient-authority
share and deny it, even though the literal public scorer still calls it
CONFUSED_DEPUTY.

## Correction

Do not rewrite the old scenario history. Add a fifth explicit stress case:

`private_authority_strict`

Synthetic effective-hit rates:

| lane | rate |
|---|---:|
| public_exfil | 0.08 |
| direct_cd | 0.10 |
| semantic_email | 0.55 |
| semantic_http | 0.60 |
| semantic_shell | 0.50 |
| semantic_write | 0.60 |

These values are intentionally scenario assumptions, not probabilities or
private-evaluator measurements.

## Minimax consequence

With 360 candidates, 12-candidate quantization and a 12-candidate floor per lane,
the original four-scenario minimax plan was:

- public_exfil 144
- direct_cd 72
- semantic_email 108
- semantic_http 12
- semantic_shell 12
- semantic_write 12

Adding the authority-strict scenario changes the deterministic coarse optimum to:

- public_exfil 144
- direct_cd 60
- semantic_email 120
- semantic_http 12
- semantic_shell 12
- semantic_write 12

Only 12 candidates move: direct-CD → semantic-email. This is a useful result: the
portfolio was already fairly robust, but it was modestly overexposed to CD.

## Promotion decision

Do **not** mutate DRAFT-ASUB-004 immediately just because the synthetic optimizer
moved one quantum. First make the expanded planner part of CI, then combine it
with the first hosted ASUB-001 evidence. If the hosted public canary is strong,
the final private-aware draft should adopt the 144/60/120/12/12/12 baseline unless
new evidence points elsewhere. If the public canary is weak because of
infrastructure/runtime rather than attack behavior, preserve uncertainty and do
not overfit the mix to that score.
