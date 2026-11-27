🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC05-05 Customer-supplied part

# 🗃️ E-SC05-05 Customer-supplied part

**Status:** ✅ specified

## Purpose

A part owned by a customer.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| customer, product | records | yes | BR-SC05-05 | - | Acme, casting C4 | no | no |
| quantity | number | yes | >= 0 | - | 50 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-SC05-05
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

- [UC-SC05-05](../use-cases/02-made-to-order/uc-sc05-05-handle-customer-supplied-parts.md)

## Open questions

None.

---

⬅️ [E-SC05-04 Engineered design](e-sc05-04-engineered-design.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC05-06 Label template](e-sc05-06-label-template.md)
