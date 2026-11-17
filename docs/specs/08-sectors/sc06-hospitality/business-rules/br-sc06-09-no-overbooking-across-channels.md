🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC06-09 No overbooking across channels

# 📏 BR-SC06-09 No overbooking across channels

**Status:** ✅ specified

## Statement

Room availability is one stock across the direct channel and every channel manager connector: rooms are bookable
resources of the shared booking engine, which takes one booking per resource and slot,
[BR-F2-18 One booking per resource and slot](../../../02-functional/f02-no-code-configuration/business-rules/br-f02-18-one-booking-per-resource-and-slot.md);
a booking closes the room type everywhere at once.

## Why

See [D332](../../../06-decisions/sectors/d332-hospitality-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Last double room booked online | Closed on all channels |

## Applies to

Every SC06 use case concerned.

## Exceptions

None.

## Configurable

Overbooking allowance, by default none.

## Open questions

None.

---

⬅️ [BR-SC06-08 Staff meals recorded](br-sc06-08-staff-meals-recorded.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC06-10 Rates by date and room type](br-sc06-10-rates-by-date-and-room-type.md)
