# Cybersecurity Portfolio

This repository is my hands-on cybersecurity learning portfolio. I use it to document what I practiced, what evidence I collected, what I observed, and how I would explain investigation steps clearly.

My background includes 8+ years of IT experience, current IT Manager work, (ISC)² Certified in Cybersecurity (CC), and ongoing Security+ SY0-701 preparation. The projects here connect that IT foundation with practical blue-team work: SOC triage, SIEM detection logic, Windows Event Log analysis, phishing analysis, network traffic review, IOC handling, vulnerability assessment, Python automation, cloud IAM review, and GRC documentation.

## Featured Projects

| Project | What I Practiced | Evidence |
| --- | --- | --- |
| [SOC Home Lab](./labs/soc-home-lab/README.md) | Alert triage, escalation notes, investigation workflow | Workflow, timeline, case study |
| [Credential Attack Case Study](./labs/soc-home-lab/case-studies/credential-attack-incident-report.md) | Failed logons followed by successful authentication | Incident report and evidence timeline |
| [Windows Event Log Analysis](./labs/windows-event-log-analysis/README.md) | Event IDs 4624/4625, suspicious login review | [Sample events](./labs/windows-event-log-analysis/sample-windows-security-events.csv), [timeline image](./assets/screenshots/windows-event-log-timeline.svg) |
| [SIEM Detection Lab](./labs/siem-detection-lab/README.md) | Detection logic, SPL/KQL thinking, MITRE ATT&CK mapping | Detection workflow and triage questions |
| [Windows Failed Logon Detection](./detections/windows/failed-logons-followed-by-successful-logon.md) | Detection writing and false-positive review | SPL, KQL, Sigma-style logic |
| [Phishing Email Analysis](./labs/phishing-email-analysis/README.md) | Sender review, URL defanging, user impact assessment | [Sample email](./labs/phishing-email-analysis/sample-email.eml), [triage image](./assets/screenshots/phishing-email-triage.svg) |
| [Network Traffic Analysis](./labs/network-traffic-analysis/README.md) | DNS, HTTPS, repeated outbound connection review | [Zeek-style log](./labs/network-traffic-analysis/sample-zeek-conn.log), [traffic image](./assets/screenshots/network-traffic-summary.svg) |
| [IOC Analysis Report](./threat-intelligence/ioc-analysis-report/README.md) | Indicator organization, enrichment, and log search planning | [IOC table](./threat-intelligence/ioc-analysis-report/indicators.csv), internal search plan |
| [Cloud IAM Risk Review](./cloud-security/iam-risk-review/README.md) | MFA, least privilege, inactive account review | IAM risk review writeup |
| [Vulnerability Assessment Report](./reports/vulnerability-assessment-report/README.md) | Risk rating, remediation planning, business impact | [Findings CSV](./reports/vulnerability-assessment-report/vulnerability-findings.csv), remediation plan |
| [Python Log Triage Tool](./tools/python-log-triage/README.md) | CSV parsing and repeatable authentication review | [Script](./tools/python-log-triage/log_triage.py), [sample output](./tools/python-log-triage/output/sample-output.txt), [output image](./assets/screenshots/python-log-triage-output.svg) |
| [Security Policy and Risk Register](./governance-risk-compliance/security-policy-and-risk-register/README.md) | Policy writing, risk tracking, control mapping | [Policy draft](./governance-risk-compliance/security-policy-and-risk-register/security-policy-draft.md), [risk register](./governance-risk-compliance/security-policy-and-risk-register/risk-register.csv) |

## How I Document Each Project

For each lab, I try to show:

1. What I was investigating.
2. What data or sample evidence I used.
3. What steps I followed.
4. What I found.
5. What I would recommend next.
6. What I learned from the exercise.

## Repository Structure

```text
.
|-- .github/                         # Issue templates, PR template, GitHub Actions
|-- assets/screenshots/              # Lab screenshots and evidence images
|-- cloud-security/                  # Cloud IAM and access review projects
|-- detections/windows/              # Detection engineering writeups
|-- docs/                            # Learning roadmap and reusable notes
|-- governance-risk-compliance/      # Policies, risk register, GRC practice
|-- labs/                            # SOC, SIEM, phishing, network, and Windows labs
|-- reports/                         # Security assessment reports
|-- templates/                       # Incident response templates
|-- threat-intelligence/             # IOC analysis and enrichment practice
|-- tools/                           # Security automation scripts and sample data
`-- README.md
```

## Skills Practiced

| Area | Practice |
| --- | --- |
| SOC Analysis | Alert triage, evidence review, escalation notes |
| SIEM and Detection | SPL, KQL, Sigma-style logic, tuning notes, MITRE ATT&CK |
| Windows Security | Event IDs 4624/4625, authentication timelines, privileged activity checks |
| Phishing Analysis | Sender review, header review, URL defanging, containment actions |
| Network Security | DNS, HTTP/TLS, traffic patterns, beaconing-style review |
| Vulnerability Management | Risk rating, remediation planning, clear summaries |
| Security Automation | Python, CSV parsing, repeatable investigation output |
| Cloud Security | IAM review, MFA, least privilege, inactive account risk |
| GRC | Security policies, risk registers, NIST/ISO-aligned thinking |

## Supporting Repositories

- [Google Cybersecurity Professional Certificate](https://github.com/wilsonvs/Google-Cybersecurity)
- [CompTIA Security+ SY0-701](https://github.com/wilsonvs/CompTIA-Security-SY0-701)

## Notes on Evidence

The sample logs and screenshots in this repository are lab artifacts. I use sanitized, fictional usernames, hosts, IP addresses reserved for documentation, and controlled examples so I can practice investigation and documentation without exposing real private data.

## Links

- GitHub: [wilsonvs](https://github.com/wilsonvs)
- LinkedIn: [wilsonvsequeira](https://www.linkedin.com/in/wilsonvsequeira)
