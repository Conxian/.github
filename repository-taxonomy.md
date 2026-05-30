# Conxian repository taxonomy

This document defines the intended role of public repositories in the Conxian GitHub organization.

Identity boundary used in this taxonomy: **Conxian** = protocol/public ecosystem. **Conxian Labs** = builder/operator/company.

## Categories

### Protocol core
Canonical smart-contract or protocol logic.

- `Conxian/Conxian`

### Protocol tooling
Deployment, coordination, or ecosystem tooling used around protocol development.

- `conxius-orbit`

### Shared core libraries
Reusable libraries and shared primitives consumed by multiple Conxian services or applications.

- `lib-conxian-core`
- `conxius-enclave-sdk`

### Product and interface surfaces
Public-facing applications, middleware, wallets, and API layers.

- `conxius-wallet`
- `conxian_ui`
- `conxian-gateway`
- `conxian-nexus`

### Labs and organization surfaces
Public organization defaults and corporate/public information surfaces.

- `.github`
- `conxian-labs-site`

### Platform and environment scaffolding
Development and control-plane tooling that may require periodic review to ensure no sensitive operational material is exposed publicly.

- `conxius-platform`

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
