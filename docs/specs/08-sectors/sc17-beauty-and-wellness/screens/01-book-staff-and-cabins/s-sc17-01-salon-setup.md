🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-01 Book staff and cabins](README.md) › 🖥️ S-SC17-01 Salon set-up

# 🖥️ S-SC17-01 Salon set-up

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): every cabin, service, skill and working day
  of the salon.

## Purpose

Set up the services, the staff skills and the cabins, and see which services can be booked.

## Entry points

Beauty and wellness › Cabins; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Salon set-up: Rue Verte salon                                              [New cabin]           |
| Cabin          Kind             Cleaning   State          Services bookable                      |
| Rose           treatment room   15 min     Active         Facial, Massage                        |
| Chair 1        hair chair       5 min      Active         Cut, Colour                            |
| Chair 2        hair chair       5 min      Out of service Cut (moved to chair 1)                 |
| Service Facial 60 min 55.00 EUR   Skill Skin care   Staff 2   Cabin kind treatment room          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-01 step 1, U23 | desktop | ![FL-SC17-01 step 1, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/1-salon-setup-desktop-light.png) | ![FL-SC17-01 step 1, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/1-salon-setup-desktop-dark.png) |
| FL-SC17-01 step 1, U23 | phone | ![FL-SC17-01 step 1, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/1-salon-setup-phone-light.png) | ![FL-SC17-01 step 1, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/1-salon-setup-phone-dark.png) |
| FL-SC17-01 step 1, U23 | tablet | ![FL-SC17-01 step 1, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/1-salon-setup-tablet-light.png) | ![FL-SC17-01 step 1, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/1-salon-setup-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-01-salon-setup-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-01-salon-setup-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-01-salon-setup-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-01-salon-setup-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-01-salon-setup-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-01-salon-setup-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-01-salon-setup-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-01-salon-setup-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Cabin | E-SC17-01 name | text | yes while Active | yes |
| Kind | E-SC17-01 kind | hair chair, treatment room, nail table, tattoo room | yes while Active | yes |
| Cleaning time | E-SC17-01 cleaning minutes | number | yes while Active | no |
| Equipment | E-SC17-01 equipment | text | yes while Active | no |
| Service | E-F4-11 appointment type | name, duration, price | yes | yes |
| Skills needed | E-F9-12 qualification | list | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New cabin | header | store manager | a cabin is created Active |
| Set out of service | cabin row | store manager | the cabin becomes Out of service and its bookings are listed |
| Back in service | cabin row | store manager | the cabin becomes Active again |
| Retire | cabin row | store manager | the cabin leaves the calendars for good |

## States

- Normal: the cabins with their kind, state and the services each one can take.
- Empty: No cabin yet, with New cabin.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a service with
  no staff member or no cabin, with the missing skill or kind.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-01 Cabin](../../data/e-sc17-01-cabin.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-01 Cabin | Active | Badge "Active"; a new record starts here; next: Out of service or Retired (UC-SC17-01); fields editable within the role | U23 | `u23-store-manager/s-sc17-01-salon-setup-e-sc17-01-cabin-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-01 Cabin | Out of service | Badge "Out of service"; next: Active (UC-SC17-01); fields editable within the role | U23 | `u23-store-manager/s-sc17-01-salon-setup-e-sc17-01-cabin-out-of-service-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-01 Cabin | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U23 | `u23-store-manager/s-sc17-01-salon-setup-e-sc17-01-cabin-retired-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; on a tablet the cabin list and the calendars stay readable.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-01 Book staff and cabins](../../flows/fl-sc17-01-book-staff-and-cabins.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC17-02 Online booking](s-sc17-02-online-booking.md)
