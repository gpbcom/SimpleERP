🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🛡️ TC-17 Security and compliance profiles

# 🛡️ TC-17 Security and compliance profiles

**Status:** ✅ listed for the technical interviews

## Challenge

Make the same product deployable under SecNumCloud, SOC 2, ISO 27001, HDS, NIS2 and the GDPR, with secrets in a vault
and hosting in the EU for the hosted edition.

## Raised by

- [F1 Administration](../../02-functional/f01-administration/README.md)
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [F20 Hosted support assistant (hosted edition)](../../02-functional/f20-hosted-support-assistant/README.md)
- [T2 Identity and access engine](../t02-identity-and-access/README.md)

## Why it is hard

- Each framework asks for evidence, not only for controls.
- Plugins, generated features and connectors widen the attack surface.
- Supply chain attacks reach through dependencies.

## Already decided

- [D240](../../06-decisions/security-and-compliance/d240-credential-vault.md) Customers' credentials in a vault
- [D241](../../06-decisions/security-and-compliance/d241-security-frameworks.md) Deployable under security frameworks
- [D375](../../06-decisions/vision/d375-managed-hosting-eu-only.md) Managed hosting in the EU only

## Options to weigh

- Compliance profiles as deployment settings, with the evidence they produce.
- Signed builds, software bills of materials and dependency scanning.

## Settled in

- 19f Security ([chapter](../../../technical/security/security.md))
- 19g Supply chain and licences ([chapter](../../../technical/security/supply-chain-and-licences.md))
- 19j CI/CD and deployment ([chapter](../../../technical/infrastructure/deployment.md))
- Then the technical capabilities: [T2 Identity and access engine](../t02-identity-and-access/README.md).

## Questions for the interview

- Which framework is targeted first for the hosted edition?
- Is an outside audit planned before launch?

---

⬅️ [TC-16 Files, media and archives](tc-16-files-media-and-archives.md) · ⬆️ [Up](README.md) ·
➡️ [TC-18 Install, upgrade and migrate without a consultant](tc-18-install-upgrade-and-migrate.md)
