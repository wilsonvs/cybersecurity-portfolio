# SIEM Detection Lab

## Executive Summary

This project documents how a junior analyst can convert suspicious behavior into clear SIEM detection logic, triage notes, and MITRE ATT&CK mapping.

## Problem Statement

A useful detection must be understandable, testable, and actionable. This lab focuses on detection quality rather than tool-specific complexity.

## Objectives

- Define suspicious behavior.
- Identify required log sources.
- Write simple detection logic.
- Map behavior to MITRE ATT&CK.
- Document triage and false-positive notes.

## Detection Use Case

Detect repeated failed authentication attempts followed by a successful login for the same account within a short time window.

## Required Fields

| Field | Purpose |
| --- | --- |
| timestamp | Build the detection window |
| user | Correlate failed and successful attempts |
| source_ip | Identify origin of activity |
| host | Identify affected system |
| event_id | Distinguish failed and successful authentication |
| logon_type | Understand interactive, remote, or service logon context |

## Pseudocode Logic

```text
IF count(failed_logon_events by user, source_ip) >= 5
AND successful_logon_event exists for same user and source_ip
WITHIN 15 minutes
THEN create medium-severity alert
```

## MITRE ATT&CK Mapping

| Tactic | Technique | Rationale |
| --- | --- | --- |
| Credential Access | Brute Force | Multiple failed attempts may indicate guessing or spraying |
| Defense Evasion / Persistence | Valid Accounts | A successful login may indicate valid credential use |

## Triage Questions

- Is the source IP expected for this user?
- Is the host a normal login destination?
- Did privileged activity occur after login?
- Is MFA enabled for the account?
- Are other users seeing similar failed logins from the same source?

## False Positive Considerations

- User mistyped password several times.
- Stored credentials were stale on a device or service.
- VPN or remote access generated repeated attempts.
- Scheduled service account activity was expected.

## Recommendations

- Validate activity with the account owner.
- Review MFA and conditional access status.
- Check for related alerts from the same source IP.
- Reset credentials if unauthorized activity is suspected.

## Future Improvements

- Add Splunk SPL, KQL, and Wazuh rule versions.
- Add sample logs and expected alert output.
- Add screenshots from a SIEM dashboard.