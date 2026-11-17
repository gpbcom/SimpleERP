🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F21-04 Module activation

# 🗃️ E-F21-04 Module activation

**Status:** ✅ specified

## Purpose

A module on or off.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| company, module, state, changed by | records | yes | BR-F21-02, BR-F21-04 | off | Acme, F10, on, admin | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> On : UC-F21-04
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

- [UC-F21-04](../use-cases/02-modules/uc-f21-04-switch-modules-on-in-one-click.md)
- [UC-F21-05](../use-cases/02-modules/uc-f21-05-understand-a-module-s-dependencies.md)
- [UC-F21-06](../use-cases/02-modules/uc-f21-06-switch-a-module-off-and-keep-its-data.md)
- [UC-F21-11](../use-cases/02-modules/uc-f21-11-follow-a-module-s-short-guide.md)
- [UC-F21-18](../use-cases/02-modules/uc-f21-18-see-what-each-module-costs-in-the-hosted-edition.md)

## Open questions

None.

---

⬅️ [E-F21-03 Set-up template](e-f21-03-set-up-template.md) · ⬆️ [Up](README.md) ·
➡️ [E-F21-05 Module dependency](e-f21-05-module-dependency.md)
