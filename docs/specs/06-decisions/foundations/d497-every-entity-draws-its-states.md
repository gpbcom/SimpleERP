🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D497 Every entity draws its states

# 📜 D497 Every entity draws its states

**Status:** 🔄 draft (GH-2 step S3, from VD-14 / D497)

## Context

Only 112 of the 747 entities drew a state diagram on 2026-11-12.

## Options

- Write the states of every entity.
- Only the entities that appear in a flow chart.
- Only the 112 that already have one.

## Choice

Every entity gets an explicit state diagram; a setting or a log may have a single state.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 14).

## Consequences

- The [entity template](../../_templates/entity.md)'s "Lifecycle" becomes a `stateDiagram-v2` with at least one state,
  in the words the screens show (change of step S3).
- About 635 diagrams to write, each transition naming its use case or rule.
- (Proposed) A check (`check_states.py`) fails on an entity without its diagram, as in step S3 of the
  [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md).

## Related

- [Entity template](../../_templates/entity.md)
- [D498 One screen with a variant per state](../ux/d498-one-screen-with-a-variant-per-state.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D496 One wording in charts and prose, reviewed first](d496-one-wording-in-charts-and-prose-reviewed-first.md) ·
⬆️ [Up](README.md) · ➡️ [D498 One screen with a variant per state](../ux/d498-one-screen-with-a-variant-per-state.md)
