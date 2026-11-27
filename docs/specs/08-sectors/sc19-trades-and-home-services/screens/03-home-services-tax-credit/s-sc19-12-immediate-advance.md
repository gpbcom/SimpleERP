🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-03 Home services tax credit](README.md) › 🖥️ S-SC19-12 Immediate advance

# 🖥️ S-SC19-12 Immediate advance

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the claims by invoice, with consent, state and
  amount.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the claim to confirm or dispute on the phone.

## Purpose

Send the immediate advance claims of opted-in households and follow their confirmation.

## Entry points

Trades and home services › Immediate advance; an invoice's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Immediate advance                                         [Send claims] [Check enrolment]        |
| Invoice  Household   Amount    Credit share   Consent   State                                    |
| 884      Lambert     312.00    156.00         yes       Confirmed                                |
| 885      Girard      160.00    80.00          yes       Waiting for the household                |
| 886      Perrin      96.00     48.00          no        Not sent                                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-03 step 4, U05 | desktop | ![FL-SC19-03 step 4, U05, light](../../images/03-home-services-tax-credit/u05-accounting/4-immediate-advance-desktop-light.png) | ![FL-SC19-03 step 4, U05, dark](../../images/03-home-services-tax-credit/u05-accounting/4-immediate-advance-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-12-immediate-advance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-12-immediate-advance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-12-immediate-advance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-12-immediate-advance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-12-immediate-advance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-12-immediate-advance-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc19-12-immediate-advance-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc19-12-immediate-advance-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Invoice | E-SC04-13 invoice | link | no | yes |
| Credit share | E-SC04-13 credit share | amount | no | yes |
| Consent | E-SC04-13 consent | yes or no with its date | no | yes |
| Household's answer | E-SC04-13 answer | confirmed, disputed, none | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send claims | header | accounting | the claims with a consent are sent |
| Check enrolment | row | accounting | the household's enrolment is checked |
| Withdraw | row | accounting | a claim is withdrawn and the invoice is billed in full |

## States

- Normal: the invoices with household, amount, credit share, consent and state.
- Empty: No invoice of an opted-in household.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  consent, a rejected claim, with the invoice named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

- [FL-SC19-03 Home services tax credit](../../flows/fl-sc19-03-home-services-tax-credit.md)

## Open questions

None.

---

⬅️ [S-SC19-11 Tax credit certificate](s-sc19-11-tax-credit-certificate.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-13 Installation project](../04-installations-and-labels/s-sc19-13-installation-project.md)
