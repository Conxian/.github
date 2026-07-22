# Cross-Lane Readiness Scorecard

This scorecard tracks the cumulative readiness of a product or service across all five Conxian governance dimensions.

## Readiness Summary: [Product/Surface Name]
**Current Readiness Score:** [0-100%]

---

### 🟢 Lane 1: Trust & Controls (Security)
- [ ] No fail-open admin/auth paths.
- [ ] Production-boundary safeguards implemented (e.g., TEE/StrongBox).
- [ ] Secret scanning and dependency review are green (Gating enabled).
- [ ] Unsafe sentinel/default secret states rejected at startup.
- [ ] **[NEW]** Sanctions-risk tagging for BRICS/G7 cross-lane traffic (CON-1351).

### 🔵 Lane 2: Release & Deployment Maturity (Ops)
- [ ] Tagged release discipline enforced.
- [ ] Protected environments used for promotion.
- [ ] Rollback path verified and documented.
- [ ] CI coverage includes integration/e2e tests.
- [ ] **[NEW]** Automated coverage gates (>=90%) with published reports (CON-1345).

### 🧪 Lane 3: Product & Technical Proof (Dev)
- [ ] Contract/Logic verified against design.
- [ ] No misleading placeholder/stub behavior (e.g., real FROST/MuSig2/DLC logic).
- [ ] Performance benchmarks meet production requirements.
- [ ] SDK/API signatures are stable and machine-readable.
- [ ] **[NEW]** ZK proof verification (Groth16/SNARK) verified for the exact source/revision and intended network with CI-backed positive/negative tests, immutable artifacts/provenance, license clarity, and independent security review (CON-1340); an upstream mainnet reference alone is insufficient.

### 💰 Lane 4: Commercial Claim Safety (Market)
- [ ] Public claims match implemented reality.
- [ ] Pricing specificity defined and approved.
- [ ] Integration paths (Gateway/Wallet/SDK) verified.
- [ ] README purpose and status are current.
- [ ] **[NEW]** ISO 20022 messaging compatibility verified (CON-1348).

### ⚖️ Lane 5: Ownership & Decision Clarity (Governance)
- [ ] CODEOWNERS updated and active.
- [ ] Legal/Compliance review points cleared.
- [ ] Stakeholder sign-off for activation recorded.
- [ ] Decision log for exceptions is current.
- [ ] **[NEW]** Unified CLI surface agreement (Orbit CLI) enforced (CON-1238).

---
**Blockers for Activation:**
1. [List critical P0 items]
