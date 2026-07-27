# Microsoft Defender for Endpoint Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Endpoint is Microsoft's enterprise endpoint security platform for
prevention, endpoint detection and response, investigation, and remediation.
It supports eligible Windows, macOS, Linux, Android, and iOS platforms.

## Deployment paths

| Device group | Common management path |
| --- | --- |
| Windows clients | Microsoft Intune, Configuration Manager, Group Policy, or script |
| Windows and Linux servers | Defender for Servers integration or direct onboarding |
| macOS and Linux clients | Intune or supported third-party management tooling |
| Android and iOS | Intune mobile threat defense integration |

## Configure

1. Choose Plan 1, Plan 2, Defender for Business, or another eligible license.
2. Review platform versions, network endpoints, coexistence, and data residency.
3. Define pilot device groups and role-based access.
4. Deploy onboarding and security settings through the management authority.
5. Configure attack surface reduction, EDR, cloud protection, and tamper protection.
6. Integrate Intune, Defender for Cloud, and Sentinel only as needed.

## Verify and operate

- Confirm device inventory, sensor health, antivirus mode, and last-seen time.
- Run Microsoft's documented detection test on an approved test device.
- Validate isolation, live response, evidence collection, and rollback authority.
- Track unmanaged devices, exposure score, vulnerabilities, and stale sensors.

## References

- [Defender for Endpoint overview](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint)
- [Plan deployment](https://learn.microsoft.com/en-us/defender-endpoint/mde-planning-guide)
- [Minimum requirements](https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements)
- [Pilot and deploy](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-defender-endpoint)
