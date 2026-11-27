🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-09 Brand, tests and return on investment](README.md) › 🖥️ S-F5-23 Budget and return

# 🖥️ S-F5-23 Budget and return

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show each campaign's budget, spend, cost per lead and return per channel.

## Entry points

Marketing › Budget.

## Wireframe

```text
+------------------------------------------------------------------+
| Budget and return   [2026 Q4 v]                                   |
| Campaign   Budget  Spend  Leads  Cost/lead  Revenue  Return       |
| Autumn     3,000   2,400  120    20 EUR     9,600    4.0          |
| Christmas  5,000   1,100  40     27 EUR     2,300    2.1          |
| Untraced revenue: 18 % of orders                                  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-09 step 3, U13 | desktop | ![FL-F5-09 step 3, U13, light](../../images/09-brand-tests-and-return-on-investment/u13-owner/3-budget-and-return-desktop-light.png) | ![FL-F5-09 step 3, U13, dark](../../images/09-brand-tests-and-return-on-investment/u13-owner/3-budget-and-return-desktop-dark.png) |
| FL-F5-09 step 3, U13 | phone | ![FL-F5-09 step 3, U13, light](../../images/09-brand-tests-and-return-on-investment/u13-owner/3-budget-and-return-phone-light.png) | ![FL-F5-09 step 3, U13, dark](../../images/09-brand-tests-and-return-on-investment/u13-owner/3-budget-and-return-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-23-budget-and-return-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-23-budget-and-return-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-23-budget-and-return-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-23-budget-and-return-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-23-budget-and-return-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-23-budget-and-return-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-23-budget-and-return-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-23-budget-and-return-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Budget, spend, leads, revenue, ratios | E-F5-17 | budget and spend |

## Actions

| Action | Who | Result |
|---|---|---|
| Edit budget | marketing | Saved |

## States

- Normal: show each campaign's budget, spend, cost per lead and return per channel.
- Empty: no campaign with a budget: Set a budget.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for the owner, who reads.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-05 Email or SMS campaign](../../data/e-f05-05-email-or-sms-campaign.md),
[E-F5-17 Campaign budget](../../data/e-f05-17-campaign-budget.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-05 Email or SMS campaign | Draft | Badge "Draft"; a new record starts here; next: Scheduled (UC-F5-08); fields editable within the role | U13 | `u13-owner/s-f05-23-budget-and-return-e-f05-05-email-or-sms-campaign-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Scheduled | Badge "Scheduled"; next: Sent (UC-F5-08); fields editable within the role | U13 | `u13-owner/s-f05-23-budget-and-return-e-f05-05-email-or-sms-campaign-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f05-23-budget-and-return-e-f05-05-email-or-sms-campaign-sent-{desktop,phone}-{light,dark}.png` |
| E-F5-17 Campaign budget | Open | Badge "Open"; a new record starts here; next: Closed (UC-F5-23); fields editable within the role | U13 | `u13-owner/s-f05-23-budget-and-return-e-f05-17-campaign-budget-open-{desktop,phone}-{light,dark}.png` |
| E-F5-17 Campaign budget | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f05-23-budget-and-return-e-f05-17-campaign-budget-closed-{desktop,phone}-{light,dark}.png` |

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

## Shown in

- [FL-F5-09 Brand, tests and return on investment](../../flows/fl-f05-09-brand-tests-and-return-on-investment.md)

## Open questions

None.

---

⬅️ [S-F5-22 A/B test](s-f05-22-a-b-test.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-24 Marketing cards](../10-referrals-push-and-listening/s-f05-24-marketing-cards.md)
