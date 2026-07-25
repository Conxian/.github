# Public release discipline

This policy defines the minimum public release, version, and deployment signaling expected across Conxian's public repositories. It applies repository purpose from the [repository taxonomy](../repository-taxonomy.md) rather than forcing one release pattern onto every surface.

It is not a production-readiness or security certification, and it does not require a release for every merge. Security support and reporting remain governed by each repository's `SECURITY.md`. Point-in-time observations are kept in [Snapshot evidence and cleanup ledger](#snapshot-evidence-and-cleanup-ledger), separate from the durable rules below.

## Release classes and decisions

| Repository | Purpose-based class | Required public signal |
| --- | --- | --- |
| `lib-conxian-core` | Library / SDK | Publish a tagged GitHub Release for every externally consumable version. |
| `conxius-enclave-sdk` | Library / SDK | Publish a tagged GitHub Release for every externally consumable version. |
| `Conxian` | Protocol / runtime / integration | Publish a tagged GitHub Release for public compatibility or milestone changes. Commits between milestones may remain unreleased when clearly labeled as unreleased development. |
| `conxian-gateway` | Protocol / runtime / integration | Publish a tagged GitHub Release for public compatibility or milestone changes. Commits between milestones may remain unreleased when clearly labeled as unreleased development. |
| `conxian-nexus` | Protocol / runtime / integration | Publish a tagged GitHub Release for public compatibility or milestone changes. Commits between milestones may remain unreleased when clearly labeled as unreleased development. |
| `conxius-platform` | Protocol / runtime / integration | Publish a tagged GitHub Release for public compatibility or milestone changes. Commits between milestones may remain unreleased when clearly labeled as unreleased development. |
| `conxius-wallet` | End-user application / tool | Publish a release signal when a user-facing or distributed version changes. Use a tagged GitHub Release when GitHub is the public distribution or compatibility record. |
| `conxian_ui` | End-user application / tool | Publish a release signal when a user-facing or distributed version changes; document the tag-driven release or deployment path used as the public record. |
| `conxius-orbit` | End-user application / tool | Publish a release signal when a user-facing or distributed version changes. Use a tagged GitHub Release when GitHub is the public distribution or compatibility record. |
| `.github` | Governance / static support | Exempt from routine versioned releases. Maintain deployment traceability where applicable and state the surface's purpose and canonical destination. |
| `conxian.github.io` | Governance / static support | Exempt from routine versioned releases. Maintain deployment traceability and state the site's purpose and canonical destination. A release is optional for a meaningful site milestone. |
| `conxian-labs-site` | Governance / static support | Exempt from routine versioned releases. Maintain deployment traceability and state the site's purpose and canonical destination. A release is optional for a meaningful site milestone. |

The governance/static-support exemption is not an exemption from traceability. A deployed site should identify the source revision or deployment record that produced the public state. A repository that changes purpose or begins distributing versioned artifacts must be reclassified.

## Published versions and version authority

A raw Git tag is not a GitHub Release. A published version represented on GitHub complies only when the tag has a GitHub Release object with usable notes and required evidence. A tag may still mark internal or unreleased work, but it must not be presented as the latest published release by itself.

Every versioned repository must name one authoritative version source, such as a package manifest, workspace manifest, or release configuration. At release time, the authoritative source, tag, GitHub Release, distributed package/store/artifact version, changelog, and README status must not silently conflict.

A repository may carry a newer working version when both conditions hold:

1. the newer value is clearly labeled as unreleased development; and
2. the latest published or reviewed release is named explicitly.

`conxius-enclave-sdk` provides the useful presentation model: it distinguishes working `2.0.12` from latest reviewed release `v2.0.11`. Its duplicate generated latest-release notes still require cleanup, but the distinction itself should be preserved.

## Minimum release notes and evidence

Release evidence is proportional to what the repository publishes or distributes. Release notes must include or link to:

