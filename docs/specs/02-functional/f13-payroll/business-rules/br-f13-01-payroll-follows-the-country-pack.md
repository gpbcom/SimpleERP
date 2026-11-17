🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-01 Payroll follows the country pack

# 📏 BR-F13-01 Payroll follows the country pack

**Status:** ✅ specified

## Statement

Every legal value of payroll (rates, ceilings, payslip format, declarations, withholding, minimum wage, end-of-contract
documents) comes from the country pack, dated by the period it applies to; in France:
[CR-FR-182 The payslip](../../../10-country-packs/france/payroll/cr-fr-182-payslip.md),
[CR-FR-183 Monthly social declaration (DSN)](../../../10-country-packs/france/payroll/cr-fr-183-dsn-monthly-declaration.md),
[CR-FR-184 Withholding tax on wages](../../../10-country-packs/france/payroll/cr-fr-184-withholding-tax.md),
[CR-FR-185 Minimum wage (SMIC)](../../../10-country-packs/france/payroll/cr-fr-185-minimum-wage.md),
[CR-FR-186 End-of-contract documents](../../../10-country-packs/france/payroll/cr-fr-186-end-of-contract-documents.md),
[CR-FR-187 Equal-pay index](../../../10-country-packs/france/payroll/cr-fr-187-equal-pay-index.md).

## Why

See [D365](../../../06-decisions/f13-payroll/d365-payroll-coverage.md).

## Examples

| Case | Result |
|---|---|
| January pay | January's rates used |

## Applies to

Every F13 use case concerned.

- [UC-F13-04 Compute gross to net](../use-cases/02-monthly-pay-run/uc-f13-04-compute-gross-to-net.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F13-02 Rates dated by period](br-f13-02-rates-dated-by-period.md)
