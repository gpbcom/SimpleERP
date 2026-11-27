🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T12-07 Generated scraper version

# 🗃️ E-T12-07 Generated scraper version

**Status:** ✅ specified

## Purpose

A scraper written by the factory.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| target, version, tests, state | records | yes | REQ-T12-06 | - | portal X, 3, passed, active | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T12-06
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

- [T12 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T12-06 Sync state](e-t12-06-sync-state.md) · ⬆️ [Up](README.md)
