# Microsoft Defender Setup and Overview Hub

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

Microsoft Defender is a family of security products, not a single switch. This
repository explains where each product applies, what it protects, how it is
onboarded, and where its alerts and recommendations appear.

> [!IMPORTANT]
> Start with [What is Microsoft Defender?](docs/00-overview.md). It separates
> Defender for Cloud, Defender XDR, Microsoft Sentinel, and enforcement tools.

## Choose the workload

| I need to protect | Microsoft product or plan | Guide |
| --- | --- | --- |
| Overall cloud posture | Foundational CSPM or Defender CSPM | [CSPM](docs/cloud/defender-cspm.md) |
| Windows and Linux servers | Defender for Servers | [Servers](docs/cloud/defender-for-servers.md) |
| Kubernetes and container images | Defender for Containers | [Containers](docs/cloud/defender-for-containers.md) |
| Blob, Files, and Data Lake storage | Defender for Storage | [Storage](docs/cloud/defender-for-storage.md) |
| Azure App Service | Defender for App Service | [App Service](docs/cloud/defender-for-app-service.md) |
| SQL, Cosmos DB, and open-source databases | Defender for Databases | [Databases](docs/cloud/defender-for-databases.md) |
| Azure Key Vault | Defender for Key Vault | [Key Vault](docs/cloud/defender-for-key-vault.md) |
| Azure control-plane operations | Defender for Resource Manager | [Resource Manager](docs/cloud/defender-for-resource-manager.md) |
| APIs published in Azure API Management | Defender for APIs | [APIs](docs/cloud/defender-for-apis.md) |
| Generative AI workloads | Defender for AI and AI security posture | [AI workloads](docs/cloud/defender-for-ai.md) |
| Source code and pipelines | Defender for Cloud DevOps security | [DevOps](docs/cloud/devops-security.md) |
| AWS accounts | Defender for Cloud multicloud connector | [AWS](docs/multicloud/aws.md) |
| Google Cloud projects | Defender for Cloud multicloud connector | [GCP](docs/multicloud/gcp.md) |
| On-premises or other-cloud workloads | Azure Arc plus Defender for Cloud | [Hybrid and other clouds](docs/multicloud/hybrid-and-other-clouds.md) |
| PCs, servers, phones, and tablets | Defender for Endpoint | [Endpoints](docs/microsoft-ecosystem/defender-for-endpoint.md) |
| Exchange Online, Teams, SharePoint, and OneDrive | Defender for Office 365 | [Microsoft 365](docs/microsoft-ecosystem/defender-for-office-365.md) |
| Active Directory identities | Defender for Identity | [Identity](docs/microsoft-ecosystem/defender-for-identity.md) |
| SaaS applications and shadow IT | Defender for Cloud Apps | [Cloud Apps](docs/microsoft-ecosystem/defender-for-cloud-apps.md) |
| Vulnerability prioritization and remediation | Defender Vulnerability Management | [Vulnerability Management](docs/microsoft-ecosystem/defender-vulnerability-management.md) |
| Small and medium business endpoints | Microsoft Defender for Business | [Defender for Business](docs/microsoft-ecosystem/defender-for-business.md) |
| Operational technology and enterprise IoT | Microsoft Defender for IoT | [IoT and OT](docs/microsoft-ecosystem/defender-for-iot.md) |
| Entra user and sign-in risk | Microsoft Entra ID Protection | [Entra ID Protection](docs/microsoft-ecosystem/entra-id-protection.md) |
| Cross-domain incidents and hunting | Microsoft Defender XDR | [Defender XDR](docs/microsoft-ecosystem/defender-xdr.md) |
| SIEM, SOAR, and long-term correlation | Microsoft Sentinel | [Sentinel](docs/operations/sentinel-integration.md) |

## Cloud coverage at a glance

| Environment | Native connection | Typical protection path |
| --- | --- | --- |
| Azure | Azure subscription | Enable Defender plans at management group or subscription scope |
| AWS | Defender for Cloud AWS connector | Connect accounts, deploy required AWS resources, and select plans |
| Google Cloud | Defender for Cloud GCP connector | Connect projects or organizations, grant roles, and select plans |
| On-premises and other clouds | Azure Arc | Arc-enable servers or Kubernetes, then enable the relevant plan |
| Microsoft 365 and SaaS | Defender portal connectors and licensing | Configure the relevant Defender XDR workload |

> [!NOTE]
> Coverage and billing differ by plan, resource type, region, and cloud. Validate
> the current support matrix and pricing before production rollout.

## Implementation path

1. Inventory subscriptions, cloud accounts, tenants, workloads, and data owners.
2. Confirm licensing, supported regions, permissions, data residency, and cost.
3. Assign security contacts and centralize plan configuration at scale.
4. Pilot one non-production scope and verify recommendations and test alerts.
5. Connect incident workflows to Defender XDR, Sentinel, ITSM, or automation.
6. Measure coverage, agent health, recommendation age, and response outcomes.

Use the [deployment checklist](docs/operations/deployment-checklist.md) and
[automation guide](docs/operations/automation-and-remediation.md) for rollout.
Estimate and govern spend with the [licensing and cost guide](docs/operations/licensing-and-cost.md).

## Authoritative references

- [Microsoft Defender for Cloud overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Defender for Cloud support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud)
- [Microsoft Defender XDR overview](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender)
- [Microsoft Defender documentation](https://learn.microsoft.com/en-us/defender/)
- [Defender for Cloud pricing](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-40-limegreen" alt="Total views">
  <p>Refresh Date: 2026-04-07</p>
</div>
<!-- END BADGE -->
