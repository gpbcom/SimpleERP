🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-30 A tool past its life count is blocked

# 📏 BR-F12-30 A tool past its life count is blocked

**Status:** ✅ specified

## Statement

A tool whose count has reached its life limit is Blocked: it cannot be mounted on a work centre or used in a production
order until it has been refurbished and its count reset with a note, or its limit extended once by the quality manager
with a reason.

## Why

A worn mould makes parts out of tolerance, and a broken die can injure. Blocking at the limit turns an estimate into a
rule. The owner's answer: "Tools and moulds"
([D531](../../../06-decisions/f12-manufacturing/d531-benchmark-gaps-f12-manufacturing.md)).

## Examples

| Case | Result |
|---|---|
| Limit 100 000, count 99 999 | still available, warning shown |
| The count reaches 100 000 | blocked, maintenance request opened |
| The mould is refurbished | count reset to 0 with a note, available |
| The quality manager extends the limit by 5 000 after inspection | available until the new limit |
| An operator mounts a blocked tool | refused with the count and the limit |

## Applies to

- [UC-F12-35 Manage tools and moulds](../use-cases/14-cad-kanban-mps-and-tools/uc-f12-35-manage-tools-and-moulds.md)
- [E-F12-33 Tool](../data/e-f12-33-tool.md)
- [UC-F12-08 Maintain equipment](../use-cases/04-quality-and-maintenance/uc-f12-08-maintain-equipment.md)

## Exceptions

One extension after inspection, with a reason, by the quality manager only.

## Configurable

Yes: the life limit, the warning percentage and the service interval are set per tool.

## Open questions

None.

---

⬅️ [BR-F12-29 The MPS stays within the capacity plan](br-f12-29-the-mps-stays-within-the-capacity-plan.md) ·
⬆️ [Up](README.md)
