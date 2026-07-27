# Microsoft Defender CSPM Overview

<details markdown>
<summary>References</summary>

- [CSPM in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management)
- [Enable Defender CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-cspm-plan)
- [Security recommendations](https://learn.microsoft.com/en-us/azure/defender-for-cloud/review-security-recommendations)
- [Attack path analysis](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-attack-path)
- [Configuration, plans, and pricing](../operations/configuration-plans-and-pricing.md)

</details>

[Back to the documentation hub](../index.md)

Cloud Security Posture Management (CSPM) discovers resources, evaluates their
configuration, and prioritizes security risk across Azure, AWS, and GCP. It
answers three questions continuously: what do I have, how is it exposed, and
what should I fix first. Foundational CSPM is free and turned on for every
connected environment; Defender CSPM adds the context that separates a long list
of findings from an actionable, risk-ranked plan.

![Defender for Cloud security posture and secure score dashboard](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/secure-score-security-controls/security-posture-page.png)

*Source: [Secure score in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls).*

## Why enable it

Most cloud incidents begin with a preventable misconfiguration: a public storage
container, an over-permissioned identity, or an internet-exposed management port.
CSPM finds that risk before an attacker does and shows the shortest path to fix it.

| Without CSPM | With Defender CSPM enabled |
| --- | --- |
| Misconfigurations surface manually or during an incident | Continuous assessment flags risky configurations automatically |
| Findings are a flat list with no clear starting point | Attack paths and risk prioritization rank the exposures that matter |
| Multicloud posture is scattered across consoles | Azure, AWS, and GCP posture is unified in one secure score |
| Progress is hard to prove to leadership | Secure score trends quantify risk reduction over time |

**Value in one line:** CSPM converts thousands of raw findings into a ranked,
measurable remediation plan that shrinks the attack surface before it is exploited.

## How it works

CSPM does not need agents to start. When you connect an Azure subscription, an AWS
account, or a GCP project, Defender for Cloud reads the cloud provider's own APIs
to build an inventory and continuously compares every resource against the
Microsoft Cloud Security Benchmark and any regulatory standards you assign. Each
gap becomes a recommendation, each recommendation affects the secure score, and
the score gives you one percentage to track and report over time.

Defender CSPM adds a graph on top of that inventory. Agentless scanning takes a
point-in-time snapshot of disks, identities, and configurations without installing
anything, and the cloud security graph links those facts together. Cloud Security
Explorer lets you query the graph — for example, "internet-exposed VMs with a
known vulnerability and a path to sensitive data" — and attack path analysis walks
the graph automatically to show the chained steps an attacker could take from
exposure to impact.

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

![Attack path analysis linking an exposed resource to sensitive data](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/concept-cloud-map/attack-path.png)

*Source: [Attack path analysis](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-attack-path).*

!!! note
    CSPM identifies risk; workload plans add threat detection. Enabling Defender
    CSPM does not automatically enable every Defender workload protection plan.
