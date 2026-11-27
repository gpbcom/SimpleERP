🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F14-10 Private store

# 🗃️ E-F14-10 Private store

**Status:** ✅ specified

## Purpose

An IT provider's store.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| provider, plugins, clients | records | yes | - | - | NetServ, 12, 30 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F14-15
```

## Indexes and search

By number, date, partner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F14-15](../use-cases/05-store-operations/uc-f14-15-run-a-private-store.md)

## Open questions

None.

---

⬅️ [E-F14-09 Seller report](e-f14-09-seller-report.md) · ⬆️ [Up](README.md) ·
➡️ [E-F14-11 Plugin withdrawal](e-f14-11-plugin-withdrawal.md)
