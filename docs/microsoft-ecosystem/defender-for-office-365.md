# Microsoft Defender for Office 365 Overview

<details markdown>
<summary>References</summary>

- [Defender for Office 365 overview](https://learn.microsoft.com/en-us/defender-office-365/mdo-about)
- [Deployment guide](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide)
- [Preset security policies](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies)
- [Email authentication](https://learn.microsoft.com/en-us/defender-office-365/email-authentication-about)

</details>

[Back to the documentation hub](../index.md)

Defender for Office 365 protects email and collaboration against phishing,
malware, malicious links, business email compromise, and related attacks across
Exchange Online, Teams, SharePoint, and OneDrive capabilities.

![Microsoft Defender for Office 365 protection layers for email and collaboration](https://learn.microsoft.com/en-us/defender-office-365/media/eop-mdop1-mdop2-comparison.png)

*Source: [Defender for Office 365 protection ladder](https://learn.microsoft.com/en-us/defender-office-365/mdo-about).* 

## Why enable it

Email and collaboration are the number-one entry point for attacks, and business
email compromise is among the costliest. Defender for Office 365 adds time-of-click
link protection, attachment detonation, and impersonation defense that basic spam
filtering does not provide — plus tools to hunt and remediate what gets through.

| Without Defender for Office 365 | With Plan 1 or Plan 2 enabled |
| --- | --- |
| Links are checked only at delivery | Safe Links re-checks URLs at time of click |
| Attachments rely on signature scanning | Safe Attachments detonates files in a sandbox |
| Impersonation and BEC are hard to catch | Impersonation and spoof intelligence flag them |
| Post-delivery cleanup is manual | Explorer and automated response hunt and remove threats |

**Value in one line:** it defends the most-attacked surface — the inbox — with
active detonation, click-time protection, and fast post-delivery remediation.

## Protection ladder

| Level | Main addition |
| --- | --- |
| Built-in cloud mailbox protection | Exchange Online Protection controls |
| Plan 1 | Safe Links, Safe Attachments, impersonation protection, and real-time detections |
| Plan 2 | Threat Explorer, campaigns, attack simulation, and automated investigation and response |

## Configure

1. Confirm licenses and accepted domains; configure SPF, DKIM, and DMARC.
2. Apply Standard or Strict preset security policies to a pilot group.
3. Review anti-phishing, anti-malware, anti-spam, Safe Links, and Safe Attachments.
4. Configure user reporting, submissions, quarantine, alerts, and notifications.
5. Extend supported protection to Teams, SharePoint, and OneDrive.
6. Pilot simulations and automation before organization-wide use.

## Verify and operate

- Use Microsoft-provided simulation or test capabilities, never real malware.
- Confirm message traces, submissions, Explorer or detections, and incidents.
- Monitor policy exceptions, forwarding, spoofing, and high-risk users.
- Test mailbox remediation, malicious-message removal, and communications.
