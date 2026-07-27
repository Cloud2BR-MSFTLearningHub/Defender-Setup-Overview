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
identities, then correlates them in Defender XDR. Active Directory is the target
of most hands-on-keyboard attacks, and its native logs rarely make an attack
obvious on their own.

## Why enable it

Once attackers have a foothold, they abuse Active Directory to move laterally and
escalate privilege using legitimate-looking actions. Defender for Identity
baselines normal identity behavior and detects the techniques, such as DCSync,
Pass-the-Hash, and Kerberoasting, that those actions represent.

| Without Defender for Identity | With sensors deployed |
| --- | --- |
| Domain controller logs must be analyzed by hand | Behavioral analytics surface identity attacks automatically |
| Lateral movement blends into normal traffic | Lateral-movement paths are mapped and alerted |
| Identity posture weaknesses are unknown | Security assessments highlight risky configurations |
| Identity alerts stand alone | Signals correlate into Defender XDR incidents |

**Value in one line:** it turns quiet Active Directory abuse into clear,
correlated alerts before attackers reach domain dominance.

## How it works

A lightweight sensor installed on domain controllers, and on supported AD FS or
AD CS servers, inspects authentication traffic, directory changes, and network
activity locally, then sends only the security signals to the cloud. Defender for
Identity baselines normal behavior for each user and device and detects the
techniques used across the attack chain, including reconnaissance and credential theft such as
Pass-the-Hash and Kerberoasting, lateral movement, and domain-dominance actions
such as DCSync.

It also continuously scores identity posture, highlighting risky configurations and
legacy protocols to remediate. Alerts correlate into Defender XDR alongside
endpoint, email, and cloud-app evidence, and its on-premises focus complements
Entra ID Protection's analysis of cloud sign-ins.

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

## Architecture and prerequisites

- **Sensor placement:** install the sensor directly on every domain controller, and on AD FS or AD CS servers where those signals are needed.
- **Directory Service Account:** configure a group managed service account (gMSA) so the sensor can query the directory securely.
- **Sizing and connectivity:** validate CPU and memory against domain-controller load, and allow outbound HTTPS to the Defender for Identity service.
- **Surface:** signals appear in the Defender portal identity experience and feed Defender XDR.

## Hybrid and multi-forest design

Model each forest, domain, trust, domain controller, federation service, and
certificate service explicitly during deployment. A healthy sensor in one domain
does not establish coverage for a separate domain controller or identity service.
Deploy and verify sensors according to the supported topology, and test the
investigation path across the trusts that the business relies on rather than
assuming every relationship produces the same visibility.

Keep the relationship between on-premises accounts and cloud identities clear in
the incident process. An on-premises account may be visible to Defender for
Identity even when it has no corresponding Entra account; cloud-risk and
Conditional Access actions must therefore be based on confirmed identity mapping,
not only matching display names. Record the relevant on-premises identifiers,
Entra identifiers when available, trust path, sensor health, and the source of
each conclusion in the investigation.

## Detections across the attack chain

| Phase | Example detection |
| --- | --- |
| Reconnaissance | Account and SPN enumeration, AS-REP roasting |
| Credential access | Kerberoasting, brute force, Pass-the-Hash |
| Lateral movement | Overpass-the-Hash, remote code execution |
| Domain dominance | DCSync, DCShadow, Golden Ticket use |

## Advanced hunting example

Surface accounts with a burst of failed logons:

```kusto
IdentityLogonEvents
| where Timestamp > ago(24h)
| where ActionType == "LogonFailed"
| summarize failures = count() by AccountUpn, DeviceName, bin(Timestamp, 1h)
| where failures > 25
```

Find directory queries that enumerate service principal names, then pivot to the
originating account and device before taking credential-response actions:

```kusto
IdentityQueryEvents
| where Timestamp > ago(24h)
| where QueryType has "SPN"
| summarize queries = count(), targets = make_set(QueryTarget, 20)
  by AccountUpn, DeviceName, bin(Timestamp, 1h)
| where queries > 20
| order by queries desc
```

!!! note
    Defender for Identity complements Microsoft Entra ID Protection. The former
    emphasizes hybrid and on-premises identity signals; the latter evaluates
    Entra user and sign-in risk.

## Operational decisions

- Separate the authority to investigate identity alerts from the authority to
  reset privileged accounts or change Active Directory configuration.
- Validate sensor deployment, directory topology, and service-account exclusions
  after domain-controller maintenance and before relying on coverage metrics.
- Retain device, user, domain controller, detection path, ticket, credential
  action, and post-remediation sign-in validation for each incident.

## Worked example

> Defender for Identity detects Kerberoasting behavior from a workstation that has
> never administered Active Directory. Analysts use the lateral-movement path to
> identify the impacted service account, reset its password, rotate the service
> credential, and remove the unnecessary service principal name that made the
> account a target.
