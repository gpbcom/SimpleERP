🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T12-05 Tool connection

# 🗃️ E-T12-05 Tool connection

**Status:** ✅ specified

## Purpose

A company's connection to a tool.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| company, connector, credentials name, state | records | yes | REQ-T12-08 | - | Acme, HubSpot, acme_hubspot, active | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

The same item as
[E-F24-02 Tool connection](../../../02-functional/f24-integrations-hub/data/e-f24-02-tool-connection.md)
([D516](../../../06-decisions/foundations/d516-naming-rules-and-the-seven-classes-of-names.md), rule 4).

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T12-08
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

⬅️ [E-T12-04 Connector run](e-t12-04-connector-run.md) · ⬆️ [Up](README.md) ·
➡️ [E-T12-06 Sync state](e-t12-06-sync-state.md)
