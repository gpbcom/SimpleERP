🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-06 Experts, cutover, parallel run and set-up from documents](README.md) ›
🖥️ S-F21-26 Expert booking

# 🖥️ S-F21-26 Expert booking

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the experts, their quotes and their own sessions.

## Purpose

Find an expert for a hard step of the set-up, read the quote and book a session.

## Entry points

Onboarding and module activation › Experts; the guide's Ask a person button; the checklist.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Book an expert        Topic [Import v]    Language [Francais v]       Included sessions: 1 left  |
|---------------------------------------------------------------------------------------------|
| EXPERT           KIND      RATING   FREE SLOTS             PRICE (excl. VAT)                  |
| Camille R.       Team      4.8      Thu 10:00, Fri 14:00   Included                            |
| Atelier Data     Partner   4.6      Mon 9:00, Tue 11:00    240 EUR for 90 min, quote needed    |
| QUOTE: Import of customers, 90 minutes, 240 EUR, valid until 2026-11-28      [Accept][Decline] |
| YOUR SESSIONS: Thu 10:00 Import, Booked [Move]                                               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-06 step 1, U13 | desktop | ![FL-F21-06 step 1, U13, light](../../images/06-experts-cutover-and-parallel-run/u13-owner/1-expert-booking-desktop-light.png) | ![FL-F21-06 step 1, U13, dark](../../images/06-experts-cutover-and-parallel-run/u13-owner/1-expert-booking-desktop-dark.png) |
| FL-F21-06 step 1, U13 | phone | ![FL-F21-06 step 1, U13, light](../../images/06-experts-cutover-and-parallel-run/u13-owner/1-expert-booking-phone-light.png) | ![FL-F21-06 step 1, U13, dark](../../images/06-experts-cutover-and-parallel-run/u13-owner/1-expert-booking-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-26-expert-booking-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-26-expert-booking-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-26-expert-booking-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-26-expert-booking-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-26-expert-booking-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-26-expert-booking-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-26-expert-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-26-expert-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Topic and language | E-F21-19 topic, language | list | yes while Quoted | yes |
| Expert | E-F21-19 expert | name and kind | yes while Quoted | yes |
| Quote | E-F21-19 scope, length, price | text, minutes, amount | no | for a paid session |
| Slot | E-F21-19 slot | date and time | yes after acceptance | yes |
| State | E-F21-19 state | badge | no | yes |
| Summary | E-F21-19 summary | text | by the expert | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask for a quote | expert | owner | creates the quote for the topic and length |
| Accept or decline | quote | owner | accepting lets the owner pick a slot |
| Book a slot | expert | owner | saves the session as Booked |
| Move or cancel | session | owner | free until 2 working days before |

## States

- Normal: the experts for the topic, the quote and the company's sessions.
- Empty: No session yet, with Ask for a quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a quote that
  expired or an expert not free says so and offers the next step.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F21-19 Expert session](../../data/e-f21-19-expert-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-19 Expert session | Quoted | Badge "Quoted"; a new record starts here; next: Booked or Declined (BR-F21-17); fields editable within the role | U13 | `u13-owner/s-f21-26-expert-booking-e-f21-19-expert-session-quoted-{desktop,phone}-{light,dark}.png` |
| E-F21-19 Expert session | Booked | Badge "Booked"; next: Held or Cancelled (UC-F21-26); fields editable within the role | U13 | `u13-owner/s-f21-26-expert-booking-e-f21-19-expert-session-booked-{desktop,phone}-{light,dark}.png` |
| E-F21-19 Expert session | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f21-26-expert-booking-e-f21-19-expert-session-declined-{desktop,phone}-{light,dark}.png` |
| E-F21-19 Expert session | Held | Badge "Held"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f21-26-expert-booking-e-f21-19-expert-session-held-{desktop,phone}-{light,dark}.png` |
| E-F21-19 Expert session | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f21-26-expert-booking-e-f21-19-expert-session-cancelled-{desktop,phone}-{light,dark}.png` |

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

- [FL-F21-06](../../flows/fl-f21-06-experts-cutover-and-parallel-run.md)

## Open questions

None.

---

⬅️ [S-F21-25 Phone onboarding](../04-learn-and-improve/s-f21-25-phone-onboarding.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-27 Cutover](s-f21-27-cutover.md)
