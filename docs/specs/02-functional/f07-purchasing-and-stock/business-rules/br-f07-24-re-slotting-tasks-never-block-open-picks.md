🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-24 Re-slotting tasks never block open picks

# 📏 BR-F7-24 Re-slotting tasks never block open picks

**Status:** 🔄 waiting for the owner

## Statement

A re-slotting move never blocks or delays an open pick: moves are low priority, wait while any open pick needs the item
or the locations concerned, and are done only in the gaps between picks.

## Why

Picks serve customers' orders; a move that blocks them costs more than the gain it brings. The owner asked for slotting
([D526](../../../06-decisions/f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)); picking is set
up in [UC-F7-06](../use-cases/04-pick-pack-and-ship/uc-f07-06-pick-pack-and-ship.md).

## Examples

| Case | Result |
|---|---|
| An approved move and no open pick on the item | the move is offered to an operator |
| An open pick needing the same item | the move waits |
| An open pick needing the destination location | the move waits |
| The night with no picks | the moves are offered first |
| A move postponed 3 times | purchasing is told and re-evaluates it |

## Applies to

- [UC-F7-30](../use-cases/10-consignment-scanning-and-edi/uc-f07-30-optimise-storage-locations.md)
- [E-F7-27 Slotting proposal](../data/e-f07-27-slotting-proposal.md)
- [E-F7-04 Transfer](../data/e-f07-04-transfer.md)
- [E-F7-07 Location](../data/e-f07-07-location.md)

## Exceptions

None.

## Configurable

Yes: the days and hours when moves are offered, by the warehouse manager.

## Open questions

None.

---

⬅️ [BR-F7-23 EDI messages are acknowledged or retried](br-f07-23-edi-messages-are-acknowledged-or-retried.md) ·
⬆️ [Up](README.md)
