🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-14 Data costs within their budget

# 📏 BR-F17-14 Data costs within their budget

**Status:** ✅ specified

## Statement

Every paid data provider's spend is counted against its budget in F22; at 80 % of the budget the owner is
warned, and at 100 % collection from that provider stops until the owner raises the budget.

## Why

Paid sources cost money that must be followed with every other platform cost (D474).

## Examples

| Case | Result |
|---|---|
| Provider P at 410.00 EUR of a 500.00 EUR monthly budget | passes: warning at 82 % |
| Provider P reaching 500.00 EUR on 2026-11-24 | passes: collection stops until December |
| Owner raises the budget to 600.00 EUR | passes: collection resumes |

## Applies to

- [UC-F17-22 Follow data-provider costs against the budget](../use-cases/01-set-up-and-profiles/uc-f17-22-follow-data-provider-costs-against-the-budget.md)
- [UC-F17-10 Connect paid data providers](../use-cases/01-set-up-and-profiles/uc-f17-10-connect-paid-data-providers.md)

## Exceptions

None.

## Configurable

The owner sets each provider's budget in F22.

## Open questions

None.

---

⬅️ [BR-F17-13 Tender opportunities matched to the company](br-f17-13-tender-opportunities-matched-to-the-company.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F17-15 Price suggestions need approval](br-f17-15-price-suggestions-need-approval.md)
