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
services and account types. Because storage accounts hold backups, application
data, and shared content, they are a frequent target for exfiltration and a
common delivery point for malware.

![How Defender for Storage protects data against common threats](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-storage-introduction/defender-for-storage-benefits.png)

*Source: [Overview of Defender for Storage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-storage-introduction).*

## Why enable it

A single malicious upload or a leaked SAS token can turn a storage account into
a malware host or a data-loss event. Defender for Storage watches access patterns
with Microsoft threat intelligence and can block malware at upload time, without
changing how applications read and write data.

| Without Defender for Storage | With the plan enabled |
| --- | --- |
| Suspicious access is only visible in raw logs | Threat intelligence flags anomalous and malicious activity |
| Uploaded files are trusted implicitly | Optional on-upload malware scanning blocks known-bad files |
| Sensitive-data exposure is discovered late | Sensitive-data threat detection prioritizes high-value accounts |
| SAS and key abuse is hard to spot | Alerts highlight unusual token and key usage |

**Value in one line:** it stops storage from becoming a quiet path for malware
delivery and data theft, while keeping normal application access unchanged.

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
