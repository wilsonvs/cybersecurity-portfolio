# Python Security Automation

## Executive Summary

This project demonstrates a small analyst helper script for reviewing authentication event data. The script summarizes failed logins, successful logins, and users that may require follow-up.

## Problem Statement

SOC analysts often review repetitive log data. Small automation scripts can reduce manual review time and make triage more consistent.

## Objectives

- Parse structured CSV event data.
- Count failed and successful login events.
- Identify users with repeated failures.
- Produce simple analyst-friendly output.

## Files

| File | Purpose |
| --- | --- |
| `log_triage.py` | Python script for CSV log triage |
| `sample_events.csv` | Sanitized sample authentication events |

## Usage

```bash
python log_triage.py sample_events.csv
```

## Expected Output

```text
Authentication Summary
Failed logons: 6
Successful logons: 2
Users requiring review: alice, service_backup
```

## Analyst Value

This script is intentionally simple. It shows the ability to convert repetitive investigation steps into repeatable tooling, which is useful for SOC analyst and security automation work.

## Future Improvements

- Add JSON input support.
- Add source IP frequency analysis.
- Add MITRE ATT&CK mapping in output.
- Export Markdown incident notes automatically.