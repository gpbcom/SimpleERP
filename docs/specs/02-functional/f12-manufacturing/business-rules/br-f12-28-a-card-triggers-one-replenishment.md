🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-28 A card triggers one replenishment

# 📏 BR-F12-28 A card triggers one replenishment

**Status:** ✅ specified

## Statement

A kanban card creates exactly one replenishment while it is Empty or Replenishing; scanning it again, from the same or
another tablet, creates nothing more, and the card is Full again only when the container it stands for is received.

## Why

A pull system works only if one empty container means one order. Double scans would flood the supplier and hide the real
consumption. The owner's answer: "Kanban pull"
([D531](../../../06-decisions/f12-manufacturing/d531-benchmark-gaps-f12-manufacturing.md)).

## Examples

| Case | Result |
|---|---|
| A full card is scanned empty | one replenishment is created |
| The same card is scanned empty again | nothing more is created |
| The container is received and the card scanned | the card is Full |
| A suspended card is scanned | refused, it is suspended |
| Two tablets scan the same card offline | one replenishment is made after the sync |

## Applies to

- [UC-F12-33 Replenish with kanban cards](../use-cases/14-cad-kanban-mps-and-tools/uc-f12-33-replenish-with-kanban-cards.md)
- [E-F12-31 Kanban card](../data/e-f12-31-kanban-card.md)
- [UC-F12-26 Keep working on the tablet without the network](../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md)

## Exceptions

A planner may force a second replenishment for an urgent need, as a separate order, audited.

## Configurable

Yes: the container size, the source and the number of cards are set per item and location.

## Open questions

None.

---

⬅️ [BR-F12-27 Only released revisions reach the shop floor](br-f12-27-only-released-revisions-reach-the-shop-floor.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F12-29 The MPS stays within the capacity plan](br-f12-29-the-mps-stays-within-the-capacity-plan.md)
