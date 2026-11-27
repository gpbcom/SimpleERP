🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-04 Personal training](README.md) › 🖥️ S-SC18-14 Training programme

# 🖥️ S-SC18-14 Training programme

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the programmes of their members.

## Purpose

Write a programme from the goal, check it against the member's declared limits and activate it.

## Entry points

Sports and fitness › Training programmes; the member's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Programme: Mia L., goal run 10 km, 8 weeks                                  Draft                |
| Declared limits: left knee (no jumping), no medical advice given                                 |
| Week 1  Mon  Easy run 20 min   Wed  Step-ups 3x12   Fri  Core 20 min                             |
| Week 2  Mon  Run 25 min        Wed  Box jumps 3x8  [Breaks a limit]                              |
| Checks: 1 exercise to correct                                                                    |
| [Add a session]  [Replace the exercise]  [Activate]                                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-04 step 2, U53 | phone | ![FL-SC18-04 step 2, U53, light](../../images/04-personal-training/u53-coach/2-training-programme-phone-light.png) | ![FL-SC18-04 step 2, U53, dark](../../images/04-personal-training/u53-coach/2-training-programme-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-14-training-programme-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-14-training-programme-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-14-training-programme-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-14-training-programme-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-14-training-programme-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-14-training-programme-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-14-training-programme-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-14-training-programme-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-11 member | link | no | yes |
| Goal | E-SC18-11 goal | text | yes while Draft | yes |
| Declared limits | E-SC18-12 limits | text | no | yes |
| Weeks and sessions | E-SC18-11 weeks | list | yes while Draft | yes |
| Checks | E-SC18-11 checks | list of flags | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a session | week | coach | a session is added to the week |
| Activate | header | coach | the programme becomes Active for the member |
| Complete | header | coach | the programme becomes Completed |
| Stop | header | coach, member | the programme becomes Stopped |

## States

- Normal: the programme with its weeks, its checks and the member's declared limits.
- Empty: No programme yet, with New programme.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an exercise
  that breaks a limit, with the limit and a proposed replacement.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-11 Training programme](../../data/e-sc18-11-training-programme.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-11 Training programme | Draft | Badge "Draft"; a new record starts here; next: Active or Stopped (BR-SC18-14, UC-SC18-14); fields editable within the role | U53 | `u53-coach/s-sc18-14-training-programme-e-sc18-11-training-programme-draft-phone-{light,dark}.png` |
| E-SC18-11 Training programme | Active | Badge "Active"; next: Completed or Stopped (UC-SC18-14); fields editable within the role | U53 | `u53-coach/s-sc18-14-training-programme-e-sc18-11-training-programme-active-phone-{light,dark}.png` |
| E-SC18-11 Training programme | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U53 | `u53-coach/s-sc18-14-training-programme-e-sc18-11-training-programme-completed-phone-{light,dark}.png` |
| E-SC18-11 Training programme | Stopped | Badge "Stopped"; final: read-only, no next state; the history shows how it got here | U53 | `u53-coach/s-sc18-14-training-programme-e-sc18-11-training-programme-stopped-phone-{light,dark}.png` |

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

⬅️ [S-SC18-13 Coaching packages](s-sc18-13-coaching-packages.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-15 Progress](s-sc18-15-progress.md)
