# Microsoft Defender for App Service Overview

<details markdown>
<summary>References</summary>

- [Defender for App Service overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-app-service-introduction)
- [Enable Defender for App Service](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-app-service-plan)
- [App Service security recommendations](https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-reference-app-services)

</details>

[Back to the documentation hub](../index.md)

Defender for App Service detects attacks against supported applications hosted
on Azure App Service by correlating platform and workload signals.

## Enable

1. Inventory App Service apps, APIs, deployment slots, plans, and environments.
2. Check operating system, hosting option, and region against current support.
3. In Defender for Cloud **Environment settings**, select the subscription.
4. Enable **App Service** under Defender plans and save.
5. Review recommendations for TLS, identity, authentication, networking, and secrets.
6. Route alerts to the application and security response owners.

## Verify and operate

- Confirm protected apps appear in Defender for Cloud inventory.
- Review recommendation and alert coverage after the documented activation time.
- Validate diagnostic settings and application telemetry needed for investigation.
- Keep deployment credentials out of source code and rotate exposed secrets.
- Test application containment and slot rollback procedures.

!!! note
    App Service plan support is specific. Azure Functions and other serverless
    hosting options can have different eligibility, telemetry, or protection.
    Check the current support matrix rather than assuming all PaaS apps are covered.
