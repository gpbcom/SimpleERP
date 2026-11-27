🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-07 Pharmacy, eyewear, vets, dental and health centres](README.md) ›
🖥️ S-SC09-23 Veterinary practice

# 🖥️ S-SC09-23 Veterinary practice

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the animals, consultations and the register.
- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md): the bookings, owners and invoices.

## Purpose

Keep the animal's record, give medicines with their lot and write the register line that the law requires.

## Entry points

Health practice › Animals; the day's agenda; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Animal: Milo, dog, Labrador, born 2019-03   Chip 250268500123456       Owner Mrs Pons            |
| Vaccines   Rabies 2025-12-02 (due)    Booster 2026-03-18 (done)                                  |
| Consultation 2026-11-14   Ear infection   Treatment antibiotic 14 days                           |
| Register   Antibiotic  Lot A-771  14 tablets  Vet Dr Lucie G.                                    |
| [Add a medicine]  [Add an act]  [Invoice]  [Book a visit]                                        |
| Owner reminders on: yes    Next vaccine due 2025-12-02                                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-07 step 3, U36 | desktop | ![FL-SC09-07 step 3, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/3-veterinary-desktop-light.png) | ![FL-SC09-07 step 3, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/3-veterinary-desktop-dark.png) |
| FL-SC09-07 step 3, U36 | phone | ![FL-SC09-07 step 3, U36, light](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/3-veterinary-phone-light.png) | ![FL-SC09-07 step 3, U36, dark](../../images/07-pharmacy-vets-dental-and-centres/u36-professional/3-veterinary-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-23-veterinary-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-23-veterinary-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-23-veterinary-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-23-veterinary-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-23-veterinary-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-23-veterinary-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-23-veterinary-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-23-veterinary-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Animal name and species | E-SC09-16 name, species | text | yes while Active | yes |
| Owner | E-SC09-16 owner | customer link | yes | yes |
| Identification | E-SC09-16 identification | number | yes while Active | no |
| Birth date | E-SC09-16 birth date | date | yes while Active | no |
| Medicine, lot and quantity | E-SC09-16 register lines | list | no | yes |
| Vaccines due | E-SC09-16 next vaccine | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add an act | animal | vet | an act in the animal's record |
| Add a medicine | animal | vet | a register line with lot and quantity |
| Change the owner | animal | secretary | the animal moves, the history keeps the old owner |
| Close | animal | vet | the animal becomes Closed with its date |

## States

- Normal: the animal, its owner, vaccines, acts and the register lines.
- Empty: No animal yet, with New animal.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a medicine
  without a lot or an unidentified animal, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC09-16 Animal](../../data/e-sc09-16-animal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-16 Animal | Active | Badge "Active"; a new record starts here; next: Closed (UC-SC09-23); fields editable within the role | U36, U33 | `u36-professional/s-sc09-23-veterinary-e-sc09-16-animal-active-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-23-veterinary-e-sc09-16-animal-active-desktop-{light,dark}.png` |
| E-SC09-16 Animal | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U36, U33 | `u36-professional/s-sc09-23-veterinary-e-sc09-16-animal-closed-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-23-veterinary-e-sc09-16-animal-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the vet and the secretary; on a phone, the owner sees the vaccine dates and the invoices.

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

⬅️ [S-SC09-22 Eyewear](s-sc09-22-eyewear.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-24 Dental quotes](s-sc09-24-dental-quotes.md)
