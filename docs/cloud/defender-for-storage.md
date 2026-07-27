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

## How it works

Defender for Storage analyzes the control-plane and data-plane telemetry that
every storage account already emits, comparing it against Microsoft threat
intelligence and behavioral models to spot anomalies such as access from a Tor
exit node, unusual data extraction, or use of a leaked SAS token. This activity
monitoring needs no agent and never sits in the data path, so it does not slow
reads or writes.

When you enable on-upload malware scanning, each uploaded blob is scanned by the
Microsoft anti-malware engine and the result is surfaced as a blob index tag and
an Event Grid event your application can act on. Sensitive-data threat detection
adds weight to accounts that Microsoft Purview has flagged as holding sensitive
information, so the highest-value data receives the closest attention.

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

## Architecture and prerequisites

![How Defender for Storage activity monitoring identifies threats to data](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-storage-introduction/activity-monitoring.png)

*Source: [Overview of Defender for Storage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-storage-introduction).*

- **Activity monitoring:** analyzes the storage account's control-plane and data-plane operations from the Azure resource-logs pipeline; it is agentless and adds no data-path latency.
- **On-upload malware scanning:** an in-account engine inspects each new blob, writes the result as a blob index tag, and emits an Event Grid event; a per-account monthly cap protects cost.
- **Sensitive-data threat detection:** uses Defender CSPM sensitive-data context (Microsoft Purview) to weight alerts on accounts holding regulated data.
- **Scope model:** enable at subscription level for inheritance or override per storage account; malware scanning and sensitive-data detection are independent toggles.
- **Permissions:** Security Admin / Owner to enable; scanning components use a system-assigned managed identity granted data access to the protected accounts.

## Detections and response

Representative alerts include access from a Tor exit node or suspicious IP, an unusual volume of data extraction, upload of a known-malicious blob, and anomalous SAS-token usage. Wire malware-scan Event Grid events to a Logic App or Function to quarantine or delete flagged blobs automatically, and export alerts to Sentinel through the `SecurityAlert` table for correlation.

!!! warning "Important"
    Malware scanning is not a substitute for access control, private networking,
    soft delete, versioning, backups, or data-loss prevention.
