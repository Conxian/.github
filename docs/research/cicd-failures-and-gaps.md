# Research: CI/CD Failures, Gaps & Alignment (2026-09 Update)

## 1. Identified Gaps
- **Silent Failures**: `dependency-review.yml` was missing explicit gating, allowing vulnerable dependencies to pass CI.
- **Missing Validation**: Several validation scripts referenced in unified workflows were stubs or missing real verification logic in `scripts/`.
- **Inconsistent Actions**: Mixed versions of `actions/checkout` (v4 vs v6) across repositories.
- **Coverage Gap**: Lightning coverage gate was missing artifact publication, making it hard to verify report generation.
- **Artifact Exposure Risk**: Incomplete ignore rules in `.gitignore` for generated test reports, build outputs, and compiled binaries.

## 2. Hardening Progress
- [x] **Standard CI**: Initialized `.github/workflows/standard-ci.yml` with explicit security gating (`fail-on-severity: high`).
- [x] **Scorecard Update**: Integrated CI/CD dimensions into the Cross-Lane Readiness Scorecard.
- [x] **Script Provisioning**: Fully implemented non-stub production verification logic for `scripts/verify_*.py` tools (CON-1322). Verified 5 active core scripts:
  - `scripts/verify_knowledge_retention.py`
  - `scripts/verify_tracked_artifacts.py`
  - `scripts/verify_bos_production_boundary.py`
  - `scripts/verify_compose_env_templates.py`
  - `scripts/verify_submodule_secret_filenames.py`
- [x] **Artifact & Gitignore Hardening**: Hardened root `.gitignore` and updated `scripts/verify_tracked_artifacts.py` to enforce mandatory ignore rules for test results (`playwright-report/`, `test-results/`), coverage outputs, compiled binaries, build dirs, and secret patterns.

## 3. Phase Breakdown & Best Candidate Initialization

To maintain an end-to-end cycle every session and easily expand on needed work, candidates are scored and prioritized based on impact, safety, and readiness:

### 🔴 Candidate Priority 0 (Immediate Execution Blockers)
1. **CON-1422 (Smart Contract Admin Governance)**: Implement multi-sig & timelock governance for the 73+ admin variables across core Clarity contracts.
2. **CON-1423 (Contract Upgradeability & Delegation)**: Implement SIP-009/SIP-010 compliant proxy dispatcher patterns to eliminate contract immutability deadlocks.
3. **CON-1424 (Contract Ownership Tautology Bug)**: Replace invalid owner verification logic across core contracts to prevent unauthorized ownership takeover.

### 🟡 Candidate Priority 1 (High Priority Feature & Protocol Advancement)
1. **CON-1434 (Clarity Stub Contract Implementation)**: Implement functional smart contract logic for the 23 placeholder stubs (33% of contract suite).
2. **RGB Protocol v0.11.1 Pivot**: Unblock RGB integration by migrating from `rgb-core` v0.12 to `rgb-lib` v0.11.1 for Tether/USDt wallet compatibility.
3. **LDK Node v0.4+ Integration**: Replace `SimulatedLightningBackend` with production LDK Node implementation across the Lightning stack.
4. **ISO 20022 Treasury Parser (CON-1348)**: Implement `camt.053/054` XML bank statement parsing in Gateway/Platform for institutional banking interoperability.

### 🟢 Candidate Priority 2 (Operations & Release Automation)
1. **CON-1323 (Pinned Vercel CLI Standardization)**: Standardize Vercel deployment action versions across showcase deploy workflows.
2. **CON-1328 (Monorepo Release Workflow)**: Deploy monorepo versioning and automated changelog generation workflow.

## 4. End-to-End Session Cycle Execution Checklist

Every engineering session must complete the following verification loop before submitting changes:
1. Run all repository verification scripts:
   - `python3 scripts/verify_knowledge_retention.py`
   - `python3 scripts/verify_tracked_artifacts.py`
   - `python3 scripts/verify_bos_production_boundary.py`
   - `python3 scripts/verify_compose_env_templates.py`
   - `python3 scripts/verify_submodule_secret_filenames.py`
2. Verify GitHub Actions workflow syntax with `actionlint` or standard workflow linter.
3. Ensure no build artifacts or sensitive files are staged in Git.
4. Update research gap maps and scorecards to reflect completed vs pending work items.

---
*Maintained by Jules / Conxian Labs AI Engineering.*
