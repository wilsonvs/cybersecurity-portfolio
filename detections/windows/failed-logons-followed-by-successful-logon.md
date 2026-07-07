# Detection: Failed Logons Followed by Successful Logon

## What I Built

I wrote detection logic for repeated Windows failed logons followed by a successful logon from the same user and source IP. This pattern can point to password guessing, password spraying, stale saved credentials, or unauthorized access using valid credentials.

## Evidence Used

| Artifact | Purpose |
| --- | --- |
| [Windows sample events](../../labs/windows-event-log-analysis/sample-windows-security-events.csv) | Event data used to model the scenario |
| [Python triage output](../../tools/python-log-triage/output/sample-output.txt) | Authentication summary used to confirm repeated failures |
| [Credential attack case study](../../labs/soc-home-lab/case-studies/credential-attack-incident-report.md) | Investigation writeup connected to this detection |

## Scenario

A user account generates several Windows Security Event ID `4625` failures from one source IP. Minutes later, the same account records Event ID `4624`, indicating a successful logon. I used this scenario to practice detection writing, triage questions, false-positive review, and response notes.

## Data Sources

| Source | Event | Why I Need It |
| --- | --- | --- |
| Windows Security Event Log | `4625` failed logon | Captures failed authentication attempts and failure reason |
| Windows Security Event Log | `4624` successful logon | Confirms access occurred after failures |
| Identity provider logs | MFA and conditional access | Confirms whether strong authentication protected the account |
| Endpoint telemetry | Process/network activity after logon | Helps check what happened after access was granted |

## Required Fields

| Field | Purpose |
| --- | --- |
| `TimeGenerated` or `_time` | Build the detection window |
| `Account_Name` or `TargetUserName` | Correlate activity by user |
| `Source_Network_Address` or `IpAddress` | Identify the source of login activity |
| `Computer` or `host` | Identify affected endpoint or server |
| `EventCode` or `EventID` | Separate failed and successful logons |
| `Logon_Type` | Distinguish interactive, network, remote, or service logons |

## Detection Logic

```text
IF failed logons for the same user and source IP >= 5
AND a successful logon for that same user and source IP occurs
WITHIN 15 minutes
THEN generate a medium-severity alert
```

## Splunk SPL Example

```spl
index=windows sourcetype=WinEventLog:Security (EventCode=4624 OR EventCode=4625)
| eval outcome=case(EventCode=4625,"failure", EventCode=4624,"success")
| bin _time span=15m
| stats count(eval(outcome="failure")) as failed_logons
        count(eval(outcome="success")) as successful_logons
        values(ComputerName) as hosts
        values(Logon_Type) as logon_types
        by _time Account_Name Source_Network_Address
| where failed_logons >= 5 AND successful_logons >= 1
| sort -_time
```

## Microsoft Sentinel KQL Example

```kql
SecurityEvent
| where EventID in (4624, 4625)
| extend Outcome = iff(EventID == 4625, "Failure", "Success")
| summarize FailedLogons=countif(Outcome == "Failure"),
            SuccessfulLogons=countif(Outcome == "Success"),
            Hosts=make_set(Computer),
            LogonTypes=make_set(LogonType)
  by bin(TimeGenerated, 15m), Account, IpAddress
| where FailedLogons >= 5 and SuccessfulLogons >= 1
| order by TimeGenerated desc
```

## Sigma-Style Detection Draft

```yaml
title: Failed Logons Followed by Successful Logon
status: experimental
description: Detects repeated failed Windows logons followed by a successful logon for the same account and source IP.
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID:
      - 4624
      - 4625
  condition: selection
fields:
  - AccountName
  - SourceNetworkAddress
  - Computer
  - LogonType
falsepositives:
  - User typing an incorrect password repeatedly
  - Stale saved credentials
  - Scheduled task or service account retry behavior
level: medium
```

## MITRE ATT&CK Mapping

| Tactic | Technique | Why I Mapped It |
| --- | --- | --- |
| Credential Access | Brute Force | Multiple failed logons may indicate guessing or password spraying |
| Defense Evasion / Persistence | Valid Accounts | A successful login may indicate use of valid credentials |
| Discovery | Account Discovery | Follow-on activity may include attempts to enumerate systems or privileges |

## Triage Workflow

1. Confirm the user, source IP, destination host, and timestamp.
2. Check whether the source IP is expected for the user, VPN, or business location.
3. Review logon type to understand whether access was local, remote, network, or service-based.
4. Search for other users targeted by the same source IP.
5. Check whether privileged activity followed the successful login.
6. Review MFA or conditional access logs if available.
7. Determine whether to close as benign, monitor, or escalate.

## False Positive Considerations

- User mistyped a password several times.
- A device or application used stale saved credentials.
- VPN reconnect behavior generated repeated attempts.
- Service account password was changed but not updated in a scheduled task.
- Help desk or admin activity was expected during troubleshooting.

## Severity Guidance

| Condition | Suggested Severity |
| --- | --- |
| Failures only, no successful login | Low to Medium |
| Failures followed by successful login | Medium |
| Successful login followed by privileged action | High |
| Same source IP targeting multiple users | High |
| External source plus impossible travel/MFA failure | High |

## Recommended Response

- Validate the login with the account owner.
- Reset the password if activity is unauthorized.
- Review MFA enrollment and conditional access status.
- Check endpoint activity after the successful login.
- Block the source IP if confirmed malicious and appropriate.
- Escalate if privileged activity or lateral movement indicators are present.

## What I Practiced

- Windows Event Log analysis
- SIEM detection logic
- SOC triage workflow
- MITRE ATT&CK mapping
- False-positive analysis
- Incident response communication

## References

- Microsoft Event ID 4625 documentation: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625
- MITRE ATT&CK Brute Force: https://attack.mitre.org/techniques/T1110/
- MITRE ATT&CK Valid Accounts: https://attack.mitre.org/techniques/T1078/
- NIST SP 800-61 incident response guidance: https://csrc.nist.gov/pubs/sp/800/61/r2/final
