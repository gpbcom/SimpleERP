🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-14 Financing options with their terms and covenants

# 📏 BR-F23-14 Financing options with their terms and covenants

**Status:** ✅ specified

## Statement

A financing option (loan, leasing, credit line) is simulated with its amount, rate, duration, fees and repayment
schedule; its effect on cash, interest and the covenant ratios is shown month by month.

## Why

Financing decisions need the full cost and the risk of breaking a covenant (D480).

## Examples

| Case | Result |
|---|---|
| Loan 80 000.00 EUR, 4.2 %, 60 months | passes: monthly instalment and interest shown |
| Covenant net debt to EBITDA below 3, reaching 3.4 in March | passes: breach flagged in March |
| Leasing of a van with option to buy | passes: rents and option shown |

## Applies to

- [UC-F23-23 Simulate financing options](../use-cases/06-goals-and-financing/uc-f23-23-simulate-financing-options.md)
- [UC-F23-29 Prepare a forecast pack for the bank](../use-cases/06-goals-and-financing/uc-f23-29-prepare-a-forecast-pack-for-the-bank.md)

## Exceptions

None.

## Configurable

The covenants of each existing loan are entered by accounting.

## Open questions

None.

---

⬅️ [BR-F23-13 Goal seeking moves only the chosen levers](br-f23-13-goal-seeking-moves-only-the-chosen-levers.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F23-15 Accuracy measured, recalibration decided](br-f23-15-accuracy-measured-recalibration-decided.md)