- release scope and the important changes included;
- compatibility, migration, and upgrade impact, including “none” where appropriate;
- known limitations or material readiness boundaries;
- the corresponding changelog entry or comparison;
- distributed artifacts and checksums when users consume binaries or bundles;
- an SBOM and provenance/attestation when the repository's release process or risk profile requires them; and
- a documented non-applicability statement or approved waiver when an expected artifact or evidence type is intentionally omitted.

Libraries and SDKs should make consumer compatibility and dependency impact explicit. Protocol/runtime/integration releases should emphasize public interfaces, state or schema changes, operator impact, and rollback or migration boundaries. End-user application/tool releases should identify the distributed version, supported delivery channel, user-visible changes, upgrade expectations, and known limitations. Governance/static-support surfaces should retain deployment evidence instead of manufacturing routine releases.

## Exceptions, ownership, and review

The owning repository owns its version declaration, release objects, notes, artifacts, deployment evidence, and remediation issues. Follow the [issue-only ITIL5 workflow](./issue-only-itil5-workflow.md): organization-wide policy and exceptions belong in `.github`, while implementation remains in linked issues in each affected repository.

An exception must record:

- the repository and rule being waived;
- the owner and reason;
- compensating public signal or evidence;
- expiry or next review date; and
- the trigger that ends or reopens the exception.

Review the repository's class and any exemption when its purpose, audience, distribution channel, compatibility contract, deployment model, or artifact set changes; when version signals diverge; or at least every six months while an exception remains active. Security-sensitive details must use the private reporting path rather than a public exception issue.

## Portfolio pins

The recommended organization pins retain the canonical portfolio narrative in this order:

1. `Conxian`
2. `lib-conxian-core`
3. `conxius-wallet`
4. `conxian_ui`
5. `conxian-gateway`
6. `conxian-labs-site`

Pins communicate narrative breadth across protocol, shared primitives, sovereign access, interaction, integration, and the Labs public surface. They are not a readiness certification or a substitute for the release rules above.

At the 2026-07-25 snapshot, the organization pins verified through GitHub were only `Conxian`, then `.github`. Applying the target six remains a manual organization-administrator action; this policy does not claim that the pins were changed.

## Snapshot evidence and cleanup ledger

The following observations are evidence from the public audit captured at **2026-07-25T10:46:46Z**. Values may change after that timestamp and do not redefine the policy.

| Priority | Repository | Snapshot gap and owning action |
| --- | --- | --- |
| P1 | `conxius-wallet` | README/manifest/changelog signal `v1.9.5`, while the latest release/tag was `v1.9.2`. Reconcile in [Conxian/conxius-wallet#356](https://github.com/Conxian/conxius-wallet/issues/356). |
| P1 | `lib-conxian-core` | README badge/source signal `v0.3.0`, while the latest release/tag was `v0.2.11`. Declare the authority and publish or label the newer version unreleased. |
| P1 | `Conxian` | Latest GitHub Release was `v1.0.0-rc1` from 2025, while raw tag `v1.0.0` existed. Publish release notes/evidence for the final tag or remove its implied published status. |
| P1 | `conxius-orbit` | Only GitHub Release was `v1.0.0` from 2025 while newer source versions were present. Establish one version authority and current release signal. |
| P2 | `conxian_ui` | No clearly visible tag-driven release path. Document the public release/deployment record used when distributed user-facing versions change. |
| P2 | `conxian.github.io` | No README, description, homepage, release guidance, or clear canonical-destination statement. Add purpose, ownership, destination, and deployment traceability. |
| P2 | `conxian-labs-site` | Deployment-versus-release wording was contradictory. State deployment traceability as the routine rule and reserve releases for optional site milestones. |
| P2 | `conxian-nexus` | README stated `v0.4.19`, while the latest release was `v0.4.22`. Align README status with the published release. |
| P3 | `conxius-enclave-sdk` | Correctly distinguished working `2.0.12` from latest reviewed release `v2.0.11`, but generated latest-release notes were duplicated. Preserve the distinction and remove duplication. |

Create additional remediation issues in the repository that owns each remaining gap and link them from the organization-level coordination issue when work is scheduled.
