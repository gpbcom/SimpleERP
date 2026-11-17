🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-04 Never below the minimum wage

# 📏 BR-F13-04 Never below the minimum wage

**Status:** ✅ specified

## Statement

A pay below the minimum wage for the hours worked blocks the run; in France:
[CR-FR-185 Minimum wage (SMIC)](../../../10-country-packs/france/payroll/cr-fr-185-minimum-wage.md).

## Why

See [D365](../../../06-decisions/f13-payroll/d365-payroll-coverage.md).

## Examples

| Case | Result |
|---|---|
| Base below the minimum | Anomaly, run blocked |

## Applies to

Every F13 use case concerned.

- [UC-F13-22 Pay an apprentice or an intern](../use-cases/07-schemes-and-special-contracts/uc-f13-22-pay-an-apprentice-or-an-intern.md)
- [UC-F13-07 Check and approve the pay run](../use-cases/02-monthly-pay-run/uc-f13-07-check-and-approve-the-pay-run.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F13-03 Inputs closed before the run](br-f13-03-inputs-closed-before-the-run.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-05 Collective-agreement rules applied](br-f13-05-agreement-rules-applied.md)
