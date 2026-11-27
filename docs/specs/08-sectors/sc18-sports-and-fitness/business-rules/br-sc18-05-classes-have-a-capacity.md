🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-05 Classes have a capacity

# 📏 BR-SC18-05 Classes have a capacity

**Status:** 🔄 waiting for the owner

## Statement

A class has a capacity that does not exceed its room's capacity, and no booking is accepted above it: once the class is
full the next member goes on the waiting list.

## Why

An overfull room is unsafe and a class that is booked beyond its places disappoints members. The owner asked for classes
and waiting lists ([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)).

## Examples

| Case | Result |
|---|---|
| Room of 20, class of 20 | the 21st member goes on the waiting list |
| Class of 25 in a room of 20 | refused |
| A cancellation frees a place | the first on the list is offered it |
| Minimum 5, 3 booked | the owner may cancel in time |
| Coach replaced | the members are told |

## Applies to

- [UC-SC18-05](../use-cases/02-classes-and-waiting-lists/uc-sc18-05-publish-the-class-timetable.md)
- [E-SC18-04 Class](../data/e-sc18-04-class.md)
- [E-SC18-04 Class](../data/e-sc18-04-class.md)

## Exceptions

None.

## Configurable

The capacity, the minimum and the cancellation delay of each class, by the owner.

## Open questions

None.

---

⬅️ [BR-SC18-04](br-sc18-04-cancellation-follows-the-legal-notice-period.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC18-06 Bookings close before the class starts](br-sc18-06-bookings-close-before-the-class-starts.md)
