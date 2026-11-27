🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-10 Orders go to their preparation station

# 📏 BR-F10-10 Orders go to their preparation station

**Status:** ✅ specified

## Statement

Each item goes to the preparation screen or printer of its category; a cancelled item is sent as cancelled.

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| Steak and wine | Steak to the kitchen screen, wine to the bar |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

Stations and categories.

## Open questions

None.

---

⬅️ [BR-F10-09 Weighed items come from the scale](br-f10-09-weighed-items-from-the-scale.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-11 Self-order only while the session is open](br-f10-11-self-order-while-open.md)
