🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🏛️ [T11 Legal corpora](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-T11-02 Country rule

# 🗃️ E-T11-02 Country rule

**Status:** ✅ specified

## Purpose

A value with its validity dates.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| rule, value, valid from, valid to | records | yes | REQ-T11-02 | - | vat-rates, 20 %, 2014-01-01, - | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T11-02
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

- [T11 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T11-01 Country pack](e-t11-01-country-pack.md) · ⬆️ [Up](README.md) ·
➡️ [E-T11-03 Article version](e-t11-03-article-version.md)
