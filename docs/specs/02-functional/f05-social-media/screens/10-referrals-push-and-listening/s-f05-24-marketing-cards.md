🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F5-24 Marketing cards

# 🖥️ S-F5-24 Marketing cards

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the campaigns they own.

## Purpose

Build personalised cards from a brand template, preview them with and without consent, and generate them for a segment.

## Entry points

Social media and marketing › Cards; a campaign's Add a card step; the AI assistant
[BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Marketing cards: thank-you, last month's buyers                       Draft   [Generate]    |
|---------------------------------------------------------------------------------------------|
| Template  Thank-you 1080x1080 v        Segment  Buyers, September (1,242)                   |
| Merge fields  [x] first name  [x] last order  [ ] loyalty tier                              |
| Consent check  1,180 personalised   62 generic (no consent)                                 |
| PREVIEW   Julien R.   | Sonia M.   | Karim D.   | Without consent                              |
|           "Thank you Julien, your oak table is on its way."                                 |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-10 step 1, U12 | desktop | ![FL-F5-10 step 1, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/1-marketing-cards-desktop-light.png) | ![FL-F5-10 step 1, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/1-marketing-cards-desktop-dark.png) |
| FL-F5-10 step 1, U12 | phone | ![FL-F5-10 step 1, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/1-marketing-cards-phone-light.png) | ![FL-F5-10 step 1, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/1-marketing-cards-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/e1-a-contact-has-no-consent-desktop-light.png) | ![Error E1, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/e1-a-contact-has-no-consent-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/e1-a-contact-has-no-consent-phone-light.png) | ![Error E1, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/e1-a-contact-has-no-consent-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-24-marketing-cards-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-24-marketing-cards-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-24-marketing-cards-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-24-marketing-cards-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-24-marketing-cards-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-24-marketing-cards-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-24-marketing-cards-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-24-marketing-cards-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Template | E-F5-15 brand asset | name and thumbnail | yes while Draft | yes |
| Segment | E-F5-09 | name and count | yes while Draft | yes |
| Merge fields | E-F5-21 merge fields | checkboxes | yes while Draft | yes |
| Consent check | E-F5-10 consent of each contact | two counts | no | yes |
| Channel | E-F5-21 channel | email, SMS, post, export | yes while Draft | yes |
| Preview | E-F5-21 cards | four cards | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Generate | header | marketing | one card and one tracked link per contact; the campaign is Ready |
| Preview contact | preview | marketing | shows the card for a chosen contact |
| Ask the AI assistant | header | marketing | prefills template, fields and segment to check |
| Withdraw | campaign | marketing | the cards are withdrawn and the links show the generic card |

## States

- Normal: the template, the segment, the merge fields and the four previews; the consent counts above them.
- Empty: No card campaign yet, with New card campaign.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a card that
  could not be generated shows its contact and the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-21 Marketing card](../../data/e-f05-21-marketing-card.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-21 Marketing card | Draft | Badge "Draft"; a new record starts here; next: Ready (UC-F5-24); fields editable within the role | U12 | `u12-marketing/s-f05-24-marketing-cards-e-f05-21-marketing-card-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-21 Marketing card | Ready | Badge "Ready"; next: Sent or Withdrawn (UC-F5-08, UC-F5-24); fields editable within the role | U12 | `u12-marketing/s-f05-24-marketing-cards-e-f05-21-marketing-card-ready-{desktop,phone}-{light,dark}.png` |
| E-F5-21 Marketing card | Sent | Badge "Sent"; next: Withdrawn (BR-F5-19); fields editable within the role | U12 | `u12-marketing/s-f05-24-marketing-cards-e-f05-21-marketing-card-sent-{desktop,phone}-{light,dark}.png` |
| E-F5-21 Marketing card | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-24-marketing-cards-e-f05-21-marketing-card-withdrawn-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F5-23 Budget and return](../09-brand-tests-and-return-on-investment/s-f05-23-budget-and-return.md) ·
⬆️ [Up](README.md) · ➡️ [S-F5-25 Referral programme](s-f05-25-referral-programme.md)
