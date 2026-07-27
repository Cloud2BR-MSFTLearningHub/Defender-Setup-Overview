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

!!! warning "Important"
  Automated isolation, blocking, or deletion can interrupt production. Start
  with audit and notification, define an owner and rollback path, and then move
  well-tested controls to enforcement.
