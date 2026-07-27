# Microsoft Defender for Cloud Apps Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Cloud Apps is a cross-SaaS security solution for discovering cloud
use, assessing application risk, protecting connected applications, and applying
session and access controls with Microsoft Entra Conditional Access.

![Microsoft Defender for Cloud Apps pillars: CASB, SSPM, XDR, and app governance](https://learn.microsoft.com/en-us/defender-cloud-apps/media/overview/defender-for-cloud-apps-pillars.png)

*Source: [Microsoft Defender for Cloud Apps overview](https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps).* 

## Capability map

| Need | Capability |
| --- | --- |
| Discover shadow IT | Cloud Discovery from network or endpoint signals |
| Investigate SaaS activity | App connectors, activity logs, and anomaly detection |
| Govern OAuth applications | App Governance and OAuth app controls |
| Control sessions in real time | Conditional Access App Control |
| Protect files and data | File policies and Microsoft Purview integrations |

## Configure

1. Confirm licensing, supported apps, privacy, and administrator roles.
2. Integrate Defender for Endpoint or upload supported traffic logs for discovery.
3. Connect sanctioned SaaS apps with least-privilege connectors.
4. Define app risk, activity, anomaly, OAuth, and file policies.
5. Pilot Conditional Access App Control with report-only policies first.
6. Assign owners for unsanctioned apps and risky OAuth grants.

## Verify and operate

- Confirm discovery data and connector status are current.
- Review false positives before enabling automated governance actions.
- Test session controls with emergency access accounts excluded appropriately.
- Reauthorize expiring connectors and remove abandoned integrations.

## References

- [Defender for Cloud Apps overview](https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps)
- [Deployment guide](https://learn.microsoft.com/en-us/defender-cloud-apps/general-setup)
- [Connect apps](https://learn.microsoft.com/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps)
- [Conditional Access App Control](https://learn.microsoft.com/en-us/defender-cloud-apps/proxy-intro-aad)
