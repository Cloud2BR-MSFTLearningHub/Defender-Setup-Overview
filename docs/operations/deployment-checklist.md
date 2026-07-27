# Microsoft Defender Deployment Checklist

<details markdown>
<summary>References</summary>

- [Defender for Cloud planning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-cloud)
- [Defender for Cloud support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud)
- [Defender XDR prerequisites](https://learn.microsoft.com/en-us/defender-xdr/prerequisites)
- [Configuration, plans, and pricing](configuration-plans-and-pricing.md)

</details>

[Back to the documentation hub](../index.md)

Use this checklist for each Defender product or workload plan. Record evidence,
owner, date, and scope instead of marking an item complete without validation.

## Discover and design

- [ ] Inventory tenants, subscriptions, cloud accounts, assets, [regions](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud), and owners.
- [ ] Classify data, business criticality, exposure, and regulatory requirements.
- [ ] Select the exact Defender product, [plan or tier](configuration-plans-and-pricing.md), and eligible resource types.
- [ ] Read the current [support matrix, prerequisites, limitations, and pricing](configuration-plans-and-pricing.md).
- [ ] Decide management hierarchy, data location, retention, and RBAC design.
- [ ] [Estimate monthly cost](configuration-plans-and-pricing.md) with representative production volume.

## Prepare and pilot

- [ ] Assign platform, security operations, finance, privacy, and workload owners.
- [ ] Document required identities, permissions, endpoints, agents, and extensions.
- [ ] Define pilot scope, success criteria, rollback, and maintenance window.
- [ ] [Configure the plan settings](configuration-plans-and-pricing.md), alert routing, escalation, ticketing, and evidence retention.
- [ ] Enable the plan for a non-production or low-risk representative scope.
- [ ] Verify inventory, sensor health, recommendations, telemetry, and test alerts.

## Expand and enforce

- [ ] Resolve pilot blockers and record accepted limitations.
- [ ] Deploy centrally with policy, infrastructure as code, or approved automation.
- [ ] Reconcile protected inventory against the source of truth.
- [ ] Start enforcement controls in audit or report-only mode.
- [ ] Test incident containment and business recovery before automatic response.
- [ ] Communicate operating procedures to service owners and support teams.

## Operate

- [ ] Monitor coverage, connector health, data freshness, exclusions, and drift.
- [ ] Triage recommendations by risk and assign remediation due dates.
- [ ] Review cost, plan changes, release notes, and support matrices regularly.
- [ ] Remove retired assets, stale connectors, permissions, and billable plans.
- [ ] Exercise response playbooks and audit privileged actions.
- [ ] Measure risk reduction and response outcomes, not only alert count.

## Operational decisions

- Treat each completed item as evidence-backed: record the owner, scope, date,
  verification method, exception, and next review date instead of a bare tick.
- Gate expansion on measurable pilot success, including inventory coverage, alert
  delivery, response ownership, recovery testing, and observed cost.
- Re-run the checklist after architecture, licensing, cloud-region, connector, or
  operating-model changes, not only during the initial deployment.

## Worked example

For an AKS pilot, the platform owner supplies two non-production clusters, the
SOC owns alert triage, and finance reviews the expected plan charges. Success
means every node and registry is visible, a benign test finding reaches the chosen
incident queue, and the cluster team can remediate it within the agreed window.
Only after those checks and a tested rollback does the organization apply the
configuration through policy to production subscriptions.
