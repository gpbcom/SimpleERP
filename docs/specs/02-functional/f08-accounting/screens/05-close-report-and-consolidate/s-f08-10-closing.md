🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-05 Close, report and consolidate](README.md) › 🖥️ S-F8-10 Closing

# 🖥️ S-F8-10 Closing

**Status:** ✅ specified

## Personas

- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Close the period and the year.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-05 step 1, U08 | desktop | ![FL-F8-05 step 1, U08, light](../../images/05-close-report-and-consolidate/u08-external-accountant/1-close-desktop-light.png) | ![FL-F8-05 step 1, U08, dark](../../images/05-close-report-and-consolidate/u08-external-accountant/1-close-desktop-dark.png) |
| Error E1, U08 | desktop | ![Error E1, U08, light](../../images/05-close-report-and-consolidate/u08-external-accountant/e1-unreconciled-blocks-close-desktop-light.png) | ![Error E1, U08, dark](../../images/05-close-report-and-consolidate/u08-external-accountant/e1-unreconciled-blocks-close-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-10-closing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-10-closing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-10-closing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-10-closing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-10-closing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-10-closing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-10-closing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-10-closing-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Close the period and the year, as the wireframe shows.
- Empty: No closing task yet for the period, with Start the closing.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-31 Closing checklist](../../data/e-f08-31-closing-checklist.md),
[E-F8-10 Fiscal period](../../data/e-f08-10-fiscal-period.md), [E-F8-27 FEC file](../../data/e-f08-27-fec-file.md),
[E-F8-29 Entry annotation](../../data/e-f08-29-entry-annotation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-31 Closing checklist | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U08 | `u05-accounting/s-f08-10-closing-e-f08-31-closing-checklist-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-10-closing-e-f08-31-closing-checklist-active-desktop-{light,dark}.png` |
| E-F8-10 Fiscal period | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U08 | `u05-accounting/s-f08-10-closing-e-f08-10-fiscal-period-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-10-closing-e-f08-10-fiscal-period-active-desktop-{light,dark}.png` |
| E-F8-27 FEC file | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U08 | `u05-accounting/s-f08-10-closing-e-f08-27-fec-file-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-10-closing-e-f08-27-fec-file-active-desktop-{light,dark}.png` |
| E-F8-29 Entry annotation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U08 | `u05-accounting/s-f08-10-closing-e-f08-29-entry-annotation-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-10-closing-e-f08-29-entry-annotation-active-desktop-{light,dark}.png` |

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

## Shown in

- [FL-F8-05 Close, report and consolidate](../../flows/fl-f08-05-close-report-and-consolidate.md)

## Open questions

None.

---

⬅️ [S-F8-09 Analytics and budgets](../04-tax-assets-and-analytics/s-f08-09-analytics-and-budgets.md) ·
⬆️ [Up](README.md) · ➡️ [S-F8-11 Financial reports](s-f08-11-financial-reports.md)
