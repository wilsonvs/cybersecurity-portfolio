# Phishing Email Analysis Lab

## Executive Summary

This project demonstrates how I would analyze a suspected phishing email as a junior SOC analyst. The goal is to review sender details, links, attachments, social engineering indicators, potential impact, and recommended response actions.

## Scenario

A user reports a suspicious email claiming that their account will be disabled unless they sign in immediately. The email contains a link to a lookalike login page. The analyst must determine whether the email is malicious, document evidence, and recommend containment steps.

## Objectives

- Identify phishing indicators.
- Review sender, subject, link, and attachment evidence.
- Determine likely user impact.
- Recommend containment and user-awareness actions.
- Produce a clear analyst summary.

## Triage Checklist

| Check | What I Look For | Why It Matters |
| --- | --- | --- |
| Sender address | Misspellings, strange domains, spoofing | Attackers often impersonate trusted brands |
| Reply-to address | Different from sender | May reveal attacker-controlled inbox |
| Subject and tone | Urgency, fear, account closure | Common social engineering pattern |
| Links | Mismatched display text and destination | May redirect to credential harvesting page |
| Attachments | Macros, archives, executables | Possible malware delivery |
| Headers | SPF, DKIM, DMARC results | Helps validate sender authenticity |
| User interaction | Clicked, opened, entered credentials | Determines response urgency |

## Sample Findings

| Indicator | Observation | Assessment |
| --- | --- | --- |
| Urgent account warning | Email pressures user to act immediately | Suspicious |
| Login link mismatch | Display text differs from destination domain | Suspicious |
| External sender | Sender domain is not official company domain | Suspicious |
| No expected business context | User was not expecting this message | Suspicious |

## Analyst Decision

**Verdict:** Likely phishing attempt.

**Severity:** Medium if no user interaction occurred. High if the user entered credentials or downloaded an attachment.

## Recommended Response

1. Quarantine the email if still present in mailboxes.
2. Search for other recipients with the same sender, subject, URL, or attachment hash.
3. Block malicious sender/domain/URL if confirmed.
4. Ask the user whether they clicked the link or submitted credentials.
5. Reset credentials and revoke sessions if credentials were entered.
6. Submit indicators to the security awareness or email security process.

## Example Analyst Summary

A suspicious email was reported by a user. The message used urgency and account-disabling language to pressure the recipient into clicking a login link. The displayed link did not match the destination domain, and the sender domain did not align with the claimed organization. Based on these indicators, the email is assessed as likely phishing. Recommended actions are mailbox search, URL blocking, user validation, and credential reset if interaction occurred.

## Skills Demonstrated

- Phishing triage
- Email security investigation
- User impact assessment
- Clear incident documentation
- Containment recommendation writing

## Future Improvements

- Add sanitized email header sample.
- Add URL defanging examples.
- Add mailbox search query examples.
- Add a phishing incident report using the incident response template.

## References

- CISA phishing guidance: https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks
- MITRE ATT&CK Phishing: https://attack.mitre.org/techniques/T1566/
