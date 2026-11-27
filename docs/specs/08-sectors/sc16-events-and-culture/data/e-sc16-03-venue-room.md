🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC16-03 Venue room

# 🗃️ E-SC16-03 Venue room

**Status:** 🔄 waiting for the owner

## Purpose

A room and its seat map.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| venue, room, seats | records | yes | - | - | Hall A, main, 800 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC16-02
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

- [UC-SC16-02](../use-cases/01-plan-and-book/uc-sc16-02-book-venues-and-rooms.md)

## Open questions

None.

---

⬅️ [E-SC16-02 Event budget](e-sc16-02-event-budget.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC16-04 Artist contract](e-sc16-04-artist-contract.md)
