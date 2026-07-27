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
Arc. Microsoft Defender for Endpoint supplies endpoint detection and response.

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

!!! warning "Important"
    Azure Arc enrollment and Defender for Servers licensing are separate concerns.
    An Arc-connected server is not necessarily protected until its plan and
    required components are healthy.
