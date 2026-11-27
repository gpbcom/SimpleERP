🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-27 Only released revisions reach the shop floor

# 📏 BR-F12-27 Only released revisions reach the shop floor

**Status:** ✅ specified

## Statement

A tablet, a work instruction or a pick list shows only the drawing revision that is Released for its product; a revision
in Draft, in review, Superseded or Withdrawn is never offered to an operator, and only the quality manager can release
or withdraw a revision.

## Why

Parts built from a drawing nobody approved are scrap, and in some trades a risk. One person releases, and the shop floor
sees only what was released. The owner's answer: "CAD and PDM link"
([D531](../../../06-decisions/f12-manufacturing/d531-benchmark-gaps-f12-manufacturing.md)).

## Examples

| Case | Result |
|---|---|
| Revision C is in review, B is released | tablets show B |
| C is released | tablets show C, B is superseded |
| C is withdrawn | tablets show B again, the orders on C are flagged |
| An engineer tries to release | refused, only the quality manager may |
| An order started on B | keeps B in its record |

## Applies to

- [UC-F12-32 Link CAD files and revisions](../use-cases/14-cad-kanban-mps-and-tools/uc-f12-32-link-cad-files-and-revisions.md)
- [E-F12-30 CAD document](../data/e-f12-30-cad-document.md)
- [UC-F12-28 Publish versioned work instructions](../use-cases/10-people-and-tools/uc-f12-28-publish-versioned-work-instructions.md)

## Exceptions

A prototype order may be started on a draft revision by the quality manager, marked as a prototype.

## Configurable

No: only released revisions reach the shop floor; the prototype case is the only exception.

## Open questions

None.

---

⬅️ [BR-F12-26](br-f12-26-recipes-scale-to-the-batch-and-keep-their-tolerances.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-28 A card triggers one replenishment](br-f12-28-a-card-triggers-one-replenishment.md)
