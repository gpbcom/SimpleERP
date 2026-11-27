🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › ⚖️ [SC11 Professional firms](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC11-02 Beneficial owner

# 🗃️ E-SC11-02 Beneficial owner

**Status:** 🔄 waiting for the owner

## Purpose

A person behind a client.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| client, person, share | records | yes | - | - | Acme SA, M. K., 60 % | yes | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC11-01
```

## Indexes and search

(Proposed) By number, date, partner.

## Retention

(Proposed) For the anti-money-laundering period after the relationship ends;
[CR-FR-149 Anti-money-laundering vigilance](../../../10-country-packs/france/professional-firms/cr-fr-149-aml-vigilance.md).

## Audit

Every change.

## Import and export

(Proposed) CSV, FEC where relevant.

## Used by

- [UC-SC11-01](../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md)

## Open questions

None.

---

⬅️ [E-SC11-01 Client identity](e-sc11-01-client-identity.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC11-03 Conflict check](e-sc11-03-conflict-check.md)
