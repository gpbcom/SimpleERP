🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-03 Home services tax credit](README.md) › 🖥️ S-SC19-11 Tax credit certificate

# 🖥️ S-SC19-11 Tax credit certificate

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the yearly certificates by household, with the
  amounts paid.

## Purpose

Issue the yearly tax-credit certificates with the amounts actually paid for eligible services.

## Entry points

Trades and home services › Tax credit certificates; the yearly reminder in January.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Tax credit certificates: 2027                      [Review] [Issue all] [Send]                   |
| Household   Eligible billed   Paid by household   Paid by advance   Certificate                  |
| Lambert     4,590.00          2,295.00            2,295.00          Ready                        |
| Girard      1,200.00          1,200.00            0.00              Ready                        |
| Perrin      800.00            400.00              0.00              Partly paid                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-03 step 3, U05 | desktop | ![FL-SC19-03 step 3, U05, light](../../images/03-home-services-tax-credit/u05-accounting/3-tax-credit-certificate-desktop-light.png) | ![FL-SC19-03 step 3, U05, dark](../../images/03-home-services-tax-credit/u05-accounting/3-tax-credit-certificate-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-11-tax-credit-certificate-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-11-tax-credit-certificate-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-11-tax-credit-certificate-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-11-tax-credit-certificate-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-11-tax-credit-certificate-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-11-tax-credit-certificate-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc19-11-tax-credit-certificate-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc19-11-tax-credit-certificate-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Household | E-SC04-09 client | link | no | yes |
| Eligible billed | E-SC04-09 billed | amount | no | yes |
| Paid by household | E-SC04-09 paid | amount | no | yes |
| Paid by advance | E-SC04-09 advance | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Review | header | accounting | the totals and the changed households are shown |
| Issue | row | accounting | the certificate is issued |
| Send | header | accounting | the certificates reach the households |

## States

- Normal: the households with billed, paid, advance amounts and certificate state.
- Empty: No eligible household this year.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a payment with
  no invoice, an unpaid balance, with the household named.
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

⬅️ [S-SC19-10 Household visits](s-sc19-10-household-visits.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-12 Immediate advance](s-sc19-12-immediate-advance.md)
