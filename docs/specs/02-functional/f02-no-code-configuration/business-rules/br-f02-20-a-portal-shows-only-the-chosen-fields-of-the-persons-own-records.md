🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-20 A portal shows only the chosen fields of the person's own records

# 📏 BR-F2-20 A portal shows only the chosen fields of the person's own records

**Status:** ✅ specified

## Statement

A record type on a portal shows only the fields and actions the configurator chose, only on records linked to the
signed-in contact; fields of other people's health, pay or identity data can never be chosen.

## Why

Portals reach outside people; one mistake exposes someone else's data.

## Examples

| Case | Result |
|---|---|
| Family member opens the care log | Her relative's visits only |
| Configurator adds another person's health notes | Refused |

## Applies to

- [UC-F2-20 Expose a record type on a portal](../use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-19 Booking rules decide who books what and when](br-f02-19-booking-rules-decide-who-books-what-and-when.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F2-21](br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md)
