# Defender for Hybrid, On-Premises, and Other Clouds

<details markdown>
<summary>References</summary>

- [Azure Arc overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)
- [Azure Arc-enabled servers](https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview)
- [Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview)
- [Connect non-Azure machines to Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-machines)

</details>

[Back to the documentation hub](../index.md)

Azure Arc projects supported non-Azure resources into Azure management. This is
the usual Defender for Cloud path for on-premises datacenters and cloud providers
without a native Defender for Cloud connector.

![Azure Arc management control plane for hybrid and multicloud resources](https://learn.microsoft.com/en-us/azure/azure-arc/media/overview/azure-arc-control-plane.png)

*Source: [Azure Arc overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview).* 

## What can connect

| Asset | Onboarding path | Defender path |
| --- | --- | --- |
| Windows or Linux server | Azure Arc-enabled servers | Defender for Servers |
| Conformant Kubernetes cluster | Azure Arc-enabled Kubernetes | Defender for Containers, subject to support |
| SQL Server on a machine | Azure Arc-enabled server and SQL extension | Defender for SQL servers on machines |
| User endpoint | Defender for Endpoint onboarding | Defender XDR, independent of Azure Arc |

Examples include physical servers, VMware environments, hosted VMs, and
supported machines or Kubernetes clusters in clouds other than AWS and GCP.

## Connect

1. Verify supported operating systems, Kubernetes distributions, regions, and egress.
2. Design Azure tenant, subscription, resource group, region, tags, and RBAC placement.
3. Arc-enable a pilot server or cluster using the documented secure onboarding method.
4. Enable the corresponding Defender plan in the Arc resource's subscription.
5. Deploy required extensions and confirm their health.
6. Expand with an approved at-scale onboarding method.

## Verify and operate

- Reconcile Arc inventory with the source CMDB or cloud inventory.
- Monitor disconnected agents, extension failures, certificates, and proxy changes.
- Confirm Defender telemetry in both Defender for Cloud and the Defender portal.
- Include Arc, Azure Monitor, data-transfer, and Defender charges in cost estimates.
- Define offboarding so retired assets do not remain billable or misleading.

> [!IMPORTANT]
> Azure Arc does not make every third-party PaaS service eligible for an Azure
> Defender workload plan. It projects supported servers, Kubernetes, data, and
> selected services according to each product's support matrix.
