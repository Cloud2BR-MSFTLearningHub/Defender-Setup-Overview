# Microsoft Defender Licensing and Cost Planning

<details markdown>
<summary>References</summary>

- [Defender for Cloud pricing](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)
- [Defender for Cloud cost calculator](https://learn.microsoft.com/en-us/azure/defender-for-cloud/cost-calculator)
- [Microsoft 365 licensing guidance](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-service-descriptions)
- [Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview)
- [Configuration, plans, and pricing](configuration-plans-and-pricing.md)

</details>

[Back to the documentation hub](../index.md)

Microsoft Defender licensing uses different meters for cloud resources, users,
devices, servers, data volume, API calls, and optional capabilities. Never infer
the price of one Defender product from another product's name.

## Build an estimate

1. Export counts by resource type, operating system, cloud, region, and owner.
2. Map every asset to the exact plan and current billing meter.
3. Separate included Microsoft 365 entitlements from add-ons and Azure charges.
4. Include optional scanning, ingestion, retention, Arc, monitoring, and egress costs.
5. Model growth, autoscaling, ephemeral resources, and non-production estates.
6. Pilot with cost alerts and compare the estimate with actual daily charges.

For the portal configuration path, plan and tier comparison, regional support
checks, and live price tools, see [configuration, plans, and pricing](configuration-plans-and-pricing.md).

## Cost controls

- Apply plans at a governed scope and continuously detect resource-level overrides.
- Set malware-scanning caps and data-collection limits where supported.
- Remove stale Arc resources, connectors, duplicate agents, and retired assets.
- Use Azure Cost Management budgets, tags, exports, and anomaly alerts.
- Revisit commitments and included allowances with current pricing documentation.
- Record who can enable billable plans and how approval is captured.

## Questions for every purchase

- Is billing per resource, transaction, protected user, device, server, or data volume?
- Does autoscaling or short resource lifetime change the meter?
- Which features require a higher plan or separate license?
- Are preview capabilities billed and supported for production?
- What telemetry creates separate Log Analytics or Sentinel ingestion charges?
- How quickly does billing stop after offboarding?

## Operational decisions

- Assign plan-enablement permissions separately from cost approval, and review
  resource-level overrides that may bypass the intended management-group scope.
- Use tags or a cost-allocation model that maps Defender charges to an environment,
  product owner, and workload so spend can be challenged and forecast accurately.
- Retain plan, meter, resource count, estimate assumptions, actual cost trend,
  budget threshold, owner approval, and offboarding date for each rollout.

## Worked example

Before enabling Defender for Servers across 800 virtual machines, a team exports
the inventory and finds that 150 are short-lived development nodes. It pilots the
plan on 50 representative servers, tags the charges by environment, and compares
daily cost with the estimate. The review leads to a production-first rollout and
a monthly check that retired dev nodes no longer remain billable.
