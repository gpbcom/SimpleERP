🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-01 Maintenance contracts](README.md) › 🖥️ S-SC19-03 Legal check-ups

# 🖥️ S-SC19-03 Legal check-ups

**Status:** ✅ specified

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the check-up form on the phone, with the
  readings, the photos and the customer's signature.

## Purpose

Record a legal check-up with its readings and result and send the certificate to the customer.

## Entry points

Trades and home services › My visits; the confirmed visit on the round.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Check-up: Gas boiler Atlas B-77120, Martin household                          [Close]            |
| Combustion CO 18 ppm      Pressure 1.4 bar      Leak test: none                                  |
| Safety devices: OK         Flue: OK                                                              |
| Result: Compliant with remarks      Remark: Expansion vessel to recheck                          |
| [Add photo] [Customer signature] [Send certificate]                                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-01 step 3, U14 | phone | ![FL-SC19-01 step 3, U14, light](../../images/01-maintenance-contracts/u14-field-worker/3-legal-check-ups-phone-light.png) | ![FL-SC19-01 step 3, U14, dark](../../images/01-maintenance-contracts/u14-field-worker/3-legal-check-ups-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-03-legal-check-ups-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-03-legal-check-ups-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-03-legal-check-ups-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-03-legal-check-ups-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-03-legal-check-ups-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-03-legal-check-ups-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-03-legal-check-ups-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-03-legal-check-ups-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Visit | E-SC19-03 visit | link | no | yes |
| Readings | E-SC19-03 readings | list of name and value | yes while Drafted | yes |
| Result | E-SC19-03 result | compliant, compliant with remarks, not compliant | no | yes |
| Remarks | E-SC19-03 remarks | text | yes while Drafted | no |
| Customer signature | E-SC19-03 signature | signature | yes while Drafted | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add photo | form | technician | a photo is attached to the check-up |
| Close check-up | header | technician | the result is computed and the certificate drafted |
| Send certificate | header | technician | the customer receives the certificate |

## States

- Normal: the form with its readings, result, remarks and signature.
- Empty: No check-up today, with the visits to come.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  reading, a technician without the qualification, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-03 Check-up certificate](../../data/e-sc19-03-check-up-certificate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-03 Check-up certificate | Drafted | Badge "Drafted"; a new record starts here; next: Signed or Sent (BR-SC19-03); fields editable within the role | U14 | `u14-field-worker/s-sc19-03-legal-check-ups-e-sc19-03-check-up-certificate-drafted-phone-{light,dark}.png` |
| E-SC19-03 Check-up certificate | Signed | Badge "Signed"; next: Sent (BR-SC19-03); fields editable within the role | U14 | `u14-field-worker/s-sc19-03-legal-check-ups-e-sc19-03-check-up-certificate-signed-phone-{light,dark}.png` |
| E-SC19-03 Check-up certificate | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U14 | `u14-field-worker/s-sc19-03-legal-check-ups-e-sc19-03-check-up-certificate-sent-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC19-01 Maintenance contracts](../../flows/fl-sc19-01-maintenance-contracts.md)

## Open questions

None.

---

⬅️ [S-SC19-02 Recurring visits](s-sc19-02-recurring-visits.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-04 Contract renewal](s-sc19-04-contract-renewal.md)
