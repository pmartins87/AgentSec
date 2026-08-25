# Source architecture — AgentSec

Implementation should evolve toward small, testable components rather than one opaque notebook.

## Intended modules

- environment adapter / official SDK boundary
- trace recorder and canonicalizer
- candidate representation
- replay verifier
- predicate classifier
- search policy interfaces
- mutation operators
- novelty/archive manager
- runtime budget allocator
- scoring/prioritization utilities
- Kaggle packaging layer that emits `attack.py`

## Design constraints

- deterministic behavior where possible
- no hidden network dependency
- explicit random seeds
- graceful handling of failed/no-op tool calls
- cheap logging disabled or minimized in final hosted runs
- competition entrypoint kept thin; core logic should remain testable outside the notebook

No production attack code has been added yet. Official starter assets should be imported and versioned before implementing the first baseline.
