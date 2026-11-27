🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-13 Low code, bulk work and data cleaning](README.md) › 🖥️ S-F2-33 Time-based rule

# 🖥️ S-F2-33 Time-based rule

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the rules of their company.

## Purpose

Set when a rule fires: an offset from a date, or a recurring schedule, and preview what is due.

## Entry points

Rule editor › Trigger › Time; No-code configuration › Time-based rules.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Time-based rule: remind unsigned quotes            State: Draft            [Publish]        |
| ------------------------------------------------------------------------------------------- |
| WHEN   [ 3 ] [days v] [after v] [Quote: sent on v]       or   [Every v] [Monday v] at [08:00] |
| IF     status = Sent and not signed                                                         |
| THEN   Send the email template 'Quote reminder' to the salesperson                          |
| WINDOW A missed run may still fire for 24 hours      Time zone: Europe/Paris                |
| PREVIEW  14 quotes due now   9 due in the next 7 days   [Show the records]                  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-13 step 3, U07 | desktop | ![FL-F2-13 step 3, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/3-time-based-rule-desktop-light.png) | ![FL-F2-13 step 3, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/3-time-based-rule-desktop-dark.png) |
| FL-F2-13 step 3, U07 | desktop | ![FL-F2-13 step 3, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/3-time-based-rule-desktop-light.png) | ![FL-F2-13 step 3, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/3-time-based-rule-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-33-time-based-rule-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-33-time-based-rule-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-33-time-based-rule-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-33-time-based-rule-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-33-time-based-rule-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-33-time-based-rule-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-33-time-based-rule-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-33-time-based-rule-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind | E-F2-32 kind | offset or schedule | yes | yes |
| Date field and offset | E-F2-32 date field, offset | field, number, unit, before or after | yes | for an offset |
| Schedule | E-F2-32 schedule | every day, week or month, at a time | yes | for a schedule |
| Window | E-F2-32 window | hours | yes | yes |
| Preview | records due | counts and list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Preview | header | the author | lists the records due now and in 7 days |
| Publish | header | the author | the rule is published with the draft |
| Pause | row | the author, the administrator | no run fires until resumed |
| Show runs | row | the author | the run log |

## States

- Normal: the trigger, the condition, the actions, the window and the preview.
- Empty: No time-based rule yet: choose a date field or a schedule.
- Loading: The rule loads first; the preview follows.
- Error: the error message pattern (D122); a rule that could loop is refused
  ([BR-F2-13](../../business-rules/br-f02-13-rules-cannot-loop.md)).
- Read-only: a retired rule: its trigger and its run log, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-32 Scheduled trigger](../../data/e-f02-32-scheduled-trigger.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-32 Scheduled trigger | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-33-time-based-rule-e-f02-32-scheduled-trigger-draft-desktop-{light,dark}.png` |
| E-F2-32 Scheduled trigger | Active | Badge "Active"; next: Paused or Retired (UC-F2-33, UC-F2-10); fields editable within the role | U07 | `u07-administrator/s-f02-33-time-based-rule-e-f02-32-scheduled-trigger-active-desktop-{light,dark}.png` |
| E-F2-32 Scheduled trigger | Paused | Badge "Paused"; next: Active or Retired (UC-F2-33, UC-F2-10); fields editable within the role | U07 | `u07-administrator/s-f02-33-time-based-rule-e-f02-32-scheduled-trigger-paused-desktop-{light,dark}.png` |
| E-F2-32 Scheduled trigger | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-33-time-based-rule-e-f02-32-scheduled-trigger-retired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

The sentence form of the trigger is read in order; counts are text; keyboard: next field, preview.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-13 Low code, bulk work and data cleaning](../../flows/fl-f02-13-low-code-bulk-and-cleaning.md)

## Open questions

None.

---

⬅️ [S-F2-32 Bulk edit](s-f02-32-bulk-edit.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-34 Translation mode](s-f02-34-translation-mode.md)
