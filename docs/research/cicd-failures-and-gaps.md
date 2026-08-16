# Research: CI/CD Failures, Gaps & Alignment (2026-06-28)

## 1. Identified Gaps
- **Silent Failures**: `dependency-review.yml` was missing explicit gating, allowing vulnerable dependencies to pass CI.
- **Missing Validation**: Several validation scripts referenced in unified workflows were stubs or missing real verification logic in `scripts/`.
- **Inconsistent Actions**: Mixed versions of `actions/checkout` (v4 vs v6) across repositories.
- **Coverage Gap**: Lightning coverage gate was missing artifact publication, making it hard to verify report generation.
- **Artifact Exposure Risk**: Incomplete ignore rules in `.gitignore` for generated test reports, build outputs, and compiled binaries.

## 2. Hardening Progress
- [x] **Standard CI**: Initialized `.github/workflows/standard-ci.yml` with explicit security gating (`fail-on-severity: high`).
- [x] **Scorecard Update**: Integrated CI/CD dimensions into the Cross-Lane Readiness Scorecard.
- [x] **Script Provisioning**: Fully implemented non-stub production verification logic for `scripts/verify_*.py` tools (CON-1322).
- [x] **Artifact & Gitignore Hardening**: Hardened root `.gitignore` and updated `scripts/verify_tracked_artifacts.py` to enforce mandatory ignore rules for test results (`playwright-report/`, `test-results/`), coverage outputs, compiled binaries, build dirs, and secret patterns.

## 3. Deployment Readiness
- **Vercel CLI**: Standardizing on pinned versions for showcase deploy flow (CON-1323).
- **Release Workflow**: Monorepo release workflow pending for versioning and changelog automation (CON-1328).
