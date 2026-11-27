🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-03 Review a meeting](README.md) › 🖥️ S-F4-05 Meeting review

# 🖥️ S-F4-05 Meeting review

**Status:** ✅ specified

## Personas

- Organisers: [U02 Manager](../../../../01-users/personas/u02-manager.md),
  [U03 Sales](../../../../01-users/personas/u03-sales.md), [U13 Owner](../../../../01-users/personas/u13-owner.md),
  [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- Participants

## Purpose

Check a meeting's outcomes (D224 to D226).

## Entry points

"Review" on the meeting; the reminder.

## Wireframe

```text
+------------------------------------------------------------------+
| Review: weekly site meeting, Villeurbanne     Kind [Site meeting v]|
| Summary   Progress on schedule; plaster delayed 2 days.           |
| Decisions 1. Tiles: model B.                                      |
| Actions   [x] Paul: order tiles by Fri     -> task                |
|           [x] Durand: confirm colour        -> follow-up email    |
| Speakers  Speaker 2 = [J. Durand v]   Links [Durand SA] [confirm] |
|                                   [Mark checked and follow up]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-03 step 1, U02 | desktop | ![FL-F4-03 step 1, U02, light](../../images/03-review-a-meeting/u02-manager/1-review-desktop-light.png) | ![FL-F4-03 step 1, U02, dark](../../images/03-review-a-meeting/u02-manager/1-review-desktop-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/03-review-a-meeting/u02-manager/e1-summary-not-produced-desktop-light.png) | ![Error E1, U02, dark](../../images/03-review-a-meeting/u02-manager/e1-summary-not-produced-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/03-review-a-meeting/u02-manager/e1-summary-not-produced-phone-light.png) | ![Error E1, U02, dark](../../images/03-review-a-meeting/u02-manager/e1-summary-not-produced-phone-dark.png) |
| Error E2, U02 | desktop | ![Error E2, U02, light](../../images/03-review-a-meeting/u02-manager/e2-task-owner-left-desktop-light.png) | ![Error E2, U02, dark](../../images/03-review-a-meeting/u02-manager/e2-task-owner-left-desktop-dark.png) |
| Error E2, U02 | phone | ![Error E2, U02, light](../../images/03-review-a-meeting/u02-manager/e2-task-owner-left-phone-light.png) | ![Error E2, U02, dark](../../images/03-review-a-meeting/u02-manager/e2-task-owner-left-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-05-meeting-review-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-05-meeting-review-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-05-meeting-review-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-05-meeting-review-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-05-meeting-review-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-05-meeting-review-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-05-meeting-review-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-05-meeting-review-offline-phone-dark.png) |

## Fields and columns

Summary sections from the template; actions with owner and due date; speakers; links.

## Actions

| Action | Who | Result |
|---|---|---|
| Mark checked | organiser | Published, tasks, audio deleted |
| Change kind | organiser | Another template |

## States

- Normal: Check a meeting's outcomes (D224 to D226), as the wireframe shows.
- Empty: never: a review opens on a meeting with outcomes.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: summary not produced (D122).
- Read-only: a checked meeting, reopened only by its organiser.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Waiting, checked, published not checked.

Shown entities (VD-15): [E-F4-17 Meeting summary](../../data/e-f04-17-meeting-summary.md),
[E-F4-03 Summary template](../../data/e-f04-03-summary-template.md),
[E-F4-04 Action item](../../data/e-f04-04-action-item.md),
[E-F4-19 Follow-up email](../../data/e-f04-19-follow-up-email.md), [E-F4-01 Meeting](../../data/e-f04-01-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-17 Meeting summary | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U06 | `u02-manager/s-f04-05-meeting-review-e-f04-17-meeting-summary-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-05-meeting-review-e-f04-17-meeting-summary-active-desktop-{light,dark}.png` |
| E-F4-03 Summary template | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F4-05); fields editable within the role | U02, U06 | `u02-manager/s-f04-05-meeting-review-e-f04-03-summary-template-draft-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-05-meeting-review-e-f04-03-summary-template-draft-desktop-{light,dark}.png` |
| E-F4-03 Summary template | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U02, U06 | `u02-manager/s-f04-05-meeting-review-e-f04-03-summary-template-published-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-05-meeting-review-e-f04-03-summary-template-published-desktop-{light,dark}.png` |
| E-F4-04 Action item | Open | Badge "Open"; a new record starts here; next: Done (UC-F4-27); fields editable within the role | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-04-action-item-open-{desktop,phone}-{light,dark}.png` |
| E-F4-04 Action item | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-04-action-item-done-{desktop,phone}-{light,dark}.png` |
| E-F4-19 Follow-up email | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-19-follow-up-email-active-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U02, U06 | `u02-manager/s-f04-05-meeting-review-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-05-meeting-review-e-f04-01-meeting-planned-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f04-05-meeting-review-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; phone for short meetings.

## Accessibility

Sections as headings; actions as a checklist.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F4-03 Review a meeting](../../flows/fl-f04-03-review-a-meeting.md)
- [FL-F4-13 Outside people and follow-up](../../flows/fl-f04-13-outside-people-and-follow-up.md)

## Open questions

None.

---

⬅️ [S-F4-04 Call](../02-record-in-person-or-by-phone/s-f04-04-call.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-06 Meetings](../04-find-and-reuse-meetings/s-f04-06-meetings.md)
