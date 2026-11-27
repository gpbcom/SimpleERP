🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-05 Reports and rules](README.md) › 🖥️ S-F13-18 Yearly reports

# 🖥️ S-F13-18 Yearly reports

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Report yearly.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-05 step 1, U45 | desktop | ![FL-F13-05 step 1, U45, light](../../images/05-reports-and-rules/u45-payroll-officer/1-rate-update-desktop-light.png) | ![FL-F13-05 step 1, U45, dark](../../images/05-reports-and-rules/u45-payroll-officer/1-rate-update-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-18-yearly-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-18-yearly-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-18-yearly-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-18-yearly-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-18-yearly-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-18-yearly-reports-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-18-yearly-reports-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-18-yearly-reports-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the yearly reports with their state: computed, checked, filed or published.
- Empty: "No year closed yet": shown before the first full year of payroll.
- Loading: the frame and titles show at once with placeholder rows for the yearly reports; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads; filed reports are read-only.
- Offline: not available offline: reports are computed on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-15 Yearly payroll report](../../data/e-f13-15-yearly-payroll-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-15 Yearly payroll report | Checked | Badge "Checked"; a new record starts here; next: Filed (UC-F13-18); fields editable within the role | U13, U45 | `u13-owner/s-f13-18-yearly-reports-e-f13-15-yearly-payroll-report-checked-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-18-yearly-reports-e-f13-15-yearly-payroll-report-checked-desktop-{light,dark}.png` |
| E-F13-15 Yearly payroll report | Filed | Badge "Filed"; final: read-only, no next state; the history shows how it got here | U13, U45 | `u13-owner/s-f13-18-yearly-reports-e-f13-15-yearly-payroll-report-filed-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-18-yearly-reports-e-f13-15-yearly-payroll-report-filed-desktop-{light,dark}.png` |

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

⬅️ [S-F13-17 Benefits](../04-events/s-f13-17-benefits.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-19 Rate updates](s-f13-19-rate-updates.md)
