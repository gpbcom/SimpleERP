🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-23 Online orders stay within kitchen capacity

# 📏 BR-F10-23 Online orders stay within kitchen capacity

**Status:** ✅ specified

## Statement

An online takeaway order is accepted only into a pickup slot that still has capacity, counted in orders or in
preparation minutes as the shop sets it, and only while the kitchen is open to online orders; when the slot is full or
the kitchen has paused orders, the slot is not offered and an order that arrives anyway is refused and refunded.

## Why

Taking more orders than the kitchen can prepare ends in waiting customers and cold food. The kitchen, not the customer,
decides how much it can make. The owner's answer: "Online takeaway"
([D529](../../../06-decisions/f10-point-of-sale/d529-benchmark-gaps-f10-point-of-sale.md)).

## Examples

| Case | Result |
|---|---|
| Slot 12:30 holds 8 orders, 7 taken | 1 more is accepted, then the slot closes |
| Two customers order the last place at once | one is accepted, the other is offered the next slot |
| The kitchen pauses online orders | no slot is offered until it resumes |
| An order for a slot in the past | refused |
| A cancellation frees a place | the slot offers it again |

## Applies to

- [UC-F10-29 Take online takeaway orders](../use-cases/12-takeaway-softpos-and-labels/uc-f10-29-take-online-takeaway-orders.md)
- [E-F10-22 Takeaway order](../data/e-f10-22-takeaway-order.md)
- [UC-F10-10 Prepare orders on kitchen screens](../use-cases/04-restaurant-service/uc-f10-10-prepare-orders-on-kitchen-screens.md)

## Exceptions

A store manager may add capacity to one slot for a known large order, audited.

## Configurable

Yes: the slot length, the capacity per slot and the pause are set per point of sale.

## Open questions

None.

---

⬅️ [BR-F10-22 Staff figures go to their managers](br-f10-22-staff-figures-go-to-their-managers.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F10-24](br-f10-24-tap-to-pay-follows-the-card-terminal-rules-and-the-till-log.md)
