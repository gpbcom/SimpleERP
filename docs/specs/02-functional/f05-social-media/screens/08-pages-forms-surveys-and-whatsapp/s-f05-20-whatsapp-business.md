🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-08 Pages, forms, surveys and WhatsApp](README.md) › 🖥️ S-F5-20 WhatsApp Business

# 🖥️ S-F5-20 WhatsApp Business

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Write and submit WhatsApp templates, and see the conversations' window.

## Entry points

Marketing › WhatsApp; conversations in the social inbox.

## Wireframe

```text
+------------------------------------------------------------------+
| WhatsApp Business  +33 4 72 00 00 00   connected                 |
| Template         Status     Used                                  |
| order_ready      approved   340                                   |
| booking_reminder submitted  -                                     |
| Open conversations: 12 (3 closing within 2 h)    [+ Template]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-08 step 4, U12 | desktop | ![FL-F5-08 step 4, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/4-whatsapp-business-desktop-light.png) | ![FL-F5-08 step 4, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/4-whatsapp-business-desktop-dark.png) |
| FL-F5-08 step 4, U12 | phone | ![FL-F5-08 step 4, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/4-whatsapp-business-phone-light.png) | ![FL-F5-08 step 4, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/4-whatsapp-business-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-20-whatsapp-business-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-20-whatsapp-business-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-20-whatsapp-business-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-20-whatsapp-business-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-20-whatsapp-business-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-20-whatsapp-business-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-20-whatsapp-business-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-20-whatsapp-business-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Templates, status, conversations | E-F5-14, E-F5-04 | templates |

## Actions

| Action | Who | Result |
|---|---|---|
| Submit a template | marketing | Sent to WhatsApp for approval |

## States

- Normal: write and submit WhatsApp templates, and see the conversations' window.
- Empty: not connected: Connect WhatsApp Business.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: approved templates: copied to change.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-04 Social message](../../data/e-f05-04-social-message.md),
[E-F5-14 WhatsApp template](../../data/e-f05-14-whatsapp-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-04 Social message | New | Badge "New"; a new record starts here; next: Answered (UC-F5-05); fields editable within the role | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-04-social-message-new-{desktop,phone}-{light,dark}.png` |
| E-F5-04 Social message | Answered | Badge "Answered"; next: Turned into a request (UC-F5-05); fields editable within the role | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-04-social-message-answered-{desktop,phone}-{light,dark}.png` |
| E-F5-04 Social message | Turned into a request | Badge "Turned into a request"; next: Hidden (UC-F5-05); fields editable within the role | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-04-social-message-turned-into-a-request-{desktop,phone}-{light,dark}.png` |
| E-F5-04 Social message | Hidden | Badge "Hidden"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-04-social-message-hidden-{desktop,phone}-{light,dark}.png` |
| E-F5-14 WhatsApp template | Draft | Badge "Draft"; a new record starts here; next: Submitted or Refused (UC-F5-20); fields editable within the role | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-14-whatsapp-template-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-14 WhatsApp template | Submitted | Badge "Submitted"; next: Approved or Refused (UC-F5-20); fields editable within the role | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-14-whatsapp-template-submitted-{desktop,phone}-{light,dark}.png` |
| E-F5-14 WhatsApp template | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-14-whatsapp-template-refused-{desktop,phone}-{light,dark}.png` |
| E-F5-14 WhatsApp template | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-20-whatsapp-business-e-f05-14-whatsapp-template-approved-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-08 Pages, forms, surveys and WhatsApp](../../flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md)

## Open questions

None.

---

⬅️ [S-F5-19 Landing page editor](s-f05-19-landing-page-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-21 Brand kit](../09-brand-tests-and-return-on-investment/s-f05-21-brand-kit.md)
