🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D457 Gaps and improvements round: what applies to every block

# 📜 D457 Gaps and improvements round: what applies to every block

**Status:** ✅ decided

## Context

The owner asked on 2026-11-12 at 20:16 for a round of interviews on each functional block and its sectors, to find gaps
and improvements, with an example screenshot for every view. A read-only analysis prepared the candidates; the answers
are kept word for word in the ticket's interview log.

## Options

- Screen states: empty, loading, read-only, offline.
- Use-case depth: all, the thinnest, or none.
- Proposals: per block, all at once, or later.
- Shared capabilities for gaps several sectors share.
- Menus: the view pages or the images.

## Choice

Confirmed by the owner on 2026-11-12 between 20:30 and 20:46:

- All blocks: screen states: "Empty, Loading, Read-only, Offline" (all four)
- All blocks: use-case depth: "Deepen all to F1's level": every use case 4 to 6 steps, alternatives, errors, concrete
  Given/When/Then with real values
- All blocks: proposals: "Confirm per block in this round"
- Sectors: shared capabilities: All four: booking and rounds; multi-payer, grants and third-party funds; recipes and one
  events and ticketing model; portals from F2 record types, offline phone forms, commissions and targets
- Views: menus: "The view pages": menus read from each view's Navigation line, every image drawn again

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- Every screen specifies its empty, loading, read-only and offline states, each with an example image.
- Every use case of F4 to F25 and of the 16 sectors is written to F1's depth.
- Shared capabilities: a booking and rounds engine, multi-payer invoicing with funders, grants and third-party funds,
  recipes, one events and ticketing model, portals for any record type, offline phone forms, commissions and targets.
- Each persona's menu is the Navigation line of its view page, and the images follow it.
- The proposals of F1 to F25 are confirmed (D458 to D482); the sectors' and the country rules' stay waiting.

## Related

- [Waiting for the owner](../../09-waiting/README.md)
- [Sectors](../../08-sectors/README.md)

---

⬅️ [D456 Mockup images per device, and the derived acceptance criteria](../ux/d456-audit-images-and-criteria.md) ·
⬆️ [Up](README.md) ·
➡️ [D458 F1 Administration: gaps and improvements](../f01-administration/d458-f01-gaps-and-improvements.md)
