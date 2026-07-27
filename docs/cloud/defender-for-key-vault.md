# Microsoft Defender for Key Vault Overview

<details markdown>
<summary>References</summary>

- [Defender for Key Vault overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-key-vault-introduction)
- [Enable Defender for Key Vault](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-key-vault-plan)
- [Azure Key Vault security](https://learn.microsoft.com/en-us/azure/key-vault/general/security-features)

</details>

[Back to the documentation hub](../index.md)

Defender for Key Vault detects unusual and potentially harmful attempts to
access or exploit Azure Key Vault vaults by analyzing control-plane and
data-plane activity with Microsoft threat intelligence.

## Enable

1. Inventory vaults, managed HSM resources, applications, identities, and owners.
2. Confirm current protection scope and regional availability for each resource.
3. In Defender for Cloud **Environment settings**, select the subscription.
4. Enable the **Key Vault** plan and save.
5. Review network access, RBAC, purge protection, logging, and secret rotation.
6. Route alerts to both the security team and vault owner.

## Verify and operate

- Confirm intended vaults appear as protected in inventory.
- Establish baselines for service principals, source networks, and operation rates.
- Investigate anomalous access with identity, application, and audit evidence.
- Predefine secret or certificate rotation and application recovery procedures.
- Monitor vaults outside the centrally managed subscription hierarchy.

> [!IMPORTANT]
> Defender detects suspicious access; it does not replace least privilege,
> private endpoints, soft-delete and purge protection, or rotation processes.
