🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-03 Licences and competitions](README.md) ›
🖥️ S-SC18-09 Federation licences

# 🖥️ S-SC18-09 Federation licences

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the licences of every member.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own licence.

## Purpose

Request, issue and renew the federation licences of the season and follow their certificates.

## Entry points

Sports and fitness › Licences; the member's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Licences: season 2026-27                                              [Send the requests]        |
| Member       Federation   Category   Certificate   State                                         |
| Mia L.       Tennis       Adult      valid         Issued  T-998213                              |
| Hugo B.      Boxing       Adult      expired       Requested (held)                              |
| Kids         Football     U12        valid         Issued  F-440012                              |
| Fees collected 4,680.00 EUR   Passed to the federations 3,900.00 EUR                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-03 step 1, U13 | desktop | ![FL-SC18-03 step 1, U13, light](../../images/03-licences-and-competitions/u13-owner/1-federation-licences-desktop-light.png) | ![FL-SC18-03 step 1, U13, dark](../../images/03-licences-and-competitions/u13-owner/1-federation-licences-desktop-dark.png) |
| FL-SC18-03 step 1, U13 | phone | ![FL-SC18-03 step 1, U13, light](../../images/03-licences-and-competitions/u13-owner/1-federation-licences-phone-light.png) | ![FL-SC18-03 step 1, U13, dark](../../images/03-licences-and-competitions/u13-owner/1-federation-licences-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-09-federation-licences-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-09-federation-licences-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-09-federation-licences-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-09-federation-licences-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-09-federation-licences-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-09-federation-licences-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-09-federation-licences-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-09-federation-licences-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-06 member | link | no | yes |
| Federation | E-SC18-06 federation | choice | yes while Requested | yes |
| Season | E-SC18-06 season | text | yes while Requested | yes |
| Category | E-SC18-06 category | choice | yes while Requested | yes |
| Licence number | E-SC18-06 number | text | no | no |
| Fee | E-SC18-06 fee | amount | yes while Requested | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Request | member row | owner | a licence is Requested |
| Send the requests | header | owner | the requests go to the federation |
| Record the number | licence row | owner | the licence becomes Issued |
| Cancel | licence row | owner | a Requested or Issued licence is cancelled |

## States

- Normal: the licences of the season with their number, category, certificate and state.
- Empty: No licence requested yet, with Request.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  certificate or a second licence, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-06 Licence](../../data/e-sc18-06-licence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-06 Licence | Requested | Badge "Requested"; a new record starts here; next: Issued or Cancelled (BR-SC18-09, UC-SC18-09); fields editable within the role | U13, U09 | `u13-owner/s-sc18-09-federation-licences-e-sc18-06-licence-requested-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-09-federation-licences-e-sc18-06-licence-requested-phone-{light,dark}.png` |
| E-SC18-06 Licence | Issued | Badge "Issued"; next: Expired or Cancelled (UC-SC18-09); fields editable within the role | U13, U09 | `u13-owner/s-sc18-09-federation-licences-e-sc18-06-licence-issued-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-09-federation-licences-e-sc18-06-licence-issued-phone-{light,dark}.png` |
| E-SC18-06 Licence | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc18-09-federation-licences-e-sc18-06-licence-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-09-federation-licences-e-sc18-06-licence-cancelled-phone-{light,dark}.png` |
| E-SC18-06 Licence | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc18-09-federation-licences-e-sc18-06-licence-expired-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-09-federation-licences-e-sc18-06-licence-expired-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the member reads their licence on a phone.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-03 Licences and competitions](../../flows/fl-sc18-03-licences-and-competitions.md)

## Open questions

None.

---

⬅️ [S-SC18-08 Coach planning](../02-classes-and-waiting-lists/s-sc18-08-coach-planning.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-10 Medical certificates](s-sc18-10-medical-certificates.md)
