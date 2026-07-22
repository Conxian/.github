# Research: BitVM3 & Groth16 Readiness (2026-07-22)

> **Status: Research / Evaluation Only**
>
> This document separates upstream/reference evidence from Conxian implementation evidence. The canonical Gateway refresh is [BitVM3 / BitVMX Evidence and Cross-Repository Triage](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md), which is tied to [Gateway issue #189](https://github.com/Conxian/conxian-gateway/issues/189). No paper, repository, SDK, demo, mainnet transaction, or local verifier call alone establishes Conxian production readiness.

## Decision summary

- **BitVM3 evidence is paper/protocol evidence.** [IACR ePrint 2026/933](https://eprint.iacr.org/2026/933) and the [BitVM3 paper](https://bitvm.org/bitvm3.pdf) describe a garbled-circuit bridge/core research family. They do not provide a stable SDK, production API, audit, or Conxian deployment.
- **The Bitcoin mainnet artifact is upstream BitVMX prototype evidence.** The [BitVMX SNARK prototype article](https://bitvmx.org/knowledge/a-new-era-for-bitcoin-successful-snark-proof-verification-with-bitvmx) links transaction [`75eb2ad4f22263440fc4ceb61c51b0bb77721661dbfbec961358520b04107ec3`](https://mempool.space/tx/75eb2ad4f22263440fc4ceb61c51b0bb77721661dbfbec961358520b04107ec3). It is not BitVM3-GC, a stable SDK, a production bridge, a Conxian verifier, or audit evidence.
- **Signet and public testnet demonstrations remain network-specific demonstrations.** The [official BitVM demo](https://github.com/BitVM/bitvm.github.io/tree/main/demo) is a developer-preview graph on BitVM signet/`bitvmnet`. The [Union Bridge announcement](https://bitvmx.org/knowledge/union-bridge-reaches-testnet-a-milestone-for-bitvmx-powered-bitcoin-bridging) describes an experimental Rootstock Testnet milestone with inactive V1.5 dispute mechanisms, no formal audit, and a 2027 mainnet roadmap.
- **Reference software is not automatically production software.** The official [BitVM Rust repository](https://github.com/BitVM/BitVM) is a BitVM2 developer preview that warns against production use. [BitVMX-CPU](https://github.com/FairgateLabs/BitVMX-CPU) is under development, unaudited, and not production-ready; its license metadata also requires reconciliation before vendoring.
- **Conxian remains research-only.** Gateway has a backend-neutral injected-verifier boundary but no production pairing backend. Platform and Wallet contain simulation/scaffold paths, Nexus has a narrow local verifier call with unresolved binding and negative-coverage gaps, Core provides structural/fail-closed boundaries rather than an established production verifier, and Enclave is fail-closed/unsupported for proof verification.

**Decision rule:** any missing, contradictory, or upstream-only production-readiness gate keeps this status at **Research / Evaluation Only**.

## Evidence classification

| Evidence class | Current classification | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| **BitVM3 paper/protocol** | Source-verified research evidence from [ePrint 2026/933](https://eprint.iacr.org/2026/933) and the [paper PDF](https://bitvm.org/bitvm3.pdf). | BitVM3 bridge/core constructions and garbled-circuit protocol research. | A shipped SDK, stable API, audit, production deployment, or Conxian implementation. |
| **Bitcoin mainnet upstream prototype** | Upstream-reported [BitVMX SNARK prototype](https://bitvmx.org/knowledge/a-new-era-for-bitcoin-successful-snark-proof-verification-with-bitvmx) with linked [mainnet transaction](https://mempool.space/tx/75eb2ad4f22263440fc4ceb61c51b0bb77721661dbfbec961358520b04107ec3). | A public Bitcoin mainnet transaction associated by the upstream project with an interactive SNARK-verifier execution. | BitVM3-GC, a stable SDK, secure implementation, production bridge, Conxian verifier, or independent audit. |
| **Bitcoin signet / `bitvmnet`** | Official [BitVM Developer Preview](https://github.com/BitVM/bitvm.github.io/tree/main/demo) and signet demonstrations. | Development/test-network execution evidence for the referenced BitVM demo. | Bitcoin mainnet evidence, BitVM3-GC deployment, or production readiness. |
| **Rootstock/public testnet** | Experimental [Union Bridge Rootstock Testnet](https://bitvmx.org/knowledge/union-bridge-reaches-testnet-a-milestone-for-bitvmx-powered-bitcoin-bridging) evidence. | A public testnet milestone and stated roadmap. | Production deployment, active dispute guarantees, formal audit, or Bitcoin mainnet readiness. |
| **SDK/reference repository maturity** | Developer preview, under-development, unaudited, WIP, toy, or research/reference classifications as recorded in the [canonical Gateway report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md). | Public source and project maturity signals that can guide evaluation. | A stable release contract, reproducible artifact, security review, or permission to vendor into a value-bearing path. |
| **Conxian implementation evidence** | Local source boundaries and tests across Gateway, Platform, Nexus, Wallet, Core, and Enclave, summarized below. | The current state of Conxian interfaces, simulations, fixtures, and fail-closed behavior. | A production BitVM3, BitVMX-GC, recursive-Groth16, or pairing-verifier deployment. |

## Terminology guardrails

- **BitVM3 is not synonymous with Groth16.** BitVM3 is the garbled-circuit bridge/core research family. A Groth16 verifier may be a circuit component in a larger construction; that does not make the construction recursive Groth16 verification.
- **The mainnet prototype is BitVMX evidence, not BitVM3-GC evidence.** Network, protocol generation, and implementation role must remain explicit in every reference.
- **A local Arkworks call is not a complete verifier contract.** Proof encoding, verification-key ownership, public-input ordering, state-root binding, negative behavior, network context, and revision provenance still require evidence.
- **A mock or injected boundary is not cryptographic verification.** The Gateway boundary is intentionally backend-neutral; its deterministic fixture verifier does not perform pairings.

## Conxian implementation evidence

The following classifications are drawn from the [canonical Gateway report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md) and are not production-readiness claims.

| Surface | Current evidence classification | Required follow-up |
| --- | --- | --- |
| **Gateway** | [PR #255](https://github.com/Conxian/conxian-gateway/pull/255) established a backend-neutral injected-verifier boundary. The production pairing backend is not wired. The legacy `verify_state_proof` path remains metadata-only and must not be treated as cryptographic verification. [PR #259](https://github.com/Conxian/conxian-gateway/pull/259) remains an isolated BitVMX-CPU evaluator, while [PR #267](https://github.com/Conxian/conxian-gateway/pull/267) and [PR #268](https://github.com/Conxian/conxian-gateway/pull/268) keep the research expansion and evidence triage non-production. | Keep [Gateway #189](https://github.com/Conxian/conxian-gateway/issues/189) open and research-only. Do not modify the legacy `verify_state_proof` path as a substitute for an approved cryptographic backend. |
| **Platform** | BitVM-related paths are simulations/scaffolds; default paths can produce success-shaped results without cryptographic verification. | [Platform #1187](https://github.com/Conxian/conxius-platform/issues/1187) is the durable remediation tracker. |
| **Nexus** | A narrow `ark_groth16::Groth16::<Bls12_381>::verify(...)` call exists, but state roots are not bound by that path, negative coverage is incomplete, and trial metadata/ownership/revision drift remains. | [Nexus #169](https://github.com/Conxian/conxian-nexus/issues/169) is the durable remediation tracker. |
| **Wallet** | TypeScript/Android BitVM paths generate simulation segments and success-shaped results; no actual verifier is present. | [Wallet #427](https://github.com/Conxian/conxius-wallet/issues/427) is the durable remediation tracker. |
| **Core** | Verifier architecture provides structural/protocol boundaries and fail-closed policy. Arkworks dependencies alone do not establish a current BitVM2/Groth16 verification call. | [Core #188](https://github.com/Conxian/lib-conxian-core/issues/188) is the durable remediation tracker. |
| **Enclave** | The BitVM2 boundary is typed, fail-closed, and unsupported for proof verification. Generic MuSig2 signing is not SNARK verification. | [Enclave #202](https://github.com/Conxian/conxius-enclave-sdk/issues/202) is the durable acceptance gate. |

## Production-readiness evidence gate

No candidate may move from research to production integration until every gate below is satisfied for the **exact source revision and deployment role**:

1. **Source, revision, and ownership:** identify the exact commit/release, maintained API, compatibility policy, accountable owner, and deployment role.
2. **CI-backed tests:** provide reproducible positive and negative tests, including malformed envelopes, wrong keys, wrong circuits, wrong inputs, subgroup/commitment failures, and network-context failures; CI must fail closed.
3. **Immutable artifacts and provenance:** publish immutable source, toolchain, feature, dependency, binary/library, key, proof, and artifact hashes with provenance that an independent builder can reproduce.
4. **License clarity:** reconcile repository metadata, checked-in license files, transitive dependencies, and redistribution terms before adoption.
5. **Network-specific evidence:** demonstrate the exact protocol and deployment role on the intended network; signet, testnet, public demo, or an upstream mainnet transaction cannot be silently promoted to another classification.
6. **Independent security review:** obtain review of cryptographic, protocol, economic, supply-chain, and operational assumptions for the exact implementation. A paper, demo, or repository is not an audit.
7. **Protocol and economic behavior:** verify challenge windows, SPV inclusion, dispute/counterproof paths, disablement, incentives, recovery, and failure behavior on the intended network.
8. **Resources and operations:** measure CPU, wall time, peak memory, artifact/key/proof size, transaction weight/count, bandwidth, process isolation, timeouts, output limits, secrets, rollback, and observability with deployment margin.
9. **Conxian integration safety:** align Gateway/Core/Nexus/Platform/Wallet/Enclave ownership and acceptance; no mock, simulation, metadata-only, or success-shaped path may be reachable from a value-bearing production flow.

**Promotion rule:** one missing, contradictory, or upstream-only gate is sufficient to keep the status at **Research / Evaluation Only**.

## Disposition and follow-up

- Keep [Gateway #189](https://github.com/Conxian/conxian-gateway/issues/189) **open and research-only**.
- Use the [canonical Gateway evidence report](https://github.com/Conxian/conxian-gateway/blob/main/docs/research/BITVM3_BITVMX_EVIDENCE_AND_TRIAGE_2026-07-22.md) as the source for upstream and cross-repository classifications.
- Do not add BitVM3/GC dependencies, production HTTP routes, settlement authorization, custody decisions, or compliance decisions from any paper, repository, SDK, demo, mainnet transaction, or local verifier call alone.
- Track the five repository-specific remediation issues: [Platform #1187](https://github.com/Conxian/conxius-platform/issues/1187), [Nexus #169](https://github.com/Conxian/conxian-nexus/issues/169), [Wallet #427](https://github.com/Conxian/conxius-wallet/issues/427), [Core #188](https://github.com/Conxian/lib-conxian-core/issues/188), and [Enclave #202](https://github.com/Conxian/conxius-enclave-sdk/issues/202).
- Keep this document and the [source-and-gap map](./source-and-gap-map.md) aligned on **Research / Evaluation Only** until every gate passes.

_Evidence and upstream metadata were refreshed against the canonical Gateway report on 2026-07-22. Upstream-reported claims remain labeled and are not Conxian benchmarks or security conclusions._
