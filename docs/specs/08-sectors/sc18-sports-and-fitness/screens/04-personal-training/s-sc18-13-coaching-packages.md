🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-04 Personal training](README.md) › 🖥️ S-SC18-13 Coaching packages

# 🖥️ S-SC18-13 Coaching packages

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the packages they sold and the sessions given.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own packages.

## Purpose

Sell a package of coaching sessions, book each session and follow the sessions left.

## Entry points

Sports and fitness › Coaching packages; the member's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Coaching: Mia L. with Hugo B.                                           [Sell a package]         |
| Package          Sessions  Left  Valid to      State                                             |
| 10 sessions      10        9     2027-05-21    Active                                            |
| Trial of 3       3         0     2026-06-30    Used up                                           |
| Terms: unused sessions are lost at the end date, one extension of 1 month for illness            |
| [Book a session]  [Extend]  [Sell a package]                                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-04 step 1, U53 | phone | ![FL-SC18-04 step 1, U53, light](../../images/04-personal-training/u53-coach/1-coaching-packages-phone-light.png) | ![FL-SC18-04 step 1, U53, dark](../../images/04-personal-training/u53-coach/1-coaching-packages-phone-dark.png) |
| Error E1, U53 | phone | ![Error E1, U53, light](../../images/04-personal-training/u53-coach/e1-the-package-is-used-up-phone-light.png) | ![Error E1, U53, dark](../../images/04-personal-training/u53-coach/e1-the-package-is-used-up-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-13-coaching-packages-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-13-coaching-packages-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-13-coaching-packages-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-13-coaching-packages-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-13-coaching-packages-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-13-coaching-packages-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-13-coaching-packages-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-13-coaching-packages-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-10 member | link | no | yes |
| Coach | E-SC18-10 coach | employee | yes while Active | yes |
| Sessions | E-SC18-10 sessions bought, left | numbers | no | yes |
| Valid to | E-SC18-10 valid to | date | yes while Active | yes |
| Terms on expiry | E-SC18-10 expiry terms | text | no | yes |
| Price | E-SC18-10 price | amount | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sell a package | header | coach | a package is created Active and invoiced |
| Book a session | package row | coach, member | one session is booked |
| Extend | package row | coach, owner | the end date moves with a reason |
| Cancel | package row | owner | the package is cancelled with a refund decision |

## States

- Normal: the member's packages with the sessions left and the end dates.
- Empty: No package yet, with Sell a package.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an expired
  package or missing terms, with the offer of a new one.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-10 Coaching package](../../data/e-sc18-10-coaching-package.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-10 Coaching package | Active | Badge "Active"; a new record starts here; next: Used up, Expired or Cancelled (UC-SC18-13, BR-SC18-13); fields editable within the role | U53, U09 | `u53-coach/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-active-phone-{light,dark}.png`, `u09-customer/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-active-phone-{light,dark}.png` |
| E-SC18-10 Coaching package | Used up | Badge "Used up"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-used-up-phone-{light,dark}.png`, `u09-customer/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-used-up-phone-{light,dark}.png` |
| E-SC18-10 Coaching package | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-expired-phone-{light,dark}.png`, `u09-customer/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-expired-phone-{light,dark}.png` |
| E-SC18-10 Coaching package | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-cancelled-phone-{light,dark}.png`, `u09-customer/s-sc18-13-coaching-packages-e-sc18-10-coaching-package-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-04 Personal training](../../flows/fl-sc18-04-personal-training.md)

## Open questions

None.

---

⬅️ [S-SC18-12 Results](../03-licences-and-competitions/s-sc18-12-results.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-14 Training programme](s-sc18-14-training-programme.md)
