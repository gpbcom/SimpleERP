🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-15 Price suggestions need approval

# 📏 BR-F17-15 Price suggestions need approval

**Status:** ✅ specified

## Statement

A suggestion drawn from the price index never changes a price by itself: it proposes a new price and a date for an F6
price list, and only the owner (or a role they grant) approves it; the suggestion shows the like-for-like prices it
rests on.

## Why

Prices are a business decision (D474); comparisons must be like for like (BR-F17-08).

## Examples

| Case | Result |
|---|---|
| Index 104 for Plans, suggestion -4 % on Plan Pro, owner approves | passes: new price list from 2026-12-01 |
| Suggestion approved by a sales person without the right | fails: refused |
| Suggestion without its price points | fails: not shown |

## Applies to

- [UC-F17-23 Suggest price-list changes from the price index](../use-cases/06-price-intelligence/uc-f17-23-suggest-price-list-changes-from-the-price-index.md)

## Exceptions

None.

## Configurable

The threshold that triggers a suggestion, a gap of 5 %.

## Open questions

None.

---

⬅️ [BR-F17-14 Data costs within their budget](br-f17-14-data-costs-within-their-budget.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F17-16 Call topics feed cards without people](br-f17-16-call-topics-feed-cards-without-people.md)
