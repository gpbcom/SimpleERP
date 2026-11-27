🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-01 A booking needs a free staff member and cabin

# 📏 BR-SC17-01 A booking needs a free staff member and cabin

**Status:** ✅ specified

## Statement

A salon booking is accepted only for a time when a staff member with the skills of the service and a cabin of the kind
the service needs are both free, including the cleaning time after the previous client. A service with no matching staff
member or cabin is not offered.

## Why

A booking without a skilled person or a free cabin sends the customer away and wastes the slot. The owner asked for
staff and cabin booking ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| Facial 60 min, skilled staff and a free room | the slot is offered |
| Facial, skilled staff but every room taken | no slot |
| Cut, free chair but no staff member with the skill | no slot |
| Room cleaned 15 minutes after a massage | the next booking starts 15 minutes later |
| Cabin out of service | never offered |

## Applies to

- [UC-SC17-01](../use-cases/01-book-staff-and-cabins/uc-sc17-01-set-up-services-staff-and-cabins.md)
- [E-SC17-01 Cabin](../data/e-sc17-01-cabin.md)
- [E-SC17-02 Salon booking](../data/e-sc17-02-salon-booking.md)

## Exceptions

A manager may force a booking at the desk with a warning when a skilled staff member agrees to work through a cleaning
time.

## Configurable

The cleaning time per cabin kind and the skills per service, by the manager.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-SC17-02 Online slots follow staff skills](br-sc17-02-online-slots-follow-staff-skills.md)
