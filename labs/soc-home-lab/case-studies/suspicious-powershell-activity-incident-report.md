# SOC Case Study: Suspicious PowerShell Activity

## What I Investigated

I investigated a lab scenario where PowerShell activity appeared unusual for a workstation. The goal was to practice endpoint alert triage, process review, command-line analysis, MITRE ATT&CK mapping, and response recommendations.

## Scenario

An endpoint alert reports that PowerShell executed with encoded or suspicious command-line arguments. The user does not normally run administrative scripts, so the activity requires validation.

## Alert Summary

| Field | Value |
| --- | --- |
| Alert Name | Suspicious PowerShell Command Line |
| Severity | High in this lab |
| User | `alice` |
| Host | `workstation-01` |
| Process | `powershell.exe` |
| Parent Process | `winword.exe` |
| Command Indicator | Encoded command and hidden window behavior |
| Initial Verdict | Suspicious, escalate for containment validation |

## Why This Matters

PowerShell is a legitimate administration tool, but attackers also use it for discovery, download activity, defense evasion, credential access, and payload execution. The parent process matters. PowerShell launched from Office, browser, or email client processes is more suspicious than PowerShell launched from an administrator shell.

## Evidence Timeline

| Time | Evidence | Interpretation |
| --- | --- | --- |
| 10:14 | User opened attachment in `winword.exe` | Possible phishing or malicious document entry point |
| 10:15 | `winword.exe` spawned `powershell.exe` | Suspicious parent-child process relationship |
| 10:15 | PowerShell used hidden window behavior | Possible attempt to avoid user visibility |
| 10:16 | Outbound connection to unfamiliar domain | Possible payload download or command-and-control check-in |
| 10:18 | Endpoint alert generated | Requires host and user validation |

## Evidence I Would Review

- Endpoint detection alert details
- PowerShell command line
- Parent process and process tree
- Windows Event ID `4688` process creation logs, if enabled
- PowerShell operational logs
- Script block logs, if enabled
- DNS and proxy logs for outbound domains
- Recent email attachments or downloaded files
- User account activity before and after execution

## Detection Logic Idea

### Plain Language

Alert when PowerShell starts from an unusual parent process and uses suspicious arguments such as encoded commands, hidden window execution, remote download behavior, or bypass flags.

### Sigma-Style Logic

```yaml
title: Suspicious PowerShell From Office Parent
status: experimental
logsource:
  product: windows
  category: process_creation
detection:
  selection_parent:
    ParentImage|endswith:
      - '\\winword.exe'
      - '\\excel.exe'
      - '\\powerpnt.exe'
      - '\\outlook.exe'
  selection_child:
    Image|endswith: '\\powershell.exe'
  suspicious_args:
    CommandLine|contains:
      - '-enc'
      - '-encodedcommand'
      - '-w hidden'
      - 'downloadstring'
      - 'iex'
      - 'bypass'
  condition: selection_parent and selection_child and suspicious_args
fields:
  - UtcTime
  - User
  - Image
  - ParentImage
  - CommandLine
falsepositives:
  - Rare administrative automation launched through Office macros
level: high
```

### KQL-Style Idea

```kql
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName in~ ("winword.exe", "excel.exe", "powerpnt.exe", "outlook.exe")
| where ProcessCommandLine has_any ("-enc", "-encodedcommand", "-w hidden", "downloadstring", "iex", "bypass")
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName, FileName, ProcessCommandLine
```

## MITRE ATT&CK Mapping

| Tactic | Technique | Reason |
| --- | --- | --- |
| Execution | PowerShell `T1059.001` | PowerShell used to execute commands |
| Defense Evasion | Obfuscated Files or Information `T1027` | Encoded command may hide intent |
| Initial Access | Phishing `T1566` | Office parent may indicate attachment-based execution |
| Command and Control | Application Layer Protocol `T1071` | Outbound connection after execution may indicate check-in |

## Triage Questions

1. Did the user expect to run a macro or script?
2. What file or document was opened before PowerShell started?
3. What exact command line executed?
4. Was a file downloaded or written to disk?
5. Did the host connect to a suspicious domain or IP?
6. Did the user account authenticate elsewhere after the activity?
7. Are other endpoints showing the same parent-child pattern?

## Findings

| Finding | Assessment |
| --- | --- |
| Office process launched PowerShell | Suspicious parent-child process chain |
| Encoded/hidden execution behavior | Raises likelihood of malicious intent |
| Outbound connection occurred shortly after execution | Requires network validation |
| User does not normally run scripts | Increases priority |

## Recommendation

1. Isolate the host if command line or network activity indicates payload execution.
2. Preserve process, PowerShell, DNS, proxy, and endpoint logs.
3. Collect the suspicious document and hash it.
4. Search for the same document hash, command line, domain, and parent-child process chain across other endpoints.
5. Reset user credentials if phishing or credential theft is suspected.
6. Block confirmed malicious domains or hashes.
7. Review macro controls, attachment filtering, and PowerShell logging coverage.

## Lessons Learned

Suspicious PowerShell triage depends on context. PowerShell alone is not malicious; the parent process, command line, user behavior, network activity, and follow-on process activity determine the risk.