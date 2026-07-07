# Network Traffic Analysis Lab

## Executive Summary

This project demonstrates how I would review suspicious network activity using packet and flow-analysis concepts. It is designed for entry-level SOC and cybersecurity analyst roles where understanding DNS, HTTP, TLS, IP addresses, ports, and unusual connections is important.

## Scenario

An endpoint generates repeated outbound connections to an unfamiliar external IP address. The analyst must review the traffic pattern, identify protocol behavior, determine whether the activity is expected, and recommend next steps.

## Objectives

- Identify source and destination systems.
- Review protocol, port, frequency, and timing.
- Determine whether the destination is expected or suspicious.
- Document findings in analyst-friendly language.
- Recommend containment or monitoring actions.

## Evidence Checklist

| Evidence | Why It Matters |
| --- | --- |
| Source IP and hostname | Identifies affected asset |
| Destination IP/domain | Identifies external system contacted |
| Destination port | Helps infer service or protocol |
| DNS query | Shows domain lookup behavior |
| Frequency and volume | Helps identify beaconing or automated activity |
| User/process context | Connects traffic to expected or suspicious behavior |
| Threat intelligence result | Adds external reputation context |

## Example Traffic Summary

| Field | Example |
| --- | --- |
| Source Host | `workstation-01` |
| Source IP | `10.0.0.50` |
| Destination IP | `203.0.113.25` |
| Destination Port | `443` |
| Protocol | HTTPS/TLS |
| Pattern | Repeated outbound connections every 5 minutes |
| Initial Assessment | Requires review for possible beaconing or background application traffic |

## Analysis Workflow

1. Confirm whether the source host is a managed corporate asset.
2. Identify the destination IP/domain and check whether it is business-approved.
3. Review DNS logs for related domain names.
4. Check connection frequency for periodic beaconing.
5. Review endpoint process data if available.
6. Search threat intelligence sources for reputation context.
7. Determine whether to close, monitor, block, or escalate.

## Findings and Recommendations

| Finding | Risk | Recommendation |
| --- | --- | --- |
| Repeated outbound connections | Medium | Validate process and destination reputation |
| Unknown destination | Medium | Check DNS, proxy, firewall, and threat intel context |
| No user/business justification | High | Isolate host or block destination if malicious indicators appear |

## Example Analyst Summary

The endpoint `workstation-01` generated repeated outbound HTTPS connections to an unfamiliar destination. The traffic pattern should be reviewed against DNS, proxy, firewall, and endpoint process logs. If the destination is not business-approved and no legitimate process explains the activity, the event should be escalated for endpoint investigation and possible containment.

## Skills Demonstrated

- Network traffic analysis
- DNS and HTTP/TLS investigation concepts
- SOC triage workflow
- Threat intelligence enrichment
- Risk-based escalation

## Future Improvements

- Add Wireshark screenshots from a sanitized packet capture.
- Add Zeek-style connection log examples.
- Add Suricata alert examples.
- Add a network IOC investigation report.

## References

- Wireshark documentation: https://www.wireshark.org/docs/
- Zeek documentation: https://docs.zeek.org/
- MITRE ATT&CK Application Layer Protocol: https://attack.mitre.org/techniques/T1071/
