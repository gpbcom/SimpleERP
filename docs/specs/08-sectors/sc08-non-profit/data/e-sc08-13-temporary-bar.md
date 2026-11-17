🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🤲 [SC08 Non-profit association](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC08-13 Temporary bar

# 🗃️ E-SC08-13 Temporary bar

**Status:** 🔄 waiting for the owner

## Purpose

A bar at an event.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| event, authorisation | records | yes | BR-SC08-11 | - | Gala, mayor's letter | no | no |
| drink groups, takings | list, amount | yes | - | - | 1 and 3, 820.00 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-SC08-11
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

- [UC-SC08-13](../use-cases/05-events/uc-sc08-13-run-a-temporary-bar-at-events.md)

## Open questions

None.

---

⬅️ [E-SC08-12 Association event](e-sc08-12-association-event.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC08-14 Dedicated fund](e-sc08-14-dedicated-fund.md)
