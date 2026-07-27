# Microsoft Defender for Business Overview

<details markdown>
<summary>References</summary>

- [Defender for Business overview](https://learn.microsoft.com/en-us/defender-business/mdb-overview)
- [Set up Defender for Business](https://learn.microsoft.com/en-us/defender-business/mdb-setup-configuration)
- [Device onboarding](https://learn.microsoft.com/en-us/defender-business/mdb-onboard-devices)

</details>

[Back to the documentation hub](../index.md)

Microsoft Defender for Business delivers endpoint protection for small and
medium-sized organizations. It can be licensed separately or included in
eligible Microsoft 365 Business Premium subscriptions. It packages enterprise-grade
endpoint security into a simplified, guided experience sized for lean IT teams.

![Microsoft Defender for Business capabilities overview](https://learn.microsoft.com/en-us/defender-business/media/mdb-offering-overview.png)

*Source: [What is Microsoft Defender for Business](https://learn.microsoft.com/en-us/defender-business/mdb-overview).*

## Why enable it

Smaller organizations face the same ransomware and phishing threats as large
enterprises but rarely have a dedicated security team. Defender for Business
delivers next-generation antivirus, EDR, and automated remediation with defaults
and guided setup so protection does not require a specialist.

| Without Defender for Business | With it enabled |
| --- | --- |
| Consumer antivirus with limited response | Enterprise-grade EDR with automated remediation |
| Security requires deep expertise | Guided setup and secure defaults do the heavy lifting |
| Threats are handled reactively | Automated investigation contains common attacks |
| Devices are managed inconsistently | Central portal covers Windows, macOS, and mobile |

**Value in one line:** it gives small teams enterprise-class endpoint detection
and automated response without needing a dedicated security operations center.

## How it works

Defender for Business packages the Defender for Endpoint engine — next-generation
antivirus, attack surface reduction, and behavioral EDR — into a streamlined
experience with security-hardened defaults and a guided setup wizard, so protection
is effective without deep configuration. Devices are onboarded through Microsoft
Intune or a simple local script across Windows, macOS, iOS, and Android.

Automated investigation and response handles common threats without analyst
intervention, and threat and vulnerability management highlights the weaknesses
that matter most. Servers can be added through a per-server add-on, and the same
portal and incidents scale up if the organization later moves to enterprise
Defender plans.

## Configure

1. Confirm tenant eligibility, user and server limits, and included licenses.
2. Complete the guided setup in the Microsoft Defender portal.
3. Onboard a pilot set of Windows, macOS, Linux, Android, or iOS devices that
   meet the current platform requirements.
4. Review default next-generation protection, firewall, and attack-surface settings.
5. Integrate Intune when available and define device groups and roles.
6. Purchase and assign server coverage separately when required.

## Verify and operate

- Confirm every intended device appears and reports healthy sensor status.
- Run the documented Defender for Endpoint detection test on a test device.
- Review incidents, vulnerabilities, and automated remediation actions.
- Maintain emergency contacts and an isolation recovery procedure.
- Reassess licensing when organization size or security needs grow.

!!! note
    Defender for Business is not Defender for Cloud. Servers can be protected
    through a Defender for Business server add-on or through Defender for Servers,
    depending on architecture and licensing.
