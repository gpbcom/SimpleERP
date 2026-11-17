🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💻 [SC14 IT and software](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC14-12 Dunning steps

# 📏 BR-SC14-12 Dunning steps

**Status:** ✅ specified

## Statement

A failed payment follows the set steps: retry, reminder, suspension warning, suspension; late penalties apply to
businesses; in France:
[CR-FR-019 Late-payment penalties](../../../10-country-packs/france/invoicing/cr-fr-019-late-payment-penalties.md).

## Why

See [D356](../../../06-decisions/sectors/d356-it-and-software-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Card declined | Retry in 3 days, email |

## Applies to

Every SC14 use case concerned.

## Exceptions

None.

## Configurable

Steps.

## Open questions

None.

---

⬅️ [BR-SC14-11 VAT by the customer's country](br-sc14-11-vat-by-the-customer-country.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC14-13 Health score from usage](br-sc14-13-health-score-from-usage.md)
