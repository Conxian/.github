# Proposed issue-only ITIL5-informed workflow baseline

## Operating rule

The seven-type taxonomy below is a proposed lightweight operating baseline, not a formally ratified BOS decision. It is informed by ITIL5, but does not claim formal ITIL adoption, compliance, certification, or conformance.

For public-safe repository and governance execution, GitHub Issues are the canonical system of record. Restricted strategy, security, legal, financial, and detailed operational context remains canonical and authoritative in the authorized Linear workspace under Zero Secret Egress (ZSE). GitHub records must link to that authority when it is relevant without duplicating restricted detail.

Public-safe issues, relationships, pull requests, and closure evidence form the repository execution layer of the BOS knowledge graph. That execution role does not make this proposed taxonomy a ratified BOS policy or move restricted authority out of the authorized Linear workspace.

Use issue state, labels, one assignee, task lists, links, sub-issues, and pull requests. This baseline does not introduce GitHub Projects, milestones, or a parallel planning layer, but that scope choice is not a portfolio-wide ban where other approved controls require those tools.

## Route work before classifying it

Create work in the repository that owns the affected product, service, documentation, or automation. Keep public-safe implementation context, discussion, pull requests, and closure evidence together in that product repository; link restricted evidence or context to authorized Linear rather than copying it into public GitHub.

Use `.github` for organization-wide defaults, shared controls and templates, repository standards, or coordination that genuinely spans repositories. Add `scope:org-wide` only when the outcome applies across the organization or multiple repositories.

For cross-repository work, create one coordination or parent issue in `.github` with one accountable DRI and one linked implementation issue in each owning repository. Prefer native sub-issues when available; otherwise use explicit issue links. Local issues remain canonical for public-safe local implementation, while the `.github` issue records public-safe shared decisions, dependencies, exceptions, and roll-up evidence. Link restricted evidence or context to its authorized Linear record; do not copy restricted detail or the same task list into multiple issues.

**Never put security vulnerability details, privileged incident details or timelines, or response runbooks in a public issue.** Follow [`SECURITY.md`](../SECURITY.md), use the affected repository's private vulnerability reporting channel, and keep authorized handling in Linear under ZSE. Sanitized public coordination or follow-up may be created only after restricted detail is removed and disclosure is approved.

## Classification and labels

Every open operational issue has:

- one operational `type:*` label;
- one `priority:*` label;
- exactly one `status:*` label; and
- one assignee acting as the directly responsible individual (DRI).

The operational label is required even when a native GitHub issue type is set. Use this mapping consistently:

| Work type | Native issue type | Required label | Use when |
| --- | --- | --- | --- |
| Incident | `Bug` | `type:incident` | An unplanned interruption, degradation, or operational failure requires restoration. |
| Service request | `Task` | `type:service-request` | A standard access, information, support, configuration, or fulfillment request must be completed. |
| Problem | `Bug` | `type:problem` | The underlying cause of incidents or recurring failures requires investigation and prevention. |
| Change | `Task` | `type:change` | A controlled modification to a product, service, policy, configuration, or environment is proposed. |
| Risk | `Task` | `type:risk` | An uncertain event or condition requires an explicit treatment decision. |
| Control | `Task` | `type:control` | A safeguard requires definition, evidence, review, remediation, or an exception. |
| Improvement | `Feature` | `type:improvement` | A measurable enhancement to quality, reliability, efficiency, or ways of working is proposed. |

Use only this workflow vocabulary:

- Type: `type:incident`, `type:service-request`, `type:problem`, `type:change`, `type:risk`, `type:control`, `type:improvement`
- Priority: `priority:P0`, `priority:P1`, `priority:P2`, `priority:P3`
- Status: `status:triage`, `status:in-progress`, `status:blocked`, `status:needs-review`
- Scope: `scope:org-wide`
- Escalation: `escalation:required`

Other contextual labels such as `governance`, `Release`, or repository-specific domain labels may be added, but they do not replace the required workflow labels.

### Severity is not priority

**Severity** describes observed impact, such as the extent of an incident or security finding. Record it in the issue body or the private security process; this baseline does not add severity labels. **Priority** determines response and sequencing after considering severity, urgency, risk, dependencies, and available capacity:

| Priority | Meaning |
| --- | --- |
| `priority:P0` | Immediate response; critical business or service impact. |
| `priority:P1` | Urgent; high-impact or time-sensitive work. |
| `priority:P2` | Normal priority; important planned work. |
| `priority:P3` | Low priority; defer while higher-priority work exists. |

A severe issue is often high priority, but the terms are not interchangeable. Security severity and response targets remain governed by [`SECURITY.md`](../SECURITY.md).

## Required issue content

Every operational issue must include:

