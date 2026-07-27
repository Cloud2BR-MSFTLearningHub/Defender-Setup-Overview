# Microsoft Defender for Cloud on AWS

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)

Last updated: 2026-07-27

----------

[Back to the documentation hub](../index.md)

Defender for Cloud connects AWS organizations or accounts to provide cloud
posture management and selected workload protections. It does not turn AWS into
an Azure subscription; protection remains resource- and plan-specific.

## Typical coverage

- Foundational CSPM and Microsoft Cloud Security Benchmark recommendations.
- Defender CSPM capabilities such as agentless discovery and attack paths where supported.
- Defender for Servers coverage for eligible EC2 machines.
- Defender for Containers coverage for eligible Amazon EKS and ECR resources.
- Additional plan-specific coverage shown by the current AWS support matrix.

## Connect

1. Decide whether to connect an AWS organization or individual accounts.
2. In Defender for Cloud **Environment settings**, create an AWS connector.
3. Select plans and review every requested AWS and Azure permission.
4. Deploy the generated CloudFormation stack or StackSet in the correct scope.
5. Configure optional agentless, server, and container components.
6. Wait for discovery, then compare inventory with AWS Organizations and Config.

## Verify and operate

- Confirm connector health, account coverage, region coverage, and scan freshness.
- Validate that required IAM roles and AWS services were created successfully.
- Review AWS API cost, data transfer, Defender plan charges, and resource limits.
- Route findings to the team that owns the AWS account and affected workload.
- Remove stale accounts and update StackSets when connector requirements change.

> [!IMPORTANT]
> Do not grant connector permissions without cloud security and AWS platform
> review. Organization-wide templates can affect every member account.

## References

- [Connect AWS accounts](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-aws)
- [AWS security features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-aws)
- [Multicloud planning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-multicloud-security-get-started)
- [Defender for Containers on AWS](https://learn.microsoft.com/en-us/azure/defender-for-cloud/tutorial-enable-container-aws)
