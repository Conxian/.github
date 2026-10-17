# Conxian

Public repositories for the Conxian-Labs builder / operator layer.

> **Status:** Operational · **Model:** Zero-custody, zero-raw-data infrastructure · 

## Purpose

This GitHub organization is the public code and documentation surface for the broader Conxian ecosystem.

- **Conxian-Labs** = builder / operator / company responsible for shipping, supporting, and explaining public products and infrastructure around the ecosystem.

Company operations, legal work, financial administration, and other sensitive internal workflows are managed separately from this public codebase. Public work is tracked in GitHub Issues and linked pull requests.

## Canonical identity

- **Conxian-Labs** = builder / operator / company-facing identity.

## Core public surfaces

| Surface | Repository | Role |
| --- | --- | --- |
| Shared protocol libraries | [lib-conxian-core](https://github.com/Conxian/lib-conxian-core) | Reusable deterministic primitives and shared ecosystem logic |
| Enclave SDK | [conxius-enclave-sdk](https://github.com/Conxian/conxius-enclave-sdk) | SDK for hardware-secured execution environments (beta/conditional) |
| Wallet | [conxius-wallet](https://github.com/Conxian/conxius-wallet) | Sovereign wallet and reference client |
| Gateway | [conxian-gateway](https://github.com/Conxian/conxian-gateway) | Middleware and integration surface |
| Nexus | [conxian-nexus](https://github.com/Conxian/conxian-nexus) | Universal-chain observation, verification, and proof layer |
| Platform | [conxius-platform](https://github.com/Conxian/conxius-platform) | Control plane, orchestration, and environment scaffolding |
| Marketplace | [conxian_market](https://github.com/Conxian/conxian_market) | Discovery, settlement, and escrow for autonomous AI labor |
| Governance | [conxian-business](https://github.com/Conxian/conxian-business) | Public-safe BOS governance and CI/CD orchestration |
| Labs site | [conxian-labs-site](https://github.com/Conxian/conxian-labs-site) | Conxian-Labs portfolio and public information site |
| Organization site | [conxian-org-site](https://github.com/Conxian/conxian-org-site) | Organization website |

Retired repositories `Conxian`, `conxian_ui`, and `conxius-orbit` are no longer public surfaces.

## Pinned repositories (recommended order)

The retained target follows the canonical [#48 decision](https://github.com/Conxian/.github/issues/48#issuecomment-5078201839). Applying it is a manual organization-administrator action. The `Conxian` repository from that decision has since been retired, so it is no longer a pin target.

| Order | Repository | Rationale |
| --- | --- | --- |
| 1 | [conxius-wallet](https://github.com/Conxian/conxius-wallet) | End-user wallet and sovereign reference client. |
| 2 | [conxian-gateway](https://github.com/Conxian/conxian-gateway) | Integration path for external systems and service connectivity. |
| 3 | [conxius-enclave-sdk](https://github.com/Conxian/conxius-enclave-sdk) | Security SDK for hardware-secured execution environments. |
| 4 | [conxian-labs-site](https://github.com/Conxian/conxian-labs-site) | Portfolio entry point and public information surface. |
| 5 | [conxian.github.io](https://github.com/Conxian/conxian.github.io) | Documentation hub, after its basic metadata cleanup under [#53](https://github.com/Conxian/.github/issues/53). |

At the 2026-07-25 snapshot, the live organization pins were only `Conxian`, then `.github`. This recommendation does not claim that the target pins have been applied.

## Public repo standards

Public repositories in this organization should clearly state:

- purpose
- current status
- scope and boundaries
- governance relation
- security reporting path
- contact path
- license

## Contact

- General: [info@conxian-labs.com](mailto:info@conxian-labs.com)
- Support: [support@conxian-labs.com](mailto:support@conxian-labs.com)
- Security: [security@conxian-labs.com](mailto:security@conxian-labs.com)
- Partnerships and business: [partners@conxian-labs.com](mailto:partners@conxian-labs.com)

Official Labs site: [conxian-labs.com](https://conxian-labs.com)
