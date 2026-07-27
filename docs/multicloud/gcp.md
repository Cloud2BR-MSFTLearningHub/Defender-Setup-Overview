# Microsoft Defender for Cloud on Google Cloud

<details markdown>
<summary>References</summary>

- [Connect GCP projects](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-gcp)
- [GCP security features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-gcp)
- [Multicloud planning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-multicloud-security-get-started)
- [Defender for Containers on GCP](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-container-gcp)

</details>

[Back to the documentation hub](../index.md)

Defender for Cloud connects Google Cloud organizations or projects to provide
cloud posture management and selected workload protections for supported GCP
resources.

![Selecting Defender plans while onboarding a GCP project](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/quickstart-onboard-gcp/select-plans.png)

*Source: [Connect your GCP projects to Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-gcp).*

## Why enable it

Google Cloud projects proliferate quickly and often sit outside the central
security program. A GCP connector applies the same benchmark, posture analysis,
and workload protection you use elsewhere, so multicloud does not mean multi-blind-spot.

| Without a GCP connector | With GCP connected |
| --- | --- |
| GCP risk is measured in a separate tool | GCP posture joins one unified secure score |
| Project sprawl hides ungoverned resources | Discovery inventories projects and resources centrally |
| Compute Engine and GKE use isolated tooling | Defender for Servers and Containers extend to GCP |
| Findings lack cross-cloud context | Attack paths and explorer span clouds |

**Value in one line:** it folds Google Cloud into the same posture and threat
model as Azure and AWS, so risk is compared on one scale.

## Typical coverage

- Foundational CSPM and recommendations mapped to multicloud standards.
- Defender CSPM inventory, attack-path, and agentless capabilities where supported.
- Defender for Servers coverage for eligible Compute Engine machines.
- Defender for Containers coverage for eligible GKE and Artifact Registry resources.
- Additional protection only when listed in the current GCP support matrix.

## Connect

1. Decide whether to connect a GCP organization or selected projects.
2. In Defender for Cloud **Environment settings**, create a GCP connector.
3. Select plans and inspect required Google Cloud and Azure permissions.
4. Run the provided onboarding script or deployment in the intended GCP scope.
5. Configure optional agentless, server, and container components.
6. Compare discovered projects and resources with Cloud Asset Inventory.

## Verify and operate

- Confirm connector health, project coverage, regions, and scan freshness.
- Verify service accounts, workload identity federation, and required APIs.
- Review GCP API usage, data handling, and Defender plan charges.
- Route findings to the correct project and workload owner.
- Monitor newly created projects and organization-policy changes for drift.

!!! note
    Connecting an organization does not imply that every GCP service receives
    runtime protection. CSPM breadth and workload-plan support are different.
