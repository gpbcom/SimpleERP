🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-06 Campsites, catering, groups, pricing and licences](README.md) › 🖥️ S-SC06-19 Dynamic pricing

# 🖥️ S-SC06-19 Dynamic pricing

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the rules, the limits and the prices they give.
- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md): the prices shown with the rule
  applied.

## Purpose

Set the rules that move the rate with demand, their floor and ceiling, and check the price each night would get.

## Entry points

Restaurant and hospitality › Price rules; the rate calendar; a channel's rate alert.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Price rules                                    Room type: Double          [New rule] [Pause]     |
| Rule                   Condition             Action     Priority  State                          |
| High occupancy         Occupancy above 80 %  +15 %      1         Active                         |
| Last minute            Arrival within 3 days -10 %      2         Active                         |
| Trade fair Lyon        13-16 Oct             +25 %      1         Draft                          |
| Limits Double: floor 90.00  ceiling 190.00      12 Jun: base 130.00 -> 149.50 (High occupancy)   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-06 step 4, U13 | desktop | ![FL-SC06-06 step 4, U13, light](../../images/06-campsites-catering-groups-and-pricing/u13-owner/4-dynamic-pricing-desktop-light.png) | ![FL-SC06-06 step 4, U13, dark](../../images/06-campsites-catering-groups-and-pricing/u13-owner/4-dynamic-pricing-desktop-dark.png) |
| FL-SC06-06 step 4, U13 | phone | ![FL-SC06-06 step 4, U13, light](../../images/06-campsites-catering-groups-and-pricing/u13-owner/4-dynamic-pricing-phone-light.png) | ![FL-SC06-06 step 4, U13, dark](../../images/06-campsites-catering-groups-and-pricing/u13-owner/4-dynamic-pricing-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-19-dynamic-pricing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-19-dynamic-pricing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-19-dynamic-pricing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-19-dynamic-pricing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-19-dynamic-pricing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-19-dynamic-pricing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-19-dynamic-pricing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-19-dynamic-pricing-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Rule name | E-SC06-16 name | text | yes while Draft | yes |
| Condition | E-SC06-16 condition | occupancy, lead time, day, event | yes while Draft | yes |
| Action | E-SC06-16 action | percentage or amount | yes while Draft | yes |
| Room types | E-SC06-16 room types | list | yes while Draft | yes |
| Floor and ceiling | E-SC06-16 floor, ceiling | amounts in EUR | yes | yes |
| Priority | E-SC06-16 priority | number | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New rule | header | owner | a rule in Draft with its preview on the next 30 days |
| Activate | rule | owner | prices are recomputed and sent to the channels |
| Pause | rule | owner, receptionist | the rule stops applying within the hour |
| Preview | rule | owner | the price each night would get |

## States

- Normal: the rules with their condition, action, limits and the preview of the next days.
- Empty: No rule yet, with New rule.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a ceiling below
  the floor or a rule with no room type, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC06-16 Price rule](../../data/e-sc06-16-price-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-16 Price rule | Draft | Badge "Draft"; a new record starts here; next: Active (BR-SC06-19); fields editable within the role | U13, U28 | `u13-owner/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-draft-{desktop,phone}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-draft-{desktop,tablet}-{light,dark}.png` |
| E-SC06-16 Price rule | Active | Badge "Active"; next: Paused or Retired (UC-SC06-19); fields editable within the role | U13, U28 | `u13-owner/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-active-{desktop,phone}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-active-{desktop,tablet}-{light,dark}.png` |
| E-SC06-16 Price rule | Paused | Badge "Paused"; next: Active (UC-SC06-19); fields editable within the role | U13, U28 | `u13-owner/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-paused-{desktop,phone}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-paused-{desktop,tablet}-{light,dark}.png` |
| E-SC06-16 Price rule | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U13, U28 | `u13-owner/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-retired-{desktop,phone}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-19-dynamic-pricing-e-sc06-16-price-rule-retired-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC06-06](../../flows/fl-sc06-06-campsites-catering-groups-and-pricing.md)

## Open questions

None.

---

⬅️ [S-SC06-18 Groups and seminars](s-sc06-18-groups-and-seminars.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-20 Alcohol licences](s-sc06-20-alcohol-licences.md)
