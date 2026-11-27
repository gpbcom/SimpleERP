🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-16 Recommendations show their saving and never act alone

# 📏 BR-F22-16 Recommendations show their saving and never act alone

**Status:** ✅ specified

## Statement

A savings recommendation shows the feature, the change, the expected monthly saving, the effect on quality and how it
was computed; nothing changes until the owner applies it, and the saving made is measured afterwards.

## Why

Savings must be decided, not imposed (D479).

## Examples

| Case | Result |
|---|---|
| Use the local model for summaries, expected 42.00 EUR a month | passes: shown, waits for the owner |
| Cache identical questions, expected 12.00 EUR | passes |
| Recommendation applied by itself | fails: never |

## Applies to

- [UC-F22-23 Act on savings recommendations](../use-cases/06-savings-and-kpis/uc-f22-23-act-on-savings-recommendations.md)

## Exceptions

None.

## Configurable

The minimum saving to show, 5.00 EUR a month.

## Open questions

None.

---

⬅️ [BR-F22-15 Self-hosted compute has a cost](br-f22-15-self-hosted-compute-has-a-cost.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F22-17 Re-billing rules per client](br-f22-17-re-billing-rules-per-client.md)
