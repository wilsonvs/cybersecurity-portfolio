# Cybersecurity Portfolio

A practical cybersecurity portfolio for entry-level SOC Analyst, Cybersecurity Analyst, Security Operations Analyst, Vulnerability Management Analyst, and GRC Analyst roles.

This repository includes hands-on blue-team projects covering SOC workflows, SIEM detection, Windows Event Log analysis, vulnerability assessment, Python security automation, incident response documentation, and governance, risk, and compliance artifacts.

## Featured Cybersecurity Projects

| Project | Focus | Hiring Signal |
| --- | --- | --- |
| [SOC Home Lab](./labs/soc-home-lab/README.md) | Alert triage, escalation notes, incident workflow | Shows practical SOC analyst workflow |
| [Windows Event Log Analysis](./labs/windows-event-log-analysis/README.md) | Event ID review, suspicious login analysis, triage notes | Demonstrates endpoint investigation fundamentals |
| [SIEM Detection Lab](./labs/siem-detection-lab/README.md) | Detection logic, SIEM queries, MITRE ATT&CK mapping | Shows detection engineering foundations |
| [Windows Failed Logon Detection](./detections/windows/failed-logons-followed-by-successful-logon.md) | Failed login pattern detection and triage | Shows detection documentation and analyst reasoning |
| [Vulnerability Assessment Report](./reports/vulnerability-assessment-report/README.md) | Risk rating, findings, remediation plan | Shows business-focused risk communication |
| [Python Log Triage Tool](./tools/python-log-triage/README.md) | Log parsing, failed login review, analyst helper script | Shows practical Python security automation |
| [Security Policy and Risk Register](./governance-risk-compliance/security-policy-and-risk-register/README.md) | Policies, risk register, NIST/ISO-aligned language | Supports GRC and security analyst roles |

## Repository Structure

```text
.
├── .github/                         # Issue templates, PR template, GitHub Actions
├── detections/                      # Detection engineering writeups
│   └── windows/
├── docs/                            # Portfolio roadmap and reusable templates
│   └── templates/
├── governance-risk-compliance/      # GRC artifacts, policies, risk register examples
├── labs/                            # SOC, SIEM, and Windows analysis labs
├── reports/                         # Security assessment reports
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
| SIEM and Detection | SIEM queries, detection logic, false-positive analysis, MITRE ATT&CK |
| Windows Security | Windows Event IDs, authentication review, privileged activity checks |
| Vulnerability Management | Risk rating, remediation planning, executive summaries |
| Security Automation | Python, CSV log parsing, repeatable investigation tasks |
| GRC | Security policies, risk registers, NIST CSF, ISO 27001 awareness |

## Search Keywords

`cybersecurity portfolio` `SOC analyst` `SIEM` `incident response` `threat detection` `Windows Event Log analysis` `vulnerability management` `Python security automation` `GRC` `MITRE ATT&CK` `NIST CSF` `Security+`

## Supporting Repositories

- [Google Cybersecurity Professional Certificate](https://github.com/wilsonvs/Google-Cybersecurity)
- [CompTIA Security+ SY0-701](https://github.com/wilsonvs/CompTIA-Security-SY0-701)

## Documentation Standards

Each project is organized to include:

- Executive summary
- Problem statement
- Objectives
- Tools and technologies
- Workflow or architecture diagram
- Evidence, sample output, or screenshots where available
- Findings and recommendations
- Lessons learned
- References

## Portfolio Roadmap

See [Portfolio Audit and Roadmap](./docs/portfolio-audit-and-roadmap.md) for improvement priorities and hiring-focused positioning.

## Contact

- GitHub: [wilsonvs](https://github.com/wilsonvs)
