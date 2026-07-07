# Learning Roadmap and Source Notes

## Purpose

This note explains why I organized my cybersecurity practice around SOC triage, SIEM/log analysis, incident response, vulnerability management, Python automation, cloud IAM, threat intelligence, and GRC.

I use this as a learning map. Each topic gives me a practical way to show what I understand and what I still need to improve.

## Why These Areas Matter

| Learning Area | Why I Practice It | Evidence in This Repository |
| --- | --- | --- |
| Security monitoring | Alerts are only useful when I can investigate and explain them | SOC Home Lab, credential attack case study |
| Log analysis | Logs are the main evidence source for many investigations | Windows Event Log Analysis, Python Log Triage Tool |
| Detection logic | A detection should be understandable, testable, and tunable | SIEM Detection Lab, failed-logon detection |
| Incident response | Good response depends on clear steps and documentation | Incident report template and case study |
| Vulnerability management | Security weaknesses need risk-based prioritization | Vulnerability Assessment Report |
| Phishing analysis | Email threats need structured triage | Phishing Email Analysis Lab |
| Network analysis | DNS, ports, protocols, and connection patterns reveal useful clues | Network Traffic Analysis Lab |
| Threat intelligence | Indicators need context before action | IOC Analysis Report |
| Cloud IAM and GRC | Access control and policy decisions affect real risk | IAM Risk Review, risk register |

## References I Used While Planning Practice Topics

- CISA/NICCS NICE Framework: https://niccs.cisa.gov/tools/nice-framework
- NIST SP 800-61 incident response guidance: https://csrc.nist.gov/pubs/sp/800/61/r2/final
- Microsoft Windows security auditing documentation: https://learn.microsoft.com/windows/security/threat-protection/auditing/security-auditing-overview
- Microsoft Sentinel hunting documentation: https://learn.microsoft.com/azure/sentinel/hunting
- MITRE ATT&CK: https://attack.mitre.org/

## Current Improvement List

- Add more sample logs for each lab.
- Add before-and-after remediation evidence for the vulnerability report.
- Add more SIEM query versions for Splunk, Microsoft Sentinel, Elastic, and Wazuh.
- Add more screenshots from controlled lab outputs.
- Keep rewriting project notes in first person so they explain what I actually practiced.
