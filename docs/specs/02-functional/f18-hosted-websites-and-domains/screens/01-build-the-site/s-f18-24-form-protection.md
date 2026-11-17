🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-01 Build the site](README.md) › 🖥️ S-F18-24 Form protection

# 🖥️ S-F18-24 Form protection

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Review messages held as spam and set each form's limits.

## Entry points

Site builder, Forms, Spam; the daily held-messages notice.

## Wireframe

```text
Form protection          Held: 14 (30 days)       Limits [Edit]
-------------------------------------------------------------------------------
Received          Form       Reason        Excerpt
2026-11-12 10:04  contact    too fast      Buy cheap ...
2026-11-12 09:40  booking    rate          Table for 2 ...   [Release] [Delete]
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-01 step 8, U12 | desktop | ![FL-F18-01 step 8, U12, light](../../images/01-build-the-site/u12-marketing/8-form-protection-desktop-light.png) | ![FL-F18-01 step 8, U12, dark](../../images/01-build-the-site/u12-marketing/8-form-protection-desktop-dark.png) |
| FL-F18-01 step 8, U12 | phone | ![FL-F18-01 step 8, U12, light](../../images/01-build-the-site/u12-marketing/8-form-protection-phone-light.png) | ![FL-F18-01 step 8, U12, dark](../../images/01-build-the-site/u12-marketing/8-form-protection-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-24-form-protection-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-24-form-protection-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-24-form-protection-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-24-form-protection-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-24-form-protection-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-24-form-protection-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-24-form-protection-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-24-form-protection-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Received | E-F18-16 received | date and time | no | yes |
| Form | E-F18-16 form | name | no | yes |
| Reason | E-F18-16 reason | list | no | yes |
| Content | E-F18-16 content | text | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Release | row | marketing | message delivered, lead created |
| Delete | row | marketing | deleted |
| Edit limits | header | marketing | limits saved |

## States

- Normal: held messages with reasons, and the limits per form.
- Empty: "No message held".
- Loading: the frame and titles show at once with placeholder rows for the held messages; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: a release whose lead exists, merged and said.
- Read-only: the owner reads.
- Offline: not available offline: held messages are on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-04 Contact message](../../data/e-f18-04-contact-message.md),
[E-F18-16 Spam hold](../../data/e-f18-16-spam-hold.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-04 Contact message | Sent | Badge "Sent"; a new record starts here; next: Held or Lost (UC-F18-24); fields editable within the role | U09, U12 | `u09-customer/s-f18-24-form-protection-e-f18-04-contact-message-sent-phone-{light,dark}.png`, `u12-marketing/s-f18-24-form-protection-e-f18-04-contact-message-sent-{desktop,phone}-{light,dark}.png` |
| E-F18-04 Contact message | Held | Badge "Held"; next: Sent (UC-F18-04); fields editable within the role | U09, U12 | `u09-customer/s-f18-24-form-protection-e-f18-04-contact-message-held-phone-{light,dark}.png`, `u12-marketing/s-f18-24-form-protection-e-f18-04-contact-message-held-{desktop,phone}-{light,dark}.png` |
| E-F18-04 Contact message | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f18-24-form-protection-e-f18-04-contact-message-lost-phone-{light,dark}.png`, `u12-marketing/s-f18-24-form-protection-e-f18-04-contact-message-lost-{desktop,phone}-{light,dark}.png` |
| E-F18-16 Spam hold | Held | Badge "Held"; a new record starts here; next: Released or Deleted (UC-F18-04, UC-F18-24); fields editable within the role | U09, U12 | `u09-customer/s-f18-24-form-protection-e-f18-16-spam-hold-held-phone-{light,dark}.png`, `u12-marketing/s-f18-24-form-protection-e-f18-16-spam-hold-held-{desktop,phone}-{light,dark}.png` |
| E-F18-16 Spam hold | Released | Badge "Released"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f18-24-form-protection-e-f18-16-spam-hold-released-phone-{light,dark}.png`, `u12-marketing/s-f18-24-form-protection-e-f18-16-spam-hold-released-{desktop,phone}-{light,dark}.png` |
| E-F18-16 Spam hold | Deleted | Not shown: the record is gone in this state, so no screen shows it | U09, U12 | None: system state, the user never sees it |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; marketing releases on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-01 Build the site](../../flows/fl-f18-01-build-the-site.md)

## Open questions

None.

---

⬅️ [S-F18-23 Mailboxes](../03-domain-and-dns/s-f18-23-mailboxes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-25 Sector templates](../06-content-and-search/s-f18-25-sector-templates.md)
