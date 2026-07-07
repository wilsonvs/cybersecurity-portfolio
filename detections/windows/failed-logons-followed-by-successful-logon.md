# Detection: Failed Logons Followed by Successful Logon

## Summary

Detect repeated failed Windows authentication attempts followed by a successful logon for the same user and source IP. This pattern may indicate password guessing, password spraying, stale credentials, or unauthorized access using valid credentials.

## Data Sources

- Windows Security Event Log
- Event ID `4625`: failed logon
- Event ID `4624`: successful logon

## Detection Logic

```text
Count failed logons by user and source_ip.
If failures >= 5 within 15 minutes
and a successful logon occurs for the same user and source_ip
then create a medium-severity alert.
```

## MITRE ATT&CK Mapping

| Tactic | Technique |
| --- | --- |
| Credential Access | Brute Force |
| Defense Evasion / Persistence | Valid Accounts |

## Triage Steps

1. Confirm the account, source IP, destination host, and timestamp.
2. Review whether the source IP is expected for the user.
3. Check for privileged activity after successful login.
4. Search for similar failures against other users.
5. Validate activity with the user or system owner.

## False Positives

- User typing the wrong password repeatedly.
- Expired or stale credentials saved by an application.
- Expected service account retries.
- VPN or remote access reconnect behavior.

## Recommended Response

- Validate the successful login.
- Reset password if activity is unauthorized.
- Review MFA and conditional access controls.
- Block suspicious source IP if appropriate.
- Escalate if privileged activity followed the login.
