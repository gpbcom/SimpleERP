🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-14 Video messages, webinars and templates](README.md) ›
🖥️ S-F4-27 Note templates

# 🖥️ S-F4-27 Note templates

**Status:** ✅ specified

## Personas

- - [U03 Sales](../../../../01-users/personas/u03-sales.md): the templates of sales meetings.
- - [U06 Human resources](../../../../01-users/personas/u06-hr.md): the templates of HR meetings.

## Purpose

Define the fields of each kind of meeting's notes and where confirmed values go.

## Entry points

Meetings › Note templates; a meeting's notes › Change template.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Note templates                                     [New template]                           |
| ------------------------------------------------------------------------------------------- |
| TEMPLATE: Discovery call            KIND: Customer call    TEAM: Sales           State: Active |
| FIELD              TYPE      FILLS AFTER REVIEW           HINT                              |
| Budget             number    Opportunity amount           the amount the customer states    |
| Decision maker     text      Contact role                 who signs                         |
| Next step          text      Next task                    the agreed action                 |
| [Try on a past meeting]  Not said in the meeting is shown for any field left empty          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-14 step 3, U03 | desktop | ![FL-F4-14 step 3, U03, light](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-desktop-light.png) | ![FL-F4-14 step 3, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-desktop-dark.png) |
| FL-F4-14 step 3, U03 | desktop | ![FL-F4-14 step 3, U03, light](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-desktop-light.png) | ![FL-F4-14 step 3, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-desktop-dark.png) |
| FL-F4-14 step 3, U03 | phone | ![FL-F4-14 step 3, U03, light](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-phone-light.png) | ![FL-F4-14 step 3, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-phone-dark.png) |
| FL-F4-14 step 3, U03 | tablet | ![FL-F4-14 step 3, U03, light](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-tablet-light.png) | ![FL-F4-14 step 3, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/3-note-templates-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-27-note-templates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-27-note-templates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-27-note-templates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-27-note-templates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-27-note-templates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-27-note-templates-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-27-note-templates-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-27-note-templates-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Template | E-F4-29 name | text | yes | yes |
| Kind and team | E-F4-29 kind, team | choice | yes | yes |
| Field | E-F4-29 fields | label, type, hint | yes | yes |
| Fills after review | E-F4-29 record field | choice | yes | no |
| State | E-F4-29 state | badge | activate, retire | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New template | header | the editor | a draft template |
| Try on a past meeting | footer | the editor | the fields are filled as a trial, nothing saved |
| Activate | header | the editor | new meetings of that kind use it |
| Retire | header | the editor | the default template applies again |

## States

- Normal: the template with its fields and where each fills the record.
- Empty: No template yet. The company's default summary is used.
- Loading: The templates load first; the trial's results follow.
- Error: the error message pattern (D122); a duplicate field label is refused under the field.
- Read-only: a retired template: its fields, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-29 Note template](../../data/e-f04-29-note-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-29 Note template | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F4-30); fields editable within the role | U03, U06 | `u03-sales/s-f04-27-note-templates-e-f04-29-note-template-draft-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f04-27-note-templates-e-f04-29-note-template-draft-desktop-{light,dark}.png` |
| E-F4-29 Note template | Active | Badge "Active"; next: Draft or Retired (UC-F4-30); fields editable within the role | U03, U06 | `u03-sales/s-f04-27-note-templates-e-f04-29-note-template-active-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f04-27-note-templates-e-f04-29-note-template-active-desktop-{light,dark}.png` |
| E-F4-29 Note template | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U03, U06 | `u03-sales/s-f04-27-note-templates-e-f04-29-note-template-retired-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f04-27-note-templates-e-f04-29-note-template-retired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Each field is a table row with a text type and hint; the trial result is text with its source; keyboard: next field,
activate.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-14 Video messages, webinars and templates](../../flows/fl-f04-14-video-messages-and-webinars.md)

## Open questions

None.

---

⬅️ [S-F4-26 Webinar](s-f04-26-webinar.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-28 Meeting time analytics](s-f04-28-meeting-time-analytics.md)
