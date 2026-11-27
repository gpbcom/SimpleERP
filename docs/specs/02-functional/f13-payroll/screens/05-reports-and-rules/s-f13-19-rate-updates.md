🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-05 Reports and rules](README.md) › 🖥️ S-F13-19 Rate updates

# 🖥️ S-F13-19 Rate updates

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Update rates and rules from the country pack.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-05 step 2, U45 | desktop | ![FL-F13-05 step 2, U45, light](../../images/05-reports-and-rules/u45-payroll-officer/2-yearly-desktop-light.png) | ![FL-F13-05 step 2, U45, dark](../../images/05-reports-and-rules/u45-payroll-officer/2-yearly-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-19-rate-updates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-19-rate-updates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-19-rate-updates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-19-rate-updates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-19-rate-updates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-19-rate-updates-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-19-rate-updates-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-19-rate-updates-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the country pack's rate updates with their changes and dates, and the runs they affect.
- Empty: "No update waiting": the date of the last update is shown.
- Loading: the frame and titles show at once with placeholder rows for the rate updates; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the payroll officer reviews; only the administrator applies.
- Offline: not available offline: updates come from the country pack (T11). D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-16 Rate set](../../data/e-f13-16-rate-set.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-16 Rate set | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U45 | `u07-administrator/s-f13-19-rate-updates-e-f13-16-rate-set-active-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-19-rate-updates-e-f13-16-rate-set-active-desktop-{light,dark}.png` |

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

- [FL-F13-05 Reports and rules](../../flows/fl-f13-05-reports-and-rules.md)

## Open questions

None.

---

⬅️ [S-F13-18 Yearly reports](s-f13-18-yearly-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-20 Payroll assistant](../06-assistant/s-f13-20-payroll-assistant.md)
