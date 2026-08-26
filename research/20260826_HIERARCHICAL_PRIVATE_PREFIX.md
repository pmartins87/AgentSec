# Hierarchical private-prefix coverage

Date: 2026-08-26

## Scope

Authorized Kaggle AI Agent Security – Multi-Step Tool Attacks sandbox only. This is an ordering analysis over the existing AgentSec private-hypothesis portfolio; it makes no claim about the hidden private guardrail.

## Observation

ASUB-009 improves on weighted-only ASUB-008 by placing every active **family** once before any family repeats. That guarantees full family coverage by position 11.

However, the current family declaration order contains multiple families from the same higher-level lane next to one another:

1. `public_exfil`
2. `direct_synonym` — lane `direct_cd`
3. `direct_launder` — lane `direct_cd`
4. `web_email` — lane `semantic_email`
5. `inbox_email` — lane `semantic_email`
6. `web_http` — lane `semantic_http`
7. `inbox_http` — lane `semantic_http`
8. `web_shell` — lane `semantic_shell`
9. `inbox_shell` — lane `semantic_shell`
10. `web_write` — lane `semantic_write`
11. `inbox_write` — lane `semantic_write`

If a private replay were truncated extremely early, positions 3 and 5 spend scarce prefix capacity on a second mechanism/source variant from a lane already represented while other lanes have not appeared yet.

## Hierarchical alternative

A lane-first round-robin prelude first emits one family from each distinct lane:

1. `public_exfil`
2. `direct_synonym`
3. `web_email`
4. `web_http`
5. `web_shell`
6. `web_write`

Only then does it emit the second family from lanes that have one:

7. `direct_launder`
8. `inbox_email`
9. `inbox_http`
10. `inbox_shell`
11. `inbox_write`

After this 11-item prelude, the same exact weighted tail can resume. Therefore total candidate counts, family weights and long-prefix behavior can remain unchanged; only the earliest ordering differs.

## Deterministic prefix comparison

Distinct high-level lanes reached by prefix length:

| Prefix | ASUB-009 family-first | Hierarchical lane-first |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 4 |
| 5 | 3 | 5 |
| 6 | 4 | **6** |
| 7 | 4 | 6 |
| 8 | 5 | 6 |
| 9 | 5 | 6 |
| 10 | 6 | 6 |
| 11 | 6 | 6 |

Discrete lane-coverage AUC over positions 1–11:

- ASUB-009 family-first: **41**
- hierarchical lane-first: **51**
- relative increase: **24.4%**

The most intuitive result is prefix 6: ASUB-009 has reached 4 of 6 high-level lanes, while lane-first ordering has reached all 6.

## Interpretation

This does **not** prove higher private score. It proves a narrower property: under ignorance about which high-level private mechanism survives, lane-first ordering dominates family-first ordering on early high-level hypothesis coverage without changing the eventual family set.

That property is especially relevant only because replay timeout now preserves the scored prefix. Under a very early truncation, each replay position has option value; spending the first six positions on six different high-level hypotheses is a cleaner robust policy than repeating two lanes before the other four are all represented.

## Next implementation gate

The analysis is implemented in:

- `src/prefix_coverage.py`
- `scripts/analyze_private_prefix.py`
- `tests/test_prefix_coverage.py`

If CI confirms the analysis tooling, the next private research draft should be **DRAFT-ASUB-017 private hedge v5 hierarchical-prefix**, changing only the ASUB-009 prelude order while preserving candidate construction, calibration, counts and weighted tail. Because the improvement is purely an ordering change, ASUB-009 remains a valid frozen candidate and ASUB-017 would be a clean ablation rather than a rewrite.
