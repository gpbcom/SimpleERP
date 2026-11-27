🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-03 Home services tax credit](README.md) › 🖥️ S-SC19-10 Household visits

# 🖥️ S-SC19-10 Household visits

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the week's visits by contract and worker.
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the day's visits on the phone, with start and
  end.

## Purpose

Plan the recurring household visits and record the hours done on each.

## Entry points

Trades and home services › Household visits; the contract's page; the worker's round.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Household visits: week 12                              [Plan the week] [Replace a worker]        |
| Day   Household   Service         Worker   Planned   Done    State                               |
| Mon   Lambert     Cleaning        Petit    3 h       3 h     Done                                |
| Tue   Girard      Lawn care       Noel     2 h       -       Planned                             |
| Wed   Lambert     Cleaning        -        3 h       -       To plan                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-03 step 2, U29 | desktop | ![FL-SC19-03 step 2, U29, light](../../images/03-home-services-tax-credit/u29-dispatcher/2-household-visits-desktop-light.png) | ![FL-SC19-03 step 2, U29, dark](../../images/03-home-services-tax-credit/u29-dispatcher/2-household-visits-desktop-dark.png) |
| FL-SC19-03 step 2, U29 | phone | ![FL-SC19-03 step 2, U29, light](../../images/03-home-services-tax-credit/u29-dispatcher/2-household-visits-phone-light.png) | ![FL-SC19-03 step 2, U29, dark](../../images/03-home-services-tax-credit/u29-dispatcher/2-household-visits-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-10-household-visits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-10-household-visits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-10-household-visits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-10-household-visits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-10-household-visits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-10-household-visits-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-10-household-visits-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-10-household-visits-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Household | E-SC19-06 household | link | no | yes |
| Service | E-SC19-06 service | text | no | yes |
| Worker | E-F9-26 worker | link | yes | no |
| Planned hours | E-SC19-06 hours | number | no | yes |
| Done hours | E-F9-17 hours | number | yes for the worker | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Plan the week | header | dispatcher | the visits of the contracts are placed |
| Replace a worker | row | dispatcher | another worker is proposed |
| End the visit | row | worker | the hours done are recorded |

## States

- Normal: the week's visits with household, service, worker, planned and done hours.
- Empty: No visit to plan this week.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a worker busy
  at the same time, no worker free, with the visit named.
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

⬅️ [S-SC19-09 Household services](s-sc19-09-household-services.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-11 Tax credit certificate](s-sc19-11-tax-credit-certificate.md)
