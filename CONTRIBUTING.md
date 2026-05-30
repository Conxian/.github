# Contributing to Conxian organization defaults

This repository contains the community health files, shared policies, templates, and default workflows used across public repositories in the Conxian GitHub organization.

## Scope

Changes here affect how public repositories present contribution, security, ownership, and issue/PR guidance.

## Contribution flow

We use GitHub Flow.

1. Create a branch from `main`.
2. Make the smallest practical change.
3. Open a pull request with a clear rationale.
4. Request review from the relevant owners when touching policy or security-sensitive files.

## Changes that require extra care

The following paths should receive CODEOWNERS review:

- `CODEOWNERS`
- `SECURITY.md`
- `SUPPORT.md`
- `.github/ISSUE_TEMPLATE/**`
- `.github/PULL_REQUEST_TEMPLATE*`
- `.github/workflows/**`
- `.github/release.yml`
- `profile/**`

## Content standards

Keep public wording:

- clear
- accurate
- security-conscious
- consistent with `conxian-labs.com` as the canonical public contact domain

Avoid describing this repository as an internal registry or private operations system.

## Security

Do not use public issues for vulnerability disclosure. Follow [SECURITY.md](SECURITY.md).

## Support

For public process or template questions, use the issue tracker in this repository. For support routing, use [SUPPORT.md](SUPPORT.md).
