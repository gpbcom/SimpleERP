🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-31 Every meeting has an agenda

# 📏 BR-F4-31 Every meeting has an agenda

**Status:** 🔄 waiting for the owner

## Statement

Every meeting has an agenda ([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md),
VC-13: "All employes MUST have one. Provide the ability to compare one employee agenda to others", clarified "both"),
and the agendas of different employees' meetings can be compared side by side from the
[S-F4-L22 Meeting agendas](../screens/00-lists/s-f04-l22-meeting-agendas.md) list, each user seeing only the agendas of
the meetings they may read. (Proposed) A meeting created without an agenda gets one drafted from its invitation and its
linked records, which the organiser edits; a recurring meeting's agenda follows
[BR-F4-16](br-f04-16-recurring-meetings-get-their-next-agenda.md).

## Why

The owner's review of the view cards on 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)).

## Examples

| Case | Result |
|---|---|
| A meeting is synced from a calendar with no agenda | (Proposed) An agenda drafted from the invitation, to edit |
| A manager compares the agendas of two sellers' customer meetings | Both shown side by side |
| An employee compares with an HR meeting they do not attend | Not offered: they may not read it |

## Applies to

- [E-F4-22 Meeting agenda](../data/e-f04-22-meeting-agenda.md)
- [E-F4-01 Meeting](../data/e-f04-01-meeting.md)
- [UC-F4-06 Find and reuse past meetings](../use-cases/04-find-and-reuse-meetings/uc-f04-06-find-and-reuse-past-meetings.md)

## Exceptions

HR meetings: their agenda only to HR and the employee
([BR-F4-18](br-f04-18-hr-meetings-are-recorded-for-hr-and-the-employee.md)).

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-30 Actions and tasks stay in step](br-f04-30-actions-and-tasks-stay-in-step.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-32 Who sees a colleague's calendar](br-f04-32-who-sees-a-colleagues-calendar.md)
