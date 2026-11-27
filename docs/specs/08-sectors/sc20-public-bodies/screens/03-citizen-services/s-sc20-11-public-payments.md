🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-03 Citizen services](README.md) › 🖥️ S-SC20-11 Public payments

# 🖥️ S-SC20-11 Public payments

**Status:** ✅ specified

## Personas

- [U56 Citizen](../../../../01-users/personas/u56-citizen.md): my bills to pay, with the amount and the payment options,
  on the phone.

## Purpose

Let citizens pay municipal bills online through the public treasury's channel.

## Entry points

Public bodies › Pay a bill; the payment link in a bill's email.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Pay a bill                                                    Citizen: M. Roux                   |
| Bill        Title      Amount    Due        State                                                |
| Canteen     T-0412     84.00     15 Mar     Open                                                 |
| Hall deposit T-0398    300.00    20 Mar     Open                                                 |
| Pay by: [Card] [Direct debit]                      [Pay 84.00 EUR]                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-03 step 3, U56 | phone | ![FL-SC20-03 step 3, U56, light](../../images/03-citizen-services/u56-citizen/3-public-payments-phone-light.png) | ![FL-SC20-03 step 3, U56, dark](../../images/03-citizen-services/u56-citizen/3-public-payments-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc20-11-public-payments-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc20-11-public-payments-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc20-11-public-payments-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc20-11-public-payments-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc20-11-public-payments-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc20-11-public-payments-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc20-11-public-payments-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc20-11-public-payments-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Bill | E-SC20-03 title | link | no | yes |
| Amount | E-SC20-03 amount | amount | no | yes |
| Due date | E-SC20-03 due | date | no | yes |
| Payment method | channel option | card, direct debit | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Pay | form | citizen | the citizen is taken to the treasury's channel |
| Download receipt | row | citizen | the receipt is shown |
| Match payment | row | public finance officer | an unmatched payment is linked to a title |

## States

- Normal: the bills with title, amount, due date and state, and the payment options.
- Empty: No bill to pay.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a channel
  unavailable, a payment failed, with the bill named.
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

- [FL-SC20-03 Citizen services](../../flows/fl-sc20-03-citizen-services.md)

## Open questions

None.

---

⬅️ [S-SC20-10 Hall booking](s-sc20-10-hall-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-12 Council decisions](s-sc20-12-council-decisions.md)
