# Security Policy and Risk Register

## Executive Summary

This project contains concise security governance artifacts suitable for a junior cybersecurity or GRC analyst portfolio. It demonstrates policy writing, risk tracking, and security control communication.

## Purpose

Security work is not only technical investigation. Organizations also need clear policies, control ownership, risk tracking, and audit-ready documentation.

## Included Artifacts

| Artifact | Purpose |
| --- | --- |
| Acceptable Use Policy | Defines safe and authorized technology use |
| Incident Response Policy | Defines how incidents should be reported and handled |
| Risk Register | Tracks risks, owners, likelihood, impact, and remediation |
| Control Mapping | Connects security activities to recognized frameworks |

## Sample Risk Register

| Risk ID | Risk | Likelihood | Impact | Rating | Owner | Treatment |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Weak authentication controls | Medium | High | High | IT/Security | Enforce MFA and password policy |
| R-002 | Unpatched endpoints | High | High | Critical | IT Operations | Patch systems and verify compliance |
| R-003 | Incomplete asset inventory | Medium | Medium | Medium | IT/Security | Update inventory and assign owners |
| R-004 | Limited log retention | Medium | High | High | Security | Increase retention for critical systems |

## Control Mapping Examples

| Control Activity | NIST CSF Function | Analyst Evidence |
| --- | --- | --- |
| Asset inventory | Identify | Asset list with owners and business function |
| MFA enforcement | Protect | Identity policy and access review evidence |
| Log monitoring | Detect | SIEM alerts and detection rules |
| Incident response | Respond | Incident report and escalation notes |
| Backup validation | Recover | Restore test evidence |

## Lessons Learned

- Security policies should be direct, enforceable, and easy to understand.
- Risk registers are only useful when each risk has an owner and treatment plan.
- GRC documentation should connect business risk with technical controls.

## Future Improvements

- Add complete policy templates.
- Add ISO 27001 and NIST 800-53 mapping examples.
- Add an audit evidence checklist.
