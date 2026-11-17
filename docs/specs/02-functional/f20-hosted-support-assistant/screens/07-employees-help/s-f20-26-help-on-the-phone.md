🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-07 Employees' help](README.md) › 🖥️ S-F20-26 Help on the phone

# 🖥️ S-F20-26 Help on the phone

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Ask for help on a task from the phone and get steps with links.

## Entry points

The help button of the phone app.

## Wireframe

```text
Help
-------------------------------------------------------------------------------
[ How do I add a receipt?            ] [Ask]
1. Open Expenses  2. Tap the expense  3. Add photo     [Open Expenses]
Was this helpful? [yes] [no]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-07 step 2, U01 | desktop | ![FL-F20-07 step 2, U01, light](../../images/07-employees-help/u01-employee/2-help-on-the-phone-desktop-light.png) | ![FL-F20-07 step 2, U01, dark](../../images/07-employees-help/u01-employee/2-help-on-the-phone-desktop-dark.png) |
| FL-F20-07 step 2, U01 | phone | ![FL-F20-07 step 2, U01, light](../../images/07-employees-help/u01-employee/2-help-on-the-phone-phone-light.png) | ![FL-F20-07 step 2, U01, dark](../../images/07-employees-help/u01-employee/2-help-on-the-phone-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-26-help-on-the-phone-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-26-help-on-the-phone-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-26-help-on-the-phone-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-26-help-on-the-phone-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-26-help-on-the-phone-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-26-help-on-the-phone-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-26-help-on-the-phone-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-26-help-on-the-phone-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question | E-F20-02 text | text | yes | yes |
| Answer | E-F20-02 text | steps | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Ask | top | employee | answer |
| Open | answer | employee | the screen |
| Rate | bottom | employee | rating |

## States

- Normal: question and answer with links.
- Empty: example questions for the employee's role.
- Loading: the frame and titles show at once with placeholder rows for the answer; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: none beyond D122.
- Read-only: past answers are read-only.
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F20-02 Message](../../data/e-f20-02-message.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-02 Message | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f20-26-help-on-the-phone-e-f20-02-message-recorded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-07 Employees' help](../../flows/fl-f20-07-employees-help.md)

## Open questions

None.

---

⬅️ [S-F20-25 NIS2 facts](../06-after-an-incident/s-f20-25-nis2-facts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-27 Report a problem](s-f20-27-report-a-problem.md)
