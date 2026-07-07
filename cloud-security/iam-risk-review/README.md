# Cloud IAM Risk Review

## Executive Summary

I practiced a cloud identity and access management review focused on risks that commonly affect real environments: excessive permissions, missing MFA, inactive accounts, shared credentials, and weak access review processes.

## Scenario

A small organization wants to improve cloud account security. I reviewed identity settings and prepared a risk-based summary for IT leadership.

## Objectives

- Identify common IAM risks.
- Explain business impact clearly.
- Recommend practical remediation actions.
- Map findings to security controls and governance language.

## Review Areas

| Area | What I Would Check | Why It Matters |
| --- | --- | --- |
| MFA coverage | Whether users and admins have MFA enabled | Reduces account takeover risk |
| Privileged accounts | Who has admin or owner permissions | Limits blast radius if credentials are stolen |
| Inactive users | Accounts with no recent activity | Reduces unnecessary access |
| Shared accounts | Non-attributable login accounts | Weakens accountability and auditability |
| Access reviews | Whether permissions are reviewed periodically | Helps maintain least privilege |
| Service accounts | Credentials, scope, and rotation | Reduces long-lived secret risk |

## Sample Findings

| Finding | Severity | Business Risk | Recommendation |
| --- | --- | --- | --- |
| MFA not enforced for all users | High | Increased account takeover risk | Enforce MFA for all users, prioritize admins first |
| Too many privileged users | High | Larger impact if one account is compromised | Review admin roles and apply least privilege |
| Inactive accounts still enabled | Medium | Unused access may be abused | Disable or remove inactive accounts after validation |
| No formal access review | Medium | Permissions may drift over time | Perform quarterly access reviews |
| Long-lived service credentials | Medium | Credentials may be exposed and reused | Rotate secrets and scope permissions tightly |

## Risk Register Entry Example

| Risk ID | Risk | Likelihood | Impact | Rating | Treatment |
| --- | --- | --- | --- | --- | --- |
| IAM-001 | Admin accounts without MFA | Medium | High | High | Enforce MFA and monitor privileged sign-ins |
| IAM-002 | Excessive privileged access | Medium | High | High | Remove unused admin roles and document exceptions |
| IAM-003 | Inactive enabled users | Medium | Medium | Medium | Disable inactive users after owner confirmation |

## Recommended Remediation Plan

1. Enforce MFA for administrators.
2. Review all privileged roles and remove unnecessary access.
3. Disable inactive accounts after business-owner validation.
4. Create a quarterly access review process.
5. Monitor privileged sign-ins and risky login behavior.
6. Rotate long-lived service credentials and document ownership.

## Control Mapping

| Control Goal | Example Evidence |
| --- | --- |
| Least privilege | Role review export and approved exceptions |
| Strong authentication | MFA policy screenshot or configuration export |
| Account lifecycle management | Disabled inactive accounts list |
| Auditability | Access review signoff and risk register update |

## What I Practiced

- IAM risk review
- Least privilege analysis
- GRC documentation
- Risk register writing
- Cloud security fundamentals
- Clear risk communication

## Improvements I Want To Add

- Add Azure Entra ID sample review checklist.
- Add AWS IAM user and role review examples.
- Add screenshots from a lab tenant with sensitive data removed.

## References

- Microsoft identity security best practices: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices
- AWS IAM security best practices: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
