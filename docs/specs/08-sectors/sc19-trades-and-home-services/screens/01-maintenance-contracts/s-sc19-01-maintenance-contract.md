🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-01 Maintenance contracts](README.md) › 🖥️ S-SC19-01 Maintenance contract

# 🖥️ S-SC19-01 Maintenance contract

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the contracts, their equipment and the yearly price, at the
  desk.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the contract to read and sign on the phone.

## Purpose

Sell a contract for customer equipment, list the legal check-ups it covers and get the customer's signature.

## Entry points

Trades and home services › Maintenance contracts; a customer's page; a quote that includes equipment.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Contract C-0412: Martin household                          State: Draft   [Send for signature]   |
| Equipment       Make      Serial    Place     Legal check-up        Interval                     |
| Gas boiler      Atlas     B-77120   Cellar    Yearly check-up       12 months                    |
| Heat pump       Nordic    HP-3381   Garden    Per the pack          24 months                    |
| Price per year 260.00 EUR   Visits 2   Response 48 h   Index clause: yes   [Add equipment]       |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-01 step 1, U13 | desktop | ![FL-SC19-01 step 1, U13, light](../../images/01-maintenance-contracts/u13-owner/1-maintenance-contract-desktop-light.png) | ![FL-SC19-01 step 1, U13, dark](../../images/01-maintenance-contracts/u13-owner/1-maintenance-contract-desktop-dark.png) |
| FL-SC19-01 step 1, U13 | phone | ![FL-SC19-01 step 1, U13, light](../../images/01-maintenance-contracts/u13-owner/1-maintenance-contract-phone-light.png) | ![FL-SC19-01 step 1, U13, dark](../../images/01-maintenance-contracts/u13-owner/1-maintenance-contract-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-01-maintenance-contract-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-01-maintenance-contract-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-01-maintenance-contract-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-01-maintenance-contract-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-01-maintenance-contract-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-01-maintenance-contract-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-01-maintenance-contract-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-01-maintenance-contract-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC19-01 customer | link | no | yes |
| Equipment | E-SC19-01 equipment | lines of kind, make, serial and place | yes while Draft | yes |
| Legal check-up | E-SC19-01 legal check-up | text from the kind | no | yes |
| Yearly price | E-SC19-01 yearly price | amount | yes while Draft | yes |
| Visits per year | E-SC19-01 visits | number | yes while Draft | yes |
| Start date | E-SC19-01 start | date | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add equipment | contract | owner | a line is added with the check-up of its kind |
| Send for signature | header | owner | the customer receives the contract to sign |
| Plan first visit | header | owner | the visit is planned on the visits screen |

## States

- Normal: the contracts with their customer, equipment, check-ups, price and state.
- Empty: No contract yet, with Create a contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an equipment
  without a check-up, a price missing, a signature missing, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-01 Maintenance contract](../../data/e-sc19-01-maintenance-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-01 Maintenance contract | Draft | Badge "Draft"; a new record starts here; next: Active or Ended (BR-SC19-01, UC-SC19-01); fields editable within the role | U13, U09 | `u13-owner/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-draft-phone-{light,dark}.png` |
| E-SC19-01 Maintenance contract | Active | Badge "Active"; next: Renewal due or Ended (UC-SC19-04); fields editable within the role | U13, U09 | `u13-owner/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-active-phone-{light,dark}.png` |
| E-SC19-01 Maintenance contract | Renewal due | Badge "Renewal due"; next: Active or Ended (BR-SC19-04); fields editable within the role | U13, U09 | `u13-owner/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-renewal-due-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-renewal-due-phone-{light,dark}.png` |
| E-SC19-01 Maintenance contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-01-maintenance-contract-e-sc19-01-maintenance-contract-ended-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

⬆️ [Up](README.md) · ➡️ [S-SC19-02 Recurring visits](s-sc19-02-recurring-visits.md)
