# Research Source & Gap Map (2026-09 Update)

This document maps research evidence and organizational standards to the actual implementation status across the Conxian codebase. For BitVM3 and Groth16, the shared status is **Research / Evaluation Only**. See the [BitVM3 & Groth16 readiness document](./bitvm3-and-groth16-readiness.md) and the [canonical Gateway evidence report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md) for the detailed evidence gate.

## 📊 Cross-Lane Readiness Scoring Index

| Lane | Domain | Current Score | Target Score | Key Blockers & Gaps |
| --- | --- | --- | --- | --- |
| **Lane 1** | Trust & Controls (Security) | **85%** | **100%** | Admin centralization (CON-1422), Tautology bugs in core contracts (CON-1424). |
| **Lane 2** | Release & Deployment Maturity (Ops) | **90%** | **100%** | Pinned Vercel CLI standard (CON-1323) & monorepo changelog automation (CON-1328). |
| **Lane 3** | Product & Technical Proof (Dev) | **65%** | **100%** | Smart contract stubs (CON-1434, 33% stubbed), BitVM3/Groth16 mock verifiers. |
| **Lane 4** | Commercial Claim Safety (Market) | **80%** | **100%** | ISO 20022 camt.053/054 treasury parser gap (CON-1348). |
| **Lane 5** | Ownership & Decision Clarity (Governance) | **95%** | **100%** | Unified Orbit CLI taxonomy enforcement (CON-1238). |

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
| **Script Provisioning** | Implementation of `verify_*` toolset. | 🟢 CON-1322: 5 core verification scripts fully active. |
| **Protocol Verification** | Automated Clarity contract auditing. | 🟡 CON-1436: Nexus audit in progress. |
| **Production Infrastructure** | Unified UI deployment on conxian.org | 🟢 CON-1443: Provisioned on Render. |

## 📉 Critical Smart Contract Gaps (Sprint 2026-09 Analysis)

| Issue ID | Severity | Impact | Status & Remediation Priority |
| --- | --- | --- | --- |
| **CON-1422** | 🔴 CRITICAL | 73+ admin vars controlled by single key; risk of key compromise taking down protocol parameters. | **P0 Candidate**: Multi-sig & governance timelock migration. |
| **CON-1423** | 🔴 CRITICAL | Contracts permanently immutable without native upgrade or proxy delegation mechanisms. | **P0 Candidate**: Implement SIP-009/SIP-010 compliant proxy dispatcher. |
| **CON-1424** | 🔴 CRITICAL | Tautology/owner validation bug allowing arbitrary callers to claim ownership of core contracts. | **P0 Candidate**: Remediation PR pending contract logic replacement. |
| **CON-1434** | 🟡 HIGH | 33% of Clarity smart contracts (23/71 contracts) are non-functional placeholders/stubs. | **P1 Candidate**: Implement functional Clarity logic for core stubs. |

## 🔬 BitVM3 / Groth16 Evidence Classification

