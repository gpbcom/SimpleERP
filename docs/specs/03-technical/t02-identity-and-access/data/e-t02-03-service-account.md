🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T02-03 Service account

# 🗃️ E-T02-03 Service account

**Status:** ✅ specified

## Purpose

A worker's or agent's identity.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name, rights, owner | records | yes | REQ-T02-05 | - | devops-agent, issues write, U47 | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T02-03
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

- [T2 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T02-02 Role and policy](e-t02-02-role-and-policy.md) · ⬆️ [Up](README.md) ·
➡️ [E-T02-04 Federated identity provider](e-t02-04-federated-identity-provider.md)
