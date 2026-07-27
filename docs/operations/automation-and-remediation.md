# Defender Automation and Remediation

<details markdown>
<summary>References</summary>

- [Defender for Cloud workflow automation](https://learn.microsoft.com/en-us/azure/defender-for-cloud/workflow-automation)
- [Azure Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)
- [Sentinel automation](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)
- [Defender XDR automated investigation](https://learn.microsoft.com/en-us/defender-xdr/m365d-autoir)

</details>

[Back to the documentation hub](../index.md)

Defender detects, recommends, investigates, and performs specific supported
response actions. Policy and automation services provide broader enforcement and
remediation. Match the tool to the decision being made.

## Why it matters

Detection without response just produces alerts faster than people can act on them.
Automation closes that gap — handling repetitive triage, enrichment, and
containment in seconds — while keeping humans in control of disruptive actions.
The value comes from pairing the right enforcement tool with each decision.

| Manual-only operations | With measured automation |
| --- | --- |
| Analysts repeat the same triage steps | Playbooks normalize and enrich alerts instantly |
| Response time depends on staff availability | Routine containment happens in seconds, any hour |
| Enforcement is inconsistent | Policy and pipelines apply controls uniformly |
| Disruptive actions risk mistakes | Approval gates protect high-impact steps |

**Value in one line:** automation removes the busywork and slow hand-offs from
response while keeping human approval on the actions that can disrupt production.

## Control map

| Goal | Typical tool |
| --- | --- |
| Prevent an unsafe Azure configuration | Azure Policy deny or modify effect |
| Enforce Kubernetes admission rules | Azure Policy for Kubernetes or Gatekeeper |
| Repair deployed infrastructure | Infrastructure-as-code pull request and pipeline |
| Respond to a Defender for Cloud alert | Workflow automation with Logic Apps |
| Orchestrate a cross-product incident | Defender XDR automation or Sentinel playbook |
| Manage endpoint settings | Intune security policy |
| Restrict risky identity access | Conditional Access |

## Safe automation pattern

1. Normalize the alert, resource, identity, severity, and confidence.
2. Enrich with ownership, criticality, exposure, maintenance, and threat context.
3. Use idempotent actions and least-privilege managed identities.
4. Start with notification or ticket creation.
5. Add approval for disruptive actions such as isolation, deletion, or key rotation.
6. Record every action and preserve evidence before remediation.
7. Verify recovery, close the loop, and expire temporary exceptions.

## Guardrails

- Do not trust an alert title as the sole authorization for a destructive action.
- Suppress duplicates without hiding recurring or escalating behavior.
- Set concurrency, retry, timeout, and cost limits.
- Protect automation credentials and restrict who can edit playbooks.
- Maintain break-glass, rollback, and manual execution procedures.
- Test with simulations and non-production resources.
