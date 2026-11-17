🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F22-05 Hosted quota

# 🗃️ E-F22-05 Hosted quota

**Status:** ✅ specified

## Purpose

A plan's monthly allowance.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| plan, kind, included units, used | records | yes | BR-F22-09 | - | business, AI, 2 M tokens, 1.4 M | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-F22-09
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

- [UC-F22-05](../use-cases/01-see-and-set-up/uc-f22-05-bring-own-keys-or-use-the-hosted-quota.md)
- [UC-F22-15](../use-cases/05-billing/uc-f22-15-see-the-hosted-quota-and-units-billed.md)

## Open questions

None.

---

⬅️ [E-F22-04 Paid provider](e-f22-04-paid-provider.md) · ⬆️ [Up](README.md) ·
➡️ [E-F22-06 Cost budget](e-f22-06-cost-budget.md)
