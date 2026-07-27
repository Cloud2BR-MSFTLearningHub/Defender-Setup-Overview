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
authentication, password change, or access blocking.

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

> [!IMPORTANT]
> Entra ID Protection is related to the Microsoft security ecosystem but is not
> a Defender for Cloud workload plan. Avoid locking out administrators by moving
> directly from an untested policy to tenant-wide enforcement.
