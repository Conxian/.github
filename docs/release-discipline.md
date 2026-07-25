# Public release discipline

This policy defines the minimum public release, version, and deployment signaling expected across Conxian's public repositories. It applies repository purpose from the [repository taxonomy](../repository-taxonomy.md) rather than forcing one release pattern onto every surface.

It is not a production-readiness or security certification, and it does not require a release for every merge. Security support and reporting remain governed by each repository's `SECURITY.md`. Point-in-time observations are kept in [Snapshot evidence and cleanup ledger](#snapshot-evidence-and-cleanup-ledger), separate from the durable rules below.

## Release classes and decisions

| Repository class | Live canonical repositories | Required public signal |
| --- | --- | --- |
| Consumable protocol, wallet, library, SDK, runtime, and integration artifacts | `Conxian`, `conxius-wallet`, `conxian-gateway`, `lib-conxian-core`, `conxian-nexus`, `conxius-enclave-sdk` | Every externally consumable release requires a SemVer tag and a matching GitHub Release. |
| Public UI and deployment tooling | `conxian_ui`, `conxius-orbit` | When users or operators consume a versioned build, package, or CLI, the externally consumable release requires a SemVer tag and matching GitHub Release. Deployment-only changes may use documented deployment or commit history. |
| Platform / control plane | `conxius-platform` | Externally consumable configuration or orchestration releases require a SemVer tag and matching GitHub Release because they can affect compatibility and operations. |
| Static sites | `conxian-labs-site`, `conxian.github.io` | GitHub Releases are optional. A lightweight deployment signal is sufficient when the README or repository metadata identifies the commit-based deployment and content-history model. |
| Governance / defaults | `.github` | Explicit rolling-change exemption: no GitHub Release is required; merged governance history on `main` is authoritative. |

The static-site exemption is not an exemption from traceability. A deployed site should identify the source revision or deployment record that produced the public state. A repository that changes purpose or begins distributing versioned artifacts must be reclassified.

## Published versions and version authority

A raw Git tag is not a GitHub Release. A formal externally consumable release complies only when its SemVer tag has a matching GitHub Release object with usable notes and required evidence. A tag may still mark internal or unreleased work, but it must not be presented as the latest published release by itself.

Every versioned repository must name one authoritative version source, such as a package manifest, workspace manifest, or release configuration. At release time, the authoritative source, SemVer tag, GitHub Release, distributed package/store/artifact version, changelog, and README status must be consistent. A newer source or manifest version is allowed only when it is explicitly marked **Unreleased** and the latest published release remains clear.

A repository may carry a newer working version when both conditions hold:

1. the newer value is clearly labeled as unreleased development; and
2. the latest published or reviewed release is named explicitly.

`conxius-enclave-sdk` provides the useful presentation model: it distinguishes working `2.0.12` from latest reviewed release `v2.0.11`. Its duplicate generated latest-release notes still require cleanup, but the distinction itself should be preserved.

## Minimum release notes and evidence

Release evidence is proportional to what the repository publishes or distributes. The matching GitHub Release must include or link to the applicable changelog, release runbook, and evidence, including:

- release scope and the important changes included;
- compatibility, migration, and upgrade impact, including “none” where appropriate;
- known limitations or material readiness boundaries;
- the corresponding changelog entry or comparison;
- distributed artifacts and checksums when users consume binaries or bundles;
- an SBOM and provenance/attestation when the repository's release process or risk profile requires them; and
- a documented non-applicability statement or approved waiver when an expected artifact or evidence type is intentionally omitted.

Libraries and SDKs should make consumer compatibility and dependency impact explicit. Protocol/runtime/integration releases should emphasize public interfaces, state or schema changes, operator impact, and rollback or migration boundaries. End-user application/tool releases should identify the distributed version, supported delivery channel, user-visible changes, upgrade expectations, and known limitations. Governance/static-support surfaces should retain deployment evidence instead of manufacturing routine releases.

Release evidence records what was built, reviewed, and published. It must not be treated as proof of production readiness, security certification, or operational approval.

