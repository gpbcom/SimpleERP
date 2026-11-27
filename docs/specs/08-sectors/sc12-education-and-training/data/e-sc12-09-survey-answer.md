🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎓 [SC12 Education and training](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC12-09 Survey answer

# 🗃️ E-SC12-09 Survey answer

**Status:** ✅ specified

## Purpose

Satisfaction or a complaint.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| enrolment, kind, score | records | yes | - | - | J. Martin, hot, 9 | yes | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-SC12-09
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

- [UC-SC12-09](../use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md)
- [UC-SC12-14](../use-cases/04-quality-and-reports/uc-sc12-14-handle-complaints-and-incidents.md)

## Open questions

None.

---

⬅️ [E-SC12-08 Completion certificate](e-sc12-08-completion-certificate.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC12-10 Training invoice](e-sc12-10-training-invoice.md)
