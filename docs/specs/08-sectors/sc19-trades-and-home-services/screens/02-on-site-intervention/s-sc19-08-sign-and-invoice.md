🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-02 On-site intervention](README.md) › 🖥️ S-SC19-08 Sign and invoice

# 🖥️ S-SC19-08 Sign and invoice

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the report to show and the invoice to issue on
  the phone.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the report to read, sign and pay on the phone.

## Purpose

Collect the customer's signature on the report and issue and send the invoice at once.

## Entry points

Trades and home services › My interventions › Sign; the Finished button of the report.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Sign: I-3305, Garcia                                            [Sign] [Customer refuses]        |
| Work: Seal replaced, cartridge changed       Time 43 min       Parts 16.30 EUR                   |
| Labour 54.00 EUR   Call-out 60.00 EUR   VAT 20 %   Total 156.00 EUR                              |
| Customer signature: ____________      Remark: ____________                                       |
| [Issue the invoice] [Send payment link]                                                          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-02 step 4, U14 | phone | ![FL-SC19-02 step 4, U14, light](../../images/02-on-site-intervention/u14-field-worker/4-sign-and-invoice-phone-light.png) | ![FL-SC19-02 step 4, U14, dark](../../images/02-on-site-intervention/u14-field-worker/4-sign-and-invoice-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-08-sign-and-invoice-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-08-sign-and-invoice-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-08-sign-and-invoice-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-08-sign-and-invoice-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-08-sign-and-invoice-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-08-sign-and-invoice-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-08-sign-and-invoice-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-08-sign-and-invoice-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Work done | E-SC19-05 work | text | no | yes |
| Total | E-F6-05 total | amount | no | yes |
| Customer signature | E-SC19-05 signature | signature | yes | yes |
| Remark | E-SC19-05 customer remark | text | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sign | form | customer | the report is Signed |
| Customer refuses | form | technician | the refusal and its reason are recorded |
| Issue the invoice | header | technician | the invoice is sent to the customer |

## States

- Normal: the report, the amounts, the signature box and the invoice button.
- Empty: No report to sign.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an address
  missing, a signature missing, an invoice not issued, with the field to correct.
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

- [FL-SC19-02 On-site intervention](../../flows/fl-sc19-02-on-site-intervention.md)

## Open questions

None.

---

⬅️ [S-SC19-07 Parts used](s-sc19-07-parts-used.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-09 Household services](../03-home-services-tax-credit/s-sc19-09-household-services.md)
