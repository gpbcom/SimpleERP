🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-05 Rentals, care records, client files and loyalty](README.md) ›
🖥️ S-SC17-19 Client file

# 🖥️ S-SC17-19 Client file

**Status:** 🔄 waiting for the owner

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the files of the clients they serve.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own file and their consents.

## Purpose

Keep a client's notes, formulas and photos with the consent that covers each photo, and let the client control it.

## Entry points

Beauty and wellness › Client files; the booking's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Client file: Noor A.                                                    Active                   |
| Allergies   Nickel, hair dye PPD     Skin notes  Sensitive scalp                                 |
| Formula     Colour 6.3 + 20 vol, 1:1.5, 35 min       Last visit 2026-11-21                       |
| Photos      3   Consent: file only (signed 2026-11-21)                                           |
| Care records  1 piercing (2026-11-21)                                                            |
| [Add a note]  [Take a photo]  [Change the consent]  [Export]  [Erase]                            |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-05 step 3, U52 | tablet | ![FL-SC17-05 step 3, U52, light](../../images/05-rentals-care-records-and-loyalty/u52-beautician/3-client-file-tablet-light.png) | ![FL-SC17-05 step 3, U52, dark](../../images/05-rentals-care-records-and-loyalty/u52-beautician/3-client-file-tablet-dark.png) |
| FL-SC17-05 step 3, U52 | phone | ![FL-SC17-05 step 3, U52, light](../../images/05-rentals-care-records-and-loyalty/u52-beautician/3-client-file-phone-light.png) | ![FL-SC17-05 step 3, U52, dark](../../images/05-rentals-care-records-and-loyalty/u52-beautician/3-client-file-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-19-client-file-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-19-client-file-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-19-client-file-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-19-client-file-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-19-client-file-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-19-client-file-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-19-client-file-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-19-client-file-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-SC17-13 client | link | no | yes |
| Allergies and notes | E-SC17-13 allergies, notes | text | yes while Active | no |
| Formulas | E-SC17-13 formulas | text | yes while Active | no |
| Photos | E-SC17-13 photos | images | yes while Active | no |
| Photo consent | E-SC17-13 photo consent | none, file only, communication | yes while Active | yes |
| Last visit | E-SC17-13 last visit | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a note | header | beautician | a note or a formula is added |
| Take a photo | header | beautician | a photo is saved with its consent |
| Change the consent | header | beautician, client | the consent changes and the photos follow |
| Archive | header | manager | the file becomes Archived |
| Erase | header | manager | the file becomes Erased within the law |

## States

- Normal: the file with its notes, formulas, photos and consents.
- Empty: No file yet, with Create the file.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a photo with no
  consent, or a refused access, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-13 Salon client file](../../data/e-sc17-13-client-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-13 Salon client file | Active | Badge "Active"; a new record starts here; next: Archived or Erased (UC-SC17-19, BR-SC17-19); fields editable within the role | U52, U09 | `u52-beautician/s-sc17-19-client-file-e-sc17-13-client-file-active-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-19-client-file-e-sc17-13-client-file-active-phone-{light,dark}.png` |
| E-SC17-13 Salon client file | Archived | Badge "Archived"; next: Active or Erased (UC-SC17-19, BR-SC17-19); fields editable within the role | U52, U09 | `u52-beautician/s-sc17-19-client-file-e-sc17-13-client-file-archived-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-19-client-file-e-sc17-13-client-file-archived-phone-{light,dark}.png` |
| E-SC17-13 Salon client file | Erased | Badge "Erased"; final: read-only, no next state; the history shows how it got here | U52, U09 | `u52-beautician/s-sc17-19-client-file-e-sc17-13-client-file-erased-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-19-client-file-e-sc17-13-client-file-erased-phone-{light,dark}.png` |

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

⬅️ [S-SC17-18 Regulated care](s-sc17-18-regulated-care.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-20 Salon loyalty](s-sc17-20-salon-loyalty.md)
