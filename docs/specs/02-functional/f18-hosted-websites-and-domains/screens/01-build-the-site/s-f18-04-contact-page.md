🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-01 Build the site](README.md) › 🖥️ S-F18-04 Contact page

# 🖥️ S-F18-04 Contact page

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Add a contact page that feeds leads.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-01 step 4, U12 | desktop | ![FL-F18-01 step 4, U12, light](../../images/01-build-the-site/u12-marketing/4-contact-desktop-light.png) | ![FL-F18-01 step 4, U12, dark](../../images/01-build-the-site/u12-marketing/4-contact-desktop-dark.png) |
| FL-F18-01 step 4, U12 | phone | ![FL-F18-01 step 4, U12, light](../../images/01-build-the-site/u12-marketing/4-contact-phone-light.png) | ![FL-F18-01 step 4, U12, dark](../../images/01-build-the-site/u12-marketing/4-contact-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-04-contact-page-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-04-contact-page-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-04-contact-page-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-04-contact-page-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-04-contact-page-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-04-contact-page-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-04-contact-page-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-04-contact-page-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the contact form's fields, consent and lead mapping.
- Empty: "No contact page": add one.
- Loading: the frame and titles show at once with placeholder rows for the form; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: visitors see the public form only.
- Offline: not available offline: the form is set online; visitors need the network. D38 keeps only today's schedule,
  time and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every
  action is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-02 Page](../../data/e-f18-02-page.md),
[E-F18-04 Contact message](../../data/e-f18-04-contact-message.md),
[E-F18-16 Spam hold](../../data/e-f18-16-spam-hold.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-02 Page | Published | Badge "Published"; a new record starts here; next: Live (UC-F18-08); fields editable within the role | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-02-page-published-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-02-page-published-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Live | Badge "Live"; next: Held (UC-F18-25); fields editable within the role | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-02-page-live-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-02-page-live-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Held | Badge "Held"; next: Live (UC-F18-08); fields editable within the role | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-02-page-held-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-02-page-held-{desktop,phone}-{light,dark}.png` |
| E-F18-04 Contact message | Sent | Badge "Sent"; a new record starts here; next: Held or Lost (UC-F18-24); fields editable within the role | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-04-contact-message-sent-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-04-contact-message-sent-{desktop,phone}-{light,dark}.png` |
| E-F18-04 Contact message | Held | Badge "Held"; next: Sent (UC-F18-04); fields editable within the role | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-04-contact-message-held-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-04-contact-message-held-{desktop,phone}-{light,dark}.png` |
| E-F18-04 Contact message | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-04-contact-message-lost-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-04-contact-message-lost-{desktop,phone}-{light,dark}.png` |
| E-F18-16 Spam hold | Held | Badge "Held"; a new record starts here; next: Released or Deleted (UC-F18-04, UC-F18-24); fields editable within the role | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-16-spam-hold-held-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-16-spam-hold-held-{desktop,phone}-{light,dark}.png` |
| E-F18-16 Spam hold | Released | Badge "Released"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f18-04-contact-page-e-f18-16-spam-hold-released-phone-{light,dark}.png`, `u12-marketing/s-f18-04-contact-page-e-f18-16-spam-hold-released-{desktop,phone}-{light,dark}.png` |
| E-F18-16 Spam hold | Deleted | Not shown: the record is gone in this state, so no screen shows it | U09, U12 | None: system state, the user never sees it |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-01 Build the site](../../flows/fl-f18-01-build-the-site.md)

## Open questions

None.

---

⬅️ [S-F18-03 Pages](s-f18-03-pages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-05 Careers page](../02-careers/s-f18-05-careers-page.md)
