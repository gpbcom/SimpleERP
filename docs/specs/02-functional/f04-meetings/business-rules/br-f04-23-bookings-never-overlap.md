🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-23 Bookings never overlap

# 📏 BR-F4-23 Bookings never overlap

**Status:** ✅ specified

## Statement

An appointment books a person or a resource only when free, within the booking notice and cancellation windows.

## Why

See [D302](../../../06-decisions/f04-meetings/d302-f4-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| Room booked 10:00 to 11:00 | 10:30 offer hidden |

## Applies to

UC-F4-18

## Exceptions

None.

## Configurable

Notice and cancellation windows.

## Open questions

None.

---

⬅️ [BR-F4-22 Only chosen content leaves](br-f04-22-only-chosen-content-leaves.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-24](br-f04-24-trends-count-only-what-the-reader-may-see-quoted.md)
