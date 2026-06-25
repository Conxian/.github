# Conxian

Public repositories for the Conxian protocol / DAO layer and the Conxian-Labs builder / operator layer.

> **Status:** Operational · **Model:** Zero-custody, zero-raw-data infrastructure · **Identity split:** Conxian (protocol / DeFi / DAO-facing) + Conxian-Labs (builder / operator / company-facing)

## Purpose

This GitHub organization is the public code and documentation surface for the broader Conxian ecosystem.

- **Conxian** = protocol, DeFi, DAO-facing, and public ecosystem assets.
- **Conxian-Labs** = builder / operator / company responsible for shipping, supporting, and explaining public products and infrastructure around the ecosystem.

Company operations, legal work, financial administration, and other sensitive internal workflows are managed separately from this public codebase.

## Canonical identity

- **Conxian** = protocol / DeFi / DAO-facing identity.
- **Conxian-Labs** = builder / operator / company-facing identity.

## Core public surfaces

| Surface | Repository | Role |
| --- | --- | --- |
| Protocol core | [Conxian](https://github.com/Conxian/Conxian) | Canonical protocol and DAO-facing logic |
| Shared protocol libraries | [lib-conxian-core](https://github.com/Conxian/lib-conxian-core) | Reusable primitives and shared ecosystem logic |
| Enclave SDK | [conxius-enclave-sdk](https://github.com/Conxian/conxius-enclave-sdk) | SDK for hardware-secured execution environments |
| Wallet | [conxius-wallet](https://github.com/Conxian/conxius-wallet) | Sovereign wallet and reference client |
| Interface | [conxian_ui](https://github.com/Conxian/conxian_ui) | Public interaction and application-facing interface |
| Gateway | [conxian-gateway](https://github.com/Conxian/conxian-gateway) | Middleware and integration surface |
| Nexus | [conxian-nexus](https://github.com/Conxian/conxian-nexus) | Cross-chain verification and state support |
| Platform scaffolding | [conxius-platform](https://github.com/Conxian/conxius-platform) | Environment and orchestration scaffolding |
| Protocol tooling | [conxius-orbit](https://github.com/Conxian/conxius-orbit) | Ecosystem coordination and deployment tooling |
| Labs site | [conxian-labs-site](https://github.com/Conxian/conxian-labs-site) | Conxian-Labs portfolio and public information site |

## Pinned repositories (recommended order)

When org pins are updated, list protocol / DAO-facing surfaces first, support and access surfaces next, and Labs narrative surfaces last.

| Order | Repository | Rationale |
| --- | --- | --- |
| 1 | [Conxian](https://github.com/Conxian/Conxian) | Canonical protocol and DAO-facing reference point. |
| 2 | [lib-conxian-core](https://github.com/Conxian/lib-conxian-core) | Shared protocol primitives reused across ecosystem repositories. |
| 3 | [conxius-wallet](https://github.com/Conxian/conxius-wallet) | Sovereign wallet reference client for ecosystem participants. |
| 4 | [conxian_ui](https://github.com/Conxian/conxian_ui) | Primary public interaction surface for users. |
| 5 | [conxian-gateway](https://github.com/Conxian/conxian-gateway) | Integration surface for external systems and service connectivity. |
| 6 | [conxian-labs-site](https://github.com/Conxian/conxian-labs-site) | Conxian-Labs portfolio and company-facing information surface. |

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
