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
next-generation antivirus, attack surface reduction, and behavioral EDR in one
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
flags suspicious sequences — including fileless and living-off-the-land attacks.

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

## Architecture and prerequisites

- **Sensor:** built into Windows 10/11 and Windows Server; installed via package on macOS and Linux; mobile uses the Defender app with Intune.
- **Onboarding:** Intune, Configuration Manager, Group Policy, or script; the onboarding blob authorizes the sensor to the tenant.
- **Cloud dependency:** cloud-delivered protection and EDR require outbound access to the documented Microsoft endpoints; sample submission improves verdicts.
- **Licensing:** Plan 1 (prevention), Plan 2 (full EDR, automated investigation, and threat intelligence), or Defender for Business for small and medium organizations.
- **RBAC:** device groups and role-based access control scope who can view and act on which devices.

## Detections and MITRE ATT&CK

Behavioral EDR maps alerts to ATT&CK tactics — Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Lateral Movement, Command and Control, and Impact — and chains them into a device timeline.

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
