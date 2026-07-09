# SOC Case Study: Unusual Outbound Network Activity

## What I Investigated

I investigated a lab scenario where a workstation generated repeated outbound connections to an unfamiliar external destination. The goal was to practice network alert triage, Zeek-style log review, source validation, possible beaconing analysis, and response recommendations.

## Scenario

A network monitoring alert identifies repeated outbound HTTPS connections from an internal workstation to a rare external domain. The destination is not part of normal business traffic.

## Alert Summary

| Field | Value |
| --- | --- |
| Alert Name | Repeated Outbound Connections to Rare Destination |
| Severity | Medium in this lab |
| Source Host | `workstation-01` |
| Source IP | `10.0.0.25` |
| Destination | `example-suspicious-domain.test` |
| Protocol | HTTPS |
| Evidence Source | Zeek-style connection log |
| Initial Verdict | Suspicious, requires endpoint and DNS validation |

## Evidence Used

| Artifact | Purpose |
| --- | --- |
| [Sample Zeek connection log](../../network-traffic-analysis/sample-zeek-conn.log) | Network connection evidence |
| [Network analysis notes](../../network-traffic-analysis/network-analysis-notes.md) | Traffic review notes |
| [Traffic summary image](../../../assets/screenshots/network-traffic-summary.svg) | Screenshot-style summary of outbound activity |

## Evidence Timeline

| Time | Source | Destination | Protocol | Interpretation |
| --- | --- | --- | --- | --- |
| 11:00 | `10.0.0.25` | Rare external domain | HTTPS | First observed connection |
| 11:05 | `10.0.0.25` | Same destination | HTTPS | Repeated connection pattern |
| 11:10 | `10.0.0.25` | Same destination | HTTPS | Possible periodic activity |
| 11:15 | `10.0.0.25` | Same destination | HTTPS | Needs endpoint correlation |

## Why This Matters

Repeated outbound connections can be normal software activity, but they can also indicate command-and-control, malware check-ins, unauthorized tools, data staging, or misconfigured applications. The triage depends on destination reputation, frequency, process ownership, DNS behavior, and endpoint evidence.

## Evidence I Would Review

- Zeek `conn.log`, `dns.log`, and `ssl.log`
- Firewall allow/deny logs
- Proxy logs and URL categories
- Endpoint process making the connection
- DNS query history for the domain
- Destination domain age and reputation
- Volume of data transferred
- Other internal hosts contacting the same destination
- Authentication or file activity around the same time

## Detection Logic Idea

### Plain Language

Alert when an internal workstation repeatedly connects to a rare external domain, especially when the domain is newly observed, low reputation, or contacted at regular intervals.

### Query Idea

```text
Search network logs
WHERE destination_domain is rare in the environment
AND source_host is a workstation
AND connection_count >= threshold within 1 hour
GROUP BY source_host, destination_domain, destination_port, protocol
```

### Useful Fields

- timestamp
- source_ip
- source_host
- destination_ip
- destination_domain
- destination_port
- protocol
- bytes_out
- bytes_in
- connection_count
- user
- process_name, if available

## MITRE ATT&CK Mapping

| Tactic | Technique | Reason |
| --- | --- | --- |
| Command and Control | Application Layer Protocol `T1071` | Repeated HTTPS connections may indicate C2-like behavior |
| Command and Control | Web Service `T1102` | External web destinations can be abused for communication |
| Exfiltration | Exfiltration Over Web Service `T1567` | Large outbound transfers would increase concern |

## Triage Questions

1. Is the destination domain known and business-related?
2. Is the domain newly registered or rarely seen?
3. Which process on the endpoint made the connection?
4. Are connections periodic or user-driven?
5. How much data was sent outbound?
6. Are other hosts contacting the same destination?
7. Did endpoint alerts occur before or after the network activity?

## Findings

| Finding | Assessment |
| --- | --- |
| Workstation contacted rare destination repeatedly | Suspicious enough to investigate |
| Traffic used HTTPS | Content may be encrypted, metadata still useful |
| Endpoint process is unknown initially | Requires host-level validation |
| Data volume must be reviewed | Determines possible exfiltration concern |

## Recommendation

1. Identify the process responsible for the connection.
2. Check DNS, proxy, firewall, and endpoint logs for the same destination.
3. Review domain reputation and business justification.
4. Search for other internal hosts contacting the destination.
5. Isolate the endpoint if malware or unauthorized tooling is suspected.
6. Block the destination if confirmed malicious.
7. Preserve logs and endpoint artifacts before cleanup.

## Lessons Learned

Network alerts need endpoint context. A rare destination alone may not prove compromise, but repeated timing, suspicious process ownership, unusual data transfer, and related endpoint activity can turn a network anomaly into a credible incident.