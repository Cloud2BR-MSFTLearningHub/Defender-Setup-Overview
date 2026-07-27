# Microsoft Defender XDR Overview

<details markdown>
<summary>References</summary>

- [Microsoft Defender XDR overview](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender)
- [Turn on Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/m365d-enable)
- [Microsoft Defender portal](https://security.microsoft.com/)
- [Advanced hunting overview](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview)

</details>

[Back to the documentation hub](../index.md)

Microsoft Defender XDR unifies prevention, detection, investigation, and
response across endpoints, identities, email, collaboration, applications, and
connected cloud signals in the Microsoft Defender portal.

## Signal sources

- Microsoft Defender for Endpoint and Defender Vulnerability Management.
- Microsoft Defender for Office 365.
- Microsoft Defender for Identity and Microsoft Entra ID Protection.
- Microsoft Defender for Cloud Apps and App Governance.
- Microsoft Defender for Cloud and other integrated Microsoft security services.

Only licensed, provisioned, and connected products contribute their full signals.

## Configure

1. Confirm tenant, data location, licenses, roles, and privacy requirements.
2. Turn on Defender XDR and configure each underlying Defender workload.
3. Review unified portal settings, alert notifications, device groups, and roles.
4. Configure automated investigation and response at an approved automation level.
5. Connect Sentinel or another SIEM only after defining incident ownership.
6. Build hunting, retention, and evidence-preservation procedures.

## Verify and operate

- Confirm alerts from enabled products correlate into incidents.
- Validate advanced-hunting schema and role-based data visibility.
- Test containment and remediation with approved simulation tooling.
- Tune alert rules and exclusions with expiry, owner, and evidence.
- Measure time to triage, contain, remediate, and close incidents.

> [!NOTE]
> Defender XDR is the correlation and response layer. It does not create missing
> telemetry from a Defender product that has not been licensed or deployed.
