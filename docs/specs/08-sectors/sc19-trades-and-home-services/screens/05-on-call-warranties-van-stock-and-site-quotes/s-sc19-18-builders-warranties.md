🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-05 On-call, warranties, van stock and site quotes](README.md) › 🖥️ S-SC19-18 Builders' warranties

# 🖥️ S-SC19-18 Builders' warranties

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the insurance certificates and the warranties delivered.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the warranty certificate of my works, with its end
  dates.

## Purpose

Keep the insurance certificates by trade and deliver the warranty terms and end dates of the works.

## Entry points

Trades and home services › Warranty certificates; a quote's cover check; a handover.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Warranty certificates                                     [Add certificate] [Hand over works]    |
| Insurer       Policy     Activities              Valid until   State                             |
| Insurer One   P-90412    Heating, plumbing       31 Dec 2027   Valid                             |
| Insurer One   P-90413    Electricity, solar      30 Apr 2027   Expiring                          |
| Handover N-0210: completion 1 year, equipment 2 years, structure 10 years                        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-05 step 2, U13 | desktop | ![FL-SC19-05 step 2, U13, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u13-owner/2-builders-warranties-desktop-light.png) | ![FL-SC19-05 step 2, U13, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u13-owner/2-builders-warranties-desktop-dark.png) |
| FL-SC19-05 step 2, U13 | phone | ![FL-SC19-05 step 2, U13, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u13-owner/2-builders-warranties-phone-light.png) | ![FL-SC19-05 step 2, U13, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u13-owner/2-builders-warranties-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-18-builders-warranties-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-18-builders-warranties-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-18-builders-warranties-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-18-builders-warranties-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-18-builders-warranties-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-18-builders-warranties-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-18-builders-warranties-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-18-builders-warranties-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Insurer | E-SC19-12 insurer | text | yes | yes |
| Policy | E-SC19-12 policy | text | yes | yes |
| Activities | E-SC19-12 activities | list of trades | yes | yes |
| Valid until | E-SC19-12 valid until | date | yes | yes |
| Warranty end dates | E-SC19-12 warranties | list of kind and end date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add certificate | header | owner | an insurance certificate is saved |
| Hand over works | header | owner | the warranty end dates are computed and delivered |
| Renew | row | owner | the new validity is recorded |

## States

- Normal: the certificates with insurer, policy, activities, validity and state, and the handovers.
- Empty: No certificate yet, with Add certificate.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an activity not
  covered, a certificate expired, a handover date missing, with the line named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-12 Warranty certificate](../../data/e-sc19-12-warranty-certificate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-12 Warranty certificate | Valid | Badge "Valid"; a new record starts here; next: Expiring or Expired (BR-SC19-18); fields editable within the role | U13, U09 | `u13-owner/s-sc19-18-builders-warranties-e-sc19-12-warranty-certificate-valid-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-18-builders-warranties-e-sc19-12-warranty-certificate-valid-phone-{light,dark}.png` |
| E-SC19-12 Warranty certificate | Expiring | Badge "Expiring"; next: Valid or Expired (UC-SC19-18, BR-SC19-18); fields editable within the role | U13, U09 | `u13-owner/s-sc19-18-builders-warranties-e-sc19-12-warranty-certificate-expiring-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-18-builders-warranties-e-sc19-12-warranty-certificate-expiring-phone-{light,dark}.png` |
| E-SC19-12 Warranty certificate | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc19-18-builders-warranties-e-sc19-12-warranty-certificate-expired-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc19-18-builders-warranties-e-sc19-12-warranty-certificate-expired-phone-{light,dark}.png` |

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

- [FL-SC19-05](../../flows/fl-sc19-05-on-call-warranties-van-stock-and-site-quotes.md)

## Open questions

None.

---

⬅️ [S-SC19-17 On-call](s-sc19-17-on-call.md) · ⬆️ [Up](README.md) · ➡️ [S-SC19-19 Van stock](s-sc19-19-van-stock.md)
