🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-16 Call topics feed cards without people

# 📏 BR-F17-16 Call topics feed cards without people

**Status:** ✅ specified

## Statement

Call topics from F4 feed battle cards only as counts and themes per competitor; no recording, transcript excerpt or
person's name reaches a card.

## Why

Recordings are announced and proportionate (CR-FR-059, CR-FR-207) and the module never profiles people (BR-F17-04).

## Examples

| Case | Result |
|---|---|
| 14 calls mention "Rival SA cheaper" | passes: theme "price objection", count 14 |
| Proposal quoting a customer's words with their name | fails: name removed |
| Link to a recording on a card | fails: removed |

## Applies to

- [UC-F17-24 Feed battle cards from call topics](../use-cases/07-sales-enablement/uc-f17-24-feed-battle-cards-from-call-topics.md)
- [UC-F17-13 Prepare battle cards for sales](../use-cases/03-analyse-and-arm-sales/uc-f17-13-prepare-battle-cards-for-sales.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F17-15 Price suggestions need approval](br-f17-15-price-suggestions-need-approval.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F17-17 Ads come only from public ad libraries](br-f17-17-ads-come-only-from-public-ad-libraries.md)
