# Microsoft Sentinel and Defender Integration

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Microsoft Sentinel is Microsoft's cloud-native SIEM and SOAR. Defender products
generate specialized detections and response context; Sentinel combines those
signals with Microsoft and third-party data for broader analytics and automation.

![Microsoft Sentinel incident investigation graph showing related security entities](https://learn.microsoft.com/en-us/azure/sentinel/media/overview/map-timeline.png)

*Source: [Microsoft Sentinel overview](https://learn.microsoft.com/en-us/azure/sentinel/overview).* 

## Decide the incident owner

Choose whether Defender XDR or Sentinel is the primary incident queue. Avoid
parallel ownership, duplicate tickets, and automation that closes or reopens the
same incident in a loop.

## Configure

1. Define use cases, retention, data residency, roles, and a cost budget.
2. Onboard Sentinel to the appropriate Microsoft Defender portal or workspace architecture.
3. Configure the supported Microsoft Defender solution and data connectors.
4. Select incident integration and alert synchronization behavior deliberately.
5. Add analytics rules only when the native Defender detection does not meet the need.
6. Create automation rules and least-privilege Logic App playbooks.

## Verify and operate

- Confirm a test Defender alert arrives once with the expected entities and severity.
- Verify incident status and owner synchronization in both experiences.
- Check hunting data availability, timestamps, and retention.
- Measure ingestion by table and remove unused high-volume data.
- Test playbook approval, failure handling, rollback, and audit records.
- Document which portal analysts use for each response action.

> [!IMPORTANT]
> Sending duplicate raw telemetry and alerts can add cost without adding detection
> value. Build integrations from explicit use cases and retention requirements.

## References

- [Microsoft Sentinel overview](https://learn.microsoft.com/en-us/azure/sentinel/overview)
- [Connect Microsoft Defender XDR](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender)
- [Sentinel in the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal)
- [Sentinel cost planning](https://learn.microsoft.com/en-us/azure/sentinel/billing-reduce-costs)
