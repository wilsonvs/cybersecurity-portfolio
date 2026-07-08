# Cybersecurity Portfolio

**Hands-on cybersecurity portfolio by Wilson Vijay Sequeira**

I am an aspiring Cybersecurity Analyst with 10+ years of IT experience across system administration, network management, technical support, and IT operations. This portfolio shows how I am applying that background to security operations: SOC triage, SIEM detection, Windows log analysis, phishing investigation, network traffic review, threat intelligence, vulnerability management, Python automation, cloud IAM, and GRC documentation.

## Why This Portfolio Exists

Security operations is built on fundamentals I have already worked with in IT: system hardening, access control, log monitoring, troubleshooting, documentation, escalation, and incident handling. These projects convert that experience into cybersecurity evidence with sample logs, screenshots, scripts, detection logic, risk registers, and investigation notes.

## Recruiter Quick Scan

| Signal | Evidence |
| --- | --- |
| 10+ years IT foundation | IT Administrator, System Administrator, IT Support Specialist experience |
| Security operations focus | SOC triage, SIEM detection, incident response, threat intelligence labs |
| Real infrastructure background | Windows/Linux administration, network management, access control, troubleshooting |
| Security credentials | ISC2 CC, Google Cybersecurity, SOC Bootcamp, Security+ in progress |
| Hands-on proof | Sample logs, screenshots, Python script, SPL/KQL, IOC tables, risk register |
| Current threat awareness | Research and writing on Oracle EBS zero-day, Cl0p, ShinyHunters, ransomware, cloud security |

## Open These First

| Priority | Project | Why |
| --- | --- | --- |
| 1 | [Windows Failed Logon Detection](./detections/windows/failed-logons-followed-by-successful-logon.md) | Shows detection logic, SPL/KQL, MITRE mapping, false-positive review, and response notes |
| 2 | [SOC Credential Attack Case Study](./labs/soc-home-lab/case-studies/credential-attack-incident-report.md) | Shows alert triage, evidence timeline, findings, and recommendations |
| 3 | [Python Log Triage Tool](./tools/python-log-triage/README.md) | Shows simple automation using Python and sample authentication logs |
| 4 | [Phishing Email Analysis](./labs/phishing-email-analysis/README.md) | Shows email triage, header review, URL defanging, and containment thinking |
| 5 | [Security Policy and Risk Register](./governance-risk-compliance/security-policy-and-risk-register/README.md) | Shows GRC artifacts: policy draft, risk register, and control mapping |

## Role Evidence Map

| Target Role Need | Evidence In This Repository |
| --- | --- |
| SOC alert triage | SOC Home Lab, Credential Attack Case Study |
| Windows log analysis | Windows Event Log Analysis, Failed Logon Detection |
| SIEM detection | SPL, KQL, Sigma-style failed-logon detection |
| Incident response | Incident report template, timeline, escalation notes |
| Threat intelligence | IOC Analysis Report and indicators CSV |
| Phishing analysis | Sample phishing email, triage report, screenshot summary |
| Network security | Zeek-style connection log and traffic analysis notes |
| Vulnerability management | Findings CSV, remediation plan, risk rating method |
| Cloud IAM | Cloud IAM Risk Review, MFA and least privilege review |
| GRC | Security policy draft, risk register, NIST CSF-style control mapping |
| Automation | Python Log Triage Tool and sample output |

See [Hiring Readiness Benchmark](./docs/hiring-readiness-benchmark.md) for the full evidence map and remaining improvement plan.

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

## Career Snapshot

| Role | Organization | Period | Security-Relevant Work |
| --- | --- | --- | --- |
| IT Administrator | RainCity Property Maintenance | Dec 2022 - Present | IT operations, support, systems, users, troubleshooting |
| System Administrator | Worldwide Cloud Solutions | Oct 2017 - Nov 2022 | Windows/Linux administration, hardening, access control, logs, incident processes |
| IT Support Specialist | United Planets Enterprises | May 2013 - Sep 2017 | Technical support, systems, users, endpoint and network troubleshooting |
| Jr Assistant / Application Support | Earlier roles | 2010 - 2012 | Business systems, support, operations exposure |

## Core Skills

| Area | Practice |
| --- | --- |
| Security Operations | SOC monitoring, alert triage, escalation notes, incident response thinking |
| SIEM and Detection | SPL, KQL, Sigma-style logic, false-positive analysis, MITRE ATT&CK |
| Windows Security | Event IDs 4624/4625, authentication timelines, privileged activity checks |
| Phishing Analysis | Sender review, header review, URL defanging, containment actions |
| Network Security | DNS, HTTP/TLS, Zeek-style traffic patterns, suspicious outbound review |
| Vulnerability Management | Risk rating, remediation planning, ownership, status tracking |
| Security Automation | Python, CSV parsing, repeatable investigation output |
| Cloud Security | AWS, Google Cloud, Azure security fundamentals, IAM review |
| GRC | Security policies, risk registers, NIST CSF-style control mapping |

## Credentials

- ISC2 Certified in Cybersecurity (CC), 2025
- SOC Bootcamp, Thinkcloudly, 2026
- Google Foundations of Cybersecurity, 2024
- Google IT Support
- Cloud Computing, NPTEL - IIT Kharagpur, 2019
- CompTIA Security+ SY0-701, in progress

## Supporting Repositories

- [Google Cybersecurity Professional Certificate](https://github.com/wilsonvs/Google-Cybersecurity)
- [CompTIA Security+ SY0-701](https://github.com/wilsonvs/CompTIA-Security-SY0-701)

## Notes on Evidence

The sample logs and screenshots in this repository are lab artifacts. I use sanitized, fictional usernames, hosts, IP addresses reserved for documentation, and controlled examples so I can practice investigation and documentation without exposing private data.

## Contact

- Email: [wilsonvijaysequeira@gmail.com](mailto:wilsonvijaysequeira@gmail.com)
- LinkedIn: [wilsonvsequeira](https://www.linkedin.com/in/wilsonvsequeira)
- GitHub: [wilsonvs](https://github.com/wilsonvs)
