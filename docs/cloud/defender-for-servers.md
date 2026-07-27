# Microsoft Defender for Servers Overview

<details markdown>
<summary>References</summary>

- [Defender for Servers overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-introduction)
- [Plan a deployment](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers)
- [Deploy Defender for Servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-servers-plan)
- [Defender for Endpoint detection test](https://learn.microsoft.com/en-us/defender-endpoint/run-detection-test)
- [Configuration, plans, and pricing](../operations/configuration-plans-and-pricing.md)

</details>

[Back to the documentation hub](../index.md)

Defender for Servers protects Windows and Linux machines in Azure, AWS, GCP,
and on-premises environments. Non-Azure machines normally connect through Azure
Arc. Microsoft Defender for Endpoint supplies endpoint detection and response,
and the plan adds vulnerability assessment, file integrity monitoring, and
agentless disk scanning so a server is protected whether or not an agent is
healthy at any moment.

## Why enable it

Servers hold the operating systems, credentials, and data that attackers pursue
after an initial foothold. Defender for Servers gives those machines the same
endpoint-grade detection and response used to protect managed devices, extended
across every cloud and on-premises estate from a single plan.

| Without Defender for Servers | With the plan enabled |
| --- | --- |
| VMs rely on inconsistent, per-team antivirus | Unified Defender for Endpoint EDR across Windows and Linux |
| Vulnerabilities are discovered on a periodic scan cycle | Integrated vulnerability assessment reports continuously |
| Non-Azure servers sit outside central security | Arc-connected AWS, GCP, and on-premises servers are covered |
| A disabled agent means a blind spot | Agentless disk scanning still evaluates the machine |

**Value in one line:** it extends enterprise endpoint detection, vulnerability
management, and hardening to every server, not just the ones inside Azure.

## How it works

Defender for Servers combines two layers. The first is Microsoft Defender for
Endpoint, whose sensor runs on the machine to provide next-generation antivirus,
attack surface reduction, and behavioral endpoint detection and response. Its
alerts and device data flow into both Defender for Cloud and the Microsoft
Defender portal, so a server incident sits next to the endpoint and identity
signals it relates to.

The second layer is agentless. Defender for Cloud periodically snapshots the
machine's disk to assess installed software, vulnerabilities, exposed secrets, and
malware without depending on a running agent, while integrated vulnerability
assessment keeps a live list of weaknesses. Non-Azure machines join through Azure
Arc, which projects them into a subscription so the same plan, policies, and
reporting apply whether the server runs in Azure, another cloud, or a datacenter.

## Plan choice

| Plan | Use case |
| --- | --- |
| [Plan 1](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers) | Core server protection with Defender for Endpoint capabilities |
| [Plan 2](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers) | Broader server protection, including additional vulnerability, monitoring, and cloud workload capabilities |

Always compare the current plan matrix before purchase; features, billing, and
included data allowances can change. Use the [configuration, plans, and pricing
reference](../operations/configuration-plans-and-pricing.md) for the current
pricing and regional-support checks.

## Enable

1. Inventory Azure VMs, Arc-enabled servers, VM scale sets, and multicloud VMs.
2. In [Environment settings](https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/~/1), enable the selected Servers plan.
3. Review **Settings & monitoring** and [configure required components](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security).
4. Configure Defender for Endpoint integration and onboarding status.
5. Define Log Analytics and data collection architecture where required.
6. Roll out through a pilot ring before enabling all subscriptions.

## Verify and operate

- Check Defender for Cloud inventory and Defender portal device inventory.
- Confirm sensor health, vulnerability assessment, and recommendation freshness.
- Run Microsoft's documented detection test only on an approved test machine.
- Route alerts to the incident owner and test machine isolation procedures.
- Track uncovered machines, stale agents, exclusions, and unsupported systems.

## Architecture and prerequisites

- **Endpoint sensor:** Plan 1 and Plan 2 provision Microsoft Defender for Endpoint through the unified MDE extension, with automatic onboarding for Azure and Arc machines.
- **Agentless disk scanning:** snapshot-based assessment evaluates vulnerabilities, exposed secrets, and malware without an in-guest agent; it complements, not replaces, the MDE sensor.
- **Data collection:** the Azure Monitor Agent (AMA) supports capabilities such as file integrity monitoring; the legacy Log Analytics agent (MMA) is retired, so new deployments should standardize on AMA or agentless.
- **Connectivity:** machines need outbound access to Defender for Endpoint and Defender for Cloud service endpoints; closed networks require the documented proxy or private configuration.
- **Permissions:** enabling the plan requires Security Admin or Owner on the subscription; Arc onboarding requires the Azure Connected Machine Onboarding role.

## Detections and MITRE ATT&CK

Alerts map to MITRE ATT&CK so responders can reason in tactic terms:

| Example detection | ATT&CK tactic |
| --- | --- |
| Suspicious PowerShell or shell command execution | Execution |
| Credential-dumping behavior (for example LSASS access) | Credential Access |
| Reverse shell or anomalous outbound connection | Command and Control |
| Web shell or scheduled-task persistence | Persistence |
| Sign-in from a known-malicious IP | Initial Access |

Alerts surface in Defender for Cloud and the Microsoft Defender portal and can be exported to the `SecurityAlert` table in Log Analytics or Microsoft Sentinel.

## Scale the deployment

- Enable the plan at management-group scope and use the Defender for Endpoint integration setting so new machines onboard automatically.
- For Arc, deploy the Connected Machine agent at scale with a service principal, a configuration-management package, or the install script.
- Govern configuration with Azure Policy (for example, "Defender for Servers should be enabled") and remediate non-compliant subscriptions with DeployIfNotExists.

!!! warning "Important"
    Azure Arc enrollment and Defender for Servers licensing are separate concerns.
    An Arc-connected server is not necessarily protected until its plan and
    required components are healthy.

## Operational decisions

- Select a single onboarding authority for Azure VMs, Arc servers, and endpoint
    tooling so duplicate agents and coverage gaps can be reconciled quickly.
- Define who may isolate a server, what application dependency check is required,
    and the recovery evidence needed before it is released.
- Retain plan scope, extension health, MDE device ID, OS owner, and offboarding
    date for every protected server.

## Worked example

An Arc-enabled SQL Server in a datacenter appears in Azure inventory but has no
Defender for Endpoint device record. The team enables Defender for Servers Plan 2
on the Arc resource's subscription, verifies the MDE extension reports healthy,
and uses the documented detection test on a maintenance-window clone. They then
add a policy initiative so future Arc servers are onboarded automatically.
