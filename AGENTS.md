# Conxian — Organization Agent Baseline

Org-wide defaults for AI agents working across the Conxian ecosystem. This is the
"rules" layer of the agentic BOS (Business Operating System). A repo-level
`AGENTS.md` overrides these where more specific; the nearest `AGENTS.md` wins.

## Ecosystem context (single source of truth)
- **Canonical KB / registry**: `Conxian/.github-private`
  (`docs/ECOSYSTEM_REGISTRY.json`, `ECOSYSTEM_STATE.md`, `GOVERNANCE_ENFORCEMENT.md`).
- **Branch model**: `main → staged → dev` promotion chain. Forward
  `auto-promotion.yml` plus reverse reconciliation
  (`conxian-business/scripts/reconcile_branches.py`).
- **Governance repos** (`.github`, `.github-private`) flow `main`-direct via
  human review; they are outside the promotion chain.

## Non-negotiable rules
- Never commit secrets, tokens, or keys; use org/repo secrets.
- Do not modify branch-protection rulesets or org governance files without
  human review.
- Rust repos: MSRV **1.98.1**; run
  `cargo clippy --all-targets --all-features -- -D warnings` before push.
- Security-first (OD-01): production deploys require multisig/TEE storage.

## Tier-1 chain focus
- **Core**: Bitcoin/UTXO (Bitcoin, Stacks, Liquid, Babylon, BOB).
- **Secondary**: EVM (Ethereum, Base, Arbitrum, Optimism, Polygon) and
  Cosmos/IBC (Cosmos Hub, Osmosis, Celestia).
- Prefer burn-block-height (Nakamoto) readiness in all Stacks contracts (OD-04).
