# What Is Microsoft Defender?

<details markdown>
<summary>References</summary>

- [Microsoft Defender for Cloud overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Microsoft Defender XDR overview](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender)
- [Microsoft Sentinel overview](https://learn.microsoft.com/en-us/azure/sentinel/overview)
- [Azure Arc overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)
- [Configuration, plans, and pricing](operations/configuration-plans-and-pricing.md)

</details>

[Back to the documentation hub](index.md)

Microsoft Defender is Microsoft's security product family. The correct product
depends on whether the asset is a cloud resource, device, identity, mailbox,
SaaS application, or security event.

![Microsoft Defender for Cloud CNAPP capabilities across cloud environments](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-cloud-introduction/defender-plans.png)

*Source: [Microsoft Defender for Cloud overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction).* 

## Why it matters

Each Defender product exists because a different part of the environment is a
distinct attack surface. Turning the right ones on replaces blind spots and
disconnected point tools with layered, correlated protection: posture management
prevents misconfigurations, workload plans detect runtime attacks, and Defender
XDR ties the signals into incidents your team can actually act on. The pages in
this hub each explain the specific value of enabling that protection.

## The four layers

| Layer | Primary role | Examples |
| --- | --- | --- |
| Microsoft Defender for Cloud | CNAPP: posture, DevSecOps, and workload protection | Azure, AWS, GCP, Arc-enabled resources |
| Microsoft Defender XDR | Unified detection and response | Endpoint, Identity, Office 365, Cloud Apps |
| Microsoft Sentinel | Cloud-native SIEM and SOAR | Analytics, retention, hunting, playbooks, third-party data |
| Policy and management | Prevention and remediation | Azure Policy, Intune, Conditional Access, Gatekeeper, Logic Apps |

## Defender for Cloud

Defender for Cloud combines three cloud-security disciplines:

- **CSPM** continuously evaluates configuration and exposure. Foundational CSPM
  is free; Defender CSPM adds capabilities such as attack paths, cloud security
  explorer, governance, and agentless scanning where supported.
- **DevSecOps** connects GitHub, Azure DevOps, and GitLab so code, secret, and
  infrastructure-as-code findings can be related to deployed resources.
- **CWPP** adds workload-specific threat protection through plans for servers,
  containers, storage, databases, App Service, Key Vault, Resource Manager,
  APIs, and AI workloads.

Azure subscriptions connect natively. AWS and GCP use multicloud connectors.
Servers and Kubernetes on-premises or in another cloud normally use Azure Arc.
Before enabling a workload plan, use the [configuration, plans, and pricing
reference](operations/configuration-plans-and-pricing.md) to compare supported
tiers, configure settings, confirm regional eligibility, and estimate cost.

## Defender XDR

Defender XDR correlates signals from products that are licensed and deployed:

- Defender for Endpoint protects Windows, Linux, macOS, Android, and iOS.
- Defender for Identity uses Active Directory signals to detect identity threats.
- Defender for Office 365 protects email and collaboration workloads.
- Defender for Cloud Apps provides cross-SaaS visibility and controls.
- Defender Vulnerability Management prioritizes endpoint vulnerabilities.

The [Microsoft Defender portal](https://security.microsoft.com/) provides
incidents, alerts, hunting, assets, exposure management, and response. Some
Defender for Cloud capabilities are also moving into this unified portal.

## Detection is not enforcement

Defender products can recommend, alert, investigate, and perform supported
response actions. They do not automatically rewrite every unsafe cloud resource.

| Desired outcome | Typical control |
| --- | --- |
| Deny a noncompliant Azure deployment | Azure Policy deny effect |
| Enforce Kubernetes admission rules | Azure Policy for Kubernetes or Gatekeeper |
| Require a compliant managed device | Intune plus Conditional Access |
| Respond to an alert | Defender automation, Logic Apps, Sentinel playbooks, or API |
| Repair infrastructure configuration | Infrastructure as code and deployment pipeline |

## Where signals surface

| Product family | Primary portal | Query and export |
| --- | --- | --- |
| Defender for Cloud plans | Microsoft Defender for Cloud in the Azure portal | Continuous export to Log Analytics (`SecurityAlert`) or Event Hubs |
| Defender XDR products | Microsoft Defender portal | Advanced hunting (KQL) and the streaming API |
| Microsoft Sentinel | Defender portal or Azure portal | Log Analytics workspace, analytics rules, and workbooks |
| Entra ID Protection | Microsoft Entra admin center | Sentinel connector and Microsoft Graph |

Alerts from every layer can converge in Defender XDR and Microsoft Sentinel, which is what makes cross-domain correlation possible. Decide the primary incident queue (Defender XDR or Sentinel) before enabling connectors so ownership and automation stay unambiguous.

!!! warning "Important"
    Automated isolation, blocking, or deletion can interrupt production. Start
    with audit and notification, define an owner and rollback path, and then move
    well-tested controls to enforcement.

## Operating model decisions

- Establish a service owner for each workload, a security owner for detection and
  triage, and a platform owner for preventive controls before enabling automation.
- Choose Defender XDR or Sentinel as the primary incident queue, then document
  which response actions are approved, automated, or reserved for the workload team.
- Retain asset inventory, plan coverage, control exceptions, incident evidence,
  response outcomes, and recovery lessons in a reviewable security record.

## Worked example

An attacker compromises a developer identity and uses it to deploy a public
container workload. Defender CSPM identifies the exposed configuration, Defender
for Containers detects suspicious activity in the pod, and Defender XDR links the
developer's risky sign-in to the workload incident. The response team revokes the
identity session, contains the workload through the approved Kubernetes process,
and adds an admission control to prevent the same public configuration.
