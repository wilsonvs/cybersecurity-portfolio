# Cybersecurity Portfolio

**Hands-on cybersecurity labs by Wilson Vijay Sequeira**

This repository documents practical cybersecurity work across SOC triage, SIEM detection, Windows log analysis, phishing investigation, network traffic review, threat intelligence, vulnerability management, Python automation, cloud IAM, and GRC documentation.

My background is built on 10+ years of IT operations, including system administration, network support, access control, Windows/Linux administration, security policy implementation, troubleshooting, and log review. The work here turns that experience into security evidence: sample logs, detection logic, screenshots, scripts, incident notes, risk registers, and response recommendations.

## Flagship SOC Work

| Priority | Case Study | What It Demonstrates |
| --- | --- | --- |
| 1 | [Failed Logons Followed by Successful Authentication](./labs/soc-home-lab/case-studies/credential-attack-incident-report.md) | Windows authentication timeline, Event ID 4624/4625 review, MITRE mapping, escalation logic |
| 2 | [Suspicious PowerShell Activity](./labs/soc-home-lab/case-studies/suspicious-powershell-activity-incident-report.md) | Endpoint process analysis, PowerShell command-line review, Sigma-style detection, KQL idea |
| 3 | [Phishing Credential Harvesting Link](./labs/soc-home-lab/case-studies/phishing-credential-harvest-incident-report.md) | Email triage, URL defanging, user-impact review, mailbox search and containment steps |
| 4 | [Unusual Outbound Network Activity](./labs/soc-home-lab/case-studies/unusual-outbound-network-activity-incident-report.md) | Zeek-style traffic review, rare destination analysis, beaconing questions, response planning |

## Evidence Preview

| Evidence Type | Example |
| --- | --- |
| Windows timeline | [Event log timeline image](./assets/screenshots/windows-event-log-timeline.svg) |
| Phishing triage | [Phishing triage image](./assets/screenshots/phishing-email-triage.svg) |
| Network traffic summary | [Network traffic image](./assets/screenshots/network-traffic-summary.svg) |
| Python output | [Python log triage output image](./assets/screenshots/python-log-triage-output.svg) |
| Sample logs | [Windows events CSV](./labs/windows-event-log-analysis/sample-windows-security-events.csv), [Zeek-style conn log](./labs/network-traffic-analysis/sample-zeek-conn.log) |
| Automation | [Python log triage script](./tools/python-log-triage/log_triage.py) |

## Skills-to-Evidence Map

| Cybersecurity Skill | Portfolio Evidence |
| --- | --- |
| SOC alert triage | [SOC Home Lab](./labs/soc-home-lab/README.md), credential attack, PowerShell, phishing, and network case studies |
| Windows log analysis | [Windows Event Log Analysis](./labs/windows-event-log-analysis/README.md), Event ID 4624/4625 timeline |
| SIEM detection | [Failed Logon Detection](./detections/windows/failed-logons-followed-by-successful-logon.md), SPL, KQL, Sigma-style logic |
| Incident response | Case-study timelines, findings, escalation notes, and response recommendations |
| Threat intelligence | [IOC Analysis Report](./threat-intelligence/ioc-analysis-report/README.md), indicator organization and log search planning |
| Phishing analysis | [Phishing Email Analysis](./labs/phishing-email-analysis/README.md), sample email, triage report, containment steps |
| Network security | [Network Traffic Analysis](./labs/network-traffic-analysis/README.md), Zeek-style connection logs and outbound traffic review |
| Vulnerability management | [Vulnerability Assessment Report](./reports/vulnerability-assessment-report/README.md), findings CSV and remediation plan |
| Cloud IAM | [Cloud IAM Risk Review](./cloud-security/iam-risk-review/README.md), MFA and least-privilege review |
| GRC | [Security Policy and Risk Register](./governance-risk-compliance/security-policy-and-risk-register/README.md), Security policy, risk register, control mapping |
| Automation | [Python Log Triage Tool](./tools/python-log-triage/README.md), CSV parsing and repeatable investigation output |

## Project Library

