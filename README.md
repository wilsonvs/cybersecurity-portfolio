# Cybersecurity Portfolio

A practical cybersecurity portfolio for entry-level SOC Analyst, Cybersecurity Analyst, Security Operations Analyst, Vulnerability Management Analyst, and GRC Analyst roles.

This repository shows hands-on blue-team work across SOC workflows, SIEM detection, Windows Event Log analysis, phishing triage, network traffic analysis, IOC review, cloud IAM risk, vulnerability assessment, Python security automation, incident response documentation, and governance, risk, and compliance artifacts.

## Recruiter Snapshot

| Hiring Need | Evidence in This Portfolio |
| --- | --- |
| Can triage alerts | SOC case study, Windows failed-logon investigation, SIEM detection workflow |
| Can work with logs | Windows Event IDs, authentication timelines, SPL/KQL examples, Python log triage |
| Can document incidents | Incident report case study and reusable incident response template |
| Can communicate risk | Vulnerability report, cloud IAM risk review, GRC risk register |
| Can reason like an analyst | False-positive analysis, severity guidance, recommendations, MITRE mapping |
| Can keep learning | Google Cybersecurity Certificate, Security+ SY0-701 study repository, structured roadmap |

## Featured Cybersecurity Projects

| Project | Focus | Hiring Signal |
| --- | --- | --- |
| [SOC Home Lab](./labs/soc-home-lab/README.md) | Alert triage, escalation notes, incident workflow | Shows practical SOC analyst workflow |
| [Credential Attack Incident Report](./labs/soc-home-lab/case-studies/credential-attack-incident-report.md) | End-to-end alert investigation and recommendations | Shows incident documentation and analyst judgment |
| [Windows Event Log Analysis](./labs/windows-event-log-analysis/README.md) | Event ID review, suspicious login analysis, triage notes | Demonstrates endpoint investigation fundamentals |
| [SIEM Detection Lab](./labs/siem-detection-lab/README.md) | Detection logic, SIEM queries, MITRE ATT&CK mapping | Shows detection engineering foundations |
| [Windows Failed Logon Detection](./detections/windows/failed-logons-followed-by-successful-logon.md) | SPL, KQL, Sigma-style logic, false positives, severity guidance | Shows practical detection documentation |
| [Phishing Email Analysis](./labs/phishing-email-analysis/README.md) | Email triage, social engineering indicators, containment | Shows common SOC investigation skill |
| [Network Traffic Analysis](./labs/network-traffic-analysis/README.md) | DNS, HTTP/TLS, beaconing-style review, traffic triage | Shows network investigation fundamentals |
| [IOC Analysis Report](./threat-intelligence/ioc-analysis-report/README.md) | Indicator enrichment and internal log search planning | Shows threat intelligence workflow |
| [Cloud IAM Risk Review](./cloud-security/iam-risk-review/README.md) | MFA, least privilege, inactive accounts, access reviews | Shows cloud security and GRC awareness |
| [Vulnerability Assessment Report](./reports/vulnerability-assessment-report/README.md) | Risk rating, findings, remediation plan | Shows business-focused risk communication |
| [Python Log Triage Tool](./tools/python-log-triage/README.md) | Log parsing, failed login review, analyst helper script | Shows practical Python security automation |
| [Security Policy and Risk Register](./governance-risk-compliance/security-policy-and-risk-register/README.md) | Policies, risk register, NIST/ISO-aligned language | Supports GRC and security analyst roles |
| [Incident Report Template](./templates/incident-response/incident-report-template.md) | Structured incident reporting format | Shows readiness to document and hand off investigations |

## Repository Structure

```text
.
├── .github/                         # Issue templates, PR template, GitHub Actions
├── cloud-security/                  # Cloud IAM and access review projects
├── detections/                      # Detection engineering writeups
│   └── windows/
├── docs/                            # Research alignment, roadmap, and reusable templates
├── governance-risk-compliance/      # GRC artifacts, policies, risk register examples
├── labs/                            # SOC, SIEM, phishing, network, and Windows analysis labs
├── reports/                         # Security assessment reports
├── templates/                       # Incident response and analyst documentation templates
├── threat-intelligence/             # IOC analysis and enrichment projects
├── tools/                           # Security automation scripts and sample data
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## Skills Demonstrated

| Area | Tools and Concepts |
| --- | --- |
| SOC Analysis | Alert triage, escalation notes, incident response workflow |
| SIEM and Detection | SPL, KQL, Sigma-style logic, false-positive analysis, MITRE ATT&CK |
| Windows Security | Event IDs 4624/4625, authentication review, privileged activity checks |
| Phishing Analysis | Sender review, link inspection, user impact assessment, containment |
| Network Security | DNS, HTTP/TLS, traffic patterns, threat intelligence enrichment |
| Vulnerability Management | Risk rating, remediation planning, executive summaries |
| Security Automation | Python, CSV log parsing, repeatable investigation tasks |
| Cloud Security | IAM review, MFA, least privilege, inactive account risk |
| GRC | Security policies, risk registers, NIST CSF, ISO 27001 awareness |

## Research Alignment

The project set is based on recurring entry-level cybersecurity requirements: SOC monitoring, SIEM/log analysis, incident response, vulnerability management, threat detection, Python automation, and risk communication.

See [Recruiter Alignment Research](./docs/research/recruiter-alignment.md) for the sources and rationale.

## Search Keywords

`cybersecurity portfolio` `SOC analyst` `SIEM` `incident response` `threat detection` `Windows Event Log analysis` `phishing analysis` `network traffic analysis` `vulnerability management` `Python security automation` `cloud IAM` `GRC` `MITRE ATT&CK` `NIST CSF` `Security+`

## Supporting Repositories

- [Google Cybersecurity Professional Certificate](https://github.com/wilsonvs/Google-Cybersecurity)
- [CompTIA Security+ SY0-701](https://github.com/wilsonvs/CompTIA-Security-SY0-701)

## Documentation Standards

Each project is organized to include:

- Executive summary
- Problem statement or scenario
- Objectives
- Tools and technologies
- Step-by-step workflow
- Evidence, sample output, or screenshots where available
- Findings and recommendations
- Lessons learned
- References

## Portfolio Roadmap

See [Portfolio Audit and Roadmap](./docs/portfolio-audit-and-roadmap.md) for improvement priorities and hiring-focused positioning.

## Contact

- GitHub: [wilsonvs](https://github.com/wilsonvs)
