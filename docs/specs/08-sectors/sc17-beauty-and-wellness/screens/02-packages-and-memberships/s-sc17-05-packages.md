🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-02 Packages and memberships](README.md) › 🖥️ S-SC17-05 Packages

# 🖥️ S-SC17-05 Packages

**Status:** ✅ specified

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the packages they sell and the sessions they take.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own packages.

## Purpose

Sell a package of sessions, take one session at a visit and see the sessions left.

## Entry points

Beauty and wellness › Session packages; the till; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Packages: Camille R.                                                    [Sell a package]         |
| Package          Sessions   Left   Valid to      State                                           |
| 5 facials        5          4      2027-05-21    Active                                          |
| 3 massages       3          0      2026-08-30    Used up                                         |
| Today's visit: Facial 60 min   [Take one session from the oldest package]                        |
| Sold on 2026-11-21 for 220.00 EUR                                                                |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-02 step 1, U52 | tablet | ![FL-SC17-02 step 1, U52, light](../../images/02-packages-and-memberships/u52-beautician/1-packages-tablet-light.png) | ![FL-SC17-02 step 1, U52, dark](../../images/02-packages-and-memberships/u52-beautician/1-packages-tablet-dark.png) |
| FL-SC17-02 step 1, U52 | phone | ![FL-SC17-02 step 1, U52, light](../../images/02-packages-and-memberships/u52-beautician/1-packages-phone-light.png) | ![FL-SC17-02 step 1, U52, dark](../../images/02-packages-and-memberships/u52-beautician/1-packages-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-05-packages-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-05-packages-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-05-packages-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-05-packages-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-05-packages-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-05-packages-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-05-packages-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-05-packages-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC17-04 customer | link | no | yes |
| Service | E-SC17-04 service | link | yes while Active | yes |
| Sessions bought | E-SC17-04 sessions bought | number | no | yes |
| Sessions left | E-SC17-04 sessions left | number | no | no |
| Valid to | E-SC17-04 valid to | date | yes while Active | yes |
| Price | E-SC17-04 price | amount | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sell a package | header | beautician | a package is created Active and invoiced |
| Take one session | package row | beautician | sessions left reduce by one |
| Correct the balance | package row | manager | sessions left change with a reason |
| Cancel | package row | manager | the package is cancelled with a refund decision |

## States

- Normal: the customer's packages with the sessions left and the end dates.
- Empty: No package yet, with Sell a package.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an expired or
  used-up package, with the offer of a new one.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-04 Session package](../../data/e-sc17-04-session-package.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-04 Session package | Active | Badge "Active"; a new record starts here; next: Used up, Expired or Cancelled (BR-SC17-05, UC-SC17-05); fields editable within the role | U52, U09 | `u52-beautician/s-sc17-05-packages-e-sc17-04-session-package-active-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-05-packages-e-sc17-04-session-package-active-phone-{light,dark}.png` |
| E-SC17-04 Session package | Used up | Badge "Used up"; final: read-only, no next state; the history shows how it got here | U52, U09 | `u52-beautician/s-sc17-05-packages-e-sc17-04-session-package-used-up-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-05-packages-e-sc17-04-session-package-used-up-phone-{light,dark}.png` |
| E-SC17-04 Session package | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U52, U09 | `u52-beautician/s-sc17-05-packages-e-sc17-04-session-package-expired-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-05-packages-e-sc17-04-session-package-expired-phone-{light,dark}.png` |
| E-SC17-04 Session package | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U52, U09 | `u52-beautician/s-sc17-05-packages-e-sc17-04-session-package-cancelled-{phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-05-packages-e-sc17-04-session-package-cancelled-phone-{light,dark}.png` |

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

- [FL-SC17-02 Packages and memberships](../../flows/fl-sc17-02-packages-and-memberships.md)

## Open questions

None.

---

⬅️ [S-SC17-04 Deposits and no-shows](../01-book-staff-and-cabins/s-sc17-04-deposits-and-no-shows.md) ·
⬆️ [Up](README.md) · ➡️ [S-SC17-06 Salon memberships](s-sc17-06-salon-memberships.md)
