🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D496 One wording in charts and prose, reviewed first

# 📜 D496 One wording in charts and prose, reviewed first

**Status:** 🔄 draft (GH-2 step S2, from VD-13 / D496)

## Context

The specs named the same actor or artifact in several ways. In the flow charts on 2026-11-12: 1,703 terms, of which 493
variants, 592 vague words and 207 with no spec; 42 names were shared by several items ([naming
map](../../../tickets/GH-2/resources/flowcharts-screens/naming/README.md)).

## Options

- The map and the prose, after the owner's review.
- The map and the prose, as proposed.
- The charts only.

## Choice

The owner reviews the shared-name renames and the new items first; the approved names then apply in every chart and
every prose page, and a check fails on any old or vague term.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 13).

## Consequences

- The naming rules and the seven classes of names: [D516](d516-naming-rules-and-the-seven-classes-of-names.md).
- (Proposed) The approved names go into a lexicon (`LEXICON.yaml`), which a check (`check_wording.py`) reads, as in step
  S2 of the [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md).
- An entity keeps its ID when renamed; its title, file name and every link change.

## Related

- [Naming map of the flow charts](../../../tickets/GH-2/resources/flowcharts-screens/naming/README.md)
- [Shared names](../../../tickets/GH-2/resources/flowcharts-screens/naming/CLASHES.md)
- [Proposed new items](../../../tickets/GH-2/resources/flowcharts-screens/naming/NEW-ITEMS.md)
- [D516 Naming rules and the seven classes of names](d516-naming-rules-and-the-seven-classes-of-names.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D495 Views listed under each capability's menu](../ux/d495-views-listed-under-each-capabilitys-menu.md) ·
⬆️ [Up](README.md) · ➡️ [D497 Every entity draws its states](d497-every-entity-draws-its-states.md)
