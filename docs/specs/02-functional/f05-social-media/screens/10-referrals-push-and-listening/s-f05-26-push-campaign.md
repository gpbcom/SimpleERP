🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F5-26 Push campaign

# 🖥️ S-F5-26 Push campaign

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the campaigns they own.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the push on their phone and the opt-in in their
  settings.

## Purpose

Write a push, choose who receives it and when, and read the result.

## Entry points

Social media and marketing › Push; a journey step; on a phone, the app's Notifications settings.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Push campaign: autumn offer                                      Draft   [Send test] [Send] |
|---------------------------------------------------------------------------------------------|
| Title   10 percent on autumn plants          Link  shop/autumn                              |
| Text    Until Sunday, with your loyalty card.                                               |
| Segment  Loyal customers      Send  2026-11-15 09:00 (device time zone)                     |
| Reach   842 devices with opt-in   120 left out (no opt-in)                                  |
| Result  Delivered 811   Opened 203   Clicked 74                                             |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-10 step 3, U12 | desktop | ![FL-F5-10 step 3, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/3-push-campaign-desktop-light.png) | ![FL-F5-10 step 3, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/3-push-campaign-desktop-dark.png) |
| FL-F5-10 step 3, U12 | phone | ![FL-F5-10 step 3, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/3-push-campaign-phone-light.png) | ![FL-F5-10 step 3, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/3-push-campaign-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-26-push-campaign-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-26-push-campaign-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-26-push-campaign-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-26-push-campaign-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-26-push-campaign-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-26-push-campaign-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-26-push-campaign-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-26-push-campaign-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title and text | E-F5-23 message | text with a length counter | yes while Draft | yes |
| Link | E-F5-23 link | tracked link | yes while Draft | no |
| Segment | E-F5-09 | name and count | yes while Draft | yes |
| Send time | E-F5-23 send time | date and time | yes while Draft | yes |
| Reach | E-F5-10 opt-ins per device | two counts | no | yes |
| Result | E-F5-23 counts | delivered, opened, clicked | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send test | header | marketing | a push to marketing's own device |
| Send | header | marketing | the campaign is queued for its time |
| Cancel | campaign | marketing | a queued campaign is stopped before it goes out |
| Opt out | phone | customer | the device gets no more marketing pushes |

## States

- Normal: the message, the segment, the reach counts and, after sending, the result.
- Empty: No push campaign yet, with New push campaign.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused send
  shows the reason and the devices concerned.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-23 Push campaign](../../data/e-f05-23-push-campaign.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-23 Push campaign | Draft | Badge "Draft"; a new record starts here; next: Queued (UC-F5-26); fields editable within the role | U12, U09 | `u12-marketing/s-f05-26-push-campaign-e-f05-23-push-campaign-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-26-push-campaign-e-f05-23-push-campaign-draft-phone-{light,dark}.png` |
| E-F5-23 Push campaign | Queued | Badge "Queued"; next: Sent or Cancelled (UC-F5-26); fields editable within the role | U12, U09 | `u12-marketing/s-f05-26-push-campaign-e-f05-23-push-campaign-queued-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-26-push-campaign-e-f05-23-push-campaign-queued-phone-{light,dark}.png` |
| E-F5-23 Push campaign | Sent | Badge "Sent"; next: Closed (UC-F5-26); fields editable within the role | U12, U09 | `u12-marketing/s-f05-26-push-campaign-e-f05-23-push-campaign-sent-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-26-push-campaign-e-f05-23-push-campaign-sent-phone-{light,dark}.png` |
| E-F5-23 Push campaign | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f05-26-push-campaign-e-f05-23-push-campaign-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-26-push-campaign-e-f05-23-push-campaign-cancelled-phone-{light,dark}.png` |
| E-F5-23 Push campaign | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f05-26-push-campaign-e-f05-23-push-campaign-closed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f05-26-push-campaign-e-f05-23-push-campaign-closed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Marketing's screen is desktop only. The customer's opt-in switch and the push itself live on the phone, in the app's
notification settings.

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

⬅️ [S-F5-25 Referral programme](s-f05-25-referral-programme.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-27 Brand mentions](s-f05-27-brand-mentions.md)
