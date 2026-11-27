🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F14-13 Usage metric

# 🗃️ E-F14-13 Usage metric

**Status:** ✅ specified

## Purpose

Installs and activity.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| plugin, period, installs, active | records | yes | - | - | Gate Booking, Nov, 120, 1 240 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-F14-18
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

- [UC-F14-18](../use-cases/04-money-and-taxes/uc-f14-18-follow-usage-and-revenue.md)

## Open questions

None.

---

⬅️ [E-F14-12 Refund](e-f14-12-refund.md) · ⬆️ [Up](README.md) ·
➡️ [E-F14-14 Software bill of materials](e-f14-14-software-bill-of-materials.md)
