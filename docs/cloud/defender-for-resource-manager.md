# Microsoft Defender for Resource Manager Overview

<details markdown>
<summary>References</summary>

- [Defender for Resource Manager overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-resource-manager-introduction)
- [Enable Defender for Resource Manager](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-resource-manager-plan)
- [Azure Activity Log](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log)

</details>

[Back to the documentation hub](../index.md)

Defender for Resource Manager monitors Azure resource-management operations for
suspicious control-plane activity, including behavior associated with credential
abuse, unusual administration, or destructive changes. Azure Resource Manager is
the management layer every deployment, role change, and configuration passes
through, so it is where an attacker with stolen credentials operates.

![Azure Resource Manager as the consistent management layer monitored by Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-resource-manager-introduction/consistent-management-layer-with-defender.png)

*Source: [Overview of Defender for Resource Manager](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-resource-manager-introduction).*

## Why enable it

Control-plane attacks — mass role assignments, toolkit-driven enumeration, or
bulk resource deletion — look like ordinary administration until you correlate
them. Defender for Resource Manager applies threat intelligence and behavioral
analytics to the management layer so those actions stand out.

| Without Defender for Resource Manager | With the plan enabled |
| --- | --- |
| Malicious admin actions hide inside the Activity Log | Suspicious control-plane operations raise alerts |
| Attack-toolkit patterns are hard to recognize | Detections map to known cloud attack techniques |
| Compromised automation identities act freely | Anomalous principal behavior is flagged for response |
| Subscription-level risk has no dedicated owner | Alerts route to a defined control-plane response process |

**Value in one line:** it watches the one layer every cloud change flows through,
turning silent control-plane abuse into an actionable alert.

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

!!! note
    Resource Manager protection observes the Azure control plane. It does not
    replace workload-specific plans, Entra ID Protection, or privileged identity
    management.
