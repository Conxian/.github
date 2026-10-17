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
- `conxian.github.io`: Public documentation hub.

### Platform and environment scaffolding

Development and control-plane tooling that may require periodic review to ensure no sensitive operational material is exposed publicly.

- `conxius-platform`: Control plane, orchestration, and environment scaffolding.

### Retired

No longer live surfaces; retained here only so historical references resolve.

- `Conxian`: Former Stacks-native protocol repository (deleted).
- `conxian_ui`: Former public application interface (deleted).
- `conxius-orbit`: Former ecosystem coordination and deployment tooling (deleted; superseded by `conxius-platform`).

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
