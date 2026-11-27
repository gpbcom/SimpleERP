🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-02 No order without a prior commitment

# 📏 BR-SC20-02 No order without a prior commitment

**Status:** ✅ specified

## Statement

An order is placed only with a commitment number, and a commitment is made only when the credit left on its chapter
covers it. An order without a commitment is refused.

## Why

Committing before ordering keeps spending within the credits voted and keeps the officer's and accountant's controls in
order ([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). The
France-pack rule is
[CR-FR-250 Public accounting M57](../../../10-country-packs/france/accounting/cr-fr-250-public-accounting-m57.md):
the mayor or the president keeps the commitment accounts, under a joint ministerial order, since the budget year 2026 (CGCT L1612-38, created by Ordonnance n° 2025-526, which repealed L2342-2), and the accountant pays only within the credits opened (L1612-39).

## Examples

| Case | Result |
|---|---|
| Credit left covers the amount | commitment made |
| Credit left too low | refused |
| Order without a number | refused |
| Order cheaper than planned | unused amount released |
| Multi-year contract | commitment split by year |

## Applies to

- [UC-SC20-02](../use-cases/01-public-accounting/uc-sc20-02-commit-expenditure.md)
- [E-SC20-02 Commitment](../data/e-sc20-02-commitment.md)
- [E-SC20-02 Commitment](../data/e-sc20-02-commitment.md)
- [E-SC20-01 Budget](../data/e-sc20-01-budget.md)

## Exceptions

None.

## Configurable

The amount above which the authorising officer's own signature is needed, set by the body.

## Open questions

None.

---

⬅️ [BR-SC20-01 Expenditure stays within voted credits](br-sc20-01-expenditure-stays-within-voted-credits.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC20-03](br-sc20-03-orders-are-signed-by-the-authorising-officer.md)
