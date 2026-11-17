🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-03 Declarations and payments](README.md) › 🖥️ S-F13-11 Corrections

# 🖥️ S-F13-11 Corrections

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

Correct a past month.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-03 step 3, U45 | desktop | ![FL-F13-03 step 3, U45, light](../../images/03-declarations-and-payments/u45-payroll-officer/3-correction-desktop-light.png) | ![FL-F13-03 step 3, U45, dark](../../images/03-declarations-and-payments/u45-payroll-officer/3-correction-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-11-corrections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-11-corrections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-11-corrections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-11-corrections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-11-corrections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-11-corrections-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-11-corrections-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-11-corrections-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the corrections waiting for the next run, per employee, period and item.
- Empty: "No correction waiting".
- Loading: the frame and titles show at once with placeholder rows for the corrections; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a correction already paid is read-only.
- Offline: not available offline: corrections are office work. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-10 Correction](../../data/e-f13-10-correction.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-10 Correction | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U45 | `u45-payroll-officer/s-f13-11-corrections-e-f13-10-correction-active-desktop-{light,dark}.png` |

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

- [FL-F13-03 Declarations and payments](../../flows/fl-f13-03-declarations-and-payments.md)

## Open questions

None.

---

⬅️ [S-F13-10 Social declaration](s-f13-10-social-declaration.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-12 Contributions](s-f13-12-contributions.md)
