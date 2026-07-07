# GitHub Portfolio Audit and Roadmap

This audit is written for entry-level cybersecurity hiring outcomes: SOC Analyst, Cybersecurity Analyst, Security Operations Analyst, Blue Team Analyst, GRC Analyst, Vulnerability Management Analyst, and Junior Security Engineer.

## Executive Summary

The current GitHub profile has useful cybersecurity learning material, but the first impression is weakened by unclear repository names, duplicate certificate repositories, a public test repository, a generic `cyber` repository, and a large public WordPress repository that does not support the cybersecurity hiring story.

The strongest path is to present a smaller, cleaner portfolio with 4-6 polished cybersecurity projects rather than many unfinished or generic repositories.

## Keep

| Repository | Decision | Why |
| --- | --- | --- |
| `Google-Cybersecurity` | Keep and improve | Directly relevant to entry-level cybersecurity roles and already has certificate credibility. |
| `CompTIA-Security-SY0-701` | Keep and improve | Relevant to Security+ preparation and recruiter keyword alignment. |
| `cyber` | Rebuild as portfolio hub | Previously too vague, but useful as a central roadmap and project index after cleanup. |

## Improve

| Repository | Improvements Needed |
| --- | --- |
| `Google-Cybersecurity` | Add project summaries, stronger business context, cleaner table of contents, screenshots/sample outputs, and practical lessons learned. |
| `CompTIA-Security-SY0-701` | Reframe from generic study repository into Security+ knowledge base with exam objective mapping and practical analyst examples. |
| `cyber` | Rename when possible to something like `cybersecurity-portfolio` or replace with a profile README repository. |

## Archive

| Repository | Reason |
| --- | --- |
| `google-cybersecurity-1` | Duplicate fork with weaker branding and copied upstream identity risk. Keep only if needed for attribution history, otherwise archive. |
| `WordPress` | Large public WordPress source tree does not support the cybersecurity hiring goal and distracts from the portfolio. |
| `Test` | Public test repository creates an unfinished/beginner impression. |

## Delete

Delete only after confirming there is nothing unique to preserve:

| Repository | Reason |
| --- | --- |
| `Test` | No hiring value. |
| `cyber` | Delete only if a renamed replacement such as `cybersecurity-portfolio` or profile repo `wilsonvs` is created. |

## Merge

| Source | Target | Notes |
| --- | --- | --- |
| `google-cybersecurity-1` | `Google-Cybersecurity` | Preserve only unique notes, scripts, or screenshots. Do not preserve copied README language. |
| `cyber` | Profile README or `cybersecurity-portfolio` | Use as a portfolio hub, not a standalone vague repo. |

## Rebuild

Recommended professional project set:

1. `soc-home-lab`
   - SIEM/log collection overview
   - Alert triage workflow
   - Incident report template
   - MITRE ATT&CK mapping

2. `windows-event-log-analysis`
   - Windows Security Event ID scenarios
   - Detection notes
   - Investigation writeups
   - Screenshots or sample logs

3. `siem-detection-lab`
   - Splunk, Wazuh, Elastic, or Microsoft Sentinel detections
   - Query examples
   - Alert logic
   - False-positive tuning notes

4. `vulnerability-assessment-report`
   - Scanner output summary
   - Risk rating
   - Remediation plan
   - Executive summary

5. `python-security-automation`
   - IOC parser
   - Log analyzer
   - Hash checker
   - Report generator

6. `security-policy-and-grc-pack`
   - Acceptable use policy
   - Incident response policy
   - Risk register
   - NIST/ISO 27001 mapping

## 30-Day Hiring Roadmap

| Week | Priority | Outcome |
| --- | --- | --- |
| Week 1 | Cleanup and branding | Archive/delete weak repos, create profile README, rewrite repo descriptions, pin strongest repos. |
| Week 2 | Build two flagship labs | Publish SOC home lab and Windows Event Log Analysis with screenshots and findings. |
| Week 3 | Add automation and vulnerability work | Publish Python security automation and vulnerability assessment report. |
| Week 4 | Final polish | Add GitHub Actions, templates, link checks, releases, and recruiter-focused README language. |

## Profile README Roadmap

Create a special GitHub profile repository named `wilsonvs` and add a recruiter-focused `README.md` with:

- Professional headline
- Short cybersecurity summary
- Core skills table
- Featured projects
- Certifications and learning
- Tools and platforms
- Current focus
- Contact links approved for public display

## Recommended Pinned Repositories

1. `soc-home-lab`
2. `windows-event-log-analysis`
3. `siem-detection-lab`
4. `python-security-automation`
5. `vulnerability-assessment-report`
6. `Google-Cybersecurity`

## Repository README Standard

Each public project should include:

- Overview
- Problem statement
- Objectives
- Architecture or workflow diagram
- Tools and technologies
- Installation or setup
- Usage or investigation steps
- Screenshots or sample output
- Findings
- Recommendations
- Lessons learned
- Future improvements
- References
- License

## Hiring Review

### Recruiter Concerns

- Too many repositories with unclear value.
- Public `Test` repository looks unfinished.
- Duplicate certificate repository creates confusion.
- No profile README currently visible through the connector.

### SOC Manager Concerns

- Need more investigation artifacts, alert notes, and incident reports.
- Need practical SIEM examples and triage workflow.

### Senior Security Engineer Concerns

- Need stronger technical depth, sample logs, scripts, detections, and validation notes.

### HR Manager Concerns

- Portfolio should quickly communicate role fit, certifications, and contact path.

## Immediate Next Actions

1. Archive `Test`, `WordPress`, and `google-cybersecurity-1` through GitHub repository settings.
2. Create the `wilsonvs/wilsonvs` profile README repository.
3. Rename `cyber` to `cybersecurity-portfolio` if GitHub allows it.
4. Build one flagship SOC lab before adding more repositories.
5. Pin only the strongest cybersecurity repositories.