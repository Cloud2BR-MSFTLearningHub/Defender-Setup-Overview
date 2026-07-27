# Microsoft Defender for AI Workloads Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Cloud addresses generative AI risk through two related capabilities:
AI security posture management discovers and evaluates AI workloads, while AI
threat protection detects supported runtime threats.

## Capability map

| Need | Capability |
| --- | --- |
| Discover an AI bill of materials and risky configurations | AI security posture management in Defender CSPM |
| Relate exposed AI components to attack paths | Defender CSPM cloud security graph |
| Detect attacks against supported AI applications | Defender for AI Services or current AI threat-protection plan |

## Enable

1. Inventory models, endpoints, data sources, plugins, agents, and identities.
2. Check the current supported services, regions, models, and preview conditions.
3. Enable Defender CSPM and required agentless capabilities for posture coverage.
4. Enable the current AI threat-protection plan for eligible resources.
5. Apply content safety, least privilege, private networking, and data governance.
6. Assign application, model, data, and incident owners.

## Verify and operate

- Confirm AI assets and dependencies appear in inventory and attack paths.
- Review findings for exposed endpoints, sensitive data, and excessive permissions.
- Validate runtime telemetry without sending secrets or regulated data in tests.
- Monitor prompt attacks, abusive use, credential theft, and data-access anomalies.
- Recheck coverage whenever models, regions, or architectures change.

> [!CAUTION]
> AI plan names, eligible services, and availability are evolving quickly. Treat
> the support matrix and pricing page as authoritative at deployment time.

## References

- [AI security in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security)
- [AI security posture management](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)
- [AI threat protection](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)
- [Enable AI threat protection](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding)
