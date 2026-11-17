🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-T04-02 Plugin package

# 🗃️ E-T04-02 Plugin package

**Status:** ✅ specified

## Purpose

A signed plugin version.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| plugin, version, signature, permissions | records | yes | REQ-T04-04 | - | Gate Booking, 2.3, sig, calendars | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T04-03
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

- [T4 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T04-01 Module](e-t04-01-module.md) · ⬆️ [Up](README.md) ·
➡️ [E-T04-03 Plugin installation](e-t04-03-plugin-installation.md)
