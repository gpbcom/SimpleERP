🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F22-06 Cost budget

# 🗃️ E-F22-06 Cost budget

**Status:** ✅ specified

## Purpose

A monthly budget at one level.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| level, target, amount, thresholds | records | yes | BR-F22-04, BR-F22-05 | 80 % | module, F17, 150, 80 % | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F22-07
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

- [UC-F22-06](../use-cases/02-budgets-and-stops/uc-f22-06-set-budgets-at-every-level.md)
- [UC-F22-07](../use-cases/02-budgets-and-stops/uc-f22-07-receive-warnings-at-thresholds.md)
- [UC-F22-08](../use-cases/02-budgets-and-stops/uc-f22-08-stop-paid-calls-at-100-legal-duties-kept.md)
- [UC-F22-09](../use-cases/02-budgets-and-stops/uc-f22-09-raise-a-budget-or-approve-a-run.md)
- [UC-F22-20](../use-cases/01-see-and-set-up/uc-f22-20-ask-the-assistant-about-costs.md)

## Open questions

None.

---

⬅️ [E-F22-05 Hosted quota](e-f22-05-hosted-quota.md) · ⬆️ [Up](README.md) ·
➡️ [E-F22-07 Cost alert](e-f22-07-cost-alert.md)
