# Microsoft Defender for Identity Overview

<details markdown>
<summary>References</summary>

- [Defender for Identity overview](https://learn.microsoft.com/en-us/defender-for-identity/what-is)
- [Deployment overview](https://learn.microsoft.com/en-us/defender-for-identity/deploy-defender-identity)
- [Prerequisites](https://learn.microsoft.com/en-us/defender-for-identity/prerequisites)
- [Security assessments](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment)

</details>

[Back to the documentation hub](../index.md)

Defender for Identity uses signals from on-premises identity infrastructure to
detect reconnaissance, credential theft, lateral movement, and compromised
identities, then correlates them in Defender XDR.

## Typical scope

- Active Directory Domain Services domain controllers.
- Active Directory Federation Services and Active Directory Certificate Services
  in scenarios supported by current sensor guidance.
- Microsoft Entra identities correlated through the Defender XDR experience.

## Configure

1. Confirm licensing, directory topology, forests, trusts, and sensor support.
2. Size domain controllers and validate required network connectivity.
3. Create the Defender for Identity instance in the Defender portal.
4. Download and deploy sensors using a dedicated directory service account design.
5. Configure directory service accounts, VPN integration, and exclusions if needed.
6. Remediate identity posture findings and remove legacy protocols where feasible.

## Verify and operate

- Confirm every intended sensor is healthy, current, and reporting.
- Review identity inventory, lateral-movement paths, and security assessments.
- Use approved Microsoft test procedures in an isolated lab.
- Correlate alerts with endpoint, cloud app, and Entra sign-in evidence.
- Protect sensor credentials and establish domain-controller recovery procedures.

!!! note
  Defender for Identity complements Microsoft Entra ID Protection. The former
  emphasizes hybrid and on-premises identity signals; the latter evaluates
  Entra user and sign-in risk.
