🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F4-10 Chat channel

# 🗃️ E-F4-10 Chat channel

**Status:** ✅ specified

## Purpose

A channel or direct conversation.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name | text | yes | - | - | Site Lyon | no | no |
| members | users, guests | yes | - | - | 12 | yes | no |
| retention | months | yes | storage limitation (country pack) | 24 | 24 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F4-17
```

## Indexes and search

By name, date, owner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

CSV.

## Used by

- [UC-F4-17](../use-cases/10-benchmark-additions/uc-f04-17-chat-with-colleagues.md)

## Open questions

None.

---

⬅️ [E-F4-09 Scheduled digest](e-f04-09-scheduled-digest.md) · ⬆️ [Up](README.md) ·
➡️ [E-F4-11 Appointment type](e-f04-11-appointment-type.md)
