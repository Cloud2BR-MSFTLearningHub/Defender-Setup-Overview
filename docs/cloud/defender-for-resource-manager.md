# Microsoft Defender for Resource Manager Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Resource Manager monitors Azure resource-management operations for
suspicious control-plane activity, including behavior associated with credential
abuse, unusual administration, or destructive changes.

## Enable

1. Identify subscriptions and management groups that form the security boundary.
2. In Defender for Cloud **Environment settings**, select each subscription.
3. Enable **Resource Manager** and save.
4. Review Azure RBAC, privileged role activation, locks, policy, and activity logs.
5. Define response ownership for subscription-level and tenant-level incidents.
6. Export alerts to the central incident platform when required.

## Verify and operate

- Confirm the plan is enabled across all intended subscriptions.
- Preserve Azure Activity Log data for investigations and compliance needs.
- Correlate alerts with Entra sign-ins, role changes, and deployment history.
- Pre-authorize containment actions for compromised automation identities.
- Monitor newly created or moved subscriptions for configuration drift.

> [!NOTE]
> Resource Manager protection observes the Azure control plane. It does not
> replace workload-specific plans, Entra ID Protection, or privileged identity
> management.

## References

- [Defender for Resource Manager overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-resource-manager-introduction)
- [Enable Defender for Resource Manager](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-resource-manager-plan)
- [Azure Activity Log](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log)
