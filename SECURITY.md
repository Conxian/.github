# Security Policy

## Scope

This policy applies to security vulnerabilities in Conxian-managed GitHub repositories and governance surfaces maintained in this repository (including templates, workflows, and repository-level policy files).

## Support Policy

Security fixes are applied on a rolling basis to the default branch (`main`). This repository does not currently publish versioned releases or support branches.

| Channel                     | Security fixes                       |
| --------------------------- | ------------------------------------ |
| `main` (default branch)     | Yes                                  |
| Other branches/tags/commits | Not actively maintained for security |

## Reporting a Vulnerability

**Do not report security vulnerabilities via public GitHub issues.**

Use one of the following private channels:

1. GitHub private vulnerability reporting (Security Advisories) on the affected repository.
2. Email: **security@conxian-labs.com**.

If you cannot use either channel, email **admin@conxian-labs.com** and clearly label the message as a security report.

Include, where possible:

- A clear description of the issue.
- Steps to reproduce or a proof-of-concept.
- Potential impact.
- Suggested remediation.

## Severity and Triage

Reports are triaged by impact and exploitability using four internal severity bands:

- **Critical:** Active or easily weaponized impact to core infrastructure, funds, keys, or governance control.
- **High:** Significant security impact with realistic exploitation path.
- **Medium:** Meaningful weakness with constrained impact or preconditions.
- **Low:** Defense-in-depth or hardening improvement with limited direct impact.

## Response and Remediation Targets

These are target timelines, not guarantees. Complex issues may require staged mitigations.

| Severity | Acknowledgement target | Triage update target | Remediation target                  |
| -------- | ---------------------- | -------------------- | ----------------------------------- |
| Critical | 24 hours               | 72 hours             | Mitigation ASAP, target <= 7 days   |
| High     | 72 hours               | 5 business days      | Target <= 30 days                   |
| Medium   | 5 business days        | 10 business days     | Target <= 90 days                   |
| Low      | 10 business days       | 15 business days     | Scheduled as planned hardening work |

## Safe Harbor and Coordinated Disclosure

We support good-faith security research and coordinated disclosure.

If you act in good faith, avoid privacy violations/data destruction/service disruption, and give us reasonable time to remediate before public disclosure, Conxian Labs will not pursue legal action for your research activity.

We may publicly credit researchers after remediation unless anonymity is requested.

## Encrypted Reporting

We do not currently publish a long-lived public PGP key for this repository.

If encrypted communication is required, contact **security@conxian-labs.com** and request an encrypted reporting channel; we can arrange a temporary encrypted channel during triage.
