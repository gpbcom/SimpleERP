🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D484 Aggregated list view per record type and persona workspaces

# 📜 D484 Aggregated list view per record type and persona workspaces

**Status:** 🔄 draft (GH-2 step S4, from VD-01 / D484)

## Context

The owner asked on 2026-11-12 for an aggregated view wherever a functional requirement handles many records ("employees,
deals and many other"): the list of records with rich filtering, respecting the user's permissions.

Before this decision the specs had the [C-03 Data table](../../04-ux/design-system/components/c-03-data-table.md), the
[search and filter pattern](../../04-ux/design-system/patterns/search-and-filter.md), the [list and detail
pattern](../../04-ux/design-system/patterns/list-detail.md), saved list views
([D109](../f02-no-code-configuration/d109-list-views.md)) and the permission model
([D12](../foundations/d12-permissions-model.md)), but no page that sees, filters, totals and acts on many records at
once.

## Options

- A list page per record type.
- Persona workspaces.
- Both.
- One universal explorer.

## Choice

Both: every record type has a list page, the aggregated list view; each persona has a workspace that embeds the list
views it works with, each opened on the persona's default saved view.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 1).

## Consequences

- The [aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md) describes the page; it
  extends C-03, the search and filter pattern and the list and detail pattern, whose list half it becomes.
- Each list page is written from the [list view template](../../_templates/list-view.md).
- (Proposed) The list pages are named "S-<capability>-L<nn> <View>" in a `screens/00-lists/` folder of each capability,
  and each persona's workspace is a page of its views folder ([Views](../../04-ux/views/README.md)), as in step S5 of
  the [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md).
- The home screen ([D48](d48-home-screen.md)) holds the persona's workspace.

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [List view template](../../_templates/list-view.md)
- [C-03 Data table](../../04-ux/design-system/components/c-03-data-table.md)
- [D109 Shared and personal list views](../f02-no-code-configuration/d109-list-views.md)
- [D48 Home screen](d48-home-screen.md)
- [D485 Every entity has an aggregated view](d485-every-entity-has-an-aggregated-view.md)
- [D493 Persona workspaces from the use cases](d493-persona-workspaces-from-the-use-cases.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D483 Roadmap: everything in V1, the DevOps agents first](../vision/d483-roadmap-devops-agents-first.md) ·
⬆️ [Up](README.md) · ➡️ [D485 Every entity has an aggregated view](d485-every-entity-has-an-aggregated-view.md)
