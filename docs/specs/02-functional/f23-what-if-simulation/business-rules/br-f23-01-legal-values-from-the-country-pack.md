🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-01 Legal values from the country pack

# 📏 BR-F23-01 Legal values from the country pack

**Status:** ✅ specified

## Statement

A scenario takes taxes, rates, thresholds and wages from the country pack at each simulated date, including changes
already announced; in France for example:
[CR-FR-046 Headcount thresholds](../../../10-country-packs/france/labour/cr-fr-046-headcount-thresholds.md),
[CR-FR-008 VAT rates](../../../10-country-packs/france/tax-and-vat/cr-fr-008-vat-rates.md),
[CR-FR-185 Minimum wage (SMIC)](../../../10-country-packs/france/payroll/cr-fr-185-minimum-wage.md),
[CR-FR-064 Accounting frameworks of the books](../../../10-country-packs/france/accounting/cr-fr-064-accounting-frameworks.md).

## Why

See [D402](../../../06-decisions/f23-what-if-simulation/d402-impact-through-the-real-rules.md).

## Examples

| Case | Result |
|---|---|
| Hiring takes the company to 50 people | Threshold crossed shown with its duties |

## Applies to

Every F23 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [BR-F23-02 The baseline comes from history and plans](br-f23-02-baseline-from-history-and-plans.md)
