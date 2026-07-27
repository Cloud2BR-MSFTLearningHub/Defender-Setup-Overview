# Microsoft Defender for Servers Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Servers protects Windows and Linux machines in Azure, AWS, GCP,
and on-premises environments. Non-Azure machines normally connect through Azure
Arc. Microsoft Defender for Endpoint supplies endpoint detection and response.

## Plan choice

| Plan | Use case |
| --- | --- |
| Plan 1 | Core server protection with Defender for Endpoint capabilities |
| Plan 2 | Broader server protection, including additional vulnerability, monitoring, and cloud workload capabilities |

Always compare the current plan matrix before purchase; features, billing, and
included data allowances can change.

## Enable

1. Inventory Azure VMs, Arc-enabled servers, VM scale sets, and multicloud VMs.
2. In **Environment settings**, enable the selected Servers plan.
3. Review **Settings & monitoring** and configure required components.
4. Configure Defender for Endpoint integration and onboarding status.
5. Define Log Analytics and data collection architecture where required.
6. Roll out through a pilot ring before enabling all subscriptions.

## Verify and operate

- Check Defender for Cloud inventory and Defender portal device inventory.
- Confirm sensor health, vulnerability assessment, and recommendation freshness.
- Run Microsoft's documented detection test only on an approved test machine.
- Route alerts to the incident owner and test machine isolation procedures.
- Track uncovered machines, stale agents, exclusions, and unsupported systems.

> [!IMPORTANT]
> Azure Arc enrollment and Defender for Servers licensing are separate concerns.
> An Arc-connected server is not necessarily protected until its plan and
> required components are healthy.

## References

- [Defender for Servers overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-introduction)
- [Plan a deployment](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers)
- [Deploy Defender for Servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-servers-plan)
- [Defender for Endpoint detection test](https://learn.microsoft.com/en-us/defender-endpoint/run-detection-test)
