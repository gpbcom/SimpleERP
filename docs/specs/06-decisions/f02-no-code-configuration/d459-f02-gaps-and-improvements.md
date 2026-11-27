🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D459 F2 No-code configuration: gaps and improvements

# 📜 D459 F2 No-code configuration: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F2 and the sectors that rely on it.

## Options

- **View types beyond lists.** E-F2-04 has columns, filters and grouping only. There is no kanban, calendar, map, Gantt
  or timeline view, yet SC04 rounds, SC06 housekeeping, SC01 site planning and SC09 schedules need them.
- **Portal exposure of custom record types.** "Portal" is absent in F2, so sector record types (tenant, family, learner)
  cannot be shown on a portal. Serves SC04, SC10, SC12.
- **Offline forms for custom records.** "Offline" is absent in F2. Site diary (SC01), care log (SC04), driver forms
  (SC07) and field records (SC13) need them.
- **Impact analysis before publishing.** Nothing lists the rules, templates, reports or plugins that use a field before
  it is renamed or deleted.
- **Field-level permissions and validation rules.** "Field-level" is absent in F2. ERPNext scores ✅ on field levels and
  data masking (B03).
- **Translations of custom labels and statuses.** Absent in F2, although the product launches in French and English
  (A09).
- **Test cases on rules and workflows.** Sample records with expected outcomes, replayed at each publish, as F16 does
  for procedures. Nebesta replay-tests its procedures (C03).
- **Pack upgrade merge.** Show a three-way diff when a sector pack update meets local customisations (UC-F2-11 only
  exports and imports).
- **One shared approval engine.** "Approval chain" appears twice. Specify multi-level, parallel, threshold and
  escalation-on-timeout once, reused by F7, F8 and F9.
- **Unused-configuration report.** Show fields, rules and views that are never used.
- **Screen states.** Add empty, loading and read-only states to the 15 screens that lack them.

## Choice

Confirmed by the owner on 2026-11-12:

- F2 No-code configuration: gaps: All: more view types (kanban, calendar, map, Gantt, timeline); portal and offline
  records; impact analysis; field rights and translations
- F2 No-code configuration: improvements: All four: rule test cases; pack upgrade merge; one approval engine;
  unused-configuration report
- F2 No-code configuration: proposals: "Confirm all of F2"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F2.
- F2's waiting proposals are confirmed (D457).

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)

---

⬅️ [D458 F1 Administration: gaps and improvements](../f01-administration/d458-f01-gaps-and-improvements.md) ·
⬆️ [Up](README.md) · ➡️ [D460 F3 Assistant: gaps and improvements](../f03-assistant/d460-f03-gaps-and-improvements.md)
