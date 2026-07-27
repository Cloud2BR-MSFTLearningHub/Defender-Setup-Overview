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

> [!NOTE]
> Connecting an organization does not imply that every GCP service receives
> runtime protection. CSPM breadth and workload-plan support are different.
