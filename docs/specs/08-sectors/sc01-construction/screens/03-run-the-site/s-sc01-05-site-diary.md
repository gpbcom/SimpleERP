🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-03 Run the site](README.md) › 🖥️ S-SC01-05 Site diary

# 🖥️ S-SC01-05 Site diary

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)

## Purpose

Used to keep the site diary ([UC-SC01-05](../../use-cases/03-run-the-site/uc-sc01-05-keep-the-site-diary.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-03 step 2, U14 | phone | ![FL-SC01-03 step 2, U14, light](../../images/03-run-the-site/u14-field-worker/2-diary-phone-light.png) | ![FL-SC01-03 step 2, U14, dark](../../images/03-run-the-site/u14-field-worker/2-diary-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc01-05-site-diary-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc01-05-site-diary-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc01-05-site-diary-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc01-05-site-diary-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc01-05-site-diary-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc01-05-site-diary-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-05-site-diary-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-05-site-diary-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-05 Site diary entry](../../data/e-sc01-05-site-diary-entry.md), shown as the entity pages list
them, with their examples.

## Actions

- Add today's entry: [UC-SC01-05](../../use-cases/03-run-the-site/uc-sc01-05-keep-the-site-diary.md), step 1.
- Attach photos: [UC-SC01-05](../../use-cases/03-run-the-site/uc-sc01-05-keep-the-site-diary.md), step 2.
- Report an incident: [UC-SC01-05](../../use-cases/03-run-the-site/uc-sc01-05-keep-the-site-diary.md), step 3.
- Sign the day: [UC-SC01-05](../../use-cases/03-run-the-site/uc-sc01-05-keep-the-site-diary.md), step 4.

## States

- Normal: the day's entry: weather, people, deliveries, events, photos and incidents, with its signature state.
- Empty: "No entry for today", with Write today's entry.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no entry for a worked day: the site manager is reminded the next
  morning.
- Read-only: a signed day is read-only; additions are dated.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the entry and its photos are kept on the phone and sync when the network is back; the incident alert is sent then.

Shown entities (VD-15): [E-SC01-05 Site diary entry](../../data/e-sc01-05-site-diary-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-05 Site diary entry | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U14, U22 | `u14-field-worker/s-sc01-05-site-diary-e-sc01-05-site-diary-entry-recorded-phone-{light,dark}.png`, `u22-site-manager/s-sc01-05-site-diary-e-sc01-05-site-diary-entry-recorded-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC01-03 Run the site](../../flows/fl-sc01-03-run-the-site.md)

## Open questions

None.

---

⬅️ [S-SC01-04 Site time](s-sc01-04-site-time.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-06 Progress bill](../04-bill-and-subcontract/s-sc01-06-progress-bill.md)
