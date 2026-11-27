🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC16-14 Safety file

# 🗃️ E-SC16-14 Safety file

**Status:** 🔄 waiting for the owner

## Purpose

The safety file and checks.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| venue or event, checks, state | records | yes | BR-SC16-09 | - | Hall A, 2026 check, OK | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Ok : UC-SC16-13
  [*] --> Open : UC-SC16-13
  [*] --> Blocked : UC-SC16-13
  [*] --> Overdue : UC-SC16-13
  [*] --> Complete : UC-SC16-13
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

- [UC-SC16-13](../use-cases/04-on-site/uc-sc16-13-keep-the-safety-file-and-register.md)

## Open questions

None.

---

⬅️ [E-SC16-13 Event till](e-sc16-13-event-till.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC16-15 Show declaration](e-sc16-15-show-declaration.md)
