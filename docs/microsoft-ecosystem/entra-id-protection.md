# Microsoft Entra ID Protection Overview

<details markdown>
<summary>References</summary>

- [Entra ID Protection overview](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection)
- [Risk policies](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)
- [Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)

</details>

[Back to the documentation hub](../index.md)

Microsoft Entra ID Protection detects and reports risky users, risky sign-ins,
and risk detections. Conditional Access can use that risk to require secure
authentication, password change, or access blocking. It applies Microsoft's
signal from trillions of authentications to spot compromised identities in real time.

![Microsoft Entra ID Protection risk overview](https://learn.microsoft.com/en-us/entra/id-protection/media/overview-identity-protection/identity-protection-overview.png)

*Source: [What is Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection).*

## Why enable it

Stolen credentials are the most common way into a tenant, and static rules cannot
tell a legitimate sign-in from an attacker using the right password. ID Protection
scores risk continuously and lets Conditional Access respond automatically —
prompting for MFA, forcing a password reset, or blocking access.

| Without Entra ID Protection | With risk policies enabled |
| --- | --- |
| Compromised sign-ins look legitimate | Risk scoring flags anomalous and leaked-credential logins |
| Response to account risk is manual | Conditional Access auto-remediates risky sign-ins |
| Risky users are found after damage | Ongoing user-risk detection surfaces them early |
| Identity risk is disconnected from the SOC | Risk events feed Defender XDR and Sentinel |

**Value in one line:** it automatically challenges or blocks compromised sign-ins
the moment risk appears, closing the most common path into the tenant.

## How it works

Entra ID Protection scores risk from Microsoft's view of trillions of
authentications. Real-time and offline detections evaluate each sign-in and user
for signals such as impossible travel, anonymized IP addresses, password spray, and
leaked credentials, producing a sign-in risk level and a user risk level.

Conditional Access consumes that risk to respond automatically: a risky sign-in can
be challenged with multifactor authentication, a risky user can be forced to reset
a password, and high risk can be blocked outright. The recommended pattern is to
roll policies out in report-only mode first, exclude emergency-access accounts, and
feed the risk events into Defender XDR or Sentinel for investigation.

## Configure

1. Confirm Microsoft Entra licensing, roles, emergency accounts, and user scope.
2. Require multifactor authentication registration through an approved policy.
3. Create user-risk and sign-in-risk Conditional Access policies in report-only mode.
4. Exclude emergency access accounts and account for service identities correctly.
5. Review impact, then move policies to enforcement through staged groups.
6. Integrate risk events with Defender XDR, Sentinel, or case management as needed.

## Verify and operate

- Monitor risky users, risky sign-ins, and risk-detection investigation status.
- Validate Conditional Access results with the What If tool and sign-in logs.
- Test self-service password reset and secure account recovery.
- Investigate risk with endpoint, email, identity, and cloud-app evidence.
- Review exclusions and emergency account health on a fixed schedule.

!!! warning "Important"
    Entra ID Protection is related to the Microsoft security ecosystem but is not
    a Defender for Cloud workload plan. Avoid locking out administrators by moving
    directly from an untested policy to tenant-wide enforcement.
