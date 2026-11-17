🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: F12 Manufacturing (plugin)](README.md) ›
📜 D531 Benchmark gaps of F12 Manufacturing

# 📜 D531 Benchmark gaps of F12 Manufacturing

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the manufacturing features of the benchmarked
suites and offered each gap as an option
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F12 Manufacturing").

## Options

- Take each gap as a use case of F12 in a new flow, or leave it out.
- Where a gap overlaps an existing use case, extend that use case or add a new one.

## Choice

The owner selected all four gaps; each becomes a use case of F12, drawn in
[FL-F12-14 CAD, kanban, MPS and tools](../../02-functional/f12-manufacturing/flows/fl-f12-14-cad-kanban-mps-and-tools.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G71 | [UC-F12-32 Link CAD files and revisions](../../02-functional/f12-manufacturing/use-cases/14-cad-kanban-mps-and-tools/uc-f12-32-link-cad-files-and-revisions.md) | "CAD and PDM link" |
| G72 | [UC-F12-33 Replenish with kanban cards](../../02-functional/f12-manufacturing/use-cases/14-cad-kanban-mps-and-tools/uc-f12-33-replenish-with-kanban-cards.md) | "Kanban pull" |
| G73 | [UC-F12-34 Run the master production schedule](../../02-functional/f12-manufacturing/use-cases/14-cad-kanban-mps-and-tools/uc-f12-34-run-the-master-production-schedule.md) | "Master production schedule" |
| G74 | [UC-F12-35 Manage tools and moulds](../../02-functional/f12-manufacturing/use-cases/14-cad-kanban-mps-and-tools/uc-f12-35-manage-tools-and-moulds.md) | "Tools and moulds" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "Block by block").

## Consequences

- Use cases
  [UC-F12-32 Link CAD files and revisions](../../02-functional/f12-manufacturing/use-cases/14-cad-kanban-mps-and-tools/uc-f12-32-link-cad-files-and-revisions.md)
  to
  [UC-F12-35 Manage tools and moulds](../../02-functional/f12-manufacturing/use-cases/14-cad-kanban-mps-and-tools/uc-f12-35-manage-tools-and-moulds.md),
  screens
  [S-F12-31 CAD link](../../02-functional/f12-manufacturing/screens/14-cad-kanban-mps-and-tools/s-f12-31-cad-link.md) to
  [S-F12-34 Tools and moulds](../../02-functional/f12-manufacturing/screens/14-cad-kanban-mps-and-tools/s-f12-34-tools-and-moulds.md),
  rules
  [BR-F12-27 Only released revisions reach the shop floor](../../02-functional/f12-manufacturing/business-rules/br-f12-27-only-released-revisions-reach-the-shop-floor.md)
  to
  [BR-F12-30 A tool past its life count is blocked](../../02-functional/f12-manufacturing/business-rules/br-f12-30-a-tool-past-its-life-count-is-blocked.md),
  entities [E-F12-30 CAD document](../../02-functional/f12-manufacturing/data/e-f12-30-cad-document.md) to
  [E-F12-33 Tool](../../02-functional/f12-manufacturing/data/e-f12-33-tool.md) and their lists
  [S-F12-L30 CAD documents](../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l30-cad-documents.md) to
  [S-F12-L33 Tools](../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l33-tools.md).
- The MPS line [E-F12-32 MPS line](../../02-functional/f12-manufacturing/data/e-f12-32-mps-line.md) firms the quantities
  of the existing plan line
  [E-F12-12 Master plan line](../../02-functional/f12-manufacturing/data/e-f12-12-master-plan-line.md) against capacity:
  it does not replace it.
- No law topic: the rules of this block are the company's own.

## Related

- [FL-F12-14 CAD, kanban, MPS and tools](../../02-functional/f12-manufacturing/flows/fl-f12-14-cad-kanban-mps-and-tools.md)
- [D458 F1 Administration: gaps and improvements](../f01-administration/d458-f01-gaps-and-improvements.md)
- [Interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)

---

⬅️ [D530 Benchmark gaps of F11 Online shop](../f11-online-shop/d530-benchmark-gaps-f11-online-shop.md) ·
⬆️ [Up](README.md) · ➡️ [D532 Benchmark gaps of F13 Payroll](../f13-payroll/d532-benchmark-gaps-f13-payroll.md)
