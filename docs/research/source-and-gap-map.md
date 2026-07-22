# Research Source & Gap Map (2026-07-22 Update)

This document maps research evidence and organizational standards to the actual implementation status across the Conxian codebase. For BitVM3 and Groth16, the shared status is **Research / Evaluation Only**. See the [BitVM3 & Groth16 readiness document](./bitvm3-and-groth16-readiness.md) and the [canonical Gateway evidence report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md) for the detailed evidence gate.

## 🏛️ Ecosystem Alignment

| Research Area | Canonical Source | Gap / Status |
| --- | --- | --- |
| **Identity & Naming** | [profile/README.md](../../profile/README.md) | 🟢 Rebranding to *Conxius Orbit* complete. |
| **Governance** | [repository-taxonomy.md](../../repository-taxonomy.md) | 🟢 Taxonomy defined and synced to docs. |
| **Security Standards** | [SECURITY.md](../../SECURITY.md) | 🟢 Vulnerability reporting path standardized. |
| **Documentation Strategy** | [SOVEREIGN_PAGES.md](../SOVEREIGN_PAGES.md) | 🟢 Hub enhanced; decentralized strategy implemented. |

## 🛠️ Technical Implementation Gaps

| Area | Requirement | Current Status |
| --- | --- | --- |
| **CI/CD Hardening** | Fail-high gating on dependency reviews. | 🟢 Implemented in `standard-ci.yml`. |
| **Artifact Safety** | Prevent tracking of build artifacts. | 🟢 `verify_tracked_artifacts.py` active. |
| **Knowledge Retention** | Verify core memories and context. | 🟢 `verify_knowledge_retention.py` active. |
| **Script Provisioning** | Implementation of `verify_*` toolset. | 🟡 CON-1322: Toolset expanding. |
| **Protocol Verification** | Automated Clarity contract auditing. | 🟡 CON-1436: Nexus audit in progress. |
| **Production Infrastructure** | Unified UI deployment on conxian.org | 🟢 CON-1443: Provisioned on Render. |

## 🔬 BitVM3 / Groth16 Evidence Classification

