🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-15 A delivery date is committed and kept

# 📏 BR-F19-15 A delivery date is committed and kept

**Status:** 🔄 waiting for the owner

## Statement

When the quote is accepted, the factory commits to a delivery date for the first try-out; a delay is announced before
the date with the new date and the reason, and an order more than (Proposed) 20 business days late may be cancelled by
the customer without charge.

## Why

Customers plan around a feature's arrival (D476).

## Examples

| Case | Result |
|---|---|
| Specification approved on 2026-11-12, delivery committed for 2026-12-03 ((Proposed) 15 business days) | passes |
| Delay announced on 2026-12-01 with a new date of 2026-12-10 | passes |
| Delay announced after the date has passed | fails: counted as missed and reported on the board |
| Order 25 business days late | passes: owner may cancel, nothing charged |

## Applies to

- [UC-F19-21 Commit to a delivery date and handle delays](../use-cases/01-describe-and-order/uc-f19-21-commit-to-a-delivery-date-and-handle-delays.md)
- [UC-F19-03 Accept the quote](../use-cases/01-describe-and-order/uc-f19-03-accept-the-quote.md)
- [UC-F19-04 Generate the plugin in the sandbox](../use-cases/02-build-and-check/uc-f19-04-generate-the-plugin-in-the-sandbox.md)
- [UC-F19-19 Follow features, costs and credits](../use-cases/05-bill-and-credit/uc-f19-19-follow-features-costs-and-credits.md)

## Exceptions

Delays caused by the customer (answers awaited) move the date by the same time.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-14 The AI is disclosed and overseen](br-f19-14-ai-disclosed-and-overseen.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F19-16 Nothing charged without an accepted feature](br-f19-16-nothing-charged-without-an-accepted-feature.md)
