# Experiments — AgentSec

Store promoted experiment summaries and lightweight reproducibility artifacts here.

Recommended layout:

`experiments/AEXP-YYYYMMDD-NNN-short-name/`

Each promoted experiment should contain at least:

- `README.md` — hypothesis, setup, result, decision
- `config.*` — exact parameters when applicable
- `metrics.*` — machine-readable summary when applicable
- references to larger external/Kaggle artifacts if they cannot live in Git

Avoid committing large generated traces unless they are uniquely valuable. Prefer compact summaries plus hashes/locations.
