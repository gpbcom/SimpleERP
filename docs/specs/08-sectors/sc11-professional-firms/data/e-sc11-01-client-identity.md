🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › ⚖️ [SC11 Professional firms](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC11-01 Client identity

# 🗃️ E-SC11-01 Client identity

**Status:** 🔄 waiting for the owner

## Purpose

A client's identity and risk.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| client, kind | records | yes | BR-SC11-02 | - | Acme SA, company | yes | no |
| documents, risk | files, level | yes | - | - | ID, high | yes | no |

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
- [UC-SC11-15](../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [E-SC11-02 Beneficial owner](e-sc11-02-beneficial-owner.md)
