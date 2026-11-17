🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T06-04 Tool call record

# 🗃️ E-T06-04 Tool call record

**Status:** ✅ specified

## Purpose

One tool call.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| tool, caller, confirmed, cost | records | yes | REQ-T06-06 | - | quotes.send, U-9, yes, 0.01 | yes | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : REQ-T06-06
```

## Indexes and search

By company and id.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change (T3).

## Import and export

With the company's export (T1).

## Used by

- [T6 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T06-03 Outside connection](e-t06-03-outside-connection.md) · ⬆️ [Up](README.md)
