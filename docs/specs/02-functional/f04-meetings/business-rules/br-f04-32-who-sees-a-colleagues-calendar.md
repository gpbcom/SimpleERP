🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-32 Who sees a colleague's calendar

# 📏 BR-F4-32 Who sees a colleague's calendar

**Status:** ✅ specified

## Statement

Every employee has a calendar ([E-F4-26](../data/e-f04-26-employee-calendar.md),
[D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)), and several employees'
calendars can be compared side by side from the
[S-F4-L26 Employee calendars](../screens/00-lists/s-f04-l26-employee-calendars.md) list. A user sees their
own calendar in full; a colleague's event shows as busy, without its title or details, unless the user takes part in it
or holds a role that reads it (a manager their team's absences, HR every absence); an HR meeting shows as busy to
everyone but its participants. Each column of the comparison follows this rule.

## Why

The owner asked to compare one employee's agenda to others (VC-13); a calendar holds private events, which the
comparison must not reveal.

## Examples

| Case | Result |
|---|---|
| A seller compares their calendar with two colleagues' | Their own events in full, the colleagues' as busy slots |
| A manager compares their team's calendars | Meetings they attend and absences in full, the rest as busy |
| Anyone looks at an HR meeting of a colleague | Busy, no title |

## Applies to

- [E-F4-26 Employee calendar](../data/e-f04-26-employee-calendar.md)
- [UC-F4-09 Prepare a meeting](../use-cases/07-prepare-and-capture-anywhere/uc-f04-09-prepare-a-meeting.md)

## Exceptions

None.

## Configurable

An employee may show their event titles to their team.

## Open questions

None.

---

⬅️ [BR-F4-31 Every meeting has an agenda](br-f04-31-every-meeting-has-an-agenda.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-33 Video messages follow meeting retention](br-f04-33-video-messages-follow-meeting-retention.md)
