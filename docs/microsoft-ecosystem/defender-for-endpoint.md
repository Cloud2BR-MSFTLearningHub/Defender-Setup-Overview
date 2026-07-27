# Microsoft Defender for Endpoint Overview

<details markdown>
<summary>References</summary>

- [Defender for Endpoint overview](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint)
- [Plan deployment](https://learn.microsoft.com/en-us/defender-endpoint/mde-planning-guide)
- [Minimum requirements](https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements)
- [Pilot and deploy](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-defender-endpoint)

</details>

[Back to the documentation hub](../index.md)

Defender for Endpoint is Microsoft's enterprise endpoint security platform for
prevention, endpoint detection and response, investigation, and remediation.
It supports eligible Windows, macOS, Linux, Android, and iOS platforms, combining
next-generation antivirus, attack surface reduction, and behavioral endpoint detection and response (EDR) in one
sensor.

## Why enable it

Endpoints are where most attacks land and where response has to happen fast.
Defender for Endpoint adds behavioral detection, one-click isolation, and
automated investigation on top of prevention, so a compromised device can be
contained in minutes rather than hours.

| Without Defender for Endpoint | With the platform deployed |
| --- | --- |
| Antivirus blocks known malware but little else | Behavioral EDR catches novel and fileless attacks |
| A compromised device stays connected during triage | One-click isolation and live response contain it |
| Vulnerability data lives in a separate scanner | Integrated vulnerability management is built in |
| Endpoint alerts are disconnected from other signals | Signals feed Defender XDR incident correlation |

**Value in one line:** it upgrades endpoints from prevention-only antivirus to
detection, investigation, and rapid containment that feeds the wider XDR picture.

## How it works

A single Defender for Endpoint sensor delivers layered protection on each device:
next-generation antivirus blocks known malware, attack surface reduction rules
close common exploitation techniques, and the behavioral EDR engine streams
process, file, network, and registry events to the cloud, where machine learning
flags suspicious sequences, including fileless and living-off-the-land attacks.

When something is found, responders can isolate the device, run live-response
commands, and collect forensic evidence from the Defender portal, while automated
investigation remediates common threats on its own. All of this feeds Defender XDR,
so an endpoint alert is correlated with the identity and email signals around it.

## Deployment paths

| Device group | Common management path |
| --- | --- |
| Windows clients | Microsoft Intune, Configuration Manager, Group Policy, or script |
| Windows and Linux servers | Defender for Servers integration or direct onboarding |
| macOS and Linux clients | Intune or supported third-party management tooling |
| Android and iOS | Intune mobile threat defense integration |

## Configure

1. Choose Plan 1, Plan 2, Defender for Business, or another eligible license.
2. Review platform versions, network endpoints, coexistence, and data residency.
3. Define pilot device groups and role-based access.
4. Deploy onboarding and security settings through the management authority.
5. Configure attack surface reduction, EDR, cloud protection, and tamper protection.
6. Integrate Intune, Defender for Cloud, and Sentinel only as needed.

## Verify and operate

- Confirm device inventory, sensor health, antivirus mode, and last-seen time.
- Run Microsoft's documented detection test on an approved test device.
- Validate isolation, live response, evidence collection, and rollback authority.
- Track unmanaged devices, exposure score, vulnerabilities, and stale sensors.

## Operational decisions

- Assign endpoint isolation and live-response permissions only to trained roles,
  and define an approval path for business-critical devices.
- Test policy changes, exclusions, and attack-surface rules with representative
  applications before broad enforcement; remove temporary exclusions on schedule.
- Retain device ID, user, process tree, network evidence, response command,
  containment approval, and clean-state validation with each case.

## Business example

> An employee opens a malicious attachment and Defender for Endpoint detects a
> suspicious child process from Office. The analyst isolates the device from the
> portal, uses live response to collect the command history, confirms no lateral
> movement in advanced hunting, and releases the device only after automated
> remediation and a clean rescan complete.

## Architecture and prerequisites

- **Sensor:** built into Windows 10/11 and Windows Server; installed via package on macOS and Linux; mobile uses the Defender app with Intune.
- **Onboarding:** Intune, Configuration Manager, Group Policy, or script; the onboarding blob authorizes the sensor to the tenant.
- **Cloud dependency:** cloud-delivered protection and EDR require outbound access to the documented Microsoft endpoints; sample submission improves verdicts.
- **Licensing:** Plan 1 (prevention), Plan 2 (full EDR, automated investigation, and threat intelligence), or Defender for Business for small and medium organizations.
- **RBAC:** device groups and role-based access control scope who can view and act on which devices.

## Detections and MITRE ATT&CK

Behavioral EDR maps alerts to ATT&CK tactics, including Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Lateral Movement, Command and Control, and Impact, then chains them into a device timeline.

## Advanced hunting example

Hunt for encoded PowerShell across every onboarded device:

```kusto
DeviceProcessEvents
| where Timestamp > ago(24h)
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any ("-enc", "-EncodedCommand")
| project Timestamp, DeviceName, AccountUpn, ProcessCommandLine
```

Convert high-value queries into custom detection rules so they generate alerts automatically.

Find Office applications that launch a command shell or PowerShell, a common
starting point for malicious attachments:

```kusto
DeviceProcessEvents
| where Timestamp > ago(24h)
| where InitiatingProcessFileName in~ ("winword.exe", "excel.exe", "powerpnt.exe")
| where FileName in~ ("cmd.exe", "powershell.exe", "pwsh.exe")
| project Timestamp, DeviceName, AccountUpn, InitiatingProcessFileName,
  FileName, ProcessCommandLine
| order by Timestamp desc
```

## Hunting data lifecycle

Before operationalizing a hunting query, define its data source, expected event
coverage, lookback period, query owner, and the incident action that follows a
match. Advanced hunting schemas, availability, and retention depend on product
configuration and can change; verify the current schema and retention policy in
the Defender portal for the tenant rather than assuming that a historical query
will always return complete endpoint evidence.

Use narrow time windows, explicit device or identity scope, and projected columns
while developing a query. Preserve the query, parameters, result reference, and
collection time with the case record, because device timelines and retained data
can change after cleanup or offboarding. For long-term or cross-source evidence,
design the approved export and retention path separately and apply the same data
classification and access controls as the underlying endpoint telemetry.
