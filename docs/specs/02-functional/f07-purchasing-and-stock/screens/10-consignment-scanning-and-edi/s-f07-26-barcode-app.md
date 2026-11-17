🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F7-26 Warehouse barcode app

# 🖥️ S-F7-26 Warehouse barcode app

**Status:** 🔄 waiting for the owner

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md): their own tasks, on a phone.

## Purpose

Do a warehouse step by scanning, with each scan checked against what the step expects.

## Entry points

The warehouse app on the phone; a task from the supervisor's list; the AI assistant
[BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md).

## Wireframe

```text
+---------------------------------------------+
| Pick wave 12                  line 3 of 8   |
|---------------------------------------------|
| Go to      A-12-3                [scanned]  |
| Expect     Oak plank 30mm  x 20             |
| Scan item  [camera]  or type the code       |
|                                             |
| STOP  Scanned: Brass hinge                  |
|       Expected: Oak plank 30mm              |
| [Scan again]            [Ask the supervisor]|
+---------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-10 step 2, U15 | phone | ![FL-F7-10 step 2, U15, light](../../images/10-consignment-scanning-and-edi/u15-warehouse-operator/2-barcode-app-phone-light.png) | ![FL-F7-10 step 2, U15, dark](../../images/10-consignment-scanning-and-edi/u15-warehouse-operator/2-barcode-app-phone-dark.png) |
| FL-F7-10 step 2, U15 | tablet | ![FL-F7-10 step 2, U15, light](../../images/10-consignment-scanning-and-edi/u15-warehouse-operator/2-barcode-app-tablet-light.png) | ![FL-F7-10 step 2, U15, dark](../../images/10-consignment-scanning-and-edi/u15-warehouse-operator/2-barcode-app-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-26-barcode-app-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-26-barcode-app-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-26-barcode-app-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-26-barcode-app-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-26-barcode-app-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-26-barcode-app-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-26-barcode-app-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-26-barcode-app-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Task and line | task lines | text and counter | no | yes |
| Location to go to | E-F7-07 | code and name | no | yes |
| Item expected | E-F7-06 | name, code and quantity | no | yes |
| Scan | the scanned code | camera or typed code | yes | yes |
| Lot or serial | E-F7-10 | code | yes | for tracked items |
| Result | the check | match, stop | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Scan | camera, scanner | warehouse operator | the code is checked against the line |
| Scan again | stop message | warehouse operator | the operator scans another item |
| Ask the supervisor | stop message | warehouse operator | the supervisor is notified |
| Override with a reason | supervisor's screen | supervisor | the line goes on with the scanned item; audited |

## States

- Normal: the current line with the location, the expected item and the scan result.
- Empty: No task for the operator, with the supervisor's name to ask.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused scan
  shows the scanned and the expected item; a task that cannot load shows Retry.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Scans are kept on the phone and checked again when the network is back: a scan that no longer matches is
  refused then
  ([BR-F7-20](../../business-rules/br-f07-20-a-scan-that-does-not-match-the-expected-item-stops-the-step.md)); the
  screen shows the count of scans waiting.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Built for a phone first: big targets, one line at a time, the camera one tap away, the result in colour and in words.
The supervisor's list is a desktop screen.

## Accessibility

Every result is also spoken or vibrated, never colour alone; buttons are large enough for gloves; the camera can be
switched off to type.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-10](../../flows/fl-f07-10-consignment-scanning-and-edi.md)

## Open questions

None.

---

⬅️ [S-F7-25 Consignment stock](s-f07-25-consignment-stock.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-27 Periodic valuation](s-f07-27-periodic-valuation.md)
