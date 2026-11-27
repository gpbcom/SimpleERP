🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T01-01 Company

# 🗃️ E-T01-01 Company

**Status:** ✅ specified

## Purpose

A company served by SimpleERP.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| id, name, country, plan, placement | records | yes | REQ-T01-01 | - | C-12, Acme, FR, business, shared | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

The same item as [E-F1-01 Company](../../../02-functional/f01-administration/data/e-f01-01-company.md)
([D516](../../../06-decisions/foundations/d516-naming-rules-and-the-seven-classes-of-names.md), rule 4).

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T01-01
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

⬆️ [Up](README.md) · ➡️ [E-T01-02 Company stores](e-t01-02-company-stores.md)
