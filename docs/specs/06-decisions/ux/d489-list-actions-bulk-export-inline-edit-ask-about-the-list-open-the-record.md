🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D489 List actions: bulk, export, inline edit, ask about the list, open the record

# 📜 D489 List actions: bulk, export, inline edit, ask about the list, open the record

**Status:** ✅ decided

## Context

Which actions an aggregated list view offers.

## Options

- Bulk actions.
- Export.
- Inline edit.
- Ask the AI assistant about the list.

The owner chose all four and added one: "go to specific artifact view".

## Choice

Bulk actions with a confirmation and an undo; a CSV or XLSX export, audited; inline edit of the fields the role may
change; "Ask about this list"; and every row opens its record's own page.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), answer 6).

## Consequences

- The [bulk actions pattern](../../04-ux/design-system/patterns/bulk-actions.md) and the [import and export
  pattern](../../04-ux/design-system/patterns/import-export.md) apply to every view.
- C-03 Data table: inline edit is no longer "Proposed", and every row has an "Open ›" action (change of step S4).
- [C-11 Chat panel](../../04-ux/design-system/components/c-11-chat-panel.md): "Ask about this list" answers from the
  filtered visible rows only, with its sources.
- T3 audits exports, bulk actions and inline edits ([T3](../../03-technical/t03-audit-trail/README.md)).
- The rules VR-10, VR-11 and VR-13 of the plan (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)
  derive each view's actions.

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [Bulk actions pattern](../../04-ux/design-system/patterns/bulk-actions.md)
- [Import and export pattern](../../04-ux/design-system/patterns/import-export.md)
- [C-11 Chat panel](../../04-ux/design-system/components/c-11-chat-panel.md)
- [D488 Totals, facets, charts, AI answers and exports on visible rows
  only](d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D488](d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md) · ⬆️ [Up](README.md) ·
➡️ [D490](d490-example-images-for-every-persona-that-can-open-a-view.md)
