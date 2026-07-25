# Issue-only operational workflow

## Purpose and scope

This document defines Conxian's lightweight, issue-only operating convention. It is informed by the ITIL 5 model requested in the governing issue, but it does not claim formal ITIL adoption, compliance, or certification.

GitHub Issues are the source of truth for operational work. Use the issue, its assignee, task lists, comments, linked pull requests, linked issues, and sub-issues to plan and report progress. Do not create GitHub Projects, milestones, duplicate trackers, or parallel status surfaces unless a separately documented gap proves that this policy must change.

This baseline applies across Conxian repositories. Repository-specific contribution, support, and security rules still apply. Suspected vulnerabilities must follow [`SECURITY.md`](../SECURITY.md) and must never be opened as public incident issues.

## Route work to the owning repository

Create actionable work in the repository that owns the affected product, service, documentation, or automation. This keeps implementation context, code review, and closure evidence together.

Use `.github` for:

- organization-wide governance and policy;
- shared controls, templates, and default workflows;
- organization-wide documentation and repository standards; and
- cross-repository coordination that cannot be completed in one owning repository.

When work begins in the wrong repository, link to the correctly routed issue and close or convert the original into a brief routing record. Escalation should link work, not duplicate its details, task list, or status reporting. See [`SUPPORT.md`](../SUPPORT.md) for existing support and governance routing.

## Choose one issue category

Each issue should have one primary category. Choose the category that best describes the outcome being managed, even if the work has secondary effects.

| Category | Use when | Minimum category-specific information | Owner expectation | Close when |
| --- | --- | --- | --- | --- |
| **Incident** | An unplanned interruption, degradation, or operational failure needs service restoration. Do not use for suspected vulnerabilities; follow [`SECURITY.md`](../SECURITY.md). | Start time or discovery time; affected service and user impact; current symptoms; containment or workaround; restoration evidence; follow-up problem link when root cause is unresolved. | The assignee coordinates restoration, updates material changes, and names any follow-up owner. | Service is restored or an accepted workaround is operating, evidence is recorded, and unresolved cause or prevention work is linked. |
| **Service request** | Someone needs a standard access, information, configuration, support, or operational fulfillment action. | Requester and desired outcome; requested scope; approvals or eligibility where applicable; delivery evidence; acceptance criterion. | The assignee confirms scope, fulfills or routes the request, and records delivery. | The request is fulfilled and accepted, or declined with a clear reason and next route. |
| **Problem** | The underlying cause of one or more incidents or recurring defects needs investigation and prevention. | Related incidents; observed pattern; known impact; hypotheses and evidence; root-cause finding or known-error record; proposed prevention work. | The assignee drives evidence-based analysis and links resulting changes or improvements. | Root cause or the best-supported explanation is documented, and agreed remediation is completed or tracked in linked owned issues. |
| **Change** | A controlled modification to a product, service, shared configuration, policy, or operating environment is proposed. | Change outcome and scope; affected surfaces; risk assessment; implementation plan; validation plan; rollback or recovery plan; required reviewers or approvals. | The assignee coordinates review, execution, validation, and rollback readiness. | The change is implemented and validated, or rejected/cancelled with the decision and any recovery action recorded. |
| **Risk** | A possible event or condition could affect objectives and needs an explicit treatment decision. | Risk statement with cause, event, and impact; likelihood and impact assessment; affected owner; treatment choice; mitigation tasks; review trigger or target date. | The assignee maintains the assessment and drives acceptance, avoidance, transfer, or mitigation by the accountable owner. | The risk is eliminated, accepted by the accountable owner, transferred, or reduced to the documented target, with residual risk recorded. |
| **Control** | An organization-wide or repository-level safeguard needs definition, evidence, review, or remediation. | Control objective; scope; control owner; expected evidence; test or review method; identified gap; remediation or exception path. | The assignee gathers evidence and coordinates with the control owner and affected repositories. | The control is evidenced as effective, or its gap and approved remediation/exception are linked and owned. |
| **Improvement** | A measurable enhancement to quality, efficiency, reliability, developer experience, or operating practice is proposed outside immediate incident restoration. | Current state; desired measurable outcome; beneficiaries; proposed approach; validation measure; constraints or dependencies. | The assignee confirms value, coordinates delivery, and captures before/after evidence where practical. | The improvement is delivered and its outcome is validated, or it is declined with the decision recorded. |

