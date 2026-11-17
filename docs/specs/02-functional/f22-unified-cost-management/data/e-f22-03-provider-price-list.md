🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F22-03 Provider price list

# 🗃️ E-F22-03 Provider price list

**Status:** ✅ specified

## Purpose

A provider's prices and their dates.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| provider, unit, price, valid from, valid to | records | yes | BR-F22-03 | - | provider A, 1 000 tokens, 0.006, 2026-11-01, - | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-F22-03
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

- [UC-F22-02](../use-cases/01-see-and-set-up/uc-f22-02-see-costs-per-module-feature-and-provider.md)
- [UC-F22-04](../use-cases/01-see-and-set-up/uc-f22-04-register-a-paid-provider-and-its-prices.md)
- [UC-F22-21 Record a provider's prices in a foreign currency](../use-cases/01-see-and-set-up/uc-f22-21-record-a-providers-prices-in-a-foreign-currency.md)

## Open questions

None.

---

⬅️ [E-F22-02 Metered call record](e-f22-02-metered-call-record.md) · ⬆️ [Up](README.md) ·
➡️ [E-F22-04 Paid provider](e-f22-04-paid-provider.md)
