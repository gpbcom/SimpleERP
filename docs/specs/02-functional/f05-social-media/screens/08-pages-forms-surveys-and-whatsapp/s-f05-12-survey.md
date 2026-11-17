🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-08 Pages, forms, surveys and WhatsApp](README.md) › 🖥️ S-F5-12 Survey

# 🖥️ S-F5-12 Survey

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Run surveys and live polls.

## Entry points

Social media and marketing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-08 step 3, U12 | desktop | ![FL-F5-08 step 3, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/3-survey-desktop-light.png) | ![FL-F5-08 step 3, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/3-survey-desktop-dark.png) |
| FL-F5-08 step 3, U12 | phone | ![FL-F5-08 step 3, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/3-survey-phone-light.png) | ![FL-F5-08 step 3, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/3-survey-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-12-survey-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-12-survey-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-12-survey-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-12-survey-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-12-survey-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-12-survey-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-12-survey-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-12-survey-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run surveys and live polls, as the wireframe shows.
- Empty: No survey yet, with New survey.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-08 Survey](../../data/e-f05-08-survey.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-08 Survey | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F5-12); fields editable within the role | U12 | `u12-marketing/s-f05-12-survey-e-f05-08-survey-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-08 Survey | Sent | Badge "Sent"; next: Closed (UC-F5-12); fields editable within the role | U12 | `u12-marketing/s-f05-12-survey-e-f05-08-survey-sent-{desktop,phone}-{light,dark}.png` |
| E-F5-08 Survey | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-12-survey-e-f05-08-survey-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F5-05 Benchmark additions](../../flows/fl-f05-05-benchmark-additions.md)
- [FL-F5-08 Pages, forms, surveys and WhatsApp](../../flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md)

## Open questions

None.

---

⬅️ [S-F5-11 Event](../07-events-and-ticketing/s-f05-11-event.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-13 Social leads](../05-benchmark-additions/s-f05-13-social-leads.md)
