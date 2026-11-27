🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-04 Personal training](README.md) › 🖥️ S-SC18-15 Progress

# 🖥️ S-SC18-15 Progress

**Status:** 🔄 waiting for the owner

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the progress of their members.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own progress.

## Purpose

Record the member's measures and notes, show the evolution and keep them private to the member and the coach.

## Entry points

Sports and fitness › Progress records; the member's app; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Progress: Mia L., run 10 km                                              Only you and your coach |
| Date        10 km time   Weight   Felt        Notes                                              |
| 2026-11-30  68 min       62.4     tired       Knee ok                                            |
| 2026-12-07  65 min       62.1     good                                                           |
| 2026-12-14  62 min       61.8     good        New best                                           |
| [Add a measure]  [Export my data]  [Erase my record]                                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-04 step 3, U53 | phone | ![FL-SC18-04 step 3, U53, light](../../images/04-personal-training/u53-coach/3-progress-phone-light.png) | ![FL-SC18-04 step 3, U53, dark](../../images/04-personal-training/u53-coach/3-progress-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-15-progress-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-15-progress-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-15-progress-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-15-progress-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-15-progress-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-15-progress-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-15-progress-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-15-progress-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-12 member | link | no | yes |
| Date | E-SC18-12 recorded on | date | no | yes |
| Measures | E-SC18-12 measures | numbers | yes while Recorded | yes |
| Felt | E-SC18-12 felt | choice | yes while Recorded | no |
| Notes | E-SC18-12 notes | text | yes while Recorded | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a measure | header | coach, member | a record is saved Recorded |
| Export my data | header | member | an export of the member's own records |
| Erase my record | header | member | the record becomes Erased |
| Archive | header | coach | the record becomes Archived |

## States

- Normal: the member's measures over time, with a chart.
- Empty: No measure recorded yet, with Add a measure.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  access or a missing agreement, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-12 Progress record](../../data/e-sc18-12-progress-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-12 Progress record | Recorded | Badge "Recorded"; a new record starts here; next: Archived or Erased (UC-SC18-15, BR-SC18-15); fields editable within the role | U53, U09 | `u53-coach/s-sc18-15-progress-e-sc18-12-progress-record-recorded-phone-{light,dark}.png`, `u09-customer/s-sc18-15-progress-e-sc18-12-progress-record-recorded-phone-{light,dark}.png` |
| E-SC18-12 Progress record | Archived | Badge "Archived"; next: Erased (BR-SC18-15); fields editable within the role | U53, U09 | `u53-coach/s-sc18-15-progress-e-sc18-12-progress-record-archived-phone-{light,dark}.png`, `u09-customer/s-sc18-15-progress-e-sc18-12-progress-record-archived-phone-{light,dark}.png` |
| E-SC18-12 Progress record | Erased | Badge "Erased"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-15-progress-e-sc18-12-progress-record-erased-phone-{light,dark}.png`, `u09-customer/s-sc18-15-progress-e-sc18-12-progress-record-erased-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-04 Personal training](../../flows/fl-sc18-04-personal-training.md)

## Open questions

None.

---

⬅️ [S-SC18-14 Training programme](s-sc18-14-training-programme.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-16 Club AI assistant](s-sc18-16-club-assistant.md)
