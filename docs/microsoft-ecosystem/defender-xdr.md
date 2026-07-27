# Microsoft Defender XDR Overview

<details markdown>
<summary>References</summary>

- [Microsoft Defender XDR overview](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender)
- [Turn on Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/m365d-enable)
- [Microsoft Defender portal](https://security.microsoft.com/)
- [Advanced hunting overview](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview)

</details>

[Back to the documentation hub](../index.md)

Microsoft Defender XDR unifies prevention, detection, investigation, and
response across endpoints, identities, email, collaboration, applications, and
connected cloud signals in the Microsoft Defender portal. Instead of chasing
separate alerts in separate consoles, analysts work a single incident that
stitches the related evidence together automatically.

## Why enable it

Modern attacks cross domains: a phishing email leads to a stolen identity, which
leads to an endpoint, which reaches the cloud. Reviewing each product separately
hides that story. Defender XDR correlates the signals into one incident and can
respond automatically, cutting the time attackers have to act.

| Without Defender XDR | With Defender XDR enabled |
| --- | --- |
| Alerts are triaged product by product | Related alerts merge into a single incident |
| Analysts pivot between multiple consoles | One portal shows the full attack story |
| Cross-domain attacks are pieced together manually | Correlation links email, identity, endpoint, and cloud |
| Response is manual and slow | Automated investigation and response contain threats faster |

**Value in one line:** it turns a flood of isolated alerts into a few
prioritized incidents and automates the routine response work behind them.

## How it works

Defender XDR does not collect telemetry itself; it consumes the signals from each
connected Defender product and Microsoft Sentinel. A correlation engine groups
related alerts across email, identity, endpoint, cloud apps, and cloud workloads
into a single incident with a shared timeline, affected assets, and evidence, so
analysts investigate one story instead of many disconnected alerts.

Automated investigation and response can then run playbooks that examine the
incident, reach a verdict, and take approved remediation such as isolating a device
or blocking a user. Advanced hunting exposes the underlying raw data through a
query language, so teams can hunt proactively and build custom detections.

## Signal sources

- Microsoft Defender for Endpoint and Defender Vulnerability Management.
- Microsoft Defender for Office 365.
- Microsoft Defender for Identity and Microsoft Entra ID Protection.
- Microsoft Defender for Cloud Apps and App Governance.
- Microsoft Defender for Cloud and other integrated Microsoft security services.

Only licensed, provisioned, and connected products contribute their full signals.

## Configure

1. Confirm tenant, data location, licenses, roles, and privacy requirements.
2. Turn on Defender XDR and configure each underlying Defender workload.
3. Review unified portal settings, alert notifications, device groups, and roles.
4. Configure automated investigation and response at an approved automation level.
5. Connect Sentinel or another SIEM only after defining incident ownership.
6. Build hunting, retention, and evidence-preservation procedures.

## Verify and operate

- Confirm alerts from enabled products correlate into incidents.
- Validate advanced-hunting schema and role-based data visibility.
- Test containment and remediation with approved simulation tooling.
- Tune alert rules and exclusions with expiry, owner, and evidence.
- Measure time to triage, contain, remediate, and close incidents.

## Architecture and data model

- **Correlation:** Defender XDR ingests alerts and entities from each connected product and fuses them into incidents with a shared graph of accounts, devices, mailboxes, and cloud resources.
- **Advanced hunting:** a unified schema exposes raw events across products (device, identity, email, cloud app, and alert tables) queried with Kusto Query Language (KQL).
- **RBAC:** unified role-based access control governs which data and actions each analyst sees; device groups scope endpoint actions.
- **Automation:** Automated Investigation and Response runs at a configurable automation level, from full audit to automatic remediation.

## Advanced hunting example

Hunt for encoded PowerShell across the fleet, then pivot to the account and device:

```kusto
DeviceProcessEvents
| where Timestamp > ago(24h)
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any ("-enc", "-EncodedCommand")
| project Timestamp, DeviceName, AccountUpn, ProcessCommandLine
```

Save high-value queries as custom detection rules so novel techniques become first-class alerts that feed the same incident correlation.

Find high-severity alerts with account, mail, URL, or device evidence, then use
the shared alert ID to pivot to the related incident:

```kusto
AlertInfo
| where Timestamp > ago(24h)
| where Severity in~ ("High", "Medium")
| join kind=inner (
    AlertEvidence
    | where EntityType in~ ("Account", "Device", "MailMessage", "Url")
    | project AlertId, EntityType, EntityValue
) on AlertId
| project Timestamp, AlertId, Title, Severity, ServiceSource, EntityType, EntityValue
| order by Timestamp desc
```

!!! note
    Defender XDR is the correlation and response layer. It does not create missing
    telemetry from a Defender product that has not been licensed or deployed.

## Operational decisions

- Select one primary incident queue and document the handoff to Sentinel or ITSM
    so two teams do not independently contain or close the same incident.
- Define automation authority by action: enrichment may be automatic, while
    isolation, account disablement, and mailbox remediation need explicit ownership.
- Retain incident ID, contributing alerts, affected entities, automation actions,
    analyst decision, and recovery evidence as a single case record.

## Worked example

> A phishing email delivers a malicious link to a finance user. Defender for Office
> 365 records the click, Defender for Endpoint detects the downloaded payload, and
> Entra records a risky sign-in. Defender XDR groups the three alerts into one
> incident; automated investigation isolates the device while the SOC resets the
> account and removes the message from other mailboxes.
