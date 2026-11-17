🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) ›
🚀 TC-18 Install, upgrade and migrate without a consultant

# 🚀 TC-18 Install, upgrade and migrate without a consultant

**Status:** ✅ listed for the technical interviews

## Challenge

Install simple-ERP, import a company's data from its old tools, and upgrade it with its plugins, sector packs and
generated features, all within the one-day promise.

## Raised by

- [F21 Onboarding and module activation](../../02-functional/f21-onboarding-and-modules/README.md)
- [F1 Administration](../../02-functional/f01-administration/README.md)
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md)

## Why it is hard

- Self-hosted, provider and hosted installs must all upgrade safely.
- Every other ERP has its own export format.
- A failed upgrade must roll back without losing data.

## Already decided

- [D1](../../06-decisions/foundations/d01-runs-for-a-company-or-a-provider.md) One company or an IT provider
- [D379](../../06-decisions/vision/d379-working-in-one-day.md) Working in one day

## Options to weigh

- Upgrades tested on a copy first, then applied, with automatic rollback.
- Importers per source system on one mapping model.
- Container images and an installer for self-hosting.

## Settled in

- 19j CI/CD and deployment ([chapter](../../../technical/infrastructure/deployment.md))
- 19k Backups, recovery and upgrades ([chapter](../../../technical/operations/operations.md))
- 19m Data migration from other ERPs ([chapter](../../../technical/data/data-migration.md))
- Then the technical capabilities: [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md).

## Questions for the interview

- Which source systems must the importer read on day one?
- How many versions back must an upgrade start from?

---

⬅️ [TC-17 Security and compliance profiles](tc-17-security-and-compliance-profiles.md) · ⬆️ [Up](README.md) ·
➡️ [TC-19 Languages, currencies and countries](tc-19-languages-currencies-and-countries.md)
