# Microsoft Defender for IoT Overview

<details markdown>
<summary>References</summary>

- [Defender for IoT overview](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/overview)
- [Plan OT monitoring](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/plan-network-monitoring)
- [Enterprise IoT security](https://learn.microsoft.com/en-us/defender-for-iot/device-builder/overview)

</details>

[Back to the documentation hub](../index.md)

Microsoft Defender for IoT provides security visibility and threat detection for
operational technology (OT) networks. Enterprise IoT discovery and protection
can also use Defender for Endpoint capabilities on supported networks and devices.
OT and IoT devices are often unpatchable, long-lived, and invisible to IT tools,
which makes purpose-built, passive monitoring essential.

![Defender for IoT end-to-end coverage across OT and enterprise IoT](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/media/overview/end-to-end-coverage.png)

*Source: [Defender for IoT overview](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/overview).*

## Why enable it

You cannot protect devices you cannot see, and active scanning can disrupt
sensitive control systems. Defender for IoT uses passive, agentless monitoring to
build an OT asset inventory and detect threats without touching production traffic.

| Without Defender for IoT | With OT monitoring enabled |
| --- | --- |
| OT and IoT assets are undocumented | Passive discovery builds a device and network map |
| IT security tools miss industrial protocols | Protocol-aware detection understands OT traffic |
| Threats to control systems go unseen | Behavioral alerts flag anomalous OT activity |
| SOC has no visibility into the plant | Alerts integrate with the SOC and Defender XDR |

**Value in one line:** it makes the operational network visible and monitored
without risking the availability or safety of control systems.

## Configure OT monitoring

1. Inventory plants, network segments, protocols, safety constraints, and owners.
2. Design passive traffic collection with network and OT engineering teams.
3. Size and deploy supported OT network sensors without disrupting control traffic.
4. Define sensor management, updates, certificates, users, and backup procedures.
5. Connect supported cloud or Defender portal experiences when permitted.
6. Integrate alerts with the SOC while preserving plant-specific response authority.

## Verify and operate

- Compare discovered devices and communication maps with the OT asset inventory.
- Baseline maintenance windows, engineering stations, and expected protocols.
- Investigate alerts jointly with OT personnel before blocking or isolating assets.
- Monitor sensor packet visibility, health, time synchronization, and update status.
- Exercise incident procedures in a lab or approved maintenance window.

!!! danger "Caution"
    Do not run active scans, isolate devices, or change control-system traffic
    without OT safety review. Availability and physical safety take priority.
