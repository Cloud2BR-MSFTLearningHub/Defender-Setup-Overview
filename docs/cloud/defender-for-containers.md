# Microsoft Defender for Containers Overview

<details markdown>
<summary>References</summary>

- [Defender for Containers overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-introduction)
- [Containers architecture](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-architecture)
- [Containers support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-containers)
- [Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview)

</details>

[Back to the documentation hub](../index.md)

Defender for Containers provides posture management, registry image
vulnerability assessment, and runtime threat protection for supported
Kubernetes environments.

![Microsoft Defender for Containers architecture for an Arc-enabled Kubernetes cluster](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-containers/architecture-arc-cluster.png)

*Source: [Microsoft Defender for Containers architecture](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-architecture).* 

## Where it applies

| Environment | Connection model |
| --- | --- |
| Azure Kubernetes Service (AKS) | Native Azure resource integration |
| Azure Red Hat OpenShift (ARO) | Connect the cluster through Azure Arc for supported runtime coverage |
| Amazon EKS | AWS connector and selected Defender components |
| Google GKE | GCP connector and selected Defender components |
| Other conformant Kubernetes | Azure Arc-enabled Kubernetes, subject to the support matrix |

## Enable

1. Confirm cluster distribution, version, operating systems, and network egress.
2. Connect non-native clusters with the appropriate cloud connector or Azure Arc.
3. Enable Defender for Containers in **Environment settings**.
4. Review settings for agentless discovery, registry assessment, Azure Policy,
   and the Defender sensor; enable only supported components.
5. Confirm extension pods can be scheduled and reach required endpoints.
6. Define admission policy separately if deployments must be blocked.

## Verify and operate

- Check cluster, node, registry, image, and extension health in inventory.
- Confirm new images receive vulnerability results within the documented period.
- Review runtime alerts and Kubernetes audit-data availability.
- Track privileged workloads, exposed services, vulnerable images, and stale data.
- Test response actions in a non-production namespace.

!!! note
    Defender recommends and detects; Azure Policy for Kubernetes, Gatekeeper, or
    another admission controller performs preventive enforcement. ARO's managed
    control plane also limits which components customers can directly manage.
