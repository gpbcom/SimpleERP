🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC13-06 Vineyards, contractors, cooperatives, baskets, forests](README.md) ›
🖥️ S-SC13-24 Basket subscriptions

# 🖥️ S-SC13-24 Basket subscriptions

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md): the contracts, the weekly plan and the pick-ups.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own contract, the week's basket and the absences
  on the phone.

## Purpose

Sell season contracts for baskets, follow the instalments and plan each week's baskets from the contracts that are
active and present.

## Entry points

Agriculture › Baskets; the season's page; the member's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Baskets: summer 2026, 24 weeks                              [New contract] [Plan week] [Pick-up] |
| Contract  Member       Size    Pick-up    Price   Paid    Absences   State                       |
| B-031     Marie L.     Medium  Market     360.00  270.00  1          Active                      |
| B-032     Karim D.     Large   Farm       540.00  540.00  0          Active                      |
| B-033     Julie R.     Small   Market     216.00  0.00    -          Pending                     |
| Week 24: 84 medium, 40 large, 22 small baskets, 2 absences                [Print list]           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-06 step 4, U40 | desktop | ![FL-SC13-06 step 4, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/4-baskets-desktop-light.png) | ![FL-SC13-06 step 4, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/4-baskets-desktop-dark.png) |
| FL-SC13-06 step 4, U40 | phone | ![FL-SC13-06 step 4, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/4-baskets-phone-light.png) | ![FL-SC13-06 step 4, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/4-baskets-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-24-baskets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-24-baskets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-24-baskets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-24-baskets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-24-baskets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-24-baskets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-24-baskets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-24-baskets-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC13-20 member | link | no | yes |
| Basket size | E-SC13-20 size | small, medium or large | yes while Pending | yes |
| Pick-up point | E-SC13-20 pick-up point | text from the settings | yes while Pending | yes |
| Season price | E-SC13-20 price | amount in EUR | no | no |
| Instalments | E-SC13-20 instalments | list of dates and amounts | yes while Pending | yes |
| Paid | E-SC13-20 paid | amount in EUR | no | no |
| Absences | E-SC13-20 absences | list of weeks | yes while Active | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New contract | header | farmer | a contract in state Pending |
| Activate | contract | farmer | the first instalment is paid and the contract is Active |
| Declare absence | contract | member | the week is skipped before the cut-off |
| Plan week | header | farmer | the baskets counted from the Active contracts present |

## States

- Normal: the contracts of the season with member, size, pick-up point, price, paid and state.
- Empty: No contract yet, with New contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); instalments
  that do not add up to the price, an absence after the cut-off, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC13-20 Basket subscription](../../data/e-sc13-20-basket-subscription.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-20 Basket subscription | Pending | Badge "Pending"; a new record starts here; next: Active or Ended (UC-SC13-24); fields editable within the role | U40, U09 | `u40-farmer/s-sc13-24-baskets-e-sc13-20-basket-subscription-pending-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc13-24-baskets-e-sc13-20-basket-subscription-pending-phone-{light,dark}.png` |
| E-SC13-20 Basket subscription | Active | Badge "Active"; next: Paused or Ended (UC-SC13-24, BR-SC13-19); fields editable within the role | U40, U09 | `u40-farmer/s-sc13-24-baskets-e-sc13-20-basket-subscription-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc13-24-baskets-e-sc13-20-basket-subscription-active-phone-{light,dark}.png` |
| E-SC13-20 Basket subscription | Paused | Badge "Paused"; next: Active (UC-SC13-24); fields editable within the role | U40, U09 | `u40-farmer/s-sc13-24-baskets-e-sc13-20-basket-subscription-paused-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc13-24-baskets-e-sc13-20-basket-subscription-paused-phone-{light,dark}.png` |
| E-SC13-20 Basket subscription | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U40, U09 | `u40-farmer/s-sc13-24-baskets-e-sc13-20-basket-subscription-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc13-24-baskets-e-sc13-20-basket-subscription-ended-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The member's phone shows their next pick-up, the week's content and the absence button.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC13-06](../../flows/fl-sc13-06-vineyards-contractors-and-cooperatives.md)

## Open questions

None.

---

⬅️ [S-SC13-23 Cooperative](s-sc13-23-cooperative.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-25 Forestry](s-sc13-25-forestry.md)
