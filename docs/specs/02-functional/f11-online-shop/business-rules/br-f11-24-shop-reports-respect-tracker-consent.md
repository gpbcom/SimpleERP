🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-24 Shop reports respect tracker consent

# 📏 BR-F11-24 Shop reports respect tracker consent

**Status:** ✅ specified

## Statement

The funnel and customer reports count sessions without trackers when consent is refused, and show the share measured
without them.

## Why

Analytics must not bypass consent (BR-F11-10).

## Examples

| Case | Result |
|---|---|
| Consent refused | Counted without trackers |

## Applies to

- [UC-F11-29 Read the funnel, customer value and return reasons](../use-cases/10-fulfil-from-stores-and-report/uc-f11-29-read-the-funnel-customer-value-and-return-reasons.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F11-23 Stores fulfil only with stock and capacity](br-f11-23-stores-fulfil-only-with-stock-and-capacity.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F11-25](br-f11-25-donations-reach-the-stated-beneficiary-with-a-receipt.md)
