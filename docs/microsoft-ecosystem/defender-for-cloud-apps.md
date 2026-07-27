# Microsoft Defender for Cloud Apps Overview

<details markdown>
<summary>References</summary>

- [Defender for Cloud Apps overview](https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps)
- [Deployment guide](https://learn.microsoft.com/en-us/defender-cloud-apps/general-setup)
- [Connect apps](https://learn.microsoft.com/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps)
- [Conditional Access App Control](https://learn.microsoft.com/en-us/defender-cloud-apps/proxy-intro-aad)

</details>

[Back to the documentation hub](../index.md)

Defender for Cloud Apps is a cross-SaaS security solution for discovering cloud
use, assessing application risk, protecting connected applications, and applying
session and access controls with Microsoft Entra Conditional Access.

![Microsoft Defender for Cloud Apps pillars: CASB, SSPM, XDR, and app governance](https://learn.microsoft.com/en-us/defender-cloud-apps/media/overview/defender-for-cloud-apps-pillars.png)

*Source: [Microsoft Defender for Cloud Apps overview](https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps).* 

## Why enable it

Employees adopt SaaS apps faster than security can review them, and sensitive data
quietly spreads across tools nobody sanctioned. Defender for Cloud Apps reveals
that shadow IT, scores each app's risk, and can control risky sessions and OAuth
grants in real time.

| Without Defender for Cloud Apps | With it enabled |
| --- | --- |
| Shadow IT usage is unknown | Cloud Discovery reveals apps in use and their risk |
| Risky OAuth grants persist unnoticed | App Governance flags and controls OAuth apps |
| SaaS activity has no unified audit | Connectors provide activity logs and anomaly detection |
| Access is all-or-nothing | Conditional Access App Control governs sessions live |

**Value in one line:** it turns invisible SaaS sprawl into a governed, monitored
estate with real-time control over risky access and data movement.

## How it works

Defender for Cloud Apps operates as a cloud access security broker. Cloud Discovery
analyzes traffic logs — often from Defender for Endpoint — to reveal which SaaS
apps are in use and score each app's risk, exposing shadow IT. App connectors then
use the APIs of sanctioned apps to pull activity logs, detect anomalies, and apply
file and governance policies.

For real-time control, Conditional Access App Control routes sessions through a
reverse proxy so actions such as download or copy can be inspected and blocked as
they happen, and App Governance monitors OAuth applications for risky permissions
and behavior. Its signals also flow into Defender XDR.

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
