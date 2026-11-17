🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-07 Client money, grants and non-profits](README.md) › 🖥️ S-F8-22 Grants

# 🖥️ S-F8-22 Grants

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Record grants and follow their recognition and reports.

## Entry points

Accounting › Grants.

## Wireframe

```text
+------------------------------------------------------------------+
| Grants                                           [+ Grant]        |
| Funder   Purpose   Amount   Received  Recognised  Deferred  Report |
| Region   van       30,000   30,000    6,000       24,000    03-31 |
| City     shelter   12,000   12,000    8,000       4,000     06-30 |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-07 step 3, U31 | desktop | ![FL-F8-07 step 3, U31, light](../../images/07-client-money-grants-and-non-profits/u31-treasurer/3-grants-desktop-light.png) | ![FL-F8-07 step 3, U31, dark](../../images/07-client-money-grants-and-non-profits/u31-treasurer/3-grants-desktop-dark.png) |
| FL-F8-07 step 3, U31 | phone | ![FL-F8-07 step 3, U31, light](../../images/07-client-money-grants-and-non-profits/u31-treasurer/3-grants-phone-light.png) | ![FL-F8-07 step 3, U31, dark](../../images/07-client-money-grants-and-non-profits/u31-treasurer/3-grants-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-22-grants-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-22-grants-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-22-grants-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-22-grants-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-22-grants-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-22-grants-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-22-grants-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-22-grants-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Funder, purpose, amounts, report date | E-F8-18 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Prepare report | accounting, treasurer | Funder report |

## States

- Normal: record grants and follow their recognition and reports.
- Empty: no grant yet: Add a grant.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed grants.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-18 Grant](../../data/e-f08-18-grant.md),
[E-F8-07 Fixed asset](../../data/e-f08-07-fixed-asset.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-18 Grant | Granted | Badge "Granted"; a new record starts here; next: Received (UC-SC12-19); fields editable within the role | U31 | `u31-treasurer/s-f08-22-grants-e-f08-18-grant-granted-{desktop,phone}-{light,dark}.png` |
| E-F8-18 Grant | Received | Badge "Received"; next: Closed (UC-F8-22); fields editable within the role | U31 | `u31-treasurer/s-f08-22-grants-e-f08-18-grant-received-{desktop,phone}-{light,dark}.png` |
| E-F8-07 Fixed asset | Running | Badge "Running"; a new record starts here; next: Disposed (UC-F8-08); fields editable within the role | U31 | `u31-treasurer/s-f08-22-grants-e-f08-07-fixed-asset-running-{desktop,phone}-{light,dark}.png` |
| E-F8-07 Fixed asset | Disposed | Badge "Disposed"; next: Sold (UC-F8-08); fields editable within the role | U31 | `u31-treasurer/s-f08-22-grants-e-f08-07-fixed-asset-disposed-{desktop,phone}-{light,dark}.png` |
| E-F8-07 Fixed asset | Sold | Badge "Sold"; final: read-only, no next state; the history shows how it got here | U31 | `u31-treasurer/s-f08-22-grants-e-f08-07-fixed-asset-sold-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-07 Client money, grants and non-profits](../../flows/fl-f08-07-client-money-grants-and-non-profits.md)

## Open questions

None.

---

⬅️ [S-F8-21 Client money](s-f08-21-client-money.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-23 Non-profit accounts](s-f08-23-non-profit-accounts.md)
