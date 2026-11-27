🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-19 Booking rules decide who books what and when

# 📏 BR-F2-19 Booking rules decide who books what and when

**Status:** ✅ specified

## Statement

Each bookable record type sets how early and late one may book and cancel, the longest booking, who may book (users,
portal users, public), and what needs approval.

## Why

The same engine serves rooms, appointments and venues with their own rules.

## Examples

| Case | Result |
|---|---|
| Book up to 60 days ahead | Day 61 refused |
| Cancel 24 h before | 3 h before refused |
| Approval for bookings over 3 days | 4-day booking waits |

## Applies to

- [UC-F2-18 Make a record type bookable](../use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md)
- [UC-F2-19 Book a resource](../use-cases/08-views-and-bookings/uc-f02-19-book-a-resource.md)
- [UC-F4-21 Book a meeting room and equipment](../../f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-21-book-a-meeting-room-and-equipment.md)

## Exceptions

None.

## Configurable

Every value, per bookable record type.

## Open questions

None.

---

⬅️ [BR-F2-18 One booking per resource and slot](br-f02-18-one-booking-per-resource-and-slot.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-20](br-f02-20-a-portal-shows-only-the-chosen-fields-of-the-persons-own-records.md)
