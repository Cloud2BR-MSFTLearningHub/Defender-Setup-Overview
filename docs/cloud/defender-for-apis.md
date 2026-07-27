# Microsoft Defender for APIs Overview

<details markdown>
<summary>References</summary>

- [Defender for APIs overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction)
- [Enable Defender for APIs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-deploy)
- [Defender for APIs support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-apis)

</details>

[Back to the documentation hub](../index.md)

Defender for APIs adds security posture and runtime threat detection for
eligible APIs managed through supported Azure API Management tiers and regions.
APIs expose business logic and data directly to the internet, and they are now
one of the most common attack surfaces, so seeing which APIs exist and how they
are being used is essential.

![Defender for APIs endpoint details and risk context](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-apis-introduction/endpoint-details.png)

*Source: [Overview of Defender for APIs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction).*

## Why enable it

Many breaches involve an API that security teams did not know was exposed or was
returning sensitive data. Defender for APIs inventories managed APIs, highlights
the risky ones, and watches traffic for exploitation of the OWASP API risks.

| Without Defender for APIs | With the plan enabled |
| --- | --- |
| Shadow and undocumented APIs go untracked | A live inventory shows APIs, usage, and exposure |
| Sensitive-data exposure is discovered during an incident | Risk context highlights APIs handling sensitive data |
| Attacks on API logic look like normal requests | Runtime detections flag suspicious and anomalous calls |
| Prioritization is guesswork | Findings rank internet-facing, sensitive APIs first |

**Value in one line:** it makes your API estate visible and monitored, so the
endpoints attackers probe are the endpoints you are already watching.

## How it works

Defender for APIs onboards eligible APIs from Azure API Management and then
observes their live traffic. It builds an inventory enriched with usage,
authentication, and exposure details, classifies which APIs handle sensitive data,
and applies machine-learning detections tuned to the OWASP API security risks, so
anomalies such as abnormal data exposure, suspicious enumeration, or abuse of a
specific endpoint generate alerts.

Onboarding is deliberate: enabling the subscription plan makes APIs eligible, and
you then choose which APIs to actively monitor within plan capacity. That two-step
model lets you focus protection on the sensitive, internet-facing production APIs
that matter most.

## Enable

1. Inventory API Management services, APIs, revisions, backends, and data owners.
2. Check API Management tier, region, protocol, and API eligibility.
3. Enable the **APIs** plan in Defender for Cloud at subscription scope.
4. In Defender for Cloud API security, onboard the selected eligible APIs.
5. Prioritize sensitive and internet-facing production APIs within plan capacity.
6. Review authentication, authorization, rate limits, schemas, and backend access.

## Verify and operate

- Confirm onboarded APIs appear in the API inventory with recent traffic data.
- Review recommendations and runtime alerts after the learning period.
- Keep owner, sensitivity, exposure, and business-criticality metadata current.
- Correlate API alerts with API Management, application, identity, and WAF logs.
- Test key revocation, backend isolation, and safe API rollback.

## Architecture and prerequisites

![Defender for APIs coverage across API Management](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-apis-introduction/templates-example.png)

*Source: [Overview of Defender for APIs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction).*

- **Platform prerequisite:** APIs must be published through supported Azure API Management tiers and regions; enabling the plan makes them eligible, and you then onboard specific APIs.
- **Traffic analysis:** Defender samples API Management traffic to build the inventory and run ML detections — no gateway change or agent.
- **Capacity model:** the plan covers a number of API requests; onboard the most sensitive, internet-facing APIs first.
- **Permissions:** Security Admin / Owner to enable; API Management contributor to onboard APIs.

## Detections and OWASP API risks

Detections align with the OWASP API Security Top 10 — for example abnormal data exposure (excessive response payloads), broken object-level authorization probing (enumeration), and suspicious spikes from a single client. Feed alerts to Sentinel and correlate with API Management `ApiManagementGatewayLogs` and any WAF logs for full request context, then respond by revoking keys, tightening product and rate-limit policies, or isolating the backend.

!!! warning "Important"
    Enabling the subscription plan and onboarding individual APIs are distinct
    steps. Unsupported or discovered APIs are not automatically protected.

## Operational decisions

- Classify each API by data sensitivity and business criticality before assigning
    response severity; catalog APIs and payment APIs should not share the same SLA.
- Coordinate key revocation, rate limiting, and backend changes with API owners
    so containment does not silently break legitimate client integrations.
- Retain API identifier, product, caller identity, request pattern, affected
    object scope, containment action, and validation result.

## Worked example

An API Management service exposes both public catalog APIs and a payment API. The
team onboards the payment API first, assigns it high criticality, and observes a
spike of object-ID enumeration from one client. They revoke the compromised key,
apply a stricter rate-limit policy, and create a backlog item to enforce
object-level authorization in the backend.
