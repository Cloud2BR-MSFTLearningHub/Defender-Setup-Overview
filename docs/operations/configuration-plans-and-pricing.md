# Configure Microsoft Defender Plans, Tiers, and Pricing

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Use this reference before enabling a Defender plan. Product capabilities,
resource eligibility, regional availability, and prices can vary by plan,
cloud, resource type, and licensing agreement.

## Configure a Defender for Cloud plan

1. Open [Microsoft Defender for Cloud](https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/~/1).
2. Select **Environment settings**, then select the subscription, management
   group, AWS account, or GCP project hierarchy that owns the resources.
3. Open **Defender plans**, choose the required plan, and review its included
   capabilities and billed components.
4. Select **Settings & monitoring** to configure supported extensions, data
   collection, agentless scanning, Defender for Endpoint integration, and
   monitoring options.
5. Save the change, verify the plan state, and confirm coverage before applying
   the same setting to a broader scope.

For the current portal workflow and plan-management prerequisites, use
[Enable enhanced security features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security).

## Choose the plan or tier

| Decision | Use this source |
| --- | --- |
| Compare Defender for Cloud workload plans, prerequisites, and supported resources | [Defender for Cloud support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud) |
| Compare Defender for Servers Plan 1 and Plan 2 | [Plan Defender for Servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers) |
| Decide whether foundational CSPM or Defender CSPM is required | [CSPM in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) |
| Confirm Microsoft 365 and Defender XDR license entitlements | [Microsoft 365 service descriptions](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-service-descriptions) |

## Check regional availability and eligibility

Before enabling a plan, use the [Defender for Cloud support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud) to verify the resource type, cloud, region, operating system, and required extension or connector. For AWS and Google Cloud, also confirm connector permissions and supported service regions before a pilot.

## Estimate and monitor cost

Use live pricing and actual resource counts rather than documentation examples:

- [Defender for Cloud pricing](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)
- [Defender for Cloud cost calculator](https://learn.microsoft.com/en-us/azure/defender-for-cloud/cost-calculator)
- [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/)
- [Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview)

Capture the selected plan, scope, billing meter, region, resource count, and
assumptions in the deployment record. Review the estimate after the pilot using
actual charges, then establish budgets and anomaly alerts before broad rollout.

## Related guidance

- [Licensing and cost planning](licensing-and-cost.md)
- [Deployment checklist](deployment-checklist.md)
- [Defender for Servers](../cloud/defender-for-servers.md)
- [Defender CSPM](../cloud/defender-cspm.md)