| Evidence or surface | Current classification | Non-claim / gap |
| --- | --- | --- |
| **BitVM3 paper/protocol** | [ePrint 2026/933](https://eprint.iacr.org/2026/933) and the [BitVM3 paper](https://bitvm.org/bitvm3.pdf) are paper/protocol research evidence for garbled-circuit bridge/core constructions. | No stable SDK, production API, audit, deployment, or Conxian implementation follows from the paper. |
| **Bitcoin mainnet upstream artifact** | The [BitVMX SNARK prototype article](https://bitvmx.org/knowledge/a-new-era-for-bitcoin-successful-snark-proof-verification-with-bitvmx) and linked [transaction](https://mempool.space/tx/75eb2ad4f22263440fc4ceb61c51b0bb77721661dbfbec961358520b04107ec3) are upstream prototype evidence. | This is not BitVM3-GC, a stable SDK, a production bridge, a Conxian verifier, or audit evidence. |
| **Signet and public testnet** | The [official BitVM demo](https://github.com/BitVM/bitvm.github.io/tree/main/demo) is a signet/`bitvmnet` developer preview; [Union Bridge](https://bitvmx.org/knowledge/union-bridge-reaches-testnet-a-milestone-for-bitvmx-powered-bitcoin-bridging) is experimental Rootstock Testnet evidence. | Network-specific demos and testnet milestones must not be relabeled as Bitcoin mainnet or Conxian production evidence. |
| **SDK/reference maturity** | Official and reference repositories remain developer preview, under development, unaudited, WIP, toy, or research/reference code as recorded in the [canonical Gateway report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md). | Repository presence, an SDK label, or a local build does not satisfy the production gate. |
| **Shared readiness status** | **Research / Evaluation Only**. | Any missing, contradictory, or upstream-only gate keeps this status unchanged. |

## 📉 Critical Smart Contract Gaps (Sprint 2026-07)

| Issue | Severity | Status |
| --- | --- | --- |
| **Admin Centralization** | 🔴 CRITICAL | CON-1422: 73+ admin vars controlled by single key. |
| **No Upgrade Path** | 🔴 CRITICAL | CON-1423: Contracts permanently immutable. |
| **Tautology Bugs** | 🔴 CRITICAL | CON-1424: Anyone can become owner of core contracts. |
| **Stub Contracts** | 🟡 HIGH | CON-1434: 33% of contracts are placeholders. |

## 🧭 Conxian BitVM3 / Groth16 Gap Map

The [canonical Gateway report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md) separates these local classifications. None is evidence of a production BitVM3, BitVMX-GC, recursive-Groth16, or pairing-verifier deployment.

| Surface | Current implementation evidence | Durable remediation |
| --- | --- | --- |
| **Gateway** | A backend-neutral injected-verifier boundary exists, but no production pairing backend is wired. The legacy `verify_state_proof` path remains metadata-only and must not be treated as cryptographic verification. | [Gateway #189](https://github.com/Conxian/conxian-gateway/issues/189) remains open and research-only. |
| **Platform** | BitVM-related paths are simulations/scaffolds and can produce success-shaped results without cryptographic verification. | [Platform #1187](https://github.com/Conxian/conxius-platform/issues/1187) |
| **Nexus** | A narrow local Arkworks Groth16 call exists, but state roots are not bound by that path, negative coverage is incomplete, and metadata/ownership/revision drift remains. | [Nexus #169](https://github.com/Conxian/conxian-nexus/issues/169) |
| **Wallet** | TypeScript/Android paths generate simulation segments and success-shaped results; no actual verifier is present. | [Wallet #427](https://github.com/Conxian/conxius-wallet/issues/427) |
| **Core** | Structural verifier boundaries and fail-closed policy exist; dependencies alone do not establish a current BitVM2/Groth16 verification call. | [Core #188](https://github.com/Conxian/lib-conxian-core/issues/188) |
| **Enclave** | The BitVM2 boundary is typed, fail-closed, and unsupported for proof verification; MuSig2 signing is not SNARK verification. | [Enclave #202](https://github.com/Conxian/conxius-enclave-sdk/issues/202) |

## 🔬 Protocol Research Alignment (2026-07)

| Research Feature | Implementation Status | Action Required |
| --- | --- | --- |
| **RGB v0.11.1 Pivot** | 🔴 BLOCKED | Replace `rgb-core` v0.12 with `rgb-lib` v0.11.1 (Tether compatible). |
| **BitVM3 / Groth16 Readiness** | 🟡 RESEARCH / EVALUATION ONLY | Keep the backend-neutral Gateway boundary and evaluate a separately owned verifier candidate against the [production-readiness gate](./bitvm3-and-groth16-readiness.md). Do not modify legacy `verify_state_proof` as a substitute for cryptographic verification. |
| **LDK Node v0.4+** | 🟡 RESEARCH | Replace `SimulatedLightningBackend` with real LDK Node implementation. |
| **DLC Integration** | 🟡 RESEARCH | Implement real CET construction using `rust-dlc`. |
| **ISO 20022 Treasury** | 🟡 GAP | Implement `camt.053/054` for institutional bank statements. |

## 📈 Roadmap for Remediation

1.  **Phase 1: Standardization (Complete):** Unified README and Docs standards deployed organization-wide.
2.  **Phase 2: Automation (Active):** Deploy standardized CI/CD and security gates across all core protocols.
3.  **Phase 3: Verification (In Progress):** Remediate critical smart contract vulnerabilities and stub implementations.

## Production-readiness decision rule

Before any BitVM3, BitVMX-GC, Groth16, or related verifier is described as production-ready, require all of the following for the exact source/revision and deployment role: named ownership, CI-backed positive and negative tests, immutable reproducible artifacts and provenance, license clarity, network-specific evidence, independent security review, protocol/economic review, resource and operational limits, and safe Conxian integration across Gateway, Platform, Nexus, Wallet, Core, and Enclave.

Any missing, contradictory, or upstream-only gate keeps the status at **Research / Evaluation Only**. A paper, repository, SDK, demo, mainnet transaction, or local verifier call does not alone establish Conxian production readiness.

---

*Updated for the 2026-07-22 Gateway evidence refresh. Upstream evidence remains classified separately from Conxian implementation status.*
