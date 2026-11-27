🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-04 Tax, assets and analytics](README.md) › 🖥️ S-F8-08 Fixed assets

# 🖥️ S-F8-08 Fixed assets

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Manage fixed assets and deferrals.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-04 step 2, U05 | desktop | ![FL-F8-04 step 2, U05, light](../../images/04-tax-assets-and-analytics/u05-accounting/2-fixed-assets-desktop-light.png) | ![FL-F8-04 step 2, U05, dark](../../images/04-tax-assets-and-analytics/u05-accounting/2-fixed-assets-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-08-fixed-assets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-08-fixed-assets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-08-fixed-assets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-08-fixed-assets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-08-fixed-assets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-08-fixed-assets-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-08-fixed-assets-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-08-fixed-assets-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Manage fixed assets and deferrals, as the wireframe shows.
- Empty: No fixed asset yet for the period, with New asset.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-07 Fixed asset](../../data/e-f08-07-fixed-asset.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-07 Fixed asset | Running | Badge "Running"; a new record starts here; next: Disposed (UC-F8-08); fields editable within the role | U05 | `u05-accounting/s-f08-08-fixed-assets-e-f08-07-fixed-asset-running-desktop-{light,dark}.png` |
| E-F8-07 Fixed asset | Disposed | Badge "Disposed"; next: Sold (UC-F8-08); fields editable within the role | U05 | `u05-accounting/s-f08-08-fixed-assets-e-f08-07-fixed-asset-disposed-desktop-{light,dark}.png` |
| E-F8-07 Fixed asset | Sold | Badge "Sold"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-08-fixed-assets-e-f08-07-fixed-asset-sold-desktop-{light,dark}.png` |

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

⬅️ [S-F8-07 VAT returns](s-f08-07-vat-returns.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-09 Analytics and budgets](s-f08-09-analytics-and-budgets.md)
