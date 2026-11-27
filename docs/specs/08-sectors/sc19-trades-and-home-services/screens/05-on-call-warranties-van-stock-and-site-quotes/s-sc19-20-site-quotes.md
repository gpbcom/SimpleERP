🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-05 On-call, warranties, van stock and site quotes](README.md) › 🖥️ S-SC19-20 Site quotes

# 🖥️ S-SC19-20 Site quotes

**Status:** ✅ specified

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
| Total incl. VAT 20 %: 1,022.40 EUR     Signed at home: yes, 2026-11-27                           |
| Withdrawal notice: attached   Withdrawal: 14 days, to 2026-12-11                                 |
| Payment: none for 7 days from the signature, allowed from 2026-12-05 (day 8)                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-05 step 4, U14 | phone | ![FL-SC19-05 step 4, U14, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u14-field-worker/4-site-quotes-phone-light.png) | ![FL-SC19-05 step 4, U14, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u14-field-worker/4-site-quotes-phone-dark.png) |
| FL-SC19-05 step 4, U09 | phone | ![FL-SC19-05 step 4, U09, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u09-customer/4-site-quotes-phone-light.png) | ![FL-SC19-05 step 4, U09, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u09-customer/4-site-quotes-phone-dark.png) |
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
| Urgent repair request | E-F6-03 urgent | the customer's express request, limited to the parts and work strictly needed; that part may be paid at once and has no withdrawal right (L221-28) | yes | no |
| Payment ban and withdrawal | computed from the signature | no payment for 7 days from the signature, allowed from day 8 (Code de la consommation L221-10); withdrawal to day 14 | no | yes when signed at home |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add line | form | technician | a line is added from the catalogue |
| Send for signature | header | technician | the customer receives the quote with the notice |
| Record urgent request | header | technician | the customer's express request is recorded; the urgent part starts at once and may be paid |

## States

- Normal: the quote with its lines, total, notice, signature state, the 7-day payment ban with its first allowed day,
  and the 14-day withdrawal period.
- Empty: No quote yet, with New site quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  notice, or a payment asked within 7 days of the signature, refused with the first allowed day (day 8), with the field
  to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: the quote is signed online, as the customer's signature and the copy sent need the
  network ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention
  records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Phone first, as UC-SC19-20 says (the use case prevails over the screen,
[D573](../../../../06-decisions/foundations/d573-precedence-between-spec-pages.md)): the technician builds and sends the
quote on the phone at the customer's home, and the customer reads and signs it on their own phone; the office reads
the quotes on the desktop, with the same content.

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
