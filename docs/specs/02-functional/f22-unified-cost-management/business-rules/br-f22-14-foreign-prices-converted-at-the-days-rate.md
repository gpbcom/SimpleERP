🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-14 Foreign prices converted at the day's rate

# 📏 BR-F22-14 Foreign prices converted at the day's rate

**Status:** 🔄 waiting for the owner

## Statement

A provider's prices may be in a foreign currency; each usage record keeps the original amount and currency, and its cost
in the company's currency at the rate of the day of use from the rate source; reports show both.

## Why

Providers bill in USD (D479); the books are in the company's currency.

## Examples

| Case | Result |
|---|---|
| 1 000 tokens at 0.0060 USD on 2026-11-12, rate 0.9200 | passes: 0.00552 EUR, USD kept |
| Provider invoice in USD matched against metered USD | passes: gap computed in USD |
| Rate missing for a day | passes: previous day's rate, flagged |

## Applies to

- [UC-F22-21 Record a provider's prices in a foreign currency](../use-cases/01-see-and-set-up/uc-f22-21-record-a-providers-prices-in-a-foreign-currency.md)
- [UC-F22-01 See all platform costs in one place](../use-cases/01-see-and-set-up/uc-f22-01-see-all-platform-costs-in-one-place.md)
- [UC-F22-04 Register a paid provider and its prices](../use-cases/01-see-and-set-up/uc-f22-04-register-a-paid-provider-and-its-prices.md)
- [UC-F22-13 Match suppliers' invoices in accounting](../use-cases/04-accounting/uc-f22-13-match-suppliers-invoices-in-accounting.md)

## Exceptions

None.

## Configurable

The rate source, (Proposed) the European Central Bank's reference rates.

## Open questions

None.

---

⬅️ [BR-F22-13 Anomalies flagged](br-f22-13-anomalies-flagged.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F22-15 Self-hosted compute has a cost](br-f22-15-self-hosted-compute-has-a-cost.md)
