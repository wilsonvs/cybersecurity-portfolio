# SOC Case Study: Failed Logons Followed by Successful Authentication

## What I Investigated

I investigated a lab scenario where repeated Windows failed logons were followed by a successful authentication. I used the scenario to practice alert triage, evidence review, MITRE ATT&CK mapping, risk assessment, and response recommendations.

## Evidence Used

| Artifact | Purpose |
| --- | --- |
| [Windows sample events](../../windows-event-log-analysis/sample-windows-security-events.csv) | Authentication events used for the timeline |
| [Windows timeline image](../../../assets/screenshots/windows-event-log-timeline.svg) | Visual summary of the event sequence |
| [Python triage output](../../../tools/python-log-triage/output/sample-output.txt) | Authentication summary generated from sample data |

## Alert Summary

| Field | Value |
| --- | --- |
| Alert Name | Multiple Failed Logons Followed by Successful Logon |
| Severity | Medium |
| User | `alice` |
| Source IP | `10.0.0.50` |
| Destination Host | `workstation-01` |
| Failed Events | Windows Event ID `4625` |
| Successful Event | Windows Event ID `4624` |
| Time Window | 15 minutes |
| Status | Escalate for validation |

## Investigation Steps

### 1. Validate Alert Scope

I first confirmed that the alert was limited to one user and one source IP. This helps determine whether the event looks like a single-user issue, password guessing, or broader password spraying.

### 2. Review Authentication Timeline

| Time | Event ID | User | Source IP | Host | Result |
| --- | --- | --- | --- | --- | --- |
| 09:00 | 4625 | alice | 10.0.0.50 | workstation-01 | Failed logon |
| 09:01 | 4625 | alice | 10.0.0.50 | workstation-01 | Failed logon |
| 09:02 | 4625 | alice | 10.0.0.50 | workstation-01 | Failed logon |
| 09:03 | 4624 | alice | 10.0.0.50 | workstation-01 | Successful logon |

The failed attempts followed by success increased the risk because access was eventually granted.

### 3. Determine Whether the Source Is Expected

I would check whether `10.0.0.50` belongs to the user's normal workstation, VPN address pool, or another internal host. If the source is unfamiliar, the alert becomes more suspicious.

### 4. Review Logon Type

| Logon Type | Meaning | Triage Value |
| --- | --- | --- |
| 2 | Interactive | Local keyboard/screen login |
| 3 | Network | Network share or remote service access |
| 10 | Remote Interactive | RDP-style access |

Remote or network logons from an unusual source would increase priority.

### 5. Search for Related Activity

I would search for:

- Other users targeted by `10.0.0.50`
- Privileged group changes after the login
- Process execution after the successful logon
- New scheduled tasks or services
- Outbound connections from the destination host

### 6. Map to MITRE ATT&CK

| Tactic | Technique | Why I Mapped It |
| --- | --- | --- |
| Credential Access | Brute Force | Repeated failed logons may indicate password guessing |
| Defense Evasion / Persistence | Valid Accounts | Successful logon may indicate valid credential use |
| Discovery | Account Discovery | Follow-on activity could include enumeration after access |

## Findings

| Finding | Assessment |
| --- | --- |
| Multiple failed logons occurred in a short period | Suspicious enough to investigate |
| A successful logon followed the failures | Increases concern because access was granted |
| Source IP must be validated | Determines whether this is benign or suspicious |
| No privileged action is shown in the sample data | Severity remains Medium unless additional evidence appears |

## Recommendation

1. Validate activity with the account owner.
2. Confirm whether the source IP is assigned to the user's normal workstation or VPN session.
3. Review MFA or conditional access logs if available.
4. Reset the user's password if the login is not expected.
5. Check endpoint activity after the successful logon.
6. Escalate to incident response if privileged activity, lateral movement, or suspicious process execution is found.

## Analyst Notes

This alert should not be closed only because the source IP is internal. Internal IPs can represent compromised endpoints, shared jump boxes, VPN sessions, or misconfigured services. The correct decision depends on identity context, source ownership, logon type, and post-login activity.

## What I Learned

- A clear timeline makes the investigation easier to communicate.
- Failed logons followed by success are more important than failed logons alone.
- False-positive review is part of good SOC work, not an afterthought.
- The best incident notes include what happened, why it matters, what was checked, and what should happen next.
