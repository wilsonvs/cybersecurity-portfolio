# Security Policy and Risk Register

## What I Practiced

I practiced writing governance artifacts that connect technical security work to risk, ownership, controls, and follow-up actions.

## Evidence

| Artifact | What I Created |
| --- | --- |
| [security-policy-draft.md](./security-policy-draft.md) | Short policy draft for MFA, patching, logging, access review, and incident reporting |
| [risk-register.csv](./risk-register.csv) | Risk register with likelihood, impact, owner, treatment, and status |
| [control-mapping.md](./control-mapping.md) | Mapping between security activities, NIST CSF functions, evidence, and risk value |

## Scenario

I used a small-organization scenario where security work needs to be tracked clearly: weak authentication, unpatched endpoints, incomplete asset inventory, limited log retention, and missing access reviews.

## What I Did

1. Wrote clear policy statements that can be checked with evidence.
2. Built a risk register with owners, treatment plans, and status.
3. Mapped common security activities to NIST CSF functions.
4. Connected technical work like MFA, patching, logging, and access review to business risk.

## Sample Risk Register View

| Risk ID | Risk | Rating | Owner | Treatment |
| --- | --- | --- | --- | --- |
| R-001 | Weak authentication controls | High | IT Security | Enforce MFA and review password policy |
| R-002 | Unpatched endpoints | Critical | IT Operations | Patch systems and verify compliance |
| R-004 | Limited log retention | High | Security Operations | Increase retention for critical systems |
| R-005 | No formal access review | High | Identity Team | Start quarterly access reviews |

## What I Learned

- A policy should be direct enough that someone can collect evidence against it.
- A risk register is stronger when every risk has an owner, treatment, and status.
- GRC work still needs technical understanding because controls must connect to real systems, logs, identities, and remediation tasks.

## Improvements I Want To Add

- Add ISO 27001 and NIST 800-53 mapping examples.
- Add an audit evidence checklist.
- Add a before-and-after risk treatment example.
