🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-06 Bookings close before the class starts

# 📏 BR-SC18-06 Bookings close before the class starts

**Status:** ✅ specified

## Statement

A class booking is accepted until the closing time set for the class, which is before the class starts; after it the
member can neither book nor cancel without a credit being lost, and the coach's list is fixed at that time.

## Why

A list that changes until the last minute leaves the coach with the wrong number and the room unprepared. The owner
asked for classes and waiting lists
([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)).

## Examples

| Case | Result |
|---|---|
| Closing time 2 hours before, 1 hour tried | refused |
| Cancel before the closing time | credit returned |
| Cancel after the closing time | credit lost |
| Class full | waiting list offered |
| Member frozen | no booking |

## Applies to

- [UC-SC18-06 Book a class](../use-cases/02-classes-and-waiting-lists/uc-sc18-06-book-a-class.md)
- [E-SC18-05 Class booking](../data/e-sc18-05-class-booking.md)
- [E-SC18-05 Class booking](../data/e-sc18-05-class-booking.md)

## Exceptions

The owner may let a member in after the closing time with a recorded reason.

## Configurable

The closing time of each class and the rule for missed classes, by the owner.

## Open questions

None.

---

⬅️ [BR-SC18-05 Classes have a capacity](br-sc18-05-classes-have-a-capacity.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC18-07 Freed places go to the first on the list](br-sc18-07-freed-places-go-to-the-first-on-the-list.md)
