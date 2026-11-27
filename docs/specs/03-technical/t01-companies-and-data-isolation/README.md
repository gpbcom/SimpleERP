🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🏢 T1 Companies and data isolation

# 🏢 T1 Companies and data isolation

**Status:** ✅ specified

## Summary

Each company's data kept apart in every store and every path, whoever runs SimpleERP: one company, an IT provider or
the hosted edition (TC-01).

## Scope

- A database, bucket and vector collection per company.
- The company context at every layer.
- Provider access, dedicated plans, copies and overlays, company creation, export and deletion.

- The analytics store kept apart and erasable (REQ-T01-08).

## Functional capabilities served

Every functional capability; especially F1, F19, F20, F21, F23, F25.

## Out of scope

- Rights inside a company: T2.
- Backups: T9.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🏗️ |  | [Architecture](architecture.md) | ✅ |
| 📌 |  | [Requirements](requirements/README.md) | ✅ |
| 🔌 |  | [Interfaces](interfaces/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |
| 🛡️ |  | [Security](security.md) | ✅ |
| ⚙️ |  | [Operations](operations.md) | ✅ |
| 🚨 |  | [Errors](errors.md) | ✅ |
| 🧪 |  | [Tests](tests.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |

---

⬆️ [Up](../README.md) · ➡️ [Identity and access engine](../t02-identity-and-access/README.md)
