# Microsoft Defender for Storage Overview

<details markdown>
<summary>References</summary>

- [Defender for Storage overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-storage-introduction)
- [Deploy Defender for Storage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-storage-plan)
- [On-upload malware scanning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/on-upload-malware-scanning)
- [Storage support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-storage)

</details>

[Back to the documentation hub](../index.md)

Defender for Storage detects storage-specific threats and can add on-upload
malware scanning and sensitive-data threat detection for supported Azure Storage
services and account types.

## Protect

- Blob Storage and Azure Data Lake Storage workloads supported by the plan.
- Suspicious access patterns, exfiltration, malicious uploads, and SAS misuse.
- Sensitive data context and malware scanning when those options are enabled.

## Enable

1. Inventory storage accounts, transaction volume, data sensitivity, and owners.
2. Choose subscription-wide enablement or resource-level configuration.
3. Enable Defender for Storage and explicitly review malware scanning and
   sensitive-data threat detection settings.
4. Set malware-scanning caps and cost controls appropriate to ingestion volume.
5. Configure Event Grid or workflow handling if applications consume scan results.
6. Exclude trusted paths only after documenting the resulting risk.

## Verify and operate

- Confirm each intended account reports the current plan status.
- Use Microsoft's harmless malware-scanning validation procedure in a test account.
- Verify scan-result delivery and application behavior for malicious files.
- Monitor scan failures, throttling, transaction anomalies, and cost.
- Do not expose test files or production data during validation.

!!! warning "Important"
   Malware scanning is not a substitute for access control, private networking,
   soft delete, versioning, backups, or data-loss prevention.
