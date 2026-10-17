# Conxian GitHub Organization Governance 🧪

### Public defaults and documentation guidance for the Conxian ecosystem

> **Status:** 🟢 Operational (governance defaults) | **Node:** ZA-GP-MID | **Protocol:** Non-Custodial | **Model:** Sovereign Autonomous Business (SAB)

Welcome to the public organization-defaults repository for **Conxian Labs**. This repository defines shared community health files, security baselines, and contribution standards for the Conxian GitHub organization.

For the canonical identity mapping and ecosystem overview, see **[profile/README.md](profile/README.md)**.

## Purpose

Provide org-wide defaults (community health files, templates, and governance policies) for the Conxian GitHub organization.

## Status

Active. This repository serves as the source of truth for organization-wide governance and documentation standards. Work is tracked exclusively in GitHub Issues and linked pull requests; see the [issue-only workflow](docs/issue-only-itil5-workflow.md).

## Ecosystem Hub

The unified documentation hub is available at **[conxian.github.io](https://conxian.github.io/)**.

---

## 🏛️ Ecosystem Architecture: The Vertical Sovereignty Model

Conxian Labs builds infrastructure for the public Conxian ecosystem. Our strategy is to keep protocol and product surfaces aligned so users can access end-to-end sovereign financial tooling. Repository status below means active development; it is not a production-readiness or release certification (see [release discipline](docs/release-discipline.md)).

### 1. The Vault: [Conxius Wallet](https://github.com/Conxian/conxius-wallet)
- **Role:** Sovereign Access.
- **Focus:** Android-first, hardware-secured (**StrongBox/TEE**) Bitcoin and Lightning node services.
- **Status:** 🟢 Active development.

### 2. The Engine: [Conxian Nexus](https://github.com/Conxian/conxian-nexus)
- **Role:** Observation and Proof Layer.
- **Focus:** Universal-chain observation, synchronization, and verification ("Glass Node"); observes and proves, while execution stays in the Gateway.
- **Status:** 🟢 Active development.

### 3. The Pipe: [Conxian Gateway](https://github.com/Conxian/conxian-gateway)
- **Role:** Unified Backend.
- **Focus:** High-performance Rust gateway and institutional bridge (ISO 20022).
- **Status:** 🔄 Active development.

### 4. The UI: [Conxius Platform](https://github.com/Conxian/conxius-platform)
- **Role:** Control Plane and Orchestration Surface.
- **Focus:** Routing and orchestration across the stack; no custody or direct protocol execution.
- **Status:** 🟢 Active development.

### Supporting surfaces
- **Shared Primitives:** [lib-conxian-core](https://github.com/Conxian/lib-conxian-core): deterministic, offline protocol primitives.
- **Security SDK:** [conxius-enclave-sdk](https://github.com/Conxian/conxius-enclave-sdk): hardware-backed signing and attestation (beta/conditional).
- **Marketplace:** [conxian_market](https://github.com/Conxian/conxian_market): discovery, settlement, and escrow for autonomous AI labor.
- **Governance:** [conxian-business](https://github.com/Conxian/conxian-business): public-safe BOS governance and CI/CD orchestration.

Retired repositories (`Conxian`, `conxian_ui`, `conxius-orbit`) are no longer live surfaces.

---

## 🏗️ Unified Infrastructure Strategy

To maintain high-performance standards and eliminate redundant development, the ecosystem is built upon:

- **Unified Backend:** The Conxian Gateway serves as the centralized logic hub.
- **Shared Primitives:** All core protocol logic is extracted into **`lib-conxian-core`**.
- **Decentralized Messaging:** Communication is unified via **Nostr** relays and **Render** telemetry.

---

## 📂 Repository Structure

- **`docs/`**: Unified ecosystem documentation hub.
- **`profile/`**: The [public organization profile](profile/README.md).
- **`docs/scorecards/`**: [Canonical templates](./docs/scorecards/README.md) for readiness reviews.
- **`REVIEWS.md`**: Comparative benchmarks against industry leaders.
- **`CONTRIBUTING.md`**: Protocols for participating in the Bitcoin Renaissance.

---

## ⚖️ Governance & Licensing

We prioritize logical sovereignty. Administrative standards are licensed under **MIT**. Individual product repositories utilize strategic licenses (**BSL 1.1**, **GPL v3**, or **MIT**) based on their role within the decentralized ecosystem.

---

**CONXIAN LABS (PTY) LTD // ALL RIGHTS RESERVED // 2026**

> _"Architecting the rails where the user owns the train."_
