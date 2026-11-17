🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎓 [SC12 Education and training](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC12-15 Class

# 🗃️ E-SC12-15 Class

**Status:** 🔄 waiting for the owner

## Purpose

A school class.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name, year, teachers | records | yes | - | - | 6e B, 2026, 9 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC12-16
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

- [UC-SC12-16](../use-cases/05-private-school/uc-sc12-16-organise-classes-and-timetables.md)

## Open questions

None.

---

⬅️ [E-SC12-14 Student](e-sc12-14-student.md) · ⬆️ [Up](README.md) · ➡️ [E-SC12-16 Grade](e-sc12-16-grade.md)
