🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-03 Home services tax credit](README.md) › 🖥️ S-SC19-09 Household services

# 🖥️ S-SC19-09 Household services

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the household contracts with their services, hours and
  eligibility.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the contract to read and accept on the phone.

## Purpose

Sell recurring cleaning and gardening to households and show which services open the tax credit.

## Entry points

Trades and home services › Household contracts; a household's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Household contract H-218: Lambert                       State: Draft   [Send for acceptance]     |
| Service           Frequency   Hours   Price/h   Eligible                                         |
| Cleaning          weekly      3       26.00     yes                                              |
| Lawn care         monthly     2       32.00     yes                                              |
| Boiler repair     one-off     1       70.00     no (own quote)                                   |
| Yearly cost 4,590 EUR   Expected credit 2,295 EUR   Advance: asked   [Add service]               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-03 step 1, U13 | desktop | ![FL-SC19-03 step 1, U13, light](../../images/03-home-services-tax-credit/u13-owner/1-household-services-desktop-light.png) | ![FL-SC19-03 step 1, U13, dark](../../images/03-home-services-tax-credit/u13-owner/1-household-services-desktop-dark.png) |
| FL-SC19-03 step 1, U13 | phone | ![FL-SC19-03 step 1, U13, light](../../images/03-home-services-tax-credit/u13-owner/1-household-services-phone-light.png) | ![FL-SC19-03 step 1, U13, dark](../../images/03-home-services-tax-credit/u13-owner/1-household-services-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/03-home-services-tax-credit/u13-owner/e1-the-service-is-not-eligible-desktop-light.png) | ![Error E1, U13, dark](../../images/03-home-services-tax-credit/u13-owner/e1-the-service-is-not-eligible-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/03-home-services-tax-credit/u13-owner/e1-the-service-is-not-eligible-phone-light.png) | ![Error E1, U13, dark](../../images/03-home-services-tax-credit/u13-owner/e1-the-service-is-not-eligible-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-09-household-services-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-09-household-services-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-09-household-services-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-09-household-services-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-09-household-services-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-09-household-services-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-09-household-services-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-09-household-services-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Household | E-SC19-06 household | link | no | yes |
| Service | E-SC19-06 services | lines of service, frequency, hours and price | yes while Draft | yes |
| Eligible | E-SC19-06 eligible | yes or no from the catalogue | no | yes |
| Advance | E-SC19-06 advance | asked, declined | yes while Draft | no |
| Start date | E-SC19-06 start | date | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add service | contract | owner | a line is added with its eligibility |
| Send for acceptance | header | owner | the household receives the contract |
| Plan visits | header | owner | the visits are planned on the visits screen |

## States

- Normal: the contracts with household, services, hours, eligibility and state.
- Empty: No household contract yet, with Create a contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  declaration, a service not in the catalogue, with the line named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-06 Household contract](../../data/e-sc19-06-household-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-06 Household contract | Draft | Badge "Draft"; a new record starts here; next: Active or Ended (BR-SC19-09, UC-SC19-09); fields editable within the role | U13, U09 | `u13-owner/s-sc19-09-household-services-e-sc19-06-household-contract-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-09-household-services-e-sc19-06-household-contract-draft-phone-{light,dark}.png` |
| E-SC19-06 Household contract | Active | Badge "Active"; next: Suspended or Ended (UC-SC19-10); fields editable within the role | U13, U09 | `u13-owner/s-sc19-09-household-services-e-sc19-06-household-contract-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-09-household-services-e-sc19-06-household-contract-active-phone-{light,dark}.png` |
| E-SC19-06 Household contract | Suspended | Badge "Suspended"; next: Active (UC-SC19-10); fields editable within the role | U13, U09 | `u13-owner/s-sc19-09-household-services-e-sc19-06-household-contract-suspended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-09-household-services-e-sc19-06-household-contract-suspended-phone-{light,dark}.png` |
| E-SC19-06 Household contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc19-09-household-services-e-sc19-06-household-contract-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-09-household-services-e-sc19-06-household-contract-ended-phone-{light,dark}.png` |

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

- [FL-SC19-03 Home services tax credit](../../flows/fl-sc19-03-home-services-tax-credit.md)

## Open questions

None.

---

⬅️ [S-SC19-08 Sign and invoice](../02-on-site-intervention/s-sc19-08-sign-and-invoice.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-10 Household visits](s-sc19-10-household-visits.md)