| Evidence or surface | Current classification | Non-claim / gap |
| --- | --- | --- |
| **BitVM3 paper/protocol** | [ePrint 2026/933](https://eprint.iacr.org/2026/933) and the [BitVM3 paper](https://bitvm.org/bitvm3.pdf) are paper/protocol research evidence for garbled-circuit bridge/core constructions. | No stable SDK, production API, audit, deployment, or Conxian implementation follows from the paper. |
| **Bitcoin mainnet upstream artifact** | The [BitVMX SNARK prototype article](https://bitvmx.org/knowledge/a-new-era-for-bitcoin-successful-snark-proof-verification-with-bitvmx) and linked [transaction](https://mempool.space/tx/75eb2ad4f22263440fc4ceb61c51b0bb77721661dbfbec961358520b04107ec3) are upstream prototype evidence. | This is not BitVM3-GC, a stable SDK, a production bridge, a Conxian verifier, or audit evidence. |
| **Signet and public testnet** | The [official BitVM demo](https://github.com/BitVM/bitvm.github.io/tree/main/demo) is a signet/`bitvmnet` developer preview; [Union Bridge](https://bitvmx.org/knowledge/union-bridge-reaches-testnet-a-milestone-for-bitvmx-powered-bitcoin-bridging) is experimental Rootstock Testnet evidence. | Network-specific demos and testnet milestones must not be relabeled as Bitcoin mainnet or Conxian production evidence. |
| **SDK/reference maturity** | Official and reference repositories remain developer preview, under development, unaudited, WIP, toy, or research/reference code as recorded in the [canonical Gateway report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md). | Repository presence, an SDK label, or a local build does not satisfy the production gate. |
| **Shared readiness status** | **Research / Evaluation Only**. | Any missing, contradictory, or upstream-only gate keeps this status unchanged. |

## 🧭 Conxian Cross-Repository Verifier Gap Map

The [canonical Gateway report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md) separates these local classifications. None is evidence of a production BitVM3, BitVMX-GC, recursive-Groth16, or pairing-verifier deployment.

| Surface | Current implementation evidence | Durable remediation Tracker |
| --- | --- | --- |
| **Gateway** | A backend-neutral injected-verifier boundary exists, but no production pairing backend is wired. The legacy `verify_state_proof` path remains metadata-only and must not be treated as cryptographic verification. | [Gateway #189](https://github.com/Conxian/conxian-gateway/issues/189) (Open, Research-Only) |
| **Platform** | BitVM-related paths are simulations/scaffolds and can produce success-shaped results without cryptographic verification. | [Platform #1187](https://github.com/Conxian/conxius-platform/issues/1187) |
| **Nexus** | A narrow local Arkworks Groth16 call exists, but state roots are not bound by that path, negative coverage is incomplete, and metadata/ownership/revision drift remains. | [Nexus #169](https://github.com/Conxian/conxian-nexus/issues/169) |
| **Wallet** | TypeScript/Android paths generate simulation segments and success-shaped results; no actual verifier is present. | [Wallet #427](https://github.com/Conxian/conxius-wallet/issues/427) |
| **Core** | Structural verifier boundaries and fail-closed policy exist; dependencies alone do not establish a current BitVM2/Groth16 verification call. | [Core #188](https://github.com/Conxian/lib-conxian-core/issues/188) |
| **Enclave** | The BitVM2 boundary is typed, fail-closed, and unsupported for proof verification; MuSig2 signing is not SNARK verification. | [Enclave #202](https://github.com/Conxian/conxius-enclave-sdk/issues/202) |

## 🔬 Protocol Research Alignment (2026-09 Update)

| Research Feature | Implementation Status | Target Action & Candidate |
| --- | --- | --- |
| **RGB v0.11.1 Pivot** | 🔴 BLOCKED | Replace `rgb-core` v0.12 with `rgb-lib` v0.11.1 (Tether/USDt wallet compatibility). |
| **BitVM3 / Groth16 Readiness** | 🟡 RESEARCH / EVALUATION ONLY | Maintain backend-neutral boundary; evaluate Arkworks/Groth16 verifier candidate against readiness gate. |
| **LDK Node v0.4+ Integration** | 🟡 RESEARCH / CANDIDATE | Replace `SimulatedLightningBackend` with production LDK Node v0.4+ implementation across Lightning stack. |
| **DLC Integration** | 🟡 RESEARCH | Implement real Discreet Log Contract CET construction using `rust-dlc`. |
| **ISO 20022 Treasury** | 🟡 GAP (CON-1348) | Implement `camt.053/054` XML parsers for institutional treasury statement ingestion. |

## 📈 Roadmap for Remediation & Phase Cycle

1. **Phase 1: Standardization & Governance (Complete):** Unified README, taxonomy, and docs standards deployed across repositories.
2. **Phase 2: Automation & Hardening (Complete):** Hardened standard CI, artifact validation, and 5 core Python verification scripts active.
3. **Phase 3: Critical Bug & Vulnerability Remediation (Active):** Address CON-1422, CON-1423, CON-1424 smart contract bugs and eliminate contract stubs (CON-1434).
4. **Phase 4: Protocol Upgrade & Integration (Upcoming):** Execute RGB v0.11.1 pivot, wire LDK Node v0.4+ backend, and integrate ISO 20022 treasury parsing.

---

*Updated for the 2026-09 End-to-End Cycle Refresh. Upstream evidence remains classified separately from Conxian implementation status.*
