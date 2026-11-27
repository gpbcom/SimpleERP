🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-41 An expensive question asks first

# 📏 BR-F3-41 An expensive question asks first

**Status:** ✅ specified

## Statement

A question whose estimated cost is above the threshold shows the estimate and runs only once the user confirms; above
the user's cap it needs the administrator's approval.

## Why

AI costs must never surprise the owner (F22).

## Examples

| Case | Result |
|---|---|
| Estimate 4.20 EUR, threshold 1 EUR | Asked first |
| Estimate 0.02 EUR | Runs |

## Applies to

- [UC-F3-18 See the cost before an expensive question](../use-cases/12-personal-cost-aware-and-learning/uc-f03-18-see-the-cost-before-an-expensive-question.md)

## Exceptions

None.

## Configurable

Threshold and caps per role (default: 1 EUR per question).

## Open questions

None.

---

⬅️ [BR-F3-40 Every figure opens its query](br-f03-40-every-figure-opens-its-query.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-42 Unanswered topics hold no names](br-f03-42-unanswered-topics-hold-no-names.md)
