🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-06 Business tools](README.md) › 🖥️ S-F24-22 E-invoicing platform

# 🖥️ S-F24-22 E-invoicing platform

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Connect the e-invoicing platform step by step.

## Entry points

Catalogue, E-invoicing; the legal check of F21.

## Wireframe

```text
E-invoicing platform   [Super PDP icon] Super PDP       Step 3 of 5
-------------------------------------------------------------------------------
1 Choose  ok   2 Register  ok   3 Test invoice  [Send test]   4 Acknowledged   5 Live
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-06 step 4, U07 | desktop | ![FL-F24-06 step 4, U07, light](../../images/06-business-tools/u07-administrator/4-e-invoicing-platform-desktop-light.png) | ![FL-F24-06 step 4, U07, dark](../../images/06-business-tools/u07-administrator/4-e-invoicing-platform-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-22-e-invoicing-platform-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-22-e-invoicing-platform-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-22-e-invoicing-platform-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-22-e-invoicing-platform-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-22-e-invoicing-platform-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-22-e-invoicing-platform-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-22-e-invoicing-platform-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-22-e-invoicing-platform-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12 | tile | no | yes |
| Platform | E-F24-14 platform | list | yes | yes |
| State | E-F24-14 state | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Send test | step 3 | accounting | test invoice sent |
| Go live | step 5 | administrator | live |

## States

- Normal: the steps with states.
- Empty: "Choose your platform".
- Loading: the frame and titles show at once with placeholder rows for the steps; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a rejected test with its reason.
- Read-only: accounting reads before live.
- Offline: not available offline: steps run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F24-14 E-invoicing registration](../../data/e-f24-14-e-invoicing-registration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-14 E-invoicing registration | Registering | Badge "Registering"; a new record starts here; next: Testing (UC-F24-24); fields editable within the role | U05, U07 | `u05-accounting/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-registering-desktop-{light,dark}.png`, `u07-administrator/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-registering-desktop-{light,dark}.png` |
| E-F24-14 E-invoicing registration | Testing | Badge "Testing"; next: Live or Failed (UC-F24-24); fields editable within the role | U05, U07 | `u05-accounting/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-testing-desktop-{light,dark}.png`, `u07-administrator/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-testing-desktop-{light,dark}.png` |
| E-F24-14 E-invoicing registration | Live | Badge "Live"; final: read-only, no next state; the history shows how it got here | U05, U07 | `u05-accounting/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-live-desktop-{light,dark}.png`, `u07-administrator/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-live-desktop-{light,dark}.png` |
| E-F24-14 E-invoicing registration | Failed | Badge "Failed"; next: Testing (UC-F24-24); fields editable within the role | U05, U07 | `u05-accounting/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-failed-desktop-{light,dark}.png`, `u07-administrator/s-f24-22-e-invoicing-platform-e-f24-14-e-invoicing-registration-failed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-13 Stepper](../../../../04-ux/design-system/components/c-13-stepper.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F24-06 Business tools](../../flows/fl-f24-06-business-tools.md)

## Open questions

None.

---

⬅️ [S-F24-21 Automation](s-f24-21-automation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-23 HR and payroll import](s-f24-23-hr-and-payroll-import.md)
