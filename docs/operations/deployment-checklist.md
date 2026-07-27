# Microsoft Defender Deployment Checklist

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Use this checklist for each Defender product or workload plan. Record evidence,
owner, date, and scope instead of marking an item complete without validation.

## Discover and design

- [ ] Inventory tenants, subscriptions, cloud accounts, assets, regions, and owners.
- [ ] Classify data, business criticality, exposure, and regulatory requirements.
- [ ] Select the exact Defender product, plan, and eligible resource types.
- [ ] Read the current support matrix, prerequisites, limitations, and pricing.
- [ ] Decide management hierarchy, data location, retention, and RBAC design.
- [ ] Estimate monthly cost with representative production volume.

## Prepare and pilot

- [ ] Assign platform, security operations, finance, privacy, and workload owners.
- [ ] Document required identities, permissions, endpoints, agents, and extensions.
- [ ] Define pilot scope, success criteria, rollback, and maintenance window.
- [ ] Configure alert routing, escalation, ticketing, and evidence retention.
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

## References

- [Defender for Cloud planning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-cloud)
- [Defender for Cloud support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-cloud)
- [Defender XDR prerequisites](https://learn.microsoft.com/en-us/defender-xdr/prerequisites)
