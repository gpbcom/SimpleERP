🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-06 Experts, cutover, parallel run and set-up from documents](README.md) › 🖥️ S-F21-27 Cutover

# 🖥️ S-F21-27 Cutover

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the plan, the steps and the Go live button.
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md): the accounting steps to sign off.

## Purpose

Plan the go-live day, follow its checklist and go live only when every required step is done.

## Entry points

Onboarding and module activation › Cutover; the first-run guide's last step; the accountant's workspace.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Cutover plan: go live 2027-01-04 07:00                 Steps 7 of 9 done     [Go live] (locked) |
|---------------------------------------------------------------------------------------------|
| STEP                              OWNER        DUE         STATE                              |
| Last export of the old tool       Claire P.    2026-12-28  Done                               |
| Final import                      Claire P.    2026-12-30  Done                               |
| Opening balances against the FEC  Accountant   2027-01-02  Waiting for sign-off               |
| Backup before go-live             SimpleERP   2027-01-03  Not yet (automatic)                |
| Locked because: 2 required steps open        Rollback point: taken at go live                |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-06 step 2, U07 | desktop | ![FL-F21-06 step 2, U07, light](../../images/06-experts-cutover-and-parallel-run/u07-administrator/2-cutover-desktop-light.png) | ![FL-F21-06 step 2, U07, dark](../../images/06-experts-cutover-and-parallel-run/u07-administrator/2-cutover-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-27-cutover-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-27-cutover-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-27-cutover-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-27-cutover-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-27-cutover-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-27-cutover-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-27-cutover-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-27-cutover-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Date and time | E-F21-20 go-live at | date and time | yes while Draft or Ready | yes |
| Steps | E-F21-20 steps | text, owner, due date | yes while Draft or Ready | yes |
| State of each step | E-F21-20 step states | open, done, signed off | by the owner of the step | yes |
| Required | E-F21-20 required | yes, no | by the administrator | yes |
| Rollback point | E-F21-20 rollback | date and time | no | no |
| Plan state | E-F21-20 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add or edit a step | list | administrator | changes the plan before go-live |
| Mark done | step | owner of the step | the step counts toward the checklist |
| Sign off | step | external accountant | the accounting step is signed |
| Go live | header | administrator | unlocks only when every required step is done |
| Roll back | header | administrator | returns to the rollback point within 48 hours |

## States

- Normal: the plan with its steps, owners, states and the Go live button or the reason it is locked.
- Empty: No plan yet, with Create the cutover plan.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a locked Go
  live names each open required step and its owner.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F21-20 Cutover plan](../../data/e-f21-20-cutover-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-20 Cutover plan | Draft | Badge "Draft"; a new record starts here; next: Ready (BR-F21-18); fields editable within the role | U07, U08 | `u07-administrator/s-f21-27-cutover-e-f21-20-cutover-plan-draft-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-27-cutover-e-f21-20-cutover-plan-draft-desktop-{light,dark}.png` |
| E-F21-20 Cutover plan | Ready | Badge "Ready"; next: Draft or Live (UC-F21-27, BR-F21-18); fields editable within the role | U07, U08 | `u07-administrator/s-f21-27-cutover-e-f21-20-cutover-plan-ready-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-27-cutover-e-f21-20-cutover-plan-ready-desktop-{light,dark}.png` |
| E-F21-20 Cutover plan | Live | Badge "Live"; next: Rolled back or Closed (UC-F21-27); fields editable within the role | U07, U08 | `u07-administrator/s-f21-27-cutover-e-f21-20-cutover-plan-live-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-27-cutover-e-f21-20-cutover-plan-live-desktop-{light,dark}.png` |
| E-F21-20 Cutover plan | Rolled back | Badge "Rolled back"; next: Draft (UC-F21-27); fields editable within the role | U07, U08 | `u07-administrator/s-f21-27-cutover-e-f21-20-cutover-plan-rolled-back-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-27-cutover-e-f21-20-cutover-plan-rolled-back-desktop-{light,dark}.png` |
| E-F21-20 Cutover plan | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U07, U08 | `u07-administrator/s-f21-27-cutover-e-f21-20-cutover-plan-closed-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-27-cutover-e-f21-20-cutover-plan-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F21-06](../../flows/fl-f21-06-experts-cutover-and-parallel-run.md)

## Open questions

None.

---

⬅️ [S-F21-26 Expert booking](s-f21-26-expert-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-28 Parallel run](s-f21-28-parallel-run.md)
