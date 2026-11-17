🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏘️ [SC10 Real estate](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC10-19 Rooms are booked within the membership's credits

# 📏 BR-SC10-19 Rooms are booked within the membership's credits

**Status:** 🔄 waiting for the owner

## Statement

A room is booked first from the credits of the member's plan; hours beyond the credits are booked only if the member
accepts to pay them at the room's price, and they are added to the month's invoice. A room cannot be booked twice for
the same slot.

## Why

The credits are what the member paid for; counting them in one place stops disputes about hours and makes the invoice
right. The owner asked for coworking ([D554](../../../06-decisions/sectors/d554-benchmark-gaps-sc10-real-estate.md)).

## Examples

| Case | Result |
|---|---|
| 6 hours of credits, 2 booked | 4 hours left |
| No credits left, 1 extra hour at 12.00 | booked if accepted, added to the invoice |
| Booking cancelled in time | the credits are returned |
| Booking cancelled late | the credits are kept |
| Same room and slot twice | refused |

## Applies to

- [UC-SC10-24](../use-cases/07-short-stays-commercial-and-coworking/uc-sc10-24-run-a-coworking-space.md)
- [E-SC10-20 Membership](../data/e-sc10-20-membership.md)
- [E-SC10-02 Property listing](../data/e-sc10-02-property-listing.md)

## Exceptions

None.

## Configurable

The plans, their credits, the expiry or carry-over of unused credits and the cancellation delay, by the property
manager.

## Open questions

None.

---

⬅️ [BR-SC10-18 Depreciation never creates a rental loss](br-sc10-18-depreciation-never-creates-a-rental-loss.md) ·
⬆️ [Up](README.md)