- operational work type and the matching `type:*` label;
- concise summary and affected scope;
- current impact or target outcome;
- `priority:P0` through `priority:P3` with a short rationale when not obvious;
- one DRI, represented by exactly one assignee;
- acceptance criteria and expected closure evidence;
- related parent, sub-issue, dependency, incident, problem, change, pull request, or external evidence links, or `None`; and
- proportionate type-specific details from the checklist below.

Add only the conditional details that apply:

- **Incident:** detection/start time, symptoms and impact, containment/workaround, restoration evidence, and a linked problem if cause remains unresolved.
- **Service request:** requester, eligibility or approval, fulfillment steps, delivery evidence, and acceptance.
- **Problem:** related incidents, observed pattern, hypotheses and evidence, root cause or known error, and linked prevention work.
- **Change:** affected surfaces, risk, implementation plan, validation plan, rollback or recovery plan, and required review or approval.
- **Risk:** cause-event-impact statement, likelihood and impact, treatment decision, mitigation owner, residual risk, and review trigger.
- **Control:** control objective and owner, scope, expected evidence, test method, gap, and remediation or exception path.
- **Improvement:** current state, measurable target, beneficiaries, proposed approach, dependencies, and before/after validation.

Keep detail proportionate. A routine request can be short; a P0 incident, risky change, or org-wide control needs enough evidence for another person to understand and verify the decision.

### Existing issue form contract

Use [`.github/ISSUE_TEMPLATE/itil_work_item.yml`](../.github/ISSUE_TEMPLATE/itil_work_item.yml) as the existing structured entry point for this baseline. The form:

- starts the issue with `status:triage`;
- requires one of the seven operational types and records the matching compact `type:*` label and native issue-type mapping for triage;
- requires summary, affected scope, impact or target outcome, priority, one named DRI, acceptance criteria and closure evidence, relationships, and proportionate type-specific details; and
- requires confirmation that the public issue contains no vulnerability details or other sensitive data.

During triage, apply the selected `type:*` and `priority:*` labels, set the mapped native issue type, assign exactly one DRI, and retain exactly one lifecycle `status:*` label. Keep the form and this vocabulary aligned; do not introduce spaced or alternate label spellings in documentation.

## Ownership and lifecycle

One assignee is the DRI. Contributors and reviewers may help, but the DRI owns routing, current status, dependencies, evidence, and the closure recommendation. If the DRI changes, update the assignee rather than maintaining a second ownership field.

For each public-safe GitHub execution record, GitHub's open/closed issue state is canonical. While an issue is open, apply exactly one status label and replace it as the work moves:

1. `status:triage` — confirm routing, type, scope, impact, priority, DRI, relationships, and closure criteria.
2. `status:in-progress` — the DRI is actively coordinating or performing the work.
3. `status:blocked` — progress cannot continue; record the blocker, who or what can clear it, and the next review point.
4. `status:needs-review` — implementation, decision, or closure evidence is ready for review.

After review, either return the issue to the appropriate open status or close it. On closure, remove the `status:*` label because the closed state is the status. Close as completed only when the acceptance criteria and closure evidence are recorded. Close as not planned, duplicate, or superseded only with a concise reason and a link to the authoritative route when one exists.

Reopen an issue when its original closure criteria were not met or the same outcome materially regressed. Restore the appropriate single status label, confirm the DRI and priority, and explain the reason. Create a new linked issue when the scope, cause, or desired outcome is materially different.

## Escalation

Add `escalation:required` when progress or risk requires an explicit decision from an accountable owner, crosses repository ownership, threatens a P0/P1 outcome, or cannot be resolved within the owning repository. The issue must identify:

- the decision or intervention required;
- the accountable person or team being asked;
- the impact and deadline or next review point; and
- the linked local and org-wide issues involved.

Escalation does not move public-safe execution authority away from the owning issue or create a duplicate tracker. Restricted decisions and evidence remain authoritative in authorized Linear under ZSE and are linked without duplication. Remove `escalation:required` once the decision or intervention is recorded and normal ownership can continue.

## Closure evidence

Before closing, the DRI must:

- update acceptance criteria and task lists;
- link merged pull requests, delivered artifacts, operational evidence, or the recorded decision;
- record validation results and, for changes, rollback/recovery outcome where applicable;
- record residual risk, exceptions, or reasons for declining/cancelling;
- link and assign any remaining follow-up issues; and
- confirm that each linked sub-issue is complete, explicitly waived, or independently owned.

An org-wide parent closes only when its roll-up criterion is met. A local implementation issue may close independently when its local criterion is met and its parent link is current.

## Legacy-label migration

Migrate legacy labels opportunistically when an issue is opened, triaged, reassigned, reopened, or otherwise materially updated. Replace old type, priority, or status labels only when their meaning maps clearly to this vocabulary, and ensure exactly one label in each required category. Do not run a blind bulk migration, rewrite historical closed issues solely for label cleanup, or remove unrelated contextual labels. If the mapping is ambiguous, leave the context intact and resolve it during normal triage.
