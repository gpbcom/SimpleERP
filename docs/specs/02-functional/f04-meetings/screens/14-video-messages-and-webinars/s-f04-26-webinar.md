🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-14 Video messages, webinars and templates](README.md) ›
🖥️ S-F4-26 Webinar

# 🖥️ S-F4-26 Webinar

**Status:** ✅ specified

## Personas

- - [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): creates and hosts.
- - [U09 Customer](../../../../01-users/personas/u09-customer.md): registers and attends, on a phone.

## Purpose

Create and host a webinar, follow registrations and questions, and publish the replay.

## Entry points

Meetings › Webinars; the registration page link; the reminder email.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Webinar: autumn product launch    Thu 26 Nov 2026 15:00    State: Scheduled   [Go live]     |
| ------------------------------------------------------------------------------------------- |
| REGISTERED 84 of 100   Agreed to be contacted 51   Waiting list 0       [Registration page] |
| SPEAKERS   Sophie L., Marc D.            REPLAY  offered, ready 1 hour after the end        |
| QUESTIONS  3 waiting   'Does it work with our bank?'  [Answer live] [Reply by text]         |
| AFTER      Follow-up email draft [Edit]   Leads to create: 51                               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-14 step 2, U12 | desktop | ![FL-F4-14 step 2, U12, light](../../images/14-video-messages-and-webinars/u12-marketing/2-webinar-desktop-light.png) | ![FL-F4-14 step 2, U12, dark](../../images/14-video-messages-and-webinars/u12-marketing/2-webinar-desktop-dark.png) |
| FL-F4-14 step 2, U12 | desktop | ![FL-F4-14 step 2, U12, light](../../images/14-video-messages-and-webinars/u12-marketing/2-webinar-desktop-light.png) | ![FL-F4-14 step 2, U12, dark](../../images/14-video-messages-and-webinars/u12-marketing/2-webinar-desktop-dark.png) |
| FL-F4-14 step 2, U12 | phone | ![FL-F4-14 step 2, U12, light](../../images/14-video-messages-and-webinars/u12-marketing/2-webinar-phone-light.png) | ![FL-F4-14 step 2, U12, dark](../../images/14-video-messages-and-webinars/u12-marketing/2-webinar-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-26-webinar-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-26-webinar-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-26-webinar-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-26-webinar-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-26-webinar-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-26-webinar-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-26-webinar-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-26-webinar-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title and date | E-F4-28 title, date | text and date-time | yes | yes |
| Registered, agreed | E-F4-28 registrations | counts | no | yes |
| Speakers | E-F4-28 speakers | people | yes | yes |
| Questions | E-F4-28 questions | list | answer | no |
| Replay | E-F4-28 replay | offered, ready | yes | no |
| Follow-up | E-F4-28 follow-up email | text | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Go live | header | the host | the live session opens |
| Answer | questions | the host, the speakers | a live or text answer |
| Publish replay | after | the host | the replay link goes in the follow-up |
| Create leads | after | the host | leads for the attendees who agreed (BR-F4-34) |
| Register | page | the attendee | a registration with the two separate agreements |

## States

- Normal: the webinar's counts, speakers, questions and follow-up, with the live controls when it is on.
- Empty: No webinar yet. Create one.
- Loading: The counts load first; the questions follow live.
- Error: the error message pattern (D122); a full webinar offers the waiting list.
- Read-only: an ended webinar: its counts, replay and leads, without live controls.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-28 Webinar](../../data/e-f04-28-webinar.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-28 Webinar | Draft | Badge "Draft"; a new record starts here; next: Scheduled or Cancelled (UC-F4-29); fields editable within the role | U12, U09 | `u12-marketing/s-f04-26-webinar-e-f04-28-webinar-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f04-26-webinar-e-f04-28-webinar-draft-phone-{light,dark}.png` |
| E-F4-28 Webinar | Scheduled | Badge "Scheduled"; next: Live or Cancelled (UC-F4-29); fields editable within the role | U12, U09 | `u12-marketing/s-f04-26-webinar-e-f04-28-webinar-scheduled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f04-26-webinar-e-f04-28-webinar-scheduled-phone-{light,dark}.png` |
| E-F4-28 Webinar | Live | Badge "Live"; next: Ended (UC-F4-29); fields editable within the role | U12, U09 | `u12-marketing/s-f04-26-webinar-e-f04-28-webinar-live-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f04-26-webinar-e-f04-28-webinar-live-phone-{light,dark}.png` |
| E-F4-28 Webinar | Ended | Badge "Ended"; next: Replay published (UC-F4-29); fields editable within the role | U12, U09 | `u12-marketing/s-f04-26-webinar-e-f04-28-webinar-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f04-26-webinar-e-f04-28-webinar-ended-phone-{light,dark}.png` |
| E-F4-28 Webinar | Replay published | Badge "Replay published"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f04-26-webinar-e-f04-28-webinar-replay-published-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f04-26-webinar-e-f04-28-webinar-replay-published-phone-{light,dark}.png` |
| E-F4-28 Webinar | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f04-26-webinar-e-f04-28-webinar-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f04-26-webinar-e-f04-28-webinar-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The attendee side is made for a phone; hosting needs a desktop with a camera.

## Accessibility

Live captions are on by default; questions are a list with a text field; keyboard: next question, answer.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)

## Shown in

- [FL-F4-14 Video messages, webinars and templates](../../flows/fl-f04-14-video-messages-and-webinars.md)

## Open questions

None.

---

⬅️ [S-F4-25 Video message](s-f04-25-video-message.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-27 Note templates](s-f04-27-note-templates.md)
