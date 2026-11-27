🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC14-07 Hardware, licences, research tax credit and sponsorship](README.md) ›
🖥️ S-SC14-22 Hardware leasing

# 🖥️ S-SC14-22 Hardware leasing

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the offers, the leases and the monthly invoices.
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the delivery and the return, with the serial
  scan, on the phone.

## Purpose

Lease and sell IT hardware, follow each device by serial number until it returns, and bill the lease for the devices
still out.

## Entry points

IT and software › Hardware; a customer's page; the technician's day on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Leases: Cabinet Perrin                       Fee 700.00 EUR / month    [New lease] [Scan return] |
| Serial       Device        Since       Term end    State       Wipe                              |
| SN-77120     Laptop 14     2024-03-01  2027-02-28  Leased      -                                 |
| SN-77121     Laptop 14     2024-03-01  2027-02-28  Returned    Certificate 8812                  |
| SN-80412     Switch 24     2025-01-10  2028-01-09  Leased      -                                 |
| Out at the customer: 18 devices                                  [Invoice the month]             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-07 step 1, U03 | desktop | ![FL-SC14-07 step 1, U03, light](../../images/07-hardware-licences-and-tax-credits/u03-sales/1-hardware-leasing-desktop-light.png) | ![FL-SC14-07 step 1, U03, dark](../../images/07-hardware-licences-and-tax-credits/u03-sales/1-hardware-leasing-desktop-dark.png) |
| FL-SC14-07 step 1, U03 | phone | ![FL-SC14-07 step 1, U03, light](../../images/07-hardware-licences-and-tax-credits/u03-sales/1-hardware-leasing-phone-light.png) | ![FL-SC14-07 step 1, U03, dark](../../images/07-hardware-licences-and-tax-credits/u03-sales/1-hardware-leasing-phone-dark.png) |
| FL-SC14-07 step 1, U03 | tablet | ![FL-SC14-07 step 1, U03, light](../../images/07-hardware-licences-and-tax-credits/u03-sales/1-hardware-leasing-tablet-light.png) | ![FL-SC14-07 step 1, U03, dark](../../images/07-hardware-licences-and-tax-credits/u03-sales/1-hardware-leasing-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-22-hardware-leasing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-22-hardware-leasing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-22-hardware-leasing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-22-hardware-leasing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-22-hardware-leasing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-22-hardware-leasing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-22-hardware-leasing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-22-hardware-leasing-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Serial number | E-SC14-17 serial number | text | no | yes |
| Device | E-SC14-17 item | link | no | yes |
| Customer | E-SC14-17 customer | link | yes while Reserved | yes |
| Lease dates | E-SC14-17 start, end | dates | yes while Reserved | yes |
| Monthly fee | E-SC14-17 fee | amount in EUR | yes while Reserved | yes |
| Wipe certificate | E-SC14-17 wipe certificate | file | yes while Returned | yes to reuse |
| Returned on | E-SC14-17 returned on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New lease | header | sales | devices reserved and a lease contract in draft |
| Scan delivery | phone | technician | the serial is saved and the device is Leased |
| Scan return | phone | technician | the device is Returned and the wipe is asked for |
| Invoice the month | header | accounting | one invoice line per device still Leased |

## States

- Normal: the devices with serial number, customer, lease dates, state and wipe certificate.
- Empty: No leased device yet, with New lease.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a serial number
  not on the lease, a missing wipe certificate, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC14-17 Leased device](../../data/e-sc14-17-leased-device.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-17 Leased device | Reserved | Badge "Reserved"; a new record starts here; next: Leased (UC-SC14-22); fields editable within the role | U03, U14 | `u03-sales/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-reserved-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-reserved-phone-{light,dark}.png` |
| E-SC14-17 Leased device | Leased | Badge "Leased"; next: Returned (BR-SC14-16); fields editable within the role | U03, U14 | `u03-sales/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-leased-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-leased-phone-{light,dark}.png` |
| E-SC14-17 Leased device | Returned | Badge "Returned"; next: Leased, Resold or Recycled (UC-SC14-22); fields editable within the role | U03, U14 | `u03-sales/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-returned-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-returned-phone-{light,dark}.png` |
| E-SC14-17 Leased device | Resold | Badge "Resold"; final: read-only, no next state; the history shows how it got here | U03, U14 | `u03-sales/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-resold-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-resold-phone-{light,dark}.png` |
| E-SC14-17 Leased device | Recycled | Badge "Recycled"; final: read-only, no next state; the history shows how it got here | U03, U14 | `u03-sales/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-recycled-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc14-22-hardware-leasing-e-sc14-17-leased-device-recycled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The technician's phone scans a serial number and shows the customer's list of devices.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC14-07](../../flows/fl-sc14-07-hardware-licences-and-tax-credits.md)

## Open questions

None.

---

⬅️ [S-SC14-21 Features](../04-product-delivery/s-sc14-21-features.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-23 Licence reselling](s-sc14-23-licence-reselling.md)
