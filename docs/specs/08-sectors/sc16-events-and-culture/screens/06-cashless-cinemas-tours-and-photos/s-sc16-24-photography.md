🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-06 Cashless, cinemas, tours and photographers](README.md) ›
🖥️ S-SC16-24 Photography

# 🖥️ S-SC16-24 Photography

**Status:** 🔄 waiting for the owner

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md): the shoots, the galleries, the releases and
  the sales.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own gallery, the pictures to pick and the payment
  on the phone.

## Purpose

Book shoots, deliver galleries, collect the releases of the people shown and sell prints and licences only for pictures
that may be sold.

## Entry points

Events and culture › Photography; a client's page; the gallery's page on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Galleries                                                   [New shoot] [Publish] [Send release] |
| Gallery   Client           Shoot       Pictures  People  Releases   Sold   State                 |
| G-0412    Maison Aubin     2026-10-03  240       3       2 of 3     0      Draft                 |
| G-0413    Studio Lenoir    2026-10-10  120       0       -          14     Published             |
| G-0414    Marie L.         2026-10-17  80        1       1 of 1     6      Shared                |
| G-0412: 28 pictures tag a person without a release                   [Send release]              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-06 step 4, U43 | desktop | ![FL-SC16-06 step 4, U43, light](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/4-photography-desktop-light.png) | ![FL-SC16-06 step 4, U43, dark](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/4-photography-desktop-dark.png) |
| FL-SC16-06 step 4, U43 | phone | ![FL-SC16-06 step 4, U43, light](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/4-photography-phone-light.png) | ![FL-SC16-06 step 4, U43, dark](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/4-photography-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-24-photography-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-24-photography-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-24-photography-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-24-photography-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-24-photography-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-24-photography-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-24-photography-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-24-photography-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-SC16-22 client | link | yes while Draft | yes |
| Shoot date | E-SC16-22 shoot date | date | yes while Draft | yes |
| Pictures | E-SC16-22 pictures | number | no | no |
| People shown | E-SC16-22 people | list of people | yes while Draft | no |
| Releases | E-SC16-22 releases | list of signed releases | no | yes to publish |
| Use and duration | E-SC16-22 release use | text and years | yes while Draft | yes to send |
| Sold | E-SC16-22 sold | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New shoot | header | photographer | a gallery in state Draft |
| Send release | gallery | photographer | the release is sent for signature |
| Share | gallery | photographer | the client sees the pictures privately |
| Publish | gallery | photographer | the pictures with a release are Published |

## States

- Normal: the galleries with client, shoot date, pictures, people, releases, sold and state.
- Empty: No gallery yet, with New shoot.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); pictures of a
  person without a release, a release without a use, with the pictures.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC16-22 Gallery](../../data/e-sc16-22-gallery.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-22 Gallery | Draft | Badge "Draft"; a new record starts here; next: Shared or Published (UC-SC16-24, BR-SC16-19); fields editable within the role | U43, U09 | `u43-event-producer/s-sc16-24-photography-e-sc16-22-gallery-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc16-24-photography-e-sc16-22-gallery-draft-phone-{light,dark}.png` |
| E-SC16-22 Gallery | Shared | Badge "Shared"; next: Published or Archived (BR-SC16-19, UC-SC16-24); fields editable within the role | U43, U09 | `u43-event-producer/s-sc16-24-photography-e-sc16-22-gallery-shared-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc16-24-photography-e-sc16-22-gallery-shared-phone-{light,dark}.png` |
| E-SC16-22 Gallery | Published | Badge "Published"; next: Archived (UC-SC16-24); fields editable within the role | U43, U09 | `u43-event-producer/s-sc16-24-photography-e-sc16-22-gallery-published-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc16-24-photography-e-sc16-22-gallery-published-phone-{light,dark}.png` |
| E-SC16-22 Gallery | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U43, U09 | `u43-event-producer/s-sc16-24-photography-e-sc16-22-gallery-archived-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc16-24-photography-e-sc16-22-gallery-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The client's phone shows the gallery as a grid with a heart to pick and a pay button.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC16-06](../../flows/fl-sc16-06-cashless-cinemas-tours-and-photos.md)

## Open questions

None.

---

⬅️ [S-SC16-23 Tour](s-sc16-23-touring.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-L01 Shows](../00-lists/s-sc16-l01-shows.md)
