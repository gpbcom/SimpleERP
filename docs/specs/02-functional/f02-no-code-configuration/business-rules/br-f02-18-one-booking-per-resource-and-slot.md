🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-18 One booking per resource and slot

# 📏 BR-F2-18 One booking per resource and slot

**Status:** ✅ specified

## Statement

A resource is booked once per slot, up to its capacity, with its buffer; the engine checks the slot again at
confirmation, so that two bookers never get the same slot.

## Why

Double bookings are the first complaint of hotels, practices and training centres.

## Examples

| Case | Result |
|---|---|
| Room 204 booked twice at the same time | Second refused |
| Training room of capacity 12, 11 seats taken | One more accepted |
| Buffer 5 minutes after 10:15 | Next booking at 10:20 |

## Applies to

- [UC-F2-18 Make a record type bookable](../use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md)
- [UC-F2-19 Book a resource](../use-cases/08-views-and-bookings/uc-f02-19-book-a-resource.md)
- [UC-F4-21 Book a meeting room and equipment](../../f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-21-book-a-meeting-room-and-equipment.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-17 What the AI builds is a draft](br-f02-17-ai-built-items-are-drafts.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-19 Booking rules decide who books what and when](br-f02-19-booking-rules-decide-who-books-what-and-when.md)
