# Microsoft Defender for APIs Overview

<details markdown>
<summary>References</summary>

- [Defender for APIs overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction)
- [Enable Defender for APIs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-deploy)
- [Defender for APIs support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-apis)

</details>

[Back to the documentation hub](../index.md)

Defender for APIs adds security posture and runtime threat detection for
eligible APIs managed through supported Azure API Management tiers and regions.

## Enable

1. Inventory API Management services, APIs, revisions, backends, and data owners.
2. Check API Management tier, region, protocol, and API eligibility.
3. Enable the **APIs** plan in Defender for Cloud at subscription scope.
4. In Defender for Cloud API security, onboard the selected eligible APIs.
5. Prioritize sensitive and internet-facing production APIs within plan capacity.
6. Review authentication, authorization, rate limits, schemas, and backend access.

## Verify and operate

- Confirm onboarded APIs appear in the API inventory with recent traffic data.
- Review recommendations and runtime alerts after the learning period.
- Keep owner, sensitivity, exposure, and business-criticality metadata current.
- Correlate API alerts with API Management, application, identity, and WAF logs.
- Test key revocation, backend isolation, and safe API rollback.

!!! warning "Important"
    Enabling the subscription plan and onboarding individual APIs are distinct
    steps. Unsupported or discovered APIs are not automatically protected.
