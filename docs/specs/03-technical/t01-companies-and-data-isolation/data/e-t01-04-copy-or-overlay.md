🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T01-04 Copy or overlay

# 🗃️ E-T01-04 Copy or overlay

**Status:** ✅ specified

## Purpose

An isolated copy or scenario overlay.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| company, kind, purpose, expires | records | yes | REQ-T01-05 | - | Acme, overlay, F23 S-4, 2026-12-01 | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T01-04
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

- [T1 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T01-03 Provider session](e-t01-03-provider-session.md) · ⬆️ [Up](README.md)
