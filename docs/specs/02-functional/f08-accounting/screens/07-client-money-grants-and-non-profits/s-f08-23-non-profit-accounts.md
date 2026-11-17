🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-07 Client money, grants and non-profits](README.md) › 🖥️ S-F8-23 Non-profit accounts

# 🖥️ S-F8-23 Non-profit accounts

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Show an association's resources, dedicated funds and volunteer contributions.

## Entry points

Accounting › Non-profit.

## Wireframe

```text
+------------------------------------------------------------------+
| Association 2026   Donations 48,000  Grants 20,000  Dues 6,400    |
| Dedicated funds: Shelter 3,000                                    |
| Volunteers: 2,400 h valued 28,000 EUR (notes)                     |
| Tax receipts issued: 312       Publication: due 2027-06-30        |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-07 step 4, U31 | desktop | ![FL-F8-07 step 4, U31, light](../../images/07-client-money-grants-and-non-profits/u31-treasurer/4-non-profit-accounts-desktop-light.png) | ![FL-F8-07 step 4, U31, dark](../../images/07-client-money-grants-and-non-profits/u31-treasurer/4-non-profit-accounts-desktop-dark.png) |
| FL-F8-07 step 4, U31 | phone | ![FL-F8-07 step 4, U31, light](../../images/07-client-money-grants-and-non-profits/u31-treasurer/4-non-profit-accounts-phone-light.png) | ![FL-F8-07 step 4, U31, dark](../../images/07-client-money-grants-and-non-profits/u31-treasurer/4-non-profit-accounts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-23-non-profit-accounts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-23-non-profit-accounts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-23-non-profit-accounts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-23-non-profit-accounts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-23-non-profit-accounts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-23-non-profit-accounts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-23-non-profit-accounts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-23-non-profit-accounts-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Resources, funds, volunteers, receipts | E-F8-19, E-F8-20 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Move to fund | treasurer | Dedicated fund |
| Publish | treasurer | Accounts published |

## States

- Normal: show an association's resources, dedicated funds and volunteer contributions.
- Empty: a new association: "No resource recorded yet".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed years.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-19 Dedicated fund](../../data/e-f08-19-dedicated-fund.md),
[E-F8-20 Volunteer contribution](../../data/e-f08-20-volunteer-contribution.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-19 Dedicated fund | Open | Badge "Open"; a new record starts here; next: Closed (UC-SC08-14); fields editable within the role | U31 | `u31-treasurer/s-f08-23-non-profit-accounts-e-f08-19-dedicated-fund-open-{desktop,phone}-{light,dark}.png` |
| E-F8-19 Dedicated fund | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U31 | `u31-treasurer/s-f08-23-non-profit-accounts-e-f08-19-dedicated-fund-closed-{desktop,phone}-{light,dark}.png` |
| E-F8-20 Volunteer contribution | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U31 | `u31-treasurer/s-f08-23-non-profit-accounts-e-f08-20-volunteer-contribution-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-07 Client money, grants and non-profits](../../flows/fl-f08-07-client-money-grants-and-non-profits.md)

## Open questions

None.

---

⬅️ [S-F8-22 Grants](s-f08-22-grants.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-24 Corporate tax](../08-year-end-duties/s-f08-24-corporate-tax.md)
