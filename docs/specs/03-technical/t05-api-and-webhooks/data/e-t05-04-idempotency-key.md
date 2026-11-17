🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-T05-04 Idempotency key

# 🗃️ E-T05-04 Idempotency key

**Status:** ✅ specified

## Purpose

A write's key and result.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| key, client, result, expires | records | yes | REQ-T05-02 | - | k-81, shop, 201, 24 h | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : REQ-T05-02
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

- [T5 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T05-03 Webhook delivery](e-t05-03-webhook-delivery.md) · ⬆️ [Up](README.md)
