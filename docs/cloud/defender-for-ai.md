# Microsoft Defender for AI Workloads Overview

<details markdown>
<summary>References</summary>

- [AI security in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security)
- [AI security posture management](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)
- [AI threat protection](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)
- [Enable AI threat protection](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding)

</details>

[Back to the documentation hub](../index.md)

Defender for Cloud addresses generative AI risk through two related capabilities:
AI security posture management discovers and evaluates AI workloads, while AI
threat protection detects supported runtime threats. As organizations ship AI
features quickly, new risks appear — exposed model endpoints, excessive data
access, and prompt-injection attacks — that traditional controls do not cover.

## Why enable it

AI applications combine models, data, identities, and plugins in ways that are
hard to inventory by hand, and a single exposed endpoint or over-privileged
connection can leak sensitive data. Defender maps the AI bill of materials and
watches supported workloads for active abuse.

| Without Defender for AI | With the capabilities enabled |
| --- | --- |
| AI components are undocumented and unmonitored | Posture management discovers models, endpoints, and data flows |
| Exposure and excessive permissions are invisible | Findings and attack paths highlight risky AI configurations |
| Prompt-injection and abuse go undetected | Runtime threat protection alerts on supported attacks |
| AI risk sits outside the security program | AI findings appear alongside the rest of cloud posture |

**Value in one line:** it brings fast-moving AI workloads under the same
discovery, posture, and threat-detection discipline as the rest of the cloud.

## How it works

AI security posture management extends Defender CSPM. Using agentless discovery, it
builds an AI bill of materials — models, endpoints, datastores, plugins, and the
identities connected to them — and evaluates that graph for risky configurations
and excessive access, surfacing the results as recommendations and attack paths
alongside the rest of your cloud posture.

AI threat protection adds runtime detection for supported generative-AI services.
By integrating with the application and Azure AI content-safety signals, it can
alert on prompt-injection attempts, credential theft, wallet abuse, and anomalous
data access. Because service names and availability change quickly, the current
support matrix is the authoritative source at deployment time.

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

## Architecture and prerequisites

- **Posture (AI-SPM):** part of Defender CSPM; agentless discovery inventories models, endpoints, datastores, plugins, and grounding data, then maps identity and network exposure into the cloud security graph.
- **Threat protection:** integrates with supported Azure AI and Azure OpenAI services and the Azure AI Content Safety prompt-shield signals to detect runtime attacks.
- **Prompt evidence:** optionally capture suspicious prompt segments in alerts (governed by privacy settings) to accelerate investigation.
- **Permissions:** Security Admin / Owner to enable; posture uses the CSPM identity while threat protection binds to the AI resource.

## Detections and mitigations

Representative alerts include detected prompt-injection or jailbreak attempts, access to an AI resource from a suspicious IP, credential leakage through a model, and denial-of-wallet spikes. Pair detection with preventive controls: Azure AI Content Safety, least-privilege managed identities for model data access, private networking for endpoints, and data governance on grounding sources. Because service coverage evolves, confirm supported services and regions in the current support matrix at deployment time.

!!! danger "Caution"
    AI plan names, eligible services, and availability are evolving quickly. Treat
    the support matrix and pricing page as authoritative at deployment time.
