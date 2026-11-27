🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-06 Beverages, van sales, catch weight and medical devices](README.md) ›
🖥️ S-SC15-24 Medical devices

# 🖥️ S-SC15-24 Medical devices

**Status:** 🔄 waiting for the owner

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the receptions, the lots and the
  supplies.
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md): the checks, the quarantines, the
  complaints and the recalls.

## Purpose

Receive device lots by UDI, check and release them, ship with the UDI and run a recall from the lot to the customers.

## Entry points

Wholesale › Medical devices; a lot's page; a safety notice's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Lot L-5521  Syringe pump 50 ml   UDI 0381200055211   Expiry 2028-06-30      [Release] [Recall]   |
| Check                    Result   By       Date                                                  |
| Conformity marking       Passed   Camille  2026-11-03                                            |
| Label and language       Passed   Camille  2026-11-03                                            |
| Storage temperature      Passed   Camille  2026-11-03                                            |
| Received 120   Shipped 80   Left 40      Customers: 3         State: Available                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-06 step 4, U04 | desktop | ![FL-SC15-06 step 4, U04, light](../../images/06-beverages-vans-weights-and-devices/u04-purchasing/4-medical-devices-desktop-light.png) | ![FL-SC15-06 step 4, U04, dark](../../images/06-beverages-vans-weights-and-devices/u04-purchasing/4-medical-devices-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-24-medical-devices-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-24-medical-devices-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-24-medical-devices-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-24-medical-devices-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-24-medical-devices-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-24-medical-devices-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-24-medical-devices-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-24-medical-devices-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Lot | E-SC15-17 lot | link | no | yes |
| Device | E-SC15-17 item | link | no | yes |
| UDI | E-SC15-17 UDI | text | yes while Received | yes |
| Expiry | E-SC15-17 expiry | date | yes while Received | yes |
| Checks | E-SC15-17 checks | list of checks and results | yes while Received | yes to release |
| Quantities | E-SC15-17 received, shipped | numbers | no | no |
| Customers | E-SC15-17 customers | list of customers | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Receive | header | purchasing | a lot in state Received with its UDI |
| Release | lot | quality manager | the checks are passed and the lot is Available |
| Quarantine | lot | quality manager | the lot cannot be shipped |
| Recall | lot | quality manager | the lot is Recalled and its customers are listed |

## States

- Normal: the lots with device, UDI, expiry, checks, quantities, customers and state.
- Empty: No device lot yet, with Receive.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unreadable
  UDI, a failed check, a shipment from a quarantined lot, with the lot.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC15-17 Device lot](../../data/e-sc15-17-device-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-17 Device lot | Received | Badge "Received"; a new record starts here; next: Available or Quarantined (BR-SC15-19, UC-SC15-24); fields editable within the role | U04, U27 | `u04-purchasing/s-sc15-24-medical-devices-e-sc15-17-device-lot-received-desktop-{light,dark}.png`, `u27-quality-manager/s-sc15-24-medical-devices-e-sc15-17-device-lot-received-{desktop,tablet}-{light,dark}.png` |
| E-SC15-17 Device lot | Available | Badge "Available"; next: Distributed or Recalled (UC-SC15-24, BR-SC15-19); fields editable within the role | U04, U27 | `u04-purchasing/s-sc15-24-medical-devices-e-sc15-17-device-lot-available-desktop-{light,dark}.png`, `u27-quality-manager/s-sc15-24-medical-devices-e-sc15-17-device-lot-available-{desktop,tablet}-{light,dark}.png` |
| E-SC15-17 Device lot | Quarantined | Badge "Quarantined"; next: Available (UC-SC15-24); fields editable within the role | U04, U27 | `u04-purchasing/s-sc15-24-medical-devices-e-sc15-17-device-lot-quarantined-desktop-{light,dark}.png`, `u27-quality-manager/s-sc15-24-medical-devices-e-sc15-17-device-lot-quarantined-{desktop,tablet}-{light,dark}.png` |
| E-SC15-17 Device lot | Distributed | Badge "Distributed"; next: Recalled (BR-SC15-19); fields editable within the role | U04, U27 | `u04-purchasing/s-sc15-24-medical-devices-e-sc15-17-device-lot-distributed-desktop-{light,dark}.png`, `u27-quality-manager/s-sc15-24-medical-devices-e-sc15-17-device-lot-distributed-{desktop,tablet}-{light,dark}.png` |
| E-SC15-17 Device lot | Recalled | Badge "Recalled"; final: read-only, no next state; the history shows how it got here | U04, U27 | `u04-purchasing/s-sc15-24-medical-devices-e-sc15-17-device-lot-recalled-desktop-{light,dark}.png`, `u27-quality-manager/s-sc15-24-medical-devices-e-sc15-17-device-lot-recalled-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC15-06](../../flows/fl-sc15-06-beverages-vans-weights-and-devices.md)

## Open questions

None.

---

⬅️ [S-SC15-23 Catch weight](s-sc15-23-catch-weight.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-L01 Price agreements](../00-lists/s-sc15-l01-price-agreements.md)
