🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-05 Rentals, care records, client files and loyalty](README.md) ›
🖥️ S-SC17-18 Regulated care

# 🖥️ S-SC17-18 Regulated care

**Status:** 🔄 waiting for the owner

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the care records of the treatments they give.

## Purpose

Check the declaration and the training, take the consent and keep the batches and the aftercare of a tattoo, a piercing
or a laser treatment.

## Entry points

Beauty and wellness › Care records; the booking's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Care record CR-2026-0412: Noor A., piercing                         Prepared                     |
| Activity declared: yes (studio)   Practitioner Ines B.  Hygiene training valid to 2028-02        |
| Consent   Signed 2026-11-21 10:12 by the client   Guardian: not needed                           |
| Place on the body: ear, helix   Needle batch N-220   Jewel batch J-17                            |
| Aftercare given: yes, leaflet and advice recorded 2026-11-21                                     |
| [Start]  [Close the record]  [Add a follow-up]                                                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-05 step 2, U52 | tablet | ![FL-SC17-05 step 2, U52, light](../../images/05-rentals-care-records-and-loyalty/u52-beautician/2-regulated-care-tablet-light.png) | ![FL-SC17-05 step 2, U52, dark](../../images/05-rentals-care-records-and-loyalty/u52-beautician/2-regulated-care-tablet-dark.png) |
| FL-SC17-05 step 2, U52 | phone | ![FL-SC17-05 step 2, U52, light](../../images/05-rentals-care-records-and-loyalty/u52-beautician/2-regulated-care-phone-light.png) | ![FL-SC17-05 step 2, U52, dark](../../images/05-rentals-care-records-and-loyalty/u52-beautician/2-regulated-care-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-18-regulated-care-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-18-regulated-care-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-18-regulated-care-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-18-regulated-care-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-18-regulated-care-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-18-regulated-care-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-18-regulated-care-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-18-regulated-care-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-SC17-12 client | link | no | yes |
| Kind | E-SC17-12 kind | tattoo, piercing, laser | yes while Prepared | yes |
| Practitioner | E-SC17-12 practitioner | employee or renter | yes while Prepared | yes |
| Consent | E-SC17-12 consent signed on | date and document | yes while Prepared | yes |
| Batches | E-SC17-12 batches | product and needle batches | yes while Prepared | yes |
| Aftercare | E-SC17-12 aftercare given on | date and text | yes while Performed | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Start | header | practitioner | the record becomes Performed |
| Close | header | practitioner | the record becomes Closed |
| Refuse | header | practitioner | the treatment is refused with a reason |
| Add a follow-up | record | practitioner | a note after a reaction is added |

## States

- Normal: the record with its checks, consent, batches and aftercare.
- Empty: No care record yet, with New record.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an undeclared
  activity, an expired training or an unsigned consent, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-12 Regulated care record](../../data/e-sc17-12-care-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-12 Regulated care record | Prepared | Badge "Prepared"; a new record starts here; next: Performed or Refused (BR-SC17-18); fields editable within the role | U52 | `u52-beautician/s-sc17-18-regulated-care-e-sc17-12-care-record-prepared-{phone,tablet}-{light,dark}.png` |
| E-SC17-12 Regulated care record | Performed | Badge "Performed"; next: Closed (UC-SC17-18); fields editable within the role | U52 | `u52-beautician/s-sc17-18-regulated-care-e-sc17-12-care-record-performed-{phone,tablet}-{light,dark}.png` |
| E-SC17-12 Regulated care record | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U52 | `u52-beautician/s-sc17-18-regulated-care-e-sc17-12-care-record-refused-{phone,tablet}-{light,dark}.png` |
| E-SC17-12 Regulated care record | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U52 | `u52-beautician/s-sc17-18-regulated-care-e-sc17-12-care-record-closed-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The beautician works on the tablet at the chair, the manager on a desktop and the customer on a phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-05](../../flows/fl-sc17-05-rentals-care-records-and-loyalty.md)

## Open questions

None.

---

⬅️ [S-SC17-17 Chair rental](s-sc17-17-chair-rental.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-19 Client file](s-sc17-19-client-file.md)
