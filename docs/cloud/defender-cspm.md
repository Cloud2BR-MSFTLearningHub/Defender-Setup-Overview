# Microsoft Defender CSPM Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Cloud Security Posture Management (CSPM) discovers resources, evaluates their
configuration, and prioritizes security risk across Azure, AWS, and GCP.

## Plans

| Plan | Main capabilities |
| --- | --- |
| [Foundational CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) | Asset inventory, security recommendations, secure score, and Microsoft Cloud Security Benchmark |
| [Defender CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) | Attack paths, cloud security explorer, governance, risk prioritization, agentless scanning, and data or AI context where supported |

## Enable

1. In Defender for Cloud, open [Environment settings](https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/~/1).
2. Select the Azure subscription, AWS account, or GCP project hierarchy.
3. Turn on **Defender CSPM** when advanced capabilities are required.
4. Open **Settings & monitoring** and review each extension and its dependencies.
5. Assign standards and regulatory initiatives at the correct management scope.
6. Exempt resources only with an owner, justification, and expiration date.

## Verify and operate

- Confirm inventory is complete and recommendations have populated.
- Review secure score by control, but prioritize findings by exploitable risk.
- Validate agentless scanning coverage, permissions, [region support](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud), and freshness.
- Assign governance owners and remediation due dates.
- Use Cloud Security Explorer and attack paths to investigate exposure chains.

> [!NOTE]
> CSPM identifies risk; workload plans add threat detection. Enabling Defender
> CSPM does not automatically enable every Defender workload protection plan.

## References

- [CSPM in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management)
- [Enable Defender CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-cspm-plan)
- [Security recommendations](https://learn.microsoft.com/en-us/azure/defender-for-cloud/review-security-recommendations)
- [Attack path analysis](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-attack-path)
- [Configuration, plans, and pricing](../operations/configuration-plans-and-pricing.md)
