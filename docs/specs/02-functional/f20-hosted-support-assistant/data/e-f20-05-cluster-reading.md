🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F20-05 Cluster reading

# 🗃️ E-F20-05 Cluster reading

**Status:** ✅ specified

## Purpose

A status, log or metric excerpt.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| request, kind, excerpt | records | yes | BR-F20-07 | - | R-41, events, OOMKilled | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : BR-F20-07
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

- [UC-F20-04](../use-cases/02-diagnose-and-fix/uc-f20-04-diagnose-on-the-cluster.md)
- [UC-F20-14](../use-cases/02-diagnose-and-fix/uc-f20-14-investigate-slowness.md)

## Open questions

None.

---

⬅️ [E-F20-04 Diagnosis](e-f20-04-diagnosis.md) · ⬆️ [Up](README.md) ·
➡️ [E-F20-06 Fix proposal](e-f20-06-fix-proposal.md)
