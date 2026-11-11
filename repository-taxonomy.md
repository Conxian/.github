# Conxian repository taxonomy

This document defines the intended role of public repositories in the Conxian GitHub organization.

Identity boundary used in this taxonomy: **Conxian** = protocol/public ecosystem. **Conxian Labs** = builder/operator/company. For canonical naming, see [profile/README.md#canonical-identity](profile/README.md#canonical-identity).

## Categories

### Shared core libraries

Reusable libraries and shared primitives consumed by multiple Conxian services or applications.

- `lib-conxian-core`: Reusable deterministic primitives and shared ecosystem logic.
- `conxius-enclave-sdk`: SDK for hardware-secured execution environments.

### Product and interface surfaces

Public-facing applications, middleware, wallets, marketplaces, and API layers.

- `conxius-wallet`: Sovereign wallet and reference client.
- `conxian-gateway`: Middleware, indexing, and institutional integration surface.
- `conxian-nexus`: Universal-chain observation, verification, and proof layer.
- `conxian_market`: Discovery, settlement, and escrow for autonomous AI labor.

### Operating and readiness metrics

Canonical templates and scorecards for ecosystem governance.

- `docs/scorecards/` (in `.github`): Executive and cross-lane readiness scorecards.

### Labs and organization surfaces

Public organization defaults, governance, and corporate/public information surfaces.

- `.github`: Public organization defaults and shared community health files.
- `conxian-business`: Public-safe BOS governance, CI/CD orchestration, and specification surface.
- `conxian-labs-site`: Corporate and public information site.
- `conxian-org-site`: Organization website.

### Platform and environment scaffolding

Development and control-plane tooling that may require periodic review to ensure no sensitive operational material is exposed publicly.

- `conxius-platform`: Control plane, orchestration, and environment scaffolding.

### Retired

No longer live surfaces; retained here only so historical references resolve.

- `Conxian`: Former Stacks-native protocol repository (deleted).
- `conxian_ui`: Former public application interface (deleted).
- `conxius-orbit`: Former ecosystem coordination and deployment tooling (deleted; superseded by `conxius-platform`).
- `conxian.github.io`: Former public documentation hub (**archived** 2026-11-01; the org Pages surface is retired — production authority is `conxian-labs-site` on Render).

## Public/private rule

Public repositories may contain:

- open-source protocol code
- public apps and SDKs
- deployment templates without secrets
- governance and contribution guidance
- public technical documentation

Public repositories must not contain:

- legal drafts
- internal finance or business development records
- production credentials or secret-bearing environment files
- sensitive internal operational playbooks
- private partner material

## README minimum standard

Each public repository should state:

- purpose
- current status
- scope and boundaries
- governance relation
- security reporting path
- contact path
- license

## Repository metadata standard

Every public repository should set, via the GitHub API or the settings page:

- **Description** — one factual sentence (not a bare name or null).
- **Homepage** — a live `https://` URL on a canonical Conxian domain
  (`www.conxian-labs.com` for corporate/product surfaces, `conxian.org` for the
  protocol surface). Do **not** point at retired hosts (e.g. `*.vercel.app`,
  `conxian-labs-site-*.onrender.com`).
- **Topics** — at least three searchable topics drawn from the repository's role
  (e.g. `bitcoin`, `rust`, `settlement`, `iso20022`, `wallet`, `sdk`).
- **License** — an OSI-approved SPDX license (a funding and reuse gate).

Metadata is part of the public surface; keep it accurate and non-secret. A null
or stale homepage, an empty topic list, or a placeholder description is a
documentation defect.
