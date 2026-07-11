# Security Policy

## Purpose

This sample security policy defines basic safeguards for a small organization. It is written as a lab artifact to show how security expectations can be documented, reviewed, and connected to evidence.

## Scope

This policy applies to company users, workstations, servers, cloud accounts, business applications, and security-relevant logs used in the lab scenario.

## Policy Statements

### 1. Multi-Factor Authentication

Multi-factor authentication must be enabled for email, cloud services, remote access, administrative accounts, and other high-risk systems.

Evidence examples:

- MFA configuration export
- Identity provider policy screenshot
- User enrollment report
- Exception list with owner and review date

### 2. Patch Management

Operating systems, applications, and security tools must be patched based on risk. Critical vulnerabilities and known exploited vulnerabilities should be prioritized.

Evidence examples:

- Patch compliance report
- Vulnerability scan results
- Change ticket
- Retest result after remediation

### 3. Logging and Monitoring

Security-relevant logs must be collected and retained for investigation. Important sources include authentication logs, endpoint alerts, firewall logs, DNS logs, VPN logs, and cloud audit logs.

Evidence examples:

- SIEM data source list
- Log retention settings
- Alert rule documentation
- Incident timeline using collected logs

### 4. Access Review

User access must be reviewed regularly. Privileged accounts, inactive accounts, shared accounts, and orphaned accounts require special attention.

Evidence examples:

- Quarterly access review record
- User and group export
- Privileged account list
- Removed access confirmation

### 5. Incident Reporting

Users must report suspected phishing, malware, account misuse, lost devices, and unusual system behavior as soon as possible.

Evidence examples:

- Reported phishing ticket
- Incident triage note
- User communication record
- Containment and remediation summary

## Exceptions

Exceptions must include:

- Business reason
- Risk owner
- Compensating controls
- Expiration or review date
- Approval record

## Review Cycle

This policy should be reviewed at least annually or after a major security incident, technology change, audit finding, or risk register update.

## Lab Notes

This is a sample policy for portfolio and learning purposes. It is intentionally concise so each statement can be mapped to evidence, risk, and controls.