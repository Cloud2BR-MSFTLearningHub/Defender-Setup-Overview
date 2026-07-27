# Microsoft Defender Setup and Overview Hub

Last updated: 2026-07-27

<details markdown>
<summary>References</summary>

- [Microsoft Defender documentation](https://learn.microsoft.com/en-us/defender/)
- [Microsoft Defender for Cloud overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Microsoft Defender XDR overview](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender)

</details>

<div class="defender-hero" markdown>

<p class="defender-hero__eyebrow">Cloud2BR OSS - Learning Hub</p>

Microsoft Defender is a security portfolio, not a single switch. Use this hub
to choose the right protection for cloud workloads, devices, identities, data,
and security operations.

</div>

<div class="guide-grid">
  <a class="guide-card" href="00-overview/">
    <span class="guide-card__label">Start here</span>
    <h2>What is Microsoft Defender?</h2>
    <p>Understand the boundaries between Defender for Cloud, Defender XDR, Sentinel, and enforcement tools.</p>
  </a>
  <a class="guide-card" href="cloud/defender-cspm/">
    <span class="guide-card__label">Cloud posture</span>
    <h2>Defender CSPM</h2>
    <p>Discover cloud risk, assess configuration, and prioritize remediation across Azure, AWS, and GCP.</p>
  </a>
  <a class="guide-card" href="cloud/defender-for-containers/">
    <span class="guide-card__label">Workload protection</span>
    <h2>Defender for Containers</h2>
    <p>Secure AKS, Arc-enabled Kubernetes, registries, and supported multicloud container estates.</p>
  </a>
  <a class="guide-card" href="cloud/defender-for-servers/">
    <span class="guide-card__label">Workload protection</span>
    <h2>Defender for Servers</h2>
    <p>Plan detection and response for Windows and Linux across Azure, hybrid, and multicloud environments.</p>
  </a>
  <a class="guide-card" href="microsoft-ecosystem/defender-xdr/">
    <span class="guide-card__label">Security operations</span>
    <h2>Microsoft Defender XDR</h2>
    <p>Correlate endpoint, identity, email, cloud app, and cloud workload signals into unified incidents.</p>
  </a>
  <a class="guide-card" href="operations/deployment-checklist/">
    <span class="guide-card__label">Deployment</span>
    <h2>Deployment checklist</h2>
    <p>Use a structured path for licensing, pilot scope, verification, response ownership, and rollout.</p>
  </a>
  <a class="guide-card" href="operations/configuration-plans-and-pricing/">
    <span class="guide-card__label">Planning</span>
    <h2>Configure plans and pricing</h2>
    <p>Compare Defender plans and tiers, check regional support, configure settings, and estimate cost.</p>
  </a>
</div>

## Browse by environment

| Environment | Recommended starting point |
| --- | --- |
| Azure | Use the **Defender for Cloud** navigation section for workload-specific plans. |
| AWS and Google Cloud | [Multicloud and hybrid guidance](multicloud/aws.md) |
| On-premises and other clouds | [Azure Arc onboarding](multicloud/hybrid-and-other-clouds.md) |
| Microsoft 365 and SaaS | Use the **Microsoft Ecosystem** navigation section. |

## Configure and estimate

Before a pilot, use the [configuration, plans, and pricing reference](operations/configuration-plans-and-pricing.md) to configure Defender settings, compare tiers, verify regional eligibility, and open current pricing and cost-calculation tools.

## Use the Guides

Start with the overview to establish product boundaries, then select the guide
that owns the asset or identity you need to protect. Each guide follows the same
operating sequence: define scope and ownership, confirm support and licensing,
enable a controlled pilot, verify telemetry and response, then expand with
evidence-backed controls. Use the deployment checklist to record the decision,
the operations guides to establish governance and automation, and the product
guides to define service-specific prevention and response actions.

<p class="site-note">Layout and palette follow the Cloud2BR TEC academy pattern. The header icon and favicon use the public Cloud2BR OSS - Learning Hub organization avatar.</p>
