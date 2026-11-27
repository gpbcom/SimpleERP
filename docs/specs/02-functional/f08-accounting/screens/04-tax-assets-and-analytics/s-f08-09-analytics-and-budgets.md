🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-04 Tax, assets and analytics](README.md) › 🖥️ S-F8-09 Analytics and budgets

# 🖥️ S-F8-09 Analytics and budgets

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Track analytics and budgets.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-04 step 3, U02 | desktop | ![FL-F8-04 step 3, U02, light](../../images/04-tax-assets-and-analytics/u02-manager/3-analytics-and-budgets-desktop-light.png) | ![FL-F8-04 step 3, U02, dark](../../images/04-tax-assets-and-analytics/u02-manager/3-analytics-and-budgets-desktop-dark.png) |
| FL-F8-04 step 3, U02 | phone | ![FL-F8-04 step 3, U02, light](../../images/04-tax-assets-and-analytics/u02-manager/3-analytics-and-budgets-phone-light.png) | ![FL-F8-04 step 3, U02, dark](../../images/04-tax-assets-and-analytics/u02-manager/3-analytics-and-budgets-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-09-analytics-and-budgets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-09-analytics-and-budgets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-09-analytics-and-budgets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-09-analytics-and-budgets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-09-analytics-and-budgets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-09-analytics-and-budgets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-09-analytics-and-budgets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-09-analytics-and-budgets-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Track analytics and budgets, as the wireframe shows.
- Empty: No budget yet for the period, with New budget.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-08 Accounting budget](../../data/e-f08-08-accounting-budget.md),
[E-F8-30 Analytic plan](../../data/e-f08-30-analytic-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-08 Accounting budget | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U05, U13 | `u02-manager/s-f08-09-analytics-and-budgets-e-f08-08-accounting-budget-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-09-analytics-and-budgets-e-f08-08-accounting-budget-active-desktop-{light,dark}.png`, `u13-owner/s-f08-09-analytics-and-budgets-e-f08-08-accounting-budget-active-{desktop,phone}-{light,dark}.png` |
| E-F8-30 Analytic plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U05, U13 | `u02-manager/s-f08-09-analytics-and-budgets-e-f08-30-analytic-plan-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-09-analytics-and-budgets-e-f08-30-analytic-plan-active-desktop-{light,dark}.png`, `u13-owner/s-f08-09-analytics-and-budgets-e-f08-30-analytic-plan-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F8-04 Tax, assets and analytics](../../flows/fl-f08-04-tax-assets-and-analytics.md)

## Open questions

None.

---

⬅️ [S-F8-08 Fixed assets](s-f08-08-fixed-assets.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-10 Closing](../05-close-report-and-consolidate/s-f08-10-closing.md)
