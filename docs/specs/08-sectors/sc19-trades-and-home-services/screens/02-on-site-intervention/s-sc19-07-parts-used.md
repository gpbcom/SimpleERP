🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-02 On-site intervention](README.md) › 🖥️ S-SC19-07 Parts used

# 🖥️ S-SC19-07 Parts used

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the parts of the intervention, taken from the
  van.

## Purpose

Record the parts used on an intervention and take them out of the van's stock.

## Entry points

Trades and home services › My interventions › Parts; the scan button of the report.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Parts: I-3305, Garcia                                        Van 4   [Scan] [Add by name]        |
| Part               Reference   Quantity   Van stock after   Price                                |
| Seal 20/27         SE-2027     1          11                1.80                                 |
| Mixer cartridge    MC-35       1          2                 14.50                                |
| Total parts 16.30 EUR                                       [Add to the invoice]                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-02 step 3, U14 | phone | ![FL-SC19-02 step 3, U14, light](../../images/02-on-site-intervention/u14-field-worker/3-parts-used-phone-light.png) | ![FL-SC19-02 step 3, U14, dark](../../images/02-on-site-intervention/u14-field-worker/3-parts-used-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-07-parts-used-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-07-parts-used-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-07-parts-used-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-07-parts-used-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-07-parts-used-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-07-parts-used-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-07-parts-used-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-07-parts-used-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Part | E-F7-06 item | link | no | yes |
| Quantity | E-SC19-13 quantity | number | yes | yes |
| Van stock after | E-SC19-13 counted | number | no | no |
| Price | E-F7-06 sales price | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Scan | header | technician | the part is added and taken out of the van |
| Add by name | header | technician | the part is picked from the van's list |
| Return | row | technician | an unused part goes back into the van's stock |

## States

- Normal: the parts of the intervention with quantity, remaining stock and price.
- Empty: No part used yet, with Scan.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a part not in
  the van, a negative quantity, with the part named.
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

⬅️ [S-SC19-06 Site report](s-sc19-06-site-report.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-08 Sign and invoice](s-sc19-08-sign-and-invoice.md)
