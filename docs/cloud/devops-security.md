# DevOps Security in Microsoft Defender for Cloud

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Cloud connects source-control and pipeline environments so security
teams can see code-to-cloud context. Supported connectors include GitHub, Azure
DevOps, and GitLab, with capability differences documented by Microsoft.

## Enable

1. Inventory organizations, projects, groups, repositories, pipelines, and owners.
2. In Defender for Cloud **Environment settings**, add the DevOps connector.
3. Grant the minimum required authorization and select the intended scope.
4. Install or authorize required scanning components for the chosen platform.
5. Enable Defender CSPM when advanced code-to-cloud context is required.
6. Define ownership and service-level objectives for findings.

## Verify and operate

- Confirm repositories and their cloud-resource relationships appear in inventory.
- Verify infrastructure-as-code, secret, dependency, and container findings that
  are supported by the selected connector and licensing.
- Revoke test credentials immediately; never commit real secrets for validation.
- Send remediation to the repository owner and fix source before redeployment.
- Review connector permissions, inactive repositories, and coverage drift.

> [!NOTE]
> A DevOps connector does not protect a running workload by itself. Enable the
> appropriate workload plan for runtime detection and response.

## References

- [Defender for Cloud DevOps security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction)
- [Connect GitHub](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-github)
- [Connect Azure DevOps](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-devops)
- [Connect GitLab](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-gitlab)
