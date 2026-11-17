🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F21-12 Provider set-up

# 🗃️ E-F21-12 Provider set-up

**Status:** ✅ specified

## Purpose

An IT provider's reusable set-up.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| provider, template, clients | records | yes | - | - | NetServ, care pack, 12 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F21-19
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

- [UC-F21-19](../use-cases/04-learn-and-improve/uc-f21-19-reuse-a-set-up-for-several-clients.md)

## Open questions

None.

---

⬅️ [E-F21-11 Legal check item](e-f21-11-legal-check-item.md) · ⬆️ [Up](README.md) ·
➡️ [E-F21-13 Onboarding figure](e-f21-13-onboarding-figure.md)
