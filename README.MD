# Conxian GitHub Organization Governance 🧪

### Public defaults and documentation guidance for the Conxian ecosystem

> **Status:** 🟢 Operational | **Node:** ZA-GP-MID | **Protocol:** Non-Custodial | **Model:** Sovereign Autonomous Business (SAB)

Welcome to the public organization-defaults repository for **Conxian Labs**. This repository defines shared community health files, security baselines, and contribution standards for the Conxian GitHub organization.

For the canonical identity mapping and ecosystem overview, see **[profile/README.md](profile/README.md)**.

## Purpose

Provide org-wide defaults (community health files, templates, and governance policies) for the Conxian GitHub organization.

Canonical identity statement: see [profile/README.md#canonical-identity](profile/README.md#canonical-identity).

## Status

Active. Changes in this repository can affect defaults across Conxian public repositories.

## Ownership

Ownership and review requirements are defined in [`CODEOWNERS`](./CODEOWNERS).

---

## 🏛️ Ecosystem Architecture: The Vertical Sovereignty Model

Conxian Labs builds infrastructure for the public Conxian ecosystem. Our strategy is to keep protocol and product surfaces aligned so users can access end-to-end sovereign financial tooling.

### 1. The Vault: [Conxius Wallet](https://github.com/Conxian/conxius-wallet)

- **Role:** Sovereign Access.
- **Focus:** Android-first, hardware-secured (**StrongBox/TEE**) Bitcoin and Lightning node services.
- **Status:** 🟢 Active.

### 2. The Engine: [Conxian Protocol Core](https://github.com/Conxian/Conxian)

- **Role:** Protocol Core.
- **Focus:** Canonical public smart-contract and protocol settlement logic for the Conxian ecosystem.
- **Status:** 🟢 Production Ready.

### 3. The Pipe: [Conxian Gateway](https://github.com/Conxian/conxian-gateway)

- **Role:** Unified Backend.
- **Focus:** High-performance Rust gateway providing a single entry point for all client applications and institutional bridges.
- **Status:** 🔄 Unified Infrastructure.

### 4. The Lens: [Conxian Interface](https://github.com/Conxian/conxian_ui)

- **Role:** Unified Interface.
- **Focus:** Comprehensive web interface for seamless interaction across all Conxian protocols.
- **Status:** 🟢 Active.

---

## 🏗️ Unified Infrastructure Strategy

To maintain high-performance standards and eliminate redundant development, the ecosystem is built upon:

- **Unified Backend:** The Conxian Gateway serves as the centralized logic hub.
- **Shared Primitives:** All core protocol logic is extracted into **`lib-conxian-core`**.
- **Decentralized Messaging:** Communication is unified via **Nostr** relays and **Render** telemetry.

---

## 📂 Repository Structure

- **`profile/`**: The [public organization profile](profile/README.md), including the canonical Conxian/Conxian Labs identity statement.
- **`REVIEWS.md`**: Comparative benchmarks against industry leaders.
- **`CONTRIBUTING.md`**: Protocols for participating in the Bitcoin Renaissance.

---

## ⚖️ Governance & Licensing

We prioritize logical sovereignty. Administrative standards are licensed under **MIT**. Individual product repositories utilize strategic licenses (**BSL 1.1**, **GPL v3**, or **MIT**) based on their role within the decentralized ecosystem.

---

**CONXIAN LABS (PTY) LTD // ALL RIGHTS RESERVED // 2026**

> _"Architecting the rails where the user owns the train."_
