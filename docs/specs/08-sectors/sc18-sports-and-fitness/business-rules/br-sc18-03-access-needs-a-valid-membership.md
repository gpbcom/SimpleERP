🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-03 Access needs a valid membership

# 📏 BR-SC18-03 Access needs a valid membership

**Status:** 🔄 waiting for the owner

## Statement

A member enters only while the membership is Active, not frozen and not overdue beyond the delay, inside the hours of
the plan and, where the activity needs it, with a valid medical certificate; otherwise the door stays closed and the
denial is recorded with its reason.

## Why

An entry for someone who has not paid or who is not covered is a cost and a risk for the club. The owner asked for
access control ([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)).

## Examples

| Case | Result |
|---|---|
| Active, up to date | granted |
| Frozen | denied |
| Dues overdue beyond the delay | denied with the amount |
| Class booked for this hour | granted for the class |
| Denied and staff override with a reason | overridden |

## Applies to

- [UC-SC18-03](../use-cases/01-memberships-and-access/uc-sc18-03-control-access-at-the-door.md)
- [E-SC18-03 Access event](../data/e-sc18-03-access-event.md)
- [E-SC18-03 Access event](../data/e-sc18-03-access-event.md)

## Exceptions

A staff member may let in a member who is denied by mistake, with a recorded reason.

## Configurable

The delay after an unpaid due, the hours of each plan and the activities that need a certificate, by the owner.

## Open questions

None.

---

⬅️ [BR-SC18-02 Direct debits need a signed mandate](br-sc18-02-direct-debits-need-a-signed-mandate.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC18-04](br-sc18-04-cancellation-follows-the-legal-notice-period.md)
