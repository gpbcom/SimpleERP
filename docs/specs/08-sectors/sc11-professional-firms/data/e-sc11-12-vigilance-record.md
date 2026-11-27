🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › ⚖️ [SC11 Professional firms](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC11-12 Vigilance record

# 🗃️ E-SC11-12 Vigilance record

**Status:** ✅ specified

## Purpose

A risk review or suspicion.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| client, date, kind | records | yes | BR-SC11-14 | - | Acme, 12 Nov, suspicion | yes | no |
| access | restricted | yes | - | - | compliance only | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-SC11-15
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

- [UC-SC11-15](../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md)

## Open questions

None.

---

⬅️ [E-SC11-11 Filing](e-sc11-11-filing.md) · ⬆️ [Up](README.md) · ➡️ [E-SC11-13 Access wall](e-sc11-13-access-wall.md)