## Minimum issue checklist

Every operational issue should state:

- [ ] the desired outcome and current impact or value;
- [ ] the scope and affected repository, product, or service;
- [ ] one primary issue category;
- [ ] one accountable assignee;
- [ ] relevant evidence and links;
- [ ] risk, rollback or recovery, and validation information when applicable; and
- [ ] an explicit done or closure criterion.

Keep details proportionate to the work. A low-risk service request may need a few sentences; a cross-repository change may need a detailed checklist and linked implementation issues.

## Lifecycle and status

GitHub's **Open** and **Closed** states are authoritative:

- **Open** means the outcome still needs triage, ownership, action, or a recorded decision.
- **Closed** means the stated closure criterion has been met, the work was declined or cancelled with a reason, or it was superseded by a clearly linked issue.

Within an open issue, use this simple progression without requiring a Project or milestone:

1. **Triage** — confirm routing, category, scope, impact, and closure criterion.
2. **Owned** — assign one accountable person and identify collaborators or reviewers.
3. **In progress** — perform the work and update the issue through comments, task lists, linked pull requests, linked issues, or sub-issues.
4. **Blocked** — record the blocker, the person or dependency that can clear it, and the next review point.
5. **Done** — provide closure evidence and close the issue.

Labels must not become a parallel status system. If configuration is approved later, `status: blocked` may be used as an optional visibility aid; it is not authoritative and must be supported by a current issue comment. Other progression states do not need labels.

Reopen an issue when its original closure criterion was not actually met or the same outcome has materially regressed and continuing the existing history is clearer than creating new work. Add a comment explaining why it was reopened, the current impact, the new owner, and the revised closure criterion. Create a new linked issue instead when the scope, cause, or desired outcome is meaningfully different.

## Ownership and closure

- **Reporter:** provides enough context for triage, answers material questions when available, and confirms acceptance when they are the appropriate requester. Reporting an issue does not automatically make the reporter its owner.
- **Assignee:** is the single accountable coordinator. They keep scope, blockers, links, and closure evidence current, even when several people contribute.
- **Repository owners:** confirm routing and priority, help assign ownership, enforce repository rules, and verify that closure evidence is sufficient for the affected surface.
- **`.github` owners:** maintain this shared baseline and coordinate organization-wide controls. They do not replace product or service repository owners for local implementation.

Before closing, the assignee should update the task list, link delivered pull requests or evidence, record any decision or residual risk, and link all remaining follow-up work. Close stale or invalid requests only with a concise reason and a correct route when one exists.

## Cross-repository escalation

Keep local implementation issues in their owning repositories. Create one parent or control issue in `.github` only when work requires organization-wide policy, a shared control, or coordinated changes across repositories.

The `.github` coordination issue should:

1. state the shared outcome, affected repositories, accountable coordinator, and roll-up closure criterion;
2. link one local implementation issue per affected repository rather than copying each task list;
3. record cross-repository decisions, dependencies, exceptions, and shared evidence; and
4. close only after linked local outcomes are complete, explicitly waived, or moved to separately owned follow-up issues.

Local issues should link back to the `.github` parent and remain authoritative for their implementation status. The parent is a coordination and closure roll-up, not a duplicate tracker.

## Follow-up configuration proposals

The following items are recommendations for separate configuration work. **They are not active configuration and are not implemented by this document:**

- consider one label for each category: `type: incident`, `type: service-request`, `type: problem`, `type: change`, `type: risk`, `type: control`, and `type: improvement`;
- optionally add `status: blocked` as the only status label;
- prefer one shared operational-work issue template with a category selector and common fields instead of seven near-duplicate templates;
- retain the existing bug-report and governance-request templates for their focused entry paths; and
- handle stale label references in the existing bounty template as separate template-hygiene work.

Any label or template rollout should first confirm naming, repository coverage, migration impact, and ownership. It must not introduce Projects, milestones, or another authoritative status surface.

## Example

A wallet service degradation belongs in the wallet repository as an **incident** with impact, symptoms, restoration actions, an assignee, and a restoration criterion. If investigation finds a recurring shared dependency failure, link a **problem** issue in the owning dependency repository. Create a `.github` **control** issue only if several repositories need a shared policy or control change; link each local implementation issue and use the control issue solely for coordination and final roll-up.
