🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F24-10 Connector incident

# 🗃️ E-F24-10 Connector incident

**Status:** ✅ specified

## Purpose

An outside API change or failure.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| connector, cause, state | records | yes | BR-F24-09 | - | Pipedrive, field renamed, repaired | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Repaired : UC-F24-16
  Repaired --> Paused : BR-F24-09
  Paused --> Repaired : UC-F24-16
  Repaired --> Flagged : UC-F24-16
  Flagged --> Repaired : UC-F24-16
  Repaired --> Failed : UC-F24-15
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

- [UC-F24-15](../use-cases/04-run-and-control/uc-f24-15-follow-each-connector-s-health-and-sync-log.md)
- [UC-F24-16](../use-cases/04-run-and-control/uc-f24-16-handle-an-outside-api-change-or-error.md)

## Open questions

None.

---

⬅️ [E-F24-09 Connector action](e-f24-09-connector-action.md) · ⬆️ [Up](README.md) ·
➡️ [E-F24-11 Connector category](e-f24-11-connector-category.md)
