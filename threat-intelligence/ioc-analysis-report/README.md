# IOC Analysis Report

## What I Practiced

I practiced organizing indicators of compromise, defanging risky values, planning internal log searches, and deciding when an indicator should be blocked, monitored, or documented only.

## Evidence

| Artifact | Purpose |
| --- | --- |
| [indicators.csv](./indicators.csv) | IOC table with type, context, confidence, search target, and action |
| This README | Enrichment workflow, search plan, assessment logic, and response notes |

## Scenario

A security bulletin includes an IP address, domain, URL, and file hash. I treated the indicators as a lab exercise and planned how I would check whether any of them appeared in internal telemetry.

## IOC Table

| Indicator | Type | Context | Initial Action |
| --- | --- | --- | --- |
| `203.0.113.25` | IP address | External destination | Search firewall/proxy logs |
| `example-login-alert.com` | Domain | Suspicious login domain | Search DNS and email logs |
| `hxxps://example-login-alert[.]com/auth` | URL | Possible credential harvesting | Review email and web proxy logs |
| `44d88612fea8a8f36de82e1278abb02f` | Hash | Suspicious file hash | Search EDR/file telemetry |

## What I Did

1. Separated indicators by type.
2. Defanged the suspicious URL before documenting it.
3. Assigned each IOC to the most useful log source.
4. Added confidence levels and recommended action.
5. Avoided broad blocking when confidence or internal relevance was not clear.

## Internal Log Search Plan

| Log Source | Search Goal |
| --- | --- |
| DNS logs | Identify hosts resolving suspicious domains |
| Proxy logs | Identify URL visits or blocked requests |
| Firewall logs | Identify outbound connections to suspicious IPs |
| EDR logs | Identify file hash execution or quarantine events |
| Email logs | Identify delivery of messages containing URL/domain |

## Decision Logic

| Result | Decision |
| --- | --- |
| IOC appears in internal logs with user activity | Escalate and investigate affected host/user |
| IOC appears only in blocked logs | Monitor and document control effectiveness |
| IOC does not appear internally | Record as intelligence-only; no incident declared |
| IOC confidence is low or source is unclear | Do not block broadly without validation |

## What I Learned

- IOC handling is about confidence and context, not just copying indicators into a block list.
- The right search source depends on indicator type.
- Defanging URLs makes reports safer to read and share.

## References

- CISA Known Exploited Vulnerabilities Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MITRE ATT&CK: https://attack.mitre.org/
