🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-02 One session per till, counted at closing

# 📏 BR-F10-02 One session per till, counted at closing

**Status:** ✅ specified

## Statement

A till sells only within an open session; its cash payment method is not shared with another till; closing counts the
cash and a difference over the threshold needs a reason.

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| Cash counted 2.40 short, threshold 5.00 | Closed, difference logged |
| 12.00 short | Reason required, the manager is told |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

The difference threshold, per till.

## Open questions

None.

---

⬅️ [BR-F10-01 The till follows the country pack](br-f10-01-till-follows-the-country-pack.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-03 Cash within the legal limit](br-f10-03-cash-within-the-legal-limit.md)
