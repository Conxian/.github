# Conxian — Organization Agent Baseline

Org-wide defaults for AI agents working across the Conxian ecosystem. This is the
"rules" layer of the agentic BOS (Business Operating System). A repo-level
`AGENTS.md` overrides these where more specific; the nearest `AGENTS.md` wins.

## Ecosystem context (single source of truth)
- **Canonical KB / registry**: `Conxian/.github-private`
  (`docs/ECOSYSTEM_REGISTRY.json`, `ECOSYSTEM_STATE.md`, `GOVERNANCE_ENFORCEMENT.md`).
- **Forward change delivery**: ordinary work → `dev → staged → main`.
  `main` is the production/default branch; `dev` is integration and `staged`
  is the release candidate. Reverse `main → staged → dev` reconciliation
  preserves already accepted changes; it is not forward release promotion.
  Follow each repository's current promotion policy and exact candidate evidence.
- **Governance repos** (`.github`, `.github-private`) flow `main`-direct via
  human review; they are outside the promotion chain.
- **Read before extending work**: inspect current repository heads, the nearest
  agent guidance, linked issues and the newest canonical KB checkpoint. Older
  continuity notes are dated evidence and must not override newer verified state.

## Non-negotiable rules
- Never commit secrets, tokens, or keys; use org/repo secrets.
- Do not modify branch-protection rulesets or org governance files without
  human review.
- Rust repos: MSRV **1.98.1**; run
  `cargo clippy --all-targets --all-features -- -D warnings` before push.
- JS/Node repos: **Node 24+** is the locked toolchain standard. Do not downgrade
  `node-version`, `engines.node`, `.nvmrc`, or toolchain-check scripts below 24 —
  downgrades are autorejected by CI (`toolchain-guard`).
- Security-first (OD-01): production deploys require multisig/TEE storage.
  A provider label, feature flag or successful build does not establish that
  requirement; preserve operation-specific evidence and independent review.

## Universal-chain scope and evidence

Conxian serves chains, networks, layers and assets with Bitcoin L1 as the
canonical trust/finality root. Bitcoin-rooted does not mean Bitcoin-only.
External assets, bridges and independently evidenced staking adapters remain
in scope. Conxian introduces no native token, native staking incentive or
speculative tokenomics. Public protocol/developer work and commercial managed
services retain their owning repository boundaries and licenses.

Keep identifiers, assets, protocol modules, evidence records, runtime
registrations, observed connections and production-qualified operations
separate. Read current machine inventories and validators before publishing a
count. Neither a registry entry nor an aggregate count authorizes signing,
custody, execution or deployment. Preserve independently qualified capabilities;
resolve uncertain claims through their specific evidence and acceptance gates.

## Priorities within universal-chain scope
- **Core**: Bitcoin/UTXO (Bitcoin, Stacks, Liquid, Babylon, BOB).
- **Secondary**: EVM (Ethereum, Base, Arbitrum, Optimism, Polygon) and
  Cosmos/IBC (Cosmos Hub, Osmosis, Celestia).
- Prefer burn-block-height (Nakamoto) readiness in all Stacks contracts (OD-04).
