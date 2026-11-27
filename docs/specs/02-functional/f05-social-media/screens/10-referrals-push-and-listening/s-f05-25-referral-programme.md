🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F5-25 Referral programme

# 🖥️ S-F5-25 Referral programme

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the programme and every referral.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own link, referrals and rewards.

## Purpose

Set up the referral programme, share a link, and follow referrals from the order to the paid reward.

## Entry points

Social media and marketing › Referral; on a phone, the customer portal › Refer a friend.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Referral programme: bring a friend           Reward 20 EUR credit / friend 10 percent      |
|---------------------------------------------------------------------------------------------|
| Pending (4)   Earned (31)   Rejected (2)   Reversed (1)       Rewards granted: 620 EUR      |
| REFERRER      FRIEND       ORDER       STATE     PAID ON      REWARD                         |
| Sonia M.      Karim D.     SO-2041     Earned    2026-11-02   20 EUR                         |
| Julien R.     Marc T.      SO-2057     Pending   -            -                              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-10 step 2, U12 | desktop | ![FL-F5-10 step 2, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/2-referral-programme-desktop-light.png) | ![FL-F5-10 step 2, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/2-referral-programme-desktop-dark.png) |
| FL-F5-10 step 2, U12 | phone | ![FL-F5-10 step 2, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/2-referral-programme-phone-light.png) | ![FL-F5-10 step 2, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/2-referral-programme-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-25-referral-programme-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-25-referral-programme-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-25-referral-programme-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-25-referral-programme-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-25-referral-programme-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-25-referral-programme-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-25-referral-programme-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-25-referral-programme-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Referrer | E-F5-22 referrer | name | no | yes |
| Friend | E-F5-22 referred customer | name | no | yes |
| Order | E-F6-04 | number link | no | yes |
| State | E-F5-22 state | badge | no | yes |
| Paid on | E-F6-06 payment date | date | no | no |
| Reward | E-F5-22 reward | amount or text | marketing, while Pending | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Set up the programme | header | marketing | reward, minimum order and dates saved |
| Share my link | phone | customer | the personal link or code opens the share sheet |
| Accept a held referral | row | marketing | the referral goes on as Pending |
| Reject | row | marketing | the referral is Rejected with the reason |

## States

- Normal: the programme's terms, the counts by state and the referrals, newest first.
- Empty: No referral yet, with Share the programme.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a referral held
  for checking shows the reason; a reward that could not be credited shows why.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-22 Referral](../../data/e-f05-22-referral.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-22 Referral | Pending | Badge "Pending"; a new record starts here; next: Earned or Rejected (BR-F5-20, UC-F5-25); fields editable within the role | U12, U09 | `u12-marketing/s-f05-25-referral-programme-e-f05-22-referral-pending-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-25-referral-programme-e-f05-22-referral-pending-phone-{light,dark}.png` |
| E-F5-22 Referral | Earned | Badge "Earned"; next: Reversed (BR-F5-20); fields editable within the role | U12, U09 | `u12-marketing/s-f05-25-referral-programme-e-f05-22-referral-earned-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-25-referral-programme-e-f05-22-referral-earned-phone-{light,dark}.png` |
| E-F5-22 Referral | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f05-25-referral-programme-e-f05-22-referral-rejected-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-25-referral-programme-e-f05-22-referral-rejected-phone-{light,dark}.png` |
| E-F5-22 Referral | Reversed | Badge "Reversed"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f05-25-referral-programme-e-f05-22-referral-reversed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-25-referral-programme-e-f05-22-referral-reversed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The customer's part is built for a phone first: one button to share the link, then the list of their referrals.
Marketing's table is desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-10](../../flows/fl-f05-10-referrals-push-and-listening.md)

## Open questions

None.

---

⬅️ [S-F5-24 Marketing cards](s-f05-24-marketing-cards.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-26 Push campaign](s-f05-26-push-campaign.md)
