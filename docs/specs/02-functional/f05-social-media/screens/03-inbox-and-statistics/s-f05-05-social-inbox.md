🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-03 Inbox and statistics](README.md) › 🖥️ S-F5-05 Social inbox

# 🖥️ S-F5-05 Social inbox

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Answer comments and messages.

## Entry points

Social media in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-03 step 1, U12 | desktop | ![FL-F5-03 step 1, U12, light](../../images/03-inbox-and-statistics/u12-marketing/1-social-inbox-desktop-light.png) | ![FL-F5-03 step 1, U12, dark](../../images/03-inbox-and-statistics/u12-marketing/1-social-inbox-desktop-dark.png) |
| FL-F5-03 step 1, U12 | phone | ![FL-F5-03 step 1, U12, light](../../images/03-inbox-and-statistics/u12-marketing/1-social-inbox-phone-light.png) | ![FL-F5-03 step 1, U12, dark](../../images/03-inbox-and-statistics/u12-marketing/1-social-inbox-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-05-social-inbox-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-05-social-inbox-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-05-social-inbox-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-05-social-inbox-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-05-social-inbox-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-05-social-inbox-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-05-social-inbox-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-05-social-inbox-offline-phone-dark.png) |

## Fields and columns

As its use case.

## Actions

As its use case's main flow.

## States

- Normal: Answer comments and messages, as the wireframe shows.
- Empty: No comment or message yet, with Connect an account.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F5-04 Social message](../../data/e-f05-04-social-message.md),
[E-F5-01 Post](../../data/e-f05-01-post.md), [E-F6-20 Lead](../../../f06-customers-and-sales/data/e-f06-20-lead.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-04 Social message | New | Badge "New"; a new record starts here; next: Answered (UC-F5-05); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-04-social-message-new-{desktop,phone}-{light,dark}.png` |
| E-F5-04 Social message | Answered | Badge "Answered"; next: Turned into a request (UC-F5-05); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-04-social-message-answered-{desktop,phone}-{light,dark}.png` |
| E-F5-04 Social message | Turned into a request | Badge "Turned into a request"; next: Hidden (UC-F5-05); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-04-social-message-turned-into-a-request-{desktop,phone}-{light,dark}.png` |
| E-F5-04 Social message | Hidden | Badge "Hidden"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-04-social-message-hidden-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F5-01, UC-F5-02); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-01-post-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | To approve | Badge "To approve"; next: Scheduled or Refused (UC-F5-01, UC-F5-02); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-01-post-to-approve-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-01-post-refused-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Scheduled | Badge "Scheduled"; next: Published or Refused (UC-F5-01, UC-F5-02); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-01-post-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Published | Badge "Published"; next: Held (UC-F5-03); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-01-post-published-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Held | Badge "Held"; next: Published (UC-F5-01); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f05-01-post-held-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Active | Badge "Active"; a new record starts here; next: Qualified or Disqualified (UC-F6-01); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-active-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Qualified | Badge "Qualified"; next: Disqualified or Converted (UC-F6-01, UC-F6-02); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-qualified-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Disqualified | Badge "Disqualified"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-disqualified-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Converted | Badge "Converted"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-converted-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Qualified | Badge "Qualified"; next: Disqualified or Converted (UC-F6-01, UC-F6-02); fields editable within the role | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-qualified-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Disqualified | Badge "Disqualified"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-disqualified-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Converted | Badge "Converted"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-05-social-inbox-e-f06-20-lead-converted-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the inbox and approvals also on the phone.

## Accessibility

Labelled controls; states as text.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F5-03 Inbox and statistics](../../flows/fl-f05-03-inbox-and-statistics.md)

## Open questions

None.

---

⬅️ [S-F5-04 Automatic post rules](../01-publish-a-post/s-f05-04-automatic-post-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-06 Social statistics](s-f05-06-social-statistics.md)
