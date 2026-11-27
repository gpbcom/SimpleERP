🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-01 Maintenance contracts](README.md) › 🖥️ S-SC19-04 Contract renewal

# 🖥️ S-SC19-04 Contract renewal

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the contracts to renew, with the new price and its
  computation.

## Purpose

Renew, change or end the contracts at their notice date and apply the index clause.

## Entry points

Trades and home services › Maintenance contracts › Renewals; the reminder of a notice date.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Renewals: December 2027                                  [Send notices] [Apply index]            |
| Contract  Customer     Old price  Index change  New price  Notice date   State                   |
| C-0412    Martin       260.00     +2.1 %        265.46     31 Oct        Renewal due             |
| C-0398    Dubois       180.00     none          180.00     15 Nov        Renewal due             |
| C-0377    Perrin       240.00     +2.1 %        245.04     30 Sep        Ended                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-01 step 4, U13 | desktop | ![FL-SC19-01 step 4, U13, light](../../images/01-maintenance-contracts/u13-owner/4-contract-renewal-desktop-light.png) | ![FL-SC19-01 step 4, U13, dark](../../images/01-maintenance-contracts/u13-owner/4-contract-renewal-desktop-dark.png) |
| FL-SC19-01 step 4, U13 | phone | ![FL-SC19-01 step 4, U13, light](../../images/01-maintenance-contracts/u13-owner/4-contract-renewal-phone-light.png) | ![FL-SC19-01 step 4, U13, dark](../../images/01-maintenance-contracts/u13-owner/4-contract-renewal-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-04-contract-renewal-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-04-contract-renewal-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-04-contract-renewal-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-04-contract-renewal-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-04-contract-renewal-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-04-contract-renewal-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-04-contract-renewal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-04-contract-renewal-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contract | E-SC19-01 contract | link | no | yes |
| Old price | E-SC19-01 yearly price | amount | no | yes |
| Index change | index of the clause | percentage | no | no |
| New price | computed price | amount | yes before sending | yes |
| Notice date | E-SC19-01 notice date | date | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Apply index | header | owner | the new price of each contract is computed |
| Send notices | header | owner | the customers receive the renewal notice |
| End contract | row | owner | the contract is Ended at its end date |

## States

- Normal: the contracts due with their old price, index change, new price, notice date and state.
- Empty: No contract reaches its notice date this month.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  index, a notice date past, a price changed without a clause, with the contract named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC19-01 Maintenance contracts](../../flows/fl-sc19-01-maintenance-contracts.md)

## Open questions

None.

---

⬅️ [S-SC19-03 Legal check-ups](s-sc19-03-legal-check-ups.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-05 Dispatch](../02-on-site-intervention/s-sc19-05-dispatch.md)
