# IOC Analysis Report

## Executive Summary

This project demonstrates how I would review indicators of compromise (IOCs) as part of a SOC or threat intelligence workflow. The goal is to enrich indicators, determine relevance, assess risk, and recommend defensive actions.

## Scenario

A security team receives several IOCs from a threat bulletin: an IP address, domain, file hash, and suspicious URL. The analyst must determine whether any indicators appear in internal logs and recommend next steps.

## Objectives

- Organize IOCs by type.
- Enrich indicators with reputation and context.
- Search for matches in logs.
- Document confidence and recommended action.
- Avoid overreacting to low-confidence indicators.

## IOC Table

| Indicator | Type | Example Context | Initial Action |
| --- | --- | --- | --- |
| `203.0.113.25` | IP address | External destination | Search firewall/proxy/DNS logs |
| `example-login-alert.com` | Domain | Suspicious login domain | Search DNS and email logs |
| `hxxps://example-login-alert.com/auth` | URL | Possible credential harvesting | Defang, review email/web proxy logs |
| `44d88612fea8a8f36de82e1278abb02f` | Hash | Suspicious file hash | Search EDR/file telemetry |

## Enrichment Workflow

1. Defang URLs before documenting or sharing.
2. Identify indicator type and source.
3. Check internal logs for matches.
4. Review external reputation sources where appropriate.
5. Determine whether the indicator is relevant to the organization.
6. Recommend blocking, monitoring, or no action based on confidence.

## Internal Log Search Plan

| Log Source | Search Goal |
| --- | --- |
| DNS logs | Identify hosts resolving suspicious domains |
| Proxy logs | Identify URL visits or blocked requests |
| Firewall logs | Identify outbound connections to suspicious IPs |
| EDR logs | Identify file hash execution or quarantine events |
| Email logs | Identify delivery of messages containing URL/domain |

## Analyst Assessment

| Result | Decision |
| --- | --- |
| IOC appears in internal logs with user activity | Escalate and investigate affected host/user |
| IOC appears only in blocked logs | Monitor and document control effectiveness |
| IOC does not appear internally | Record as intelligence-only; no incident declared |
| IOC confidence is low or source is unclear | Do not block broadly without validation |

## Recommended Response

- Search across DNS, proxy, firewall, email, and endpoint logs.
- Block high-confidence malicious domains or URLs.
- Monitor suspicious IPs if confidence is medium.
- Investigate any host with confirmed IOC contact.
- Preserve evidence and document confidence level.

## Skills Demonstrated

- IOC handling
- Threat intelligence enrichment
- Log search planning
- Risk-based decision making
- Defensive recommendation writing

## References

- CISA Known Exploited Vulnerabilities Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MITRE ATT&CK: https://attack.mitre.org/
