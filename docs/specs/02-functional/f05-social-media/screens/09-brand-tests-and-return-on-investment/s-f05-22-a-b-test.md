🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-09 Brand, tests and return on investment](README.md) › 🖥️ S-F5-22 A/B test

# 🖥️ S-F5-22 A/B test

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Set a test's variants and measure, and follow it to its winner.

## Entry points

A campaign or post › Test variants.

## Wireframe

```text
+------------------------------------------------------------------+
| Test: Autumn email   measure clicks   20 %   ends 14:00          |
| Variant  Subject                    Sent   Clicks                |
| A        Autumn sale is on          1,000  3.1 %                 |
| B        30 % off, this week only   1,000  4.4 %  leading        |
|                               [Pick winner now]                  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-09 step 2, U12 | desktop | ![FL-F5-09 step 2, U12, light](../../images/09-brand-tests-and-return-on-investment/u12-marketing/2-a-b-test-desktop-light.png) | ![FL-F5-09 step 2, U12, dark](../../images/09-brand-tests-and-return-on-investment/u12-marketing/2-a-b-test-desktop-dark.png) |
| FL-F5-09 step 2, U12 | phone | ![FL-F5-09 step 2, U12, light](../../images/09-brand-tests-and-return-on-investment/u12-marketing/2-a-b-test-phone-light.png) | ![FL-F5-09 step 2, U12, dark](../../images/09-brand-tests-and-return-on-investment/u12-marketing/2-a-b-test-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-22-a-b-test-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-22-a-b-test-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-22-a-b-test-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-22-a-b-test-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-22-a-b-test-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-22-a-b-test-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-22-a-b-test-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-22-a-b-test-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Variants, measure, share, results | E-F5-16 | before the start |

## Actions

| Action | Who | Result |
|---|---|---|
| Pick winner now | marketing | Winner sent to the rest |

## States

- Normal: set a test's variants and measure, and follow it to its winner.
- Empty: no variant: Add a variant.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a decided test.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-16 A/B test](../../data/e-f05-16-a-b-test.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-16 A/B test | Running | Badge "Running"; a new record starts here; no other state; fields editable within the role | U12 | `u12-marketing/s-f05-22-a-b-test-e-f05-16-a-b-test-running-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-09 Brand, tests and return on investment](../../flows/fl-f05-09-brand-tests-and-return-on-investment.md)

## Open questions

None.

---

⬅️ [S-F5-21 Brand kit](s-f05-21-brand-kit.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-23 Budget and return](s-f05-23-budget-and-return.md)
