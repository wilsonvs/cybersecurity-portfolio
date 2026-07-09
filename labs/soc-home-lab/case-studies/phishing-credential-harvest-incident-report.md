# SOC Case Study: Phishing Email With Credential Harvesting Link

## What I Investigated

I investigated a lab phishing scenario where a user reported an account-expiration email containing a login-themed link. The goal was to practice email triage, indicator handling, user impact review, containment planning, and communication notes.

## Scenario

A user receives an email claiming their account will be disabled unless they sign in immediately. The message contains a link to an unfamiliar domain designed to look like a legitimate login page.

## Alert Summary

| Field | Value |
| --- | --- |
| Alert Name | Reported Phishing Email |
| Severity | Medium, escalates to High if credentials were submitted |
| Reporter | `alice` |
| Sender Display Name | `IT Support` |
| Sender Domain | Lookalike or unfamiliar domain |
| Link Type | Login-themed credential collection link |
| Initial Verdict | Likely phishing |

## Evidence Used

| Artifact | Purpose |
| --- | --- |
| [Sample email](../../phishing-email-analysis/sample-email.eml) | Sanitized phishing email sample |
| [Phishing triage report](../../phishing-email-analysis/phishing-triage-report.md) | Detailed indicator review and verdict |
| [Triage image](../../../assets/screenshots/phishing-email-triage.svg) | Screenshot-style summary of decision points |

## Triage Checklist

| Check | Result | Why It Matters |
| --- | --- | --- |
| Sender domain | Unfamiliar or lookalike | Suggests impersonation |
| Reply-To | Different path from sender | May indicate attacker-controlled mailbox |
| Urgency | Account closure language | Common social engineering pressure |
| Link destination | Unfamiliar login domain | Possible credential harvesting |
| SPF/DKIM/DMARC | Failing or misaligned | Weakens sender authenticity |
| User interaction | Unknown initially | Determines containment urgency |

## Indicator Handling

| Indicator Type | Example Handling |
| --- | --- |
| URL | Defang before sharing in notes |
| Domain | Search email gateway and proxy logs |
| Sender | Search for similar messages across mailboxes |
| Subject | Search for campaign spread |
| Attachment | Hash and sandbox only in controlled environment |

## Detection Logic Idea

### Plain Language

Alert on emails that combine failed authentication alignment, urgent account language, and links to newly seen or suspicious domains.

### Email Gateway Query Idea

```text
Search email logs
WHERE subject contains account expiration, password reset, mailbox full, or urgent sign-in language
AND URL domain is not in trusted login domains
AND SPF/DKIM/DMARC result is fail, softfail, or misaligned
GROUP BY sender, subject, URL domain, recipient
```

### SIEM Review Fields

- timestamp
- sender
- reply_to
- recipient
- subject
- URL domain
- SPF result
- DKIM result
- DMARC result
- delivery action
- user clicked

## MITRE ATT&CK Mapping

| Tactic | Technique | Reason |
| --- | --- | --- |
| Initial Access | Phishing `T1566` | Email used to lure user |
| Credential Access | Credentials from Web Browsers / Input Capture | Link attempts to collect credentials |
| Defense Evasion | Masquerading `T1036` | Message impersonates IT or trusted service |

## Triage Questions

1. Did the message reach one user or multiple users?
2. Did the user click the link?
3. Did the user enter credentials?
4. Was the URL accessed from corporate network or endpoint logs?
5. Did the account show unusual sign-in activity afterward?
6. Are there similar messages with different senders or subjects?
7. Were any mailbox rules created after the event?

## Findings

| Finding | Assessment |
| --- | --- |
| Urgent account-disabling language | Social engineering indicator |
| Login link points to unfamiliar domain | Strong credential-harvesting indicator |
| Sender identity does not align with expected service | Likely impersonation |
| User interaction must be confirmed | Determines whether credential reset is required |

## Recommendation

1. Quarantine the message and search for campaign spread.
2. Block the URL/domain at email gateway, proxy, or DNS layer if confirmed malicious.
3. Ask the user whether they clicked or submitted credentials.
4. Reset password, revoke sessions, and review MFA if credentials were entered.
5. Review mailbox forwarding rules, sign-in logs, and impossible travel alerts.
6. Send a short user-awareness note if campaign spread is confirmed.

## Lessons Learned

A phishing verdict is strongest when multiple indicators are documented together. Sender, authentication results, URL behavior, message tone, and user interaction all matter.