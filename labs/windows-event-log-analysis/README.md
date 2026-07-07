# Windows Event Log Analysis

## Executive Summary

This project demonstrates beginner-friendly Windows Security Event Log analysis for suspicious authentication activity. It focuses on evidence collection, event interpretation, risk assessment, and analyst documentation.

## Problem Statement

Windows authentication logs are a core source for SOC investigations. Analysts must identify suspicious login patterns, understand event IDs, and explain whether activity appears benign, suspicious, or malicious.

## Objectives

- Review common Windows Security Event IDs.
- Identify suspicious login behavior.
- Document findings using an analyst-friendly format.
- Recommend practical response actions.

## Key Event IDs

| Event ID | Meaning | Analyst Use |
| --- | --- | --- |
| 4624 | Successful logon | Confirm access and logon type |
| 4625 | Failed logon | Identify brute force, password spraying, or user error |
| 4634 | Logoff | Track session end |
| 4672 | Special privileges assigned | Review privileged account activity |
| 4720 | User account created | Investigate unexpected account creation |
| 4728 | Member added to privileged group | Review privilege escalation risk |

## Investigation Workflow

1. Filter events around the alert timestamp.
2. Identify account name, source IP, workstation, and logon type.
3. Compare failed and successful logon patterns.
4. Check whether privileged activity followed authentication.
5. Determine whether activity aligns with expected user behavior.
6. Document findings and response recommendations.

## Sample Scenario

A workstation records multiple `4625` failed logons for one user followed by a `4624` successful logon from the same source. The analyst should validate whether the user was active, confirm the source device, and review whether privileged events occurred after login.

## Findings and Recommendations

| Finding | Risk | Recommendation |
| --- | --- | --- |
| Multiple failed logons | Medium | Validate user activity and review source host |
| Successful login after failures | Medium | Confirm whether login was expected |
| Privileged event after login | High | Escalate for account review and possible containment |

## Lessons Learned

- Authentication context is essential: account, host, IP, time, and logon type all matter.
- A single failed login is often low risk, but repeated failures followed by success deserves review.
- Privileged activity after suspicious authentication increases severity.

## References

- Microsoft Security Auditing Events: https://learn.microsoft.com/windows/security/threat-protection/auditing/security-auditing-overview
- MITRE ATT&CK Valid Accounts: https://attack.mitre.org/techniques/T1078/