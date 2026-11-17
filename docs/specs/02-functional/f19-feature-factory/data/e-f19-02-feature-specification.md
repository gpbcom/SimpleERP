🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F19-02 Feature specification

# 🗃️ E-F19-02 Feature specification

**Status:** ✅ specified

## Purpose

The agreed specification.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| request, use cases, screens, data, approved | records | yes | BR-F19-03 | - | FR-12, 4, 3, 2, yes | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-F19-03
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

- [UC-F19-02](../use-cases/01-describe-and-order/uc-f19-02-refine-the-feature-with-the-chatbot.md)

## Open questions

None.

---

⬅️ [E-F19-01 Feature request](e-f19-01-feature-request.md) · ⬆️ [Up](README.md) ·
➡️ [E-F19-03 Feature subscription](e-f19-03-feature-subscription.md)
