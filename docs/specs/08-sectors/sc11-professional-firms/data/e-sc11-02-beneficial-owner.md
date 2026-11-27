🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › ⚖️ [SC11 Professional firms](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC11-02 Beneficial owner

# 🗃️ E-SC11-02 Beneficial owner

**Status:** ✅ specified

## Purpose

A person behind a client.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| client, person, share | records | yes | - | - | Acme SA, M. K., 60 % | yes | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC11-01
```

## Indexes and search

By number, date, partner.

## Retention

5 years from the end of the relationship (Code monétaire et financier L561-12);
[CR-FR-149 Anti-money-laundering vigilance](../../../10-country-packs/france/professional-firms/cr-fr-149-aml-vigilance.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-SC11-01](../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md)

## Open questions

None.

---

⬅️ [E-SC11-01 Client identity](e-sc11-01-client-identity.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC11-03 Conflict check](e-sc11-03-conflict-check.md)
