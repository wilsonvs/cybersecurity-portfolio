# SIEM Detection Lab

## What I Practiced

I practiced turning suspicious behavior into SIEM detection logic that is understandable, testable, and useful for triage.

## Detection Use Case

Repeated failed authentication attempts followed by a successful login for the same account and source IP within a short time window.

## Evidence Used

| Artifact | Purpose |
| --- | --- |
| [Windows sample events](../windows-event-log-analysis/sample-windows-security-events.csv) | Events used to model the detection |
| [Python triage output](../../tools/python-log-triage/output/sample-output.txt) | Quick summary of authentication counts |
| [Failed logon detection writeup](../../detections/windows/failed-logons-followed-by-successful-logon.md) | SPL, KQL, Sigma-style logic, and response notes |

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

| Tactic | Technique | Why I Mapped It |
| --- | --- | --- |
| Credential Access | Brute Force | Multiple failures may indicate guessing or spraying |
| Defense Evasion / Persistence | Valid Accounts | A successful login may indicate use of valid credentials |

## Triage Questions

- Is the source IP expected for this user?
- Is the host a normal login destination?
- Did privileged activity occur after login?
- Is MFA enabled for the account?
- Are other users seeing similar failed logins from the same source?

## What I Learned

Good detections need clear logic and clear limitations. I should document false positives and next checks so the alert can be investigated consistently.
