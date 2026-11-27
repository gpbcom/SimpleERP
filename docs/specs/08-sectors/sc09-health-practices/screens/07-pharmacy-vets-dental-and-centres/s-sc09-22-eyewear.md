🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-07 Pharmacy, eyewear, vets, dental and health centres](README.md) ›
🖥️ S-SC09-22 Eyewear

# 🖥️ S-SC09-22 Eyewear

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the corrections, quotes and lab orders.
- [U17 Cashier](../../../../01-users/personas/u17-cashier.md): the handing over and the payment.

## Purpose

Record the correction, check the prescription's validity, prepare the quote and follow the lab order to the delivery.

## Entry points

Health practice › Eyewear orders; the counter tablet; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Order EO-2026-088: Mrs Lopez                                       Quote signed   [Order lenses] |
| Prescription of 2025-09-10 by Dr Hugo B.   Valid until 2030-09-10 for this wearer                |
| Eye    Sphere   Cylinder   Axis   Addition                                                       |
| Right  -1.50    -0.50      80     +1.25                                                          |
| Left   -1.75    -0.25      95     +1.25                                                          |
| Frame F-310  Lenses progressive  Total 420.00 EUR  Insurance 18.00  Patient 54.00                |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-07 step 2, U36 | desktop | ![FL-SC09-07 step 2, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/2-eyewear-desktop-light.png) | ![FL-SC09-07 step 2, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/2-eyewear-desktop-dark.png) |
| FL-SC09-07 step 2, U36 | phone | ![FL-SC09-07 step 2, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/2-eyewear-phone-light.png) | ![FL-SC09-07 step 2, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/2-eyewear-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-22-eyewear-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-22-eyewear-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-22-eyewear-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-22-eyewear-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-22-eyewear-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-22-eyewear-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-22-eyewear-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-22-eyewear-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Wearer | E-SC09-15 wearer | link | no | yes |
| Prescription | E-SC09-15 prescription | prescriber, date | yes while Quoted | yes |
| Correction | E-SC09-15 correction | values per eye | yes while Quoted | yes |
| Frame and lenses | E-SC09-15 frame, lenses | stock items | yes while Quoted | yes |
| Quote signed on | E-SC09-15 quote signed on | date and time | no | no |
| Lab order | E-SC09-15 lab order | reference | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Check the prescription | header | optician | the validity for the wearer is shown |
| Sign the quote | header | patient | the order may be sent to the lab |
| Order lenses | header | optician | the order becomes Ordered |
| Hand over | header | optician, cashier | the order becomes Delivered and is invoiced |

## States

- Normal: the correction, the validity, the quote with its shares and the lab order.
- Empty: No order yet, with New order.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a prescription
  past its validity or an unsigned quote, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC09-15 Eyewear order](../../data/e-sc09-15-eyewear-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-15 Eyewear order | Quoted | Badge "Quoted"; a new record starts here; next: Ordered or Cancelled (BR-SC09-17, UC-SC09-22); fields editable within the role | U36, U17 | `u36-professional/s-sc09-22-eyewear-e-sc09-15-eyewear-order-quoted-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-22-eyewear-e-sc09-15-eyewear-order-quoted-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC09-15 Eyewear order | Ordered | Badge "Ordered"; next: Delivered (UC-SC09-22); fields editable within the role | U36, U17 | `u36-professional/s-sc09-22-eyewear-e-sc09-15-eyewear-order-ordered-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-22-eyewear-e-sc09-15-eyewear-order-ordered-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC09-15 Eyewear order | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U36, U17 | `u36-professional/s-sc09-22-eyewear-e-sc09-15-eyewear-order-delivered-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-22-eyewear-e-sc09-15-eyewear-order-delivered-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC09-15 Eyewear order | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U36, U17 | `u36-professional/s-sc09-22-eyewear-e-sc09-15-eyewear-order-cancelled-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-22-eyewear-e-sc09-15-eyewear-order-cancelled-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The pharmacist and the doctor work on a desktop; the cashier and the patient use the tablet or the phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC09-07](../../flows/fl-sc09-07-pharmacy-vets-dental-and-centres.md)

## Open questions

None.

---

⬅️ [S-SC09-21 Pharmacy](s-sc09-21-pharmacy.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-23 Veterinary practice](s-sc09-23-veterinary.md)
