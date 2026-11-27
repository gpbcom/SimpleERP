🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-02 Online slots follow staff skills

# 📏 BR-SC17-02 Online slots follow staff skills

**Status:** ✅ specified

## Statement

Online slots are offered only where a staff member who has every skill of the chosen services is free for the whole
duration of the services, in the order chosen. 'Anyone' means the first free staff member with those skills, never one
without them.

## Why

A customer who books a colour with a person who cannot do it gets a bad service or a cancelled visit. The owner asked
for staff and cabin booking ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| Colour needs skill Colour, three staff, one with the skill | only that person's slots |
| 'Anyone' chosen | the first free skilled person is assigned |
| Cut then colour, 45 + 90 minutes | two chained slots held together |
| Last slot taken meanwhile | refused, nearest slots shown |
| A beginner with skill level Junior | only the services of their level are offered |

## Applies to

- [UC-SC17-02](../use-cases/01-book-staff-and-cabins/uc-sc17-02-let-customers-book-online.md)
- [E-SC17-02 Salon booking](../data/e-sc17-02-salon-booking.md)
- [E-SC17-01 Cabin](../data/e-sc17-01-cabin.md)

## Exceptions

The manager may book a service at the desk on a staff member without the skill, with a warning, when the customer asks
for that person by name.

## Configurable

The hold time (ten minutes by default), the free cancellation time and the slot step, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-01](br-sc17-01-a-booking-needs-a-free-staff-member-and-cabin.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC17-03 Desk bookings send the same confirmation](br-sc17-03-desk-bookings-send-the-same-confirmation.md)
