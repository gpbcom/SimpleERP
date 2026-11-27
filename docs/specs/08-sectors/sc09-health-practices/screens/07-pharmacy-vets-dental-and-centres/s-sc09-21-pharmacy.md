🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-07 Pharmacy, eyewear, vets, dental and health centres](README.md) ›
🖥️ S-SC09-21 Pharmacy

# 🖥️ S-SC09-21 Pharmacy

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): every prescription and dispensation of the
  pharmacy.
- [U17 Cashier](../../../../01-users/personas/u17-cashier.md): the orders prepared for the patients at the counter.

## Purpose

Check a prescription, choose the packs by lot and expiry, record the dispensation and take the patient's share.

## Entry points

Health practice › Dispensations; the counter tablet; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Prescription O-2026-0412: Dr Mireille D., Mr Aubert                    Valid   [Scan the card]   |
| Medicine              Prescribed  Dispensed  Left   Lot       Expiry                             |
| Amoxicillin 500 mg    3 packs     1          2      L-2204    2027-06                            |
| Paracetamol 1 g       2 packs     0          2      L-1187    2027-02                            |
| Patient's share 6.40 EUR   Third-party payment 14.60 EUR                                         |
| [Substitute]  [Dispense]  [Refuse and explain]                                                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-07 step 1, U36 | desktop | ![FL-SC09-07 step 1, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/1-pharmacy-desktop-light.png) | ![FL-SC09-07 step 1, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/1-pharmacy-desktop-dark.png) |
| FL-SC09-07 step 1, U36 | phone | ![FL-SC09-07 step 1, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/1-pharmacy-phone-light.png) | ![FL-SC09-07 step 1, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/1-pharmacy-phone-dark.png) |
| Error E1, U36 | desktop | ![Error E1, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/e1-there-is-no-valid-prescription-desktop-light.png) | ![Error E1, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/e1-there-is-no-valid-prescription-desktop-dark.png) |
| Error E1, U36 | phone | ![Error E1, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/e1-there-is-no-valid-prescription-phone-light.png) | ![Error E1, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/e1-there-is-no-valid-prescription-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-21-pharmacy-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-21-pharmacy-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-21-pharmacy-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-21-pharmacy-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-21-pharmacy-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-21-pharmacy-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-21-pharmacy-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-21-pharmacy-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Patient | E-SC09-14 patient | link | no | yes |
| Prescription | E-SC09-14 prescription | prescriber, date, medicines | yes while Prepared | yes |
| Medicine and quantity | E-SC09-14 medicine, quantity | stock item and number | yes while Prepared | yes |
| Lot and expiry | E-SC09-14 lot, expiry | text and month | yes while Prepared | yes |
| Substitution | E-SC09-14 substituted for | stock item | yes while Prepared | no |
| Patient's share | E-SC09-14 patient share | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Dispense | header | pharmacist | the dispensation becomes Dispensed and the stock is reduced |
| Substitute | medicine row | pharmacist | an equivalent pack, recorded as a substitution |
| Refuse | header | pharmacist | the dispensation becomes Refused with its reason |
| Cancel | header | pharmacist | a prepared dispensation is cancelled |

## States

- Normal: the prescription with its medicines, quantities left, lots, expiry and the patient's share.
- Empty: No dispensation yet, with Scan the card.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an invalid
  prescription or a recalled lot, with the reason and what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC09-14 Dispensation](../../data/e-sc09-14-dispensation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-14 Dispensation | Prepared | Badge "Prepared"; a new record starts here; next: Dispensed, Refused or Cancelled (BR-SC09-16, UC-SC09-21); fields editable within the role | U36, U17 | `u36-professional/s-sc09-21-pharmacy-e-sc09-14-dispensation-prepared-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-21-pharmacy-e-sc09-14-dispensation-prepared-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC09-14 Dispensation | Dispensed | Badge "Dispensed"; final: read-only, no next state; the history shows how it got here | U36, U17 | `u36-professional/s-sc09-21-pharmacy-e-sc09-14-dispensation-dispensed-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-21-pharmacy-e-sc09-14-dispensation-dispensed-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC09-14 Dispensation | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U36, U17 | `u36-professional/s-sc09-21-pharmacy-e-sc09-14-dispensation-refused-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-21-pharmacy-e-sc09-14-dispensation-refused-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC09-14 Dispensation | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U36, U17 | `u36-professional/s-sc09-21-pharmacy-e-sc09-14-dispensation-cancelled-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc09-21-pharmacy-e-sc09-14-dispensation-cancelled-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC09-20 Practice assistant](../01-appointments/s-sc09-20-practice-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-22 Eyewear](s-sc09-22-eyewear.md)
