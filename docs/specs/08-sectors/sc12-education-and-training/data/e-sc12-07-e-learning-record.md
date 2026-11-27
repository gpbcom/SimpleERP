🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎓 [SC12 Education and training](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC12-07 E-learning record

# 🗃️ E-SC12-07 E-learning record

**Status:** 🔄 waiting for the owner

## Purpose

Progress on the platform.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| learner, module, hours | records | yes | BR-SC12-15 | - | J. Martin, module 3, 2 | yes | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-SC12-07
```

## Indexes and search

(Proposed) By number, date, partner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

(Proposed) CSV, FEC where relevant.

## Used by

- [UC-SC12-07](../use-cases/03-deliver-and-assess/uc-sc12-07-run-e-learning-modules.md)

## Open questions

None.

---

⬅️ [E-SC12-06 Attendance sheet](e-sc12-06-attendance-sheet.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC12-08 Completion certificate](e-sc12-08-completion-certificate.md)