| Project | What I Practiced | Evidence |
| --- | --- | --- |
| [SOC Home Lab](./labs/soc-home-lab/README.md) | Alert triage, escalation notes, investigation workflow | Four SOC case studies with timelines and recommendations |
| [Windows Event Log Analysis](./labs/windows-event-log-analysis/README.md) | Event IDs 4624/4625, suspicious login review | [Sample events](./labs/windows-event-log-analysis/sample-windows-security-events.csv), [timeline image](./assets/screenshots/windows-event-log-timeline.svg) |
| [SIEM Detection Lab](./labs/siem-detection-lab/README.md) | Detection logic, SPL/KQL thinking, MITRE ATT&CK mapping | Detection workflow and triage questions |
| [Windows Failed Logon Detection](./detections/windows/failed-logons-followed-by-successful-logon.md) | Detection writing and false-positive review | SPL, KQL, Sigma-style logic |
| [Phishing Email Analysis](./labs/phishing-email-analysis/README.md) | Sender review, URL defanging, user impact assessment | [Sample email](./labs/phishing-email-analysis/sample-email.eml), [triage image](./assets/screenshots/phishing-email-triage.svg) |
| [Network Traffic Analysis](./labs/network-traffic-analysis/README.md) | DNS, HTTPS, repeated outbound connection review | [Zeek-style log](./labs/network-traffic-analysis/sample-zeek-conn.log), [traffic image](./assets/screenshots/network-traffic-summary.svg) |
| [IOC Analysis Report](./threat-intelligence/ioc-analysis-report/README.md) | Indicator organization, enrichment, and log search planning | [IOC table](./threat-intelligence/ioc-analysis-report/indicators.csv), internal search plan |
| [Cloud IAM Risk Review](./cloud-security/iam-risk-review/README.md) | MFA, least privilege, inactive account review | IAM risk review writeup |
| [Vulnerability Assessment Report](./reports/vulnerability-assessment-report/README.md) | Risk rating, remediation planning, business impact | [Findings CSV](./reports/vulnerability-assessment-report/vulnerability-findings.csv), remediation plan |
| [Python Log Triage Tool](./tools/python-log-triage/README.md) | CSV parsing and repeatable authentication review | [Script](./tools/python-log-triage/log_triage.py), [sample output](./tools/python-log-triage/output/sample-output.txt), [output image](./assets/screenshots/python-log-triage-output.svg) |
| [Security Policy and Risk Register](./governance-risk-compliance/security-policy-and-risk-register/README.md) | Policy writing, risk tracking, control mapping | [Security policy](./governance-risk-compliance/security-policy-and-risk-register/security-policy.md), [risk register](./governance-risk-compliance/security-policy-and-risk-register/risk-register.csv) |

## Technical Coverage

| Area | Practice |
| --- | --- |
| Security Operations | SOC monitoring, alert triage, escalation notes, incident response thinking |
| SIEM and Detection | SPL, KQL, Sigma-style logic, false-positive analysis, MITRE ATT&CK |
| Windows Security | Event IDs 4624/4625, authentication timelines, process and privileged activity checks |
| Phishing Analysis | Sender review, header review, URL defanging, containment actions |
| Network Security | DNS, HTTP/TLS, Zeek-style traffic patterns, suspicious outbound review |
| Vulnerability Management | Risk rating, remediation planning, ownership, status tracking |
| Security Automation | Python, CSV parsing, repeatable investigation output |
| Cloud Security | AWS, Google Cloud, Azure security fundamentals, IAM review |
| GRC | Security policies, risk registers, NIST CSF-style control mapping |

## Notes on Evidence

The sample logs and screenshots in this repository are lab artifacts. I use sanitized, fictional usernames, hosts, IP addresses reserved for documentation, and controlled examples so I can practice investigation and documentation without exposing private data.

## Supporting Repositories

- [Cybersecurity Research](https://github.com/wilsonvs/Cybersecurity-Research)
- [Cybersecurity Study Guides](https://github.com/wilsonvs/Cybersecurity-Study-Guides)
- [CompTIA Security+ SY0-701](https://github.com/wilsonvs/CompTIA-Security-SY0-701)
- [Google Cybersecurity Professional Certificate](https://github.com/wilsonvs/Google-Cybersecurity)

## Contact

- Email: [wilsonvijaysequeira@gmail.com](mailto:wilsonvijaysequeira@gmail.com)
- LinkedIn: [wilsonvsequeira](https://www.linkedin.com/in/wilsonvsequeira)
- GitHub: [wilsonvs](https://github.com/wilsonvs)