🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F13-01 Set up](README.md) ›
🖥️ S-F13-01 Payroll set-up

# 🖥️ S-F13-01 Payroll set-up

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Set up the company's payroll.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-01 step 1, U45 | desktop | ![FL-F13-01 step 1, U45, light](../../images/01-set-up/u45-payroll-officer/1-company-desktop-light.png) | ![FL-F13-01 step 1, U45, dark](../../images/01-set-up/u45-payroll-officer/1-company-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-01-payroll-set-up-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-01-payroll-set-up-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-01-payroll-set-up-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-01-payroll-set-up-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-01-payroll-set-up-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-01-payroll-set-up-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-01-payroll-set-up-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-01-payroll-set-up-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the company's establishments, contribution accounts, collective agreements and pay calendar, each with its
  completeness.
- Empty: "Payroll is not set up": a first-time panel lists the four steps and opens the first.
- Loading: the frame and titles show at once with placeholder rows for the establishments and agreements; within 1
  second (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: HR and the owner read the set-up; only the payroll officer and the administrator change it.
- Offline: not available offline: payroll set-up is office work on a desktop. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-01 Payroll establishment](../../data/e-f13-01-payroll-establishment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-01 Payroll establishment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U45 | `u07-administrator/s-f13-01-payroll-set-up-e-f13-01-payroll-establishment-active-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-01-payroll-set-up-e-f13-01-payroll-establishment-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-01 Set up](../../flows/fl-f13-01-set-up.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F13-02 Employee pay](s-f13-02-employee-pay.md)
