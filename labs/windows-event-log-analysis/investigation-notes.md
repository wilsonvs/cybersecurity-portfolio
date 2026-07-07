# Windows Event Log Investigation Notes

## Evidence Reviewed

- Sample Windows Security events in `sample-windows-security-events.csv`
- Event ID `4625` failed logons
- Event ID `4624` successful logon
- Source IP, destination host, user, timestamp, and logon type

## Timeline

| Time | Event ID | User | Source | Host | Result |
| --- | --- | --- | --- | --- | --- |
| 09:00 | 4625 | alice | 10.0.0.50 | workstation-01 | Failed logon |
| 09:01 | 4625 | alice | 10.0.0.50 | workstation-01 | Failed logon |
| 09:02 | 4625 | alice | 10.0.0.50 | workstation-01 | Failed logon |
| 09:03 | 4624 | alice | 10.0.0.50 | workstation-01 | Successful logon |
| 10:10-10:12 | 4625 | service_backup | 10.0.0.20 | server-02 | Repeated failed logons |

## My Assessment

The `alice` activity is more important than isolated failed logons because the account eventually authenticated successfully from the same source. I would validate whether `10.0.0.50` belongs to Alice's normal workstation or a known VPN/session source.

The `service_backup` activity could be a stale saved password, a misconfigured service, or password guessing. I would check recent password changes and service ownership before escalating.

## Next Checks

1. Confirm source host ownership.
2. Check whether MFA or conditional access was used.
3. Search for privileged events after successful authentication.
4. Search for other users targeted by the same source IP.
5. Document whether this is expected, suspicious, or requires containment.