## Exceptions, ownership, and review

The owning repository owns its version declaration, release objects, notes, artifacts, deployment evidence, and remediation evidence. Organization-wide policy and exceptions belong in `.github`; each observed repository mismatch must be corrected or explicitly dispositioned in that repository and linked back as follow-up evidence.

An exception must record:

- the repository and rule being waived;
- the owner and reason;
- compensating public signal or evidence;
- expiry or next review date; and
- the trigger that ends or reopens the exception.

Review the repository's class and any exemption when its purpose, audience, distribution channel, compatibility contract, deployment model, or artifact set changes; when version signals diverge; or at least every six months while an exception remains active. Security-sensitive details must use the private reporting path rather than a public exception issue.

## Portfolio pins

The retained organization-pin target from the canonical [#48 decision](https://github.com/Conxian/.github/issues/48#issuecomment-5078201839) is, in order:

1. `Conxian`
2. `conxius-wallet`
3. `conxian-gateway`
4. `conxius-enclave-sdk`
5. `conxian-labs-site`
6. `conxian.github.io`, after its basic metadata cleanup under [#53](https://github.com/Conxian/.github/issues/53)

Pins prioritize the protocol, end-user wallet, integration path, security SDK, portfolio entry point, and documentation hub rather than control-plane or supporting repositories. They are not a readiness certification or a substitute for the release rules above.

At the 2026-07-25 snapshot, the organization pins verified through GitHub were only `Conxian`, then `.github`. Applying the target six remains a manual organization-administrator action; this policy does not claim that the pins were changed.

## Snapshot evidence and cleanup ledger

The following observations are evidence from the public audit captured at **2026-07-25T10:46:46Z**. Values may change after that timestamp and do not redefine the policy.

| Priority | Repository | Snapshot gap and owning action |
| --- | --- | --- |
| P1 | `conxius-wallet` | README/manifest/changelog signal `v1.9.5`, while the latest release/tag was `v1.9.2`. Reconcile in [Conxian/conxius-wallet#356](https://github.com/Conxian/conxius-wallet/issues/356). |
| P1 | `lib-conxian-core` | README badge/source signal `v0.3.0`, while the latest release/tag was `v0.2.11`. Record repository-local follow-up evidence that declares the authority and publishes the release or labels the newer version Unreleased. |
| P1 | `Conxian` | Latest GitHub Release was `v1.0.0-rc1` from 2025, while raw tag `v1.0.0` existed. Record repository-local follow-up evidence that publishes matching release notes/evidence for the final tag or removes its implied published status. |
| P1 | `conxius-orbit` | Only GitHub Release was `v1.0.0` from 2025 while newer source versions were present. Record repository-local follow-up evidence that establishes one version authority and current release signal. |
| P2 | `conxian_ui` | No clearly visible tag-driven release path. Record repository-local follow-up evidence documenting the public release or deployment record used when distributed user-facing versions change. |
| P2 | `conxian.github.io` | No README, description, homepage, release guidance, or clear canonical-destination statement. Record repository-local follow-up evidence for purpose, ownership, destination, and lightweight deployment traceability. |
| P2 | `conxian-labs-site` | Deployment-versus-release wording was contradictory. Record repository-local follow-up evidence that states lightweight deployment traceability as the routine rule and GitHub Releases as optional. |
| P2 | `conxian-nexus` | README stated `v0.4.19`, while the latest release was `v0.4.22`. Record repository-local follow-up evidence aligning README status with the published release. |
| P3 | `conxius-enclave-sdk` | Correctly distinguished working `2.0.12` from latest reviewed release `v2.0.11`, but generated latest-release notes were duplicated. Record repository-local follow-up evidence that preserves the distinction and removes duplication. |

The authoritative decision is recorded in [#48](https://github.com/Conxian/.github/issues/48#issuecomment-5078201839), while cross-repository presentation and basic metadata cleanup remains under [#53](https://github.com/Conxian/.github/issues/53). Repository-local corrections or explicit dispositions are the follow-up evidence for each mismatch.
