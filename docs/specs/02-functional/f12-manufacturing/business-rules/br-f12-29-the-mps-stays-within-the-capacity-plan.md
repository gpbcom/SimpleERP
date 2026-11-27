🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-29 The MPS stays within the capacity plan

# 📏 BR-F12-29 The MPS stays within the capacity plan

**Status:** ✅ specified

## Statement

A line of the master production schedule can be firmed only when the load of its week, with all the firm lines of that
week, fits the capacity plan of the work centres it uses; a week over capacity is shown with the hours missing and can
be firmed only with the planner's written note.

## Why

A schedule that ignores capacity promises dates the plant cannot keep. Showing the gap before firming makes the planner
choose: move, add shifts, subcontract or accept the delay. The owner's answer: "Master production schedule"
([D531](../../../06-decisions/f12-manufacturing/d531-benchmark-gaps-f12-manufacturing.md)).

## Examples

| Case | Result |
|---|---|
| Week 48 load 94 hours, capacity 100 | the line can be firmed |
| Week 49 load 112, capacity 100 | flagged 12 hours over, firming needs a note |
| The planner adds a shift of 16 hours | capacity 116, the line can be firmed |
| A line in the frozen fence is changed | refused without a reason |
| A maintenance stop cuts capacity | the week is flagged again |

## Applies to

- [UC-F12-34 Run the master production schedule](../use-cases/14-cad-kanban-mps-and-tools/uc-f12-34-run-the-master-production-schedule.md)
- [E-F12-32 MPS line](../data/e-f12-32-mps-line.md)
- [UC-F12-23 Schedule with finite capacity](../use-cases/11-finite-schedule-and-the-tablet/uc-f12-23-schedule-with-finite-capacity.md)

## Exceptions

An urgent order may be firmed over capacity by the plant manager, with the note and the audit.

## Configurable

Yes: the frozen fence, the release fence and the tolerance over capacity are set per plant.

## Open questions

None.

---

⬅️ [BR-F12-28 A card triggers one replenishment](br-f12-28-a-card-triggers-one-replenishment.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-30 A tool past its life count is blocked](br-f12-30-a-tool-past-its-life-count-is-blocked.md)
