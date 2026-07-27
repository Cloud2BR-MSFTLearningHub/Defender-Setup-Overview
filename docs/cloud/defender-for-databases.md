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
subplan that matches the database engine and hosting model. Databases hold the
most sensitive data in most environments, so they are a primary target for
injection, brute force, privilege abuse, and exfiltration.

![Defender for Cloud database threat alerts](https://learn.microsoft.com/en-us/azure/defender-for-cloud/media/defender-for-databases-introduction/defender-alerts.png)

*Source: [Overview of Defender for Databases](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-databases-introduction).*

## Why enable it

Attackers who reach a database rarely trigger platform alarms — they use valid
queries and stolen credentials. Defender for Databases applies behavioral
analytics and threat intelligence to flag anomalous access and known attack
patterns against the exact engine you run.

| Without Defender for Databases | With the matching subplan enabled |
| --- | --- |
| SQL injection and brute force are found in raw audit logs | Behavioral detections raise prioritized alerts |
| Anomalous access looks like normal query traffic | Unusual locations, principals, and volumes are highlighted |
| Vulnerability posture is assessed ad hoc | Built-in vulnerability assessment reports drift (where supported) |
| Each engine is monitored differently | Consistent coverage across Azure SQL, open-source, and Cosmos DB |

**Value in one line:** it catches credential-based and injection attacks on your
data tier that infrastructure monitoring simply cannot see.

## How it works

Defender for Databases attaches to the database service rather than the host. For
each supported engine it applies behavioral analytics and threat intelligence to
query and login telemetry, learning what normal access looks like and alerting on
deviations such as a brute-force login, a SQL injection pattern, or access from an
unfamiliar principal or location. Where the engine supports it, vulnerability
assessment also scans the database configuration and schema for weaknesses.

Because it is a family of subplans, coverage is engine-specific: Azure SQL, SQL
Server on machines, open-source relational databases, and Azure Cosmos DB each
have their own subplan and meter. Alerts flow into Defender for Cloud and the
Defender portal, so a database alert can be correlated with the identity and
application evidence around it.

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

!!! warning "Important"
    A generic Databases toggle can expose separate subplans and charges. Review
    the current plan configuration and pricing before broad enablement.
