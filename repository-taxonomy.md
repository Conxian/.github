# Conxian repository taxonomy

This document defines the intended role of public repositories in the Conxian GitHub organization.

Identity boundary used in this taxonomy: **Conxian** = protocol/public ecosystem. **Conxian Labs** = builder/operator/company. For canonical naming, see [profile/README.md#canonical-identity](profile/README.md#canonical-identity).

## Categories

### Protocol core

Canonical smart-contract or protocol logic.

- `Conxian/Conxian`: Canonical smart-contract and protocol logic.

### Protocol tooling

Deployment, coordination, or ecosystem tooling used around protocol development.

- `conxius-orbit`: Ecosystem coordination and deployment tooling.

### Shared core libraries

Reusable libraries and shared primitives consumed by multiple Conxian services or applications.

- `lib-conxian-core`: Reusable primitives and shared ecosystem logic.
- `conxius-enclave-sdk`: SDK for hardware-secured execution environments.

### Product and interface surfaces

Public-facing applications, middleware, wallets, and API layers.

- `conxius-wallet`: Sovereign wallet and reference client.
- `conxian_ui`: Public application interface.
- `conxian-gateway`: Middleware, indexing, and institutional integration surface.
- `conxian-nexus`: Cross-chain maneuver orchestration and state verification.

### Operating and readiness metrics

Canonical templates and scorecards for ecosystem governance.

- : Executive and cross-lane readiness scorecards.

### Labs and organization surfaces

Public organization defaults and corporate/public information surfaces.

- `.github`: Public organization defaults and shared community health files.
- `conxian-labs-site`: Corporate and public information site.

### Platform and environment scaffolding

Development and control-plane tooling that may require periodic review to ensure no sensitive operational material is exposed publicly.

- `conxius-platform`: Declarative NixOS control plane and environment scaffolding.

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
