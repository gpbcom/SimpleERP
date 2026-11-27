🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-07 Passengers, removals, courier and freight](README.md) › 🖥️ S-SC07-24 Freight forwarding

# 🖥️ S-SC07-24 Freight forwarding

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the files, their documents and their carrier legs.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the duties and VAT to check and the invoice to
  issue.

## Purpose

Prepare a shipment file with its documents, its customs declaration and its carrier legs, and bill the customer what was
advanced.

## Entry points

Transport and logistics › Shipment files; a customer's page; the customs reminder.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| File SF-0420  Import  Hai Phong -> Lyon   Customer: Atelier Roche     State: Documents  [Declare |
| Incoterm FOB   Goods 4 pallets, 2,300 kg   Value 38,200 USD   EORI declarant FR12345678901234    |
| Document             Status      Required for                                                    |
| Commercial invoice   Received    Customs value                                                   |
| Packing list         Received    Weights                                                         |
| Bill of lading       Missing     Transport and release          [Ask the carrier]                |
| Duties 1,240.00  VAT 7,870.00 (deferred)  Fee 180.00          Next: lodge when documents complet |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-07 step 4, U29 | desktop | ![FL-SC07-07 step 4, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/4-freight-forwarding-desktop-light.png) | ![FL-SC07-07 step 4, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/4-freight-forwarding-desktop-dark.png) |
| FL-SC07-07 step 4, U29 | phone | ![FL-SC07-07 step 4, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/4-freight-forwarding-phone-light.png) | ![FL-SC07-07 step 4, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/4-freight-forwarding-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-24-freight-forwarding-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-24-freight-forwarding-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-24-freight-forwarding-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-24-freight-forwarding-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-24-freight-forwarding-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-24-freight-forwarding-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-24-freight-forwarding-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-24-freight-forwarding-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC07-21 customer | link | no | yes |
| Direction | E-SC07-21 direction | import, export, transit | yes while Opened | yes |
| Incoterm | E-SC07-21 incoterm | code | yes while Opened | yes |
| Goods and codes | E-SC07-21 goods | lines with tariff code | yes while Documents | yes |
| EORI numbers | E-SC07-21 eori numbers | text per party | yes | yes |
| Documents | E-SC07-21 documents | list with status | yes | yes |
| Duties and VAT | E-SC07-21 duties | amounts in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Create file | header | dispatcher | a file with the parties and goods |
| Attach document | document row | dispatcher, customer | the document is Received |
| Lodge declaration | header | dispatcher | the declaration is sent and the file is Declared |
| Bill | header | accounting | the invoice with the duties advanced and the fee |

## States

- Normal: the file with its parties, goods, documents, duties and carrier legs.
- Empty: No file yet, with New file.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing EORI
  number, tariff code or document, with the field to complete.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC07-21 Shipment file](../../data/e-sc07-21-shipment-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-21 Shipment file | Opened | Badge "Opened"; a new record starts here; next: Documents (UC-SC07-24); fields editable within the role | U29, U05 | `u29-dispatcher/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-opened-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-opened-desktop-{light,dark}.png` |
| E-SC07-21 Shipment file | Documents | Badge "Documents"; next: Declared (BR-SC07-19); fields editable within the role | U29, U05 | `u29-dispatcher/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-documents-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-documents-desktop-{light,dark}.png` |
| E-SC07-21 Shipment file | Declared | Badge "Declared"; next: Cleared (UC-SC07-24); fields editable within the role | U29, U05 | `u29-dispatcher/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-declared-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-declared-desktop-{light,dark}.png` |
| E-SC07-21 Shipment file | Cleared | Badge "Cleared"; next: Closed (UC-SC07-24); fields editable within the role | U29, U05 | `u29-dispatcher/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-cleared-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-cleared-desktop-{light,dark}.png` |
| E-SC07-21 Shipment file | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U29, U05 | `u29-dispatcher/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-closed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc07-24-freight-forwarding-e-sc07-21-shipment-file-closed-desktop-{light,dark}.png` |

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

- [FL-SC07-07](../../flows/fl-sc07-07-passengers-removals-courier-and-freight.md)

## Open questions

None.

---

⬅️ [S-SC07-23 Last mile](s-sc07-23-last-mile.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-L01 Transport orders](../00-lists/s-sc07-l01-transport-orders.md)
