🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-06 Excise, refurbishment, personalisation and cutting](README.md) ›
🖥️ S-SC05-18 Personalisation

# 🖥️ S-SC05-18 Personalisation

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the proofs of their orders and the customers' answers.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the proof of their order, to approve or to change.

## Purpose

Prepare the mock-up of a personalised product, send the proof and see the customer's answer before production is
released.

## Entry points

Manufacturing › Proofs; an order line with a personalised product; the customer's portal.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Proof P-0412 v2  Order SO-2210  Mug 33 cl x 200          State: Sent   [Resend] [Cancel]         |
| Customer: Atelier Roche        Zone: front   Method: print   Colours: 2                          |
| [ Mock-up of the mug with the logo ]        Artwork: logo-roche.svg (vector)                     |
| Version  Sent        Answer                    By                                                |
| v1       2026-11-02  Changes: darker blue      Mia R.                                            |
| v2       2026-11-04  Waiting                   -        Reminder in 1 day                        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-06 step 3, U03 | desktop | ![FL-SC05-06 step 3, U03, light](../../images/06-excise-refurbishment-and-cutting/u03-sales/3-personalisation-desktop-light.png) | ![FL-SC05-06 step 3, U03, dark](../../images/06-excise-refurbishment-and-cutting/u03-sales/3-personalisation-desktop-dark.png) |
| FL-SC05-06 step 3, U03 | phone | ![FL-SC05-06 step 3, U03, light](../../images/06-excise-refurbishment-and-cutting/u03-sales/3-personalisation-phone-light.png) | ![FL-SC05-06 step 3, U03, dark](../../images/06-excise-refurbishment-and-cutting/u03-sales/3-personalisation-phone-dark.png) |
| FL-SC05-06 step 3, U03 | tablet | ![FL-SC05-06 step 3, U03, light](../../images/06-excise-refurbishment-and-cutting/u03-sales/3-personalisation-tablet-light.png) | ![FL-SC05-06 step 3, U03, dark](../../images/06-excise-refurbishment-and-cutting/u03-sales/3-personalisation-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-18-personalisation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-18-personalisation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-18-personalisation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-18-personalisation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-18-personalisation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-18-personalisation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-18-personalisation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-18-personalisation-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Order line | E-SC05-17 order line | link | no | yes |
| Artwork | E-SC05-17 artwork | file | yes while Draft | yes |
| Zone and method | E-SC05-17 zone, method | choice lists | yes while Draft | yes |
| Colours | E-SC05-17 colours | number | yes while Draft | yes |
| Version | E-SC05-17 version | number | no | no |
| Customer answer | E-SC05-17 answer | approved, changes asked | customer | no |
| Approved on | E-SC05-17 approved on | date and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send proof | header | sales | the customer receives it and the proof becomes Sent |
| Approve | customer's page | customer | the proof becomes Approved with the signature |
| Ask for changes | customer's page | customer | a remark and a new version to prepare |
| Release production | header | production planner | only offered when the proof is Approved |

## States

- Normal: the mock-up, the versions with their answers and the state.
- Empty: No proof yet, with New proof on an order line.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an artwork that
  is too small or in a format the workshop does not accept, with the way to correct it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC05-17 Proof](../../data/e-sc05-17-proof.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-17 Proof | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-SC05-18); fields editable within the role | U03, U09 | `u03-sales/s-sc05-18-personalisation-e-sc05-17-proof-draft-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc05-18-personalisation-e-sc05-17-proof-draft-phone-{light,dark}.png` |
| E-SC05-17 Proof | Sent | Badge "Sent"; next: Approved, Superseded or Expired (BR-SC05-18, UC-SC05-18); fields editable within the role | U03, U09 | `u03-sales/s-sc05-18-personalisation-e-sc05-17-proof-sent-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc05-18-personalisation-e-sc05-17-proof-sent-phone-{light,dark}.png` |
| E-SC05-17 Proof | Approved | Badge "Approved"; next: Used (UC-SC05-18); fields editable within the role | U03, U09 | `u03-sales/s-sc05-18-personalisation-e-sc05-17-proof-approved-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc05-18-personalisation-e-sc05-17-proof-approved-phone-{light,dark}.png` |
| E-SC05-17 Proof | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-sc05-18-personalisation-e-sc05-17-proof-superseded-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc05-18-personalisation-e-sc05-17-proof-superseded-phone-{light,dark}.png` |
| E-SC05-17 Proof | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-sc05-18-personalisation-e-sc05-17-proof-expired-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc05-18-personalisation-e-sc05-17-proof-expired-phone-{light,dark}.png` |
| E-SC05-17 Proof | Used | Badge "Used"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-sc05-18-personalisation-e-sc05-17-proof-used-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc05-18-personalisation-e-sc05-17-proof-used-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for sales. The customer's page works on a phone: the mock-up fits the screen and the two buttons Approve and Ask
for changes stay at the bottom.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC05-06](../../flows/fl-sc05-06-excise-refurbishment-and-cutting.md)

## Open questions

None.

---

⬅️ [S-SC05-17 Refurbishment](s-sc05-17-refurbishment.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-19 Cutting](s-sc05-19-cutting.md)
