🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D497 Every entity draws its states

# 📜 D497 Every entity draws its states

**Status:** ✅ decided

## Context

Only 112 of the 747 entities drew a state diagram on 2026-11-12.

## Options

- Write the states of every entity.
- Only the entities that appear in a flow chart.
- Only the 112 that already have one.

## Choice

Every entity gets an explicit state diagram; a setting or a log may have a single state.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), answer 14).

## Consequences

- The [entity template](../../_templates/entity.md)'s "Lifecycle" becomes a `stateDiagram-v2` with at least one state,
  in the words the screens show (change of step S3).
- About 635 diagrams to write, each transition naming its use case or rule.
- A check (`check_states.py`) fails on an entity without its diagram, as in step S3 of the
  plan (the owner's interview notes of 2026-11 for the specifications, not kept in the repository).

## Related

- [Entity template](../../_templates/entity.md)
- [D498 One screen with a variant per state](../ux/d498-one-screen-with-a-variant-per-state.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D496 One wording in charts and prose, reviewed first](d496-one-wording-in-charts-and-prose-reviewed-first.md) ·
⬆️ [Up](README.md) · ➡️ [D498 One screen with a variant per state](../ux/d498-one-screen-with-a-variant-per-state.md)
