🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-05 On-call, warranties, van stock and site quotes](README.md) › 🖥️ S-SC19-20 Site quotes

# 🖥️ S-SC19-20 Site quotes

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the quote lines, price and notice, at the
  customer's home.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the quote to read and sign on my phone, with the
  withdrawal form.

## Purpose

Make a quote on site and have it signed on the phone with the withdrawal notice.

## Entry points

Trades and home services › Site quotes; a customer's page on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Site quote Q-5529: Garcia                                 [Send for signature]                   |
| Line                   Quantity   Price      Total                                               |
| Replace water heater   1          690.00     690.00                                              |
| Labour                 3 h        54.00      162.00                                              |
| Total incl. VAT 20 %: 1,022.40 EUR     Signed at home: yes                                       |
| Withdrawal notice: attached   Delay: 14 days   Deposit: not before the delay                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-05 step 4, U14 | phone | ![FL-SC19-05 step 4, U14, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u14-field-worker/4-site-quotes-phone-light.png) | ![FL-SC19-05 step 4, U14, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u14-field-worker/4-site-quotes-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-20-site-quotes-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-20-site-quotes-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-20-site-quotes-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-20-site-quotes-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-20-site-quotes-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-20-site-quotes-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-20-site-quotes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-20-site-quotes-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Lines | E-F6-03 lines | item, quantity and price | yes while Draft | yes |
| Signed at home | E-F6-03 signed at home | yes or no | yes | yes |
| Withdrawal notice | E-F6-03 notice | document | no | yes when signed at home |
| Customer signature | E-F2-14 signature | signature | no | yes |
| Urgent repair request | E-F6-03 urgent | written request | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add line | form | technician | a line is added from the catalogue |
| Send for signature | header | technician | the customer receives the quote with the notice |
| Record urgent request | header | technician | the customer's written request is recorded |

## States

- Normal: the quote with its lines, total, notice, delay and signature state.
- Empty: No quote yet, with New site quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  notice, a payment asked in the delay, with the field to correct.
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

- [FL-SC19-05](../../flows/fl-sc19-05-on-call-warranties-van-stock-and-site-quotes.md)

## Open questions

None.

---

⬅️ [S-SC19-19 Van stock](s-sc19-19-van-stock.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-L01 Maintenance contracts](../00-lists/s-sc19-l01-maintenance-contracts.md)
