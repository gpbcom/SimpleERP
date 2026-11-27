🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-07 Pharmacy, eyewear, vets, dental and health centres](README.md) ›
🖥️ S-SC09-24 Dental quotes

# 🖥️ S-SC09-24 Dental quotes

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the quotes of their patients.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own quote to read and sign.

## Purpose

Prepare the regulated quote for prosthetic work on the official model, show the complementary cover's share and the
remaining cost apart, as information, and have the patient sign it before the care.

## Entry points

Health practice › Dental quotes; the patient's file; the portal for the patient.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Quote DQ-2026-031: Mrs Lopez                                     Sent   [Send]   [New version]   |
| Act               Tooth  Materials  Made in  Fees     Base     Insurance  Basket                 |
| Ceramic crown     26     ceramic    EU       120.00   120.00   70.00      no remaining cost      |
| Metal inlay core  26     metal      EU        60.00    60.00   42.00      no remaining cost      |
| Total                                        180.00   180.00  112.00                             |
| Alternatives: none needed, both acts have no remaining cost      Valid until 2027-05-14          |
| Information, not on the regulated quote: cover 68.00 EUR, remaining cost 0.00 EUR                |
| Signed on  -      Reminder in 7 days                                                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-07 step 4, U36 | desktop | ![FL-SC09-07 step 4, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/4-dental-quotes-desktop-light.png) | ![FL-SC09-07 step 4, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/4-dental-quotes-desktop-dark.png) |
| FL-SC09-07 step 4, U36 | phone | ![FL-SC09-07 step 4, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/4-dental-quotes-phone-light.png) | ![FL-SC09-07 step 4, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/4-dental-quotes-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-24-dental-quotes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-24-dental-quotes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-24-dental-quotes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-24-dental-quotes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-24-dental-quotes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-24-dental-quotes-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-24-dental-quotes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-24-dental-quotes-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Patient | E-SC09-17 patient | link | no | yes |
| Acts and teeth | E-SC09-17 acts | act, code, tooth, fees, device and materials | yes while Draft | yes |
| Place of manufacture | E-SC09-17 place of manufacture | EU or outside the EU, per device | yes while Draft | yes |
| Base and insurance | E-SC09-17 basis, insurance share | amounts | no | yes |
| Cover and remaining cost | E-SC09-17 cover share, patient remaining cost | amounts, shown apart as information, not part of the regulated quote | no | no |
| Basket | E-SC09-17 basket | no remaining cost, moderate, free, per act | no | yes |
| Alternatives | E-SC09-17 alternatives | acts with no or a moderate remaining cost | yes while Draft | for each act concerned |
| Valid until | E-SC09-17 valid until | date | yes while Draft | yes |
| Signed on | E-SC09-17 signed on | date and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add an act | quote | dentist | a line with its price and shares |
| Send | quote | dentist, secretary | the quote becomes Sent to the patient |
| Sign | quote | patient | the quote becomes Signed |
| New version | quote | dentist | a new quote replaces the unsigned one |

## States

- Normal: the regulated quote on the official model (each act with its code, fees, materials and place of manufacture,
  the base, the insurance's amount, the basket, the alternatives and the validity), then apart, as information, the
  cover's share and the remaining cost, and the signature.
- Empty: No quote yet, with New quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an act with no
  price or an unsigned quote for a prosthetic plan, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC09-17 Dental quote](../../data/e-sc09-17-dental-quote.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-17 Dental quote | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-SC09-24); fields editable within the role | U36, U09 | `u36-professional/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-draft-phone-{light,dark}.png` |
| E-SC09-17 Dental quote | Sent | Badge "Sent"; next: Signed or Refused (BR-SC09-19, UC-SC09-24); fields editable within the role | U36, U09 | `u36-professional/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-sent-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-sent-phone-{light,dark}.png` |
| E-SC09-17 Dental quote | Signed | Badge "Signed"; next: Completed (UC-SC09-24); fields editable within the role | U36, U09 | `u36-professional/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-signed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-signed-phone-{light,dark}.png` |
| E-SC09-17 Dental quote | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U36, U09 | `u36-professional/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-completed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-completed-phone-{light,dark}.png` |
| E-SC09-17 Dental quote | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U36, U09 | `u36-professional/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-refused-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc09-24-dental-quotes-e-sc09-17-dental-quote-refused-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the dentist and the secretary; the patient reads and signs on the phone.

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

⬅️ [S-SC09-23 Veterinary practice](s-sc09-23-veterinary.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-25 Health centre](s-sc09-25-health-centre.md)
