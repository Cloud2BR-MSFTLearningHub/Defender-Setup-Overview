# Microsoft Defender for Databases Overview

<details markdown>
<summary>References</summary>

- [Protect databases with Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-databases-plan)
- [Defender for Azure SQL](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-introduction)
- [Defender for open-source databases](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-databases-introduction)
- [Defender for Cosmos DB](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-defender-for-cosmos)

</details>

[Back to the documentation hub](../index.md)

Defender for Databases is a family of data-workload protections. Enable the
subplan that matches the database engine and hosting model.

## Workload map

| Workload | Protection family |
| --- | --- |
| Azure SQL Database and Azure SQL Managed Instance | Defender for Azure SQL |
| SQL Server on Azure VM or Arc-enabled machine | Defender for SQL servers on machines |
| Azure Database for PostgreSQL, MySQL, or MariaDB where supported | Defender for open-source relational databases |
| Azure Cosmos DB | Defender for Azure Cosmos DB |

## Enable

1. Inventory database engines, hosting models, subscriptions, and data owners.
2. Open **Environment settings**, select the subscription, and choose Databases.
3. Enable only the required subplans and inspect resource-level overrides.
4. Configure auditing and vulnerability assessment prerequisites where applicable.
5. Restrict network paths, use managed identities, and minimize database privileges.
6. Route alerts to database and incident-response teams.

## Verify and operate

- Confirm each database maps to the intended enabled subplan.
- Review alert and recommendation availability for that exact engine.
- Establish an approved test method; never run attack simulations on production.
- Correlate database alerts with identity, application, and network evidence.
- Track unprotected instances and stale vulnerability findings.

> [!IMPORTANT]
> A generic Databases toggle can expose separate subplans and charges. Review
> the current plan configuration and pricing before broad enablement.
