🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-07 Freed places go to the first on the list

# 📏 BR-SC18-07 Freed places go to the first on the list

**Status:** ✅ specified

## Statement

A freed place goes to the first member on the waiting list who is able to take it, in the order they joined; a member
skipped (no credit, no answer) keeps their place in the order of the next free place only if the rule says so, and a
place is never given out of order without a recorded reason.

## Why

A list that is not followed in order breeds complaints, and an empty place is lost income. The owner asked for waiting
lists ([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)).

## Examples

| Case | Result |
|---|---|
| Three on the list, one place freed | the first is offered it |
| First does not answer in 30 minutes | the second is offered it |
| First has no credit | skipped and told |
| Coach adds a member by hand | recorded with a reason |
| Class about to close | offer ends at the closing time |

## Applies to

- [UC-SC18-07](../use-cases/02-classes-and-waiting-lists/uc-sc18-07-handle-the-waiting-list.md)
- [E-SC18-05 Class booking](../data/e-sc18-05-class-booking.md)

## Exceptions

None.

## Configurable

The time to accept and whether a skipped member keeps their place, by the owner.

## Open questions

None.

---

⬅️ [BR-SC18-06 Bookings close before the class starts](br-sc18-06-bookings-close-before-the-class-starts.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC18-08 Coaches hold the diploma for the activity](br-sc18-08-coaches-hold-the-diploma-for-the-activity.md)
