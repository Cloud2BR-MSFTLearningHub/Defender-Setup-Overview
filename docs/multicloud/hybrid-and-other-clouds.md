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

## Why enable it

On-premises datacenters, private clouds, and providers without a native connector
are often the least monitored part of an estate — yet they run legacy systems
attackers love. Azure Arc projects those machines and clusters into Azure so a
single Defender plan can protect them alongside cloud-native resources.

| Without Azure Arc | With Arc-connected resources |
| --- | --- |
| On-premises and other-cloud assets sit outside Defender | Supported servers and clusters gain Defender coverage |
| Security tooling differs per location | One plan and portal span every environment |
| Inventory is incomplete and manual | Arc builds a central, queryable inventory |
| Legacy systems are hard to monitor | EDR, vulnerability, and posture reach them consistently |

**Value in one line:** it brings the hardest-to-reach servers and clusters under
the same protection, inventory, and reporting as the rest of the cloud estate.

## How it works

Azure Arc installs a lightweight connected-machine agent, for servers, or an agent
set, for Kubernetes, that registers the resource as an Arc-enabled object inside an
Azure subscription. Once projected, the resource can receive the same Defender
plan, Azure Policy, and extensions as a native Azure resource, and its telemetry
appears in both Defender for Cloud and the Microsoft Defender portal.

Arc handles projection, not eligibility. A machine becomes protected only when the
relevant Defender plan is enabled in its subscription and the required components
are healthy, and only the resource types listed in each product's support matrix
are covered.

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

## Architecture and prerequisites

- **Connected Machine agent (azcmagent):** registers a server as an Arc resource and needs outbound HTTPS to Arc and Defender endpoints, or a configured proxy or private link.
- **Arc-enabled Kubernetes agents:** deploy via Helm and require cluster-admin and egress to Arc endpoints.
- **Extensions:** Defender capabilities (MDE, AMA, vulnerability assessment) are delivered as Arc VM extensions once the plan is enabled in the resource's subscription.
- **Placement:** choose tenant, subscription, resource group, region, and RBAC deliberately, because they define cost, policy inheritance, and access.
- **Permissions:** Azure Connected Machine Onboarding plus Contributor to onboard; Security Admin / Owner to enable plans.

## Scale and operate

- Onboard at scale with a service principal and a configuration-management package (Group Policy, Ansible, or the install script).
- Govern with Azure Policy at the management-group scope so Arc resources receive the intended Defender plan and extensions automatically.
- Reconcile Arc inventory against the CMDB, monitor disconnected agents and certificate or proxy health, and define offboarding so retired assets stop billing and reporting.

!!! warning "Important"
    Azure Arc does not make every third-party PaaS service eligible for an Azure
    Defender workload plan. It projects supported servers, Kubernetes, data, and
    selected services according to each product's support matrix.

## Operational decisions

- Treat Arc onboarding as a configuration-management deployment with proxy,
    certificate, patching, and removal ownership rather than a one-time install.
- Confirm local administrators understand the approved isolation and recovery
    procedure before enabling disruptive endpoint response on critical servers.
- Retain server asset ID, Arc resource ID, extension state, network dependency,
    local owner, and decommissioning date for coverage reconciliation.

## Worked example

A manufacturing site has 40 VMware-hosted Linux servers with inconsistent
antivirus coverage. The platform team Arc-enables five non-production servers
through its outbound proxy, enables Defender for Servers on the target
subscription, and validates extension health and alert routing. After the pilot,
the same configuration-management package rolls out to the remaining servers.
