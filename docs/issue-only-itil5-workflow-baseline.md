# Issue-only ITIL-aligned workflow baseline

This document proposes the lightweight, reusable operating baseline requested in [issue #45](https://github.com/Conxian/.github/issues/45) for work tracked in Conxian GitHub repositories. It uses ITIL-aligned concepts without claiming formal ratification, ITIL certification, or conformance.

For public-safe repository and governance work, GitHub issues are the canonical execution records. Restricted strategy, security, legal, financial, and detailed operational material remains canonical in the authorized Linear workspace under Zero Secret Egress (ZSE); GitHub should link to that authority without duplicating restricted context. Do not maintain competing public and private plans, status narratives, or acceptance checklists for the same scope. This issue-only baseline does not require GitHub Projects or milestones; that is a scope choice for this baseline, not a ban on those tools in every Conxian delivery process.

## Issue types and labels

Every issue using this baseline should have exactly one type label when the labels are available.

| Work type | Label | Use when |
| --- | --- | --- |
| Incident | `type: incident` | An unplanned interruption, degradation, or operational failure needs restoration. Security vulnerabilities, privileged incident details, and response runbooks must use [private security reporting](../SECURITY.md) and authorized Linear/ZSE handling, not a public issue; a sanitized issue may coordinate non-sensitive follow-up. |
| Service request | `type: service-request` | A user or maintainer requests a standard, bounded service or access outcome. |
| Problem | `type: problem` | The underlying cause of one or more incidents needs investigation or permanent correction. |
| Change | `type: change` | A controlled modification to code, infrastructure, configuration, policy, or a shared operating default is proposed. |
| Risk | `type: risk` | An uncertain event or condition could affect an objective and needs treatment or acceptance. |
| Control | `type: control` | A preventive, detective, or corrective safeguard needs definition, operation, or evidence. |
| Improvement | `type: improvement` | A measurable enhancement to a product, service, process, or operating outcome is proposed. |

Labels are routing metadata, not a second workflow system. Repositories may add domain labels, but should preserve these type names for organization-wide consistency. Repositories that do not yet have the labels may state the type in the issue body until label provisioning is completed.

## Minimum issue structure

Use one GitHub issue for one owned outcome. All seven issue types share this minimum structure:

- **Summary:** the condition, request, or proposed outcome in plain language.
- **Type:** one of the seven types above.
- **Scope and affected surface:** repository, component, service, policy, or user group in scope; include explicit boundaries when useful.
- **Impact and priority:** who or what is affected, the consequence, urgency, and any time constraint.
- **Owner:** one directly responsible assignee; list collaborators separately when needed.
- **Required outcome:** the observable result that permits closure.
- **Checklist:** the smallest ordered set of actions needed to reach the outcome.
- **Evidence and references:** relevant issues, pull requests, runs, decisions, logs, or documents. Redact secrets and sensitive operational data.
- **Dependencies and blockers:** external decisions or work that can prevent progress.
- **Closure evidence:** links or a concise record proving the outcome and validation.
- **Follow-ups:** linked work explicitly excluded from this issue, or `None`.

Issue bodies may use this compact checklist:

```markdown
## Summary
## Type
## Scope and affected surface
## Impact and priority
## Owner
## Required outcome
## Checklist
- [ ]
## Evidence and references
## Dependencies and blockers
## Closure evidence
## Follow-ups
```

## Type-specific evidence and exit criteria

The common structure applies first. Add the following minimum evidence before closing each type.

| Type | Minimum issue evidence | Exit criteria |
| --- | --- | --- |
| Incident | Public-safe start/detection time, observed impact, affected surface, response timeline, mitigation or workaround, and related incident/problem links. Keep vulnerability data, privileged timelines, response runbooks, secrets, and sensitive operational detail in the private channels defined above. | Service is restored or impact is contained; public-safe validation and restoration time are recorded; unresolved cause or prevention work is linked as a problem or improvement. |
| Service request | Requester or beneficiary, requested outcome, authorization/dependency notes where relevant, and acceptance criteria. | The requested outcome is delivered or a reasoned denial/cancellation is recorded; the requester or owner has evidence of validation. |
| Problem | Related incidents, symptoms and known facts, investigation notes, workaround or known-error status, and cause hypothesis or finding. | Root cause is recorded or the limits of the investigation are explicit; permanent correction, accepted risk, or further investigation is linked and owned. |
| Change | Proposed change, reason, affected surfaces, risk/impact assessment, implementation plan, validation plan, and rollback or recovery plan. | The change and validation evidence are linked; outcome and any rollback are recorded; follow-up defects or improvements are separately linked. |
| Risk | Cause-event-impact statement, likelihood, impact, current safeguards, treatment choice, treatment owner, and target date or review trigger. | Treatment is completed and residual risk recorded, or acceptance/transfer/avoidance is explicitly approved by an accountable owner with a review condition. |
| Control | Control objective, owner, scope, operation/frequency, expected evidence, test method, and known exceptions. | Operation and test evidence are linked; exceptions have owners and dispositions; the next review trigger is recorded when recurring. |
| Improvement | Current condition, target condition, expected value, success measure, proposed action, and affected stakeholders. | The change is delivered and the measure is recorded, or the issue documents why it was stopped; remaining opportunities are linked separately. |

## State, status, and priority

GitHub's native issue state stays lean: an issue is **open** while action, validation, or an explicit disposition remains, and **closed** once its exit criteria and closure evidence are recorded.

Use at most one status label at a time when the common labels are provisioned:

1. `status: triage` — type, scope, owner, priority, and routing are being confirmed.
2. `status: ready` — outcome and minimum acceptance or exit criteria are clear enough to start.
3. `status: in-progress` — the assignee is actively driving the work.
4. `status: review` — implementation, evidence, or a decision is awaiting validation.
5. `status: blocked` — progress cannot continue; the blocking dependency and next review point must be in the issue.

The normal progression is `triage` → `ready` → `in-progress` → `review` → closed. `blocked` temporarily replaces the active status and returns to the appropriate status when cleared. Reopen a closed issue only when its recorded outcome is no longer valid; otherwise create and link a new issue for newly discovered scope.

Priority is a triage decision based on impact and urgency, not issue type. Use the repository's existing priority labels if available, or record one of these terms in the issue body:

- **Critical:** active or imminent severe impact; triage immediately.
- **High:** material impact or time-sensitive obligation; prioritize ahead of routine work.
- **Medium:** meaningful impact with a practical workaround or normal scheduling tolerance.
- **Low:** limited impact, preventive work, or an opportunity that can wait.

For incidents, record both severity of current impact and urgency of restoration. For risks, record likelihood and impact separately before deriving priority. Priority does not replace a clear impact statement.

## Ownership and triage

- The repository maintainers triage new issues and confirm type, routing, priority, and sufficient minimum information.
- The assignee is the single directly responsible owner for progress, status accuracy, escalation, and closure evidence. Unassigned issues remain in triage.
- CODEOWNERS identify reviewers for affected files or governance surfaces; they do not replace the issue assignee or automatically approve risk acceptance.
- Contributors complete checklist items and provide evidence through linked pull requests, comments, or artifacts without copying the work plan elsewhere.
- The accountable maintainer or governance owner makes approval, denial, exception, or risk-acceptance decisions when those decisions exceed the assignee's authority.

Triage should correct the issue in place rather than duplicate it. If the issue is misrouted, transfer it when GitHub supports the destination; otherwise open the destination issue, link both records, and close the original with the routing reason.

## Repository routing and cross-repository escalation

Open work in the repository that owns the affected product, service, code, configuration, or documentation:

- Product-specific incidents, requests, problems, changes, risks, controls, and improvements belong in that product repository.
- Organization-wide contribution defaults, shared community health files, common workflow guidance, repository governance, taxonomy, or cross-repository operating controls belong in `Conxian/.github`.
- Sensitive internal business, partner, strategy, financial, legal, credential, security, or detailed operational material does not belong in public repositories. Follow the [repository taxonomy](../repository-taxonomy.md), [security reporting policy](../SECURITY.md), and authorized Linear/ZSE boundaries.

When one outcome spans repositories:

1. Keep one coordinating issue in the repository accountable for the overall outcome; use `.github` when the outcome is organization-wide governance.
2. Create repo-local issues only for independently owned implementation or evidence that must be maintained with that repository.
3. Link every repo-local issue to the coordinating issue and state the exact delegated scope.
4. Record aggregate decisions and final closure evidence on the coordinating issue; keep implementation detail on the repo-local issue.
5. Escalate unresolved ownership, conflicting controls, material cross-repository risk, or a blocked dependency to `.github` with links to the source records and a specific decision request.

Do not copy checklists or status updates across coordinating, repo-local, and Linear records. Each public-safe GitHub issue is canonical for its stated execution scope; when restricted context is required, link to the authorized Linear authority without reproducing it. Links provide the organization-wide view.

## Closure and follow-up boundaries

Before closing, the assignee should:

- complete or disposition every required checklist item;
- add the type-specific exit evidence;
- link delivered changes, validation, approvals, or decisions;
- summarize the actual outcome and any variance from the original plan;
- identify remaining risks, exceptions, or follow-ups with an owner, or state `None`;
- remove obsolete status labels and close the issue with the correct resolution context.

Do not hold an otherwise complete issue open for unrelated improvements. Create a linked follow-up when work has a different owner, priority, repository, acceptance criterion, or delivery window. A follow-up link is not closure evidence for the current issue's required outcome.

## Follow-ups and non-goals

Follow-up decisions may include:

- provisioning the common type and status labels in repositories that adopt the baseline;
- deciding whether a small number of shared issue forms would reduce missing information;
- adding proportionate checks for label consistency only if repeated usage proves a need.

This baseline does **not**:

- create seven issue forms or require one form per type;
- mutate repository labels or settings;
- require GitHub Projects, milestones, or another planning layer for this baseline;
- make Linear canonical for public-safe repository execution or duplicate restricted Linear context in GitHub;
- automate approvals, risk acceptance, routing, or closure;
- replace repository-specific incident response, security, release, or regulatory procedures.
