🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F5-28 Postal campaign

# 🖥️ S-F5-28 Postal campaign

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the mailings they own.

## Purpose

Prepare a postal mailing, see who is left out and why, approve the proof and the cost, and follow the posting.

## Entry points

Social media and marketing › Postal mail; a campaign's Add a letter step.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Postal campaign: welcome pack                           Draft   [Approve proof] [Send]      |
|---------------------------------------------------------------------------------------------|
| Letter  Welcome A4 v1       Segment  New customers (1,364)    Post on  2026-11-20           |
| Left out  30 objections   24 bad addresses     Letters  1,310                               |
| Cost   0.90 EUR per letter  1,180 EUR in total   Budget left  2,400 EUR                     |
| PROOF  Dear Julien, welcome to Atelier Verdier ...                                          |
| Posted 0   Returned 0                                                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-10 step 5, U12 | desktop | ![FL-F5-10 step 5, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/5-postal-campaign-desktop-light.png) | ![FL-F5-10 step 5, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/5-postal-campaign-desktop-dark.png) |
| FL-F5-10 step 5, U12 | phone | ![FL-F5-10 step 5, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/5-postal-campaign-phone-light.png) | ![FL-F5-10 step 5, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/5-postal-campaign-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-28-postal-campaign-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-28-postal-campaign-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-28-postal-campaign-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-28-postal-campaign-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-28-postal-campaign-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-28-postal-campaign-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-28-postal-campaign-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-28-postal-campaign-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Letter | E-F5-15 template | name and thumbnail | yes while Draft | yes |
| Segment | E-F5-09 | name and count | yes while Draft | yes |
| Left out | E-F5-25 contacts left out | two counts and the list | no | yes |
| Cost | E-F5-25 cost | amount with currency | no | yes |
| Post on | E-F5-25 posting date | date | yes while Draft | yes |
| Posted and returned | E-F5-25 counts | two numbers | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve proof | header | marketing | the proof is fixed; the file can be sent |
| Send | header | marketing | the file goes to the print partner |
| Show who is left out | counts | marketing | the list with the reason of each contact |
| Cancel | campaign | marketing | a mailing not yet printed is stopped |

## States

- Normal: the letter, the segment, the counts of letters and of contacts left out, the cost and the proof.
- Empty: No postal campaign yet, with New postal campaign.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused file
  shows the partner's reason; a failed address check shows the contacts concerned.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-25 Postal campaign](../../data/e-f05-25-postal-campaign.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-25 Postal campaign | Draft | Badge "Draft"; a new record starts here; next: Approved or Cancelled (UC-F5-28); fields editable within the role | U12 | `u12-marketing/s-f05-28-postal-campaign-e-f05-25-postal-campaign-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-25 Postal campaign | Approved | Badge "Approved"; next: Sent or Cancelled (UC-F5-28); fields editable within the role | U12 | `u12-marketing/s-f05-28-postal-campaign-e-f05-25-postal-campaign-approved-{desktop,phone}-{light,dark}.png` |
| E-F5-25 Postal campaign | Sent | Badge "Sent"; next: Posted (UC-F5-28); fields editable within the role | U12 | `u12-marketing/s-f05-28-postal-campaign-e-f05-25-postal-campaign-sent-{desktop,phone}-{light,dark}.png` |
| E-F5-25 Postal campaign | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-28-postal-campaign-e-f05-25-postal-campaign-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F5-25 Postal campaign | Posted | Badge "Posted"; next: Closed (UC-F5-28); fields editable within the role | U12 | `u12-marketing/s-f05-28-postal-campaign-e-f05-25-postal-campaign-posted-{desktop,phone}-{light,dark}.png` |
| E-F5-25 Postal campaign | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-28-postal-campaign-e-f05-25-postal-campaign-closed-{desktop,phone}-{light,dark}.png` |

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

- [FL-F5-10](../../flows/fl-f05-10-referrals-push-and-listening.md)

## Open questions

None.

---

⬅️ [S-F5-27 Brand mentions](s-f05-27-brand-mentions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-L01 Posts](../00-lists/s-f05-l01-posts.md)
