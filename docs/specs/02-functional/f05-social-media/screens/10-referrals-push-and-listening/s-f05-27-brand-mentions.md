🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F5-27 Brand mentions

# 🖥️ S-F5-27 Brand mentions

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the watched terms and every
  mention.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the daily summary and the alerts.

## Purpose

Read the public mentions of the brand with their tone, and decide which to answer.

## Entry points

Social media and marketing › Listening; the alert on a phone; the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Brand mentions     Today 64   Negative 9 (x3)   Positive 31        Terms: Atelier Verdier   |
|---------------------------------------------------------------------------------------------|
| TONE      SOURCE        AUTHOR        TOPIC       REACH   MENTION                           |
| Negative  Review site   a customer    delivery    1,200   "Table arrived late and scratched"|
| Positive  Network       a blogger     range       8,400   "The new oak range is lovely"     |
| [Mark handled] [Answer] [Make a lead] [Open at source]                                      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-10 step 4, U12 | desktop | ![FL-F5-10 step 4, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/4-brand-mentions-desktop-light.png) | ![FL-F5-10 step 4, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/4-brand-mentions-desktop-dark.png) |
| FL-F5-10 step 4, U12 | phone | ![FL-F5-10 step 4, U12, light](../../images/10-referrals-push-and-listening/u12-marketing/4-brand-mentions-phone-light.png) | ![FL-F5-10 step 4, U12, dark](../../images/10-referrals-push-and-listening/u12-marketing/4-brand-mentions-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-27-brand-mentions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-27-brand-mentions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-27-brand-mentions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-27-brand-mentions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-27-brand-mentions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-27-brand-mentions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-27-brand-mentions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-27-brand-mentions-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tone | E-F5-24 tone | badge | yes, by marketing | yes |
| Source | E-F5-24 source | text | no | yes |
| Author | E-F5-24 author | public name | no | no |
| Topic | E-F5-24 topic | text | yes, by marketing | no |
| Reach | E-F5-24 reach | number | no | no |
| Mention | E-F5-24 excerpt and link | text and link | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Mark handled | row | marketing | the mention leaves the to-do list |
| Answer | row | marketing | opens the reply in the inbox ([UC-F5-05](../../use-cases/03-inbox-and-statistics/uc-f05-05-answer-comments-and-messages.md)) |
| Make a lead | row | marketing | creates a lead in sales ([UC-F5-13](../../use-cases/05-benchmark-additions/uc-f05-13-turn-social-interactions-into-leads.md)) |
| Change tone | row | marketing | corrects the rating; audited |

## States

- Normal: the counts, the mentions newest first and the actions on the selected one.
- Empty: No mention collected yet, with Set the watched terms.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a source that
  could not be read shows its name and the last good reading.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-24 Brand mention](../../data/e-f05-24-brand-mention.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-24 Brand mention | Collected | Badge "Collected"; a new record starts here; next: Rated (UC-F5-27); fields editable within the role | U12, U13 | `u12-marketing/s-f05-27-brand-mentions-e-f05-24-brand-mention-collected-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f05-27-brand-mentions-e-f05-24-brand-mention-collected-{desktop,phone}-{light,dark}.png` |
| E-F5-24 Brand mention | Rated | Badge "Rated"; next: Handled or Deleted at source (UC-F5-27); fields editable within the role | U12, U13 | `u12-marketing/s-f05-27-brand-mentions-e-f05-24-brand-mention-rated-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f05-27-brand-mentions-e-f05-24-brand-mention-rated-{desktop,phone}-{light,dark}.png` |
| E-F5-24 Brand mention | Handled | Badge "Handled"; next: Erased (BR-F5-22); fields editable within the role | U12, U13 | `u12-marketing/s-f05-27-brand-mentions-e-f05-24-brand-mention-handled-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f05-27-brand-mentions-e-f05-24-brand-mention-handled-{desktop,phone}-{light,dark}.png` |
| E-F5-24 Brand mention | Deleted at source | Badge "Deleted at source"; next: Erased (BR-F5-22); fields editable within the role | U12, U13 | `u12-marketing/s-f05-27-brand-mentions-e-f05-24-brand-mention-deleted-at-source-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f05-27-brand-mentions-e-f05-24-brand-mention-deleted-at-source-{desktop,phone}-{light,dark}.png` |
| E-F5-24 Brand mention | Erased | Badge "Erased"; final: read-only, no next state; the history shows how it got here | U12, U13 | `u12-marketing/s-f05-27-brand-mentions-e-f05-24-brand-mention-erased-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f05-27-brand-mentions-e-f05-24-brand-mention-erased-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Marketing's table is desktop only. The owner reads the alert and the day's summary on a phone: counts first, then the
three main mentions.

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

⬅️ [S-F5-26 Push campaign](s-f05-26-push-campaign.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-28 Postal campaign](s-f05-28-postal-campaign.md)
