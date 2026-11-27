🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-01 Win and price](README.md) › 🖥️ S-SC03-01 Statement of work

# 🖥️ S-SC03-01 Statement of work

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to win an engagement and write its statement of work,
[UC-SC03-01](../../use-cases/01-win-and-price/uc-sc03-01-win-an-engagement-and-write-its-statement-of-work.md).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-01 step 1, U03 | desktop | ![FL-SC03-01 step 1, U03, light](../../images/01-win-and-price/u03-sales/1-statement-of-work-desktop-light.png) | ![FL-SC03-01 step 1, U03, dark](../../images/01-win-and-price/u03-sales/1-statement-of-work-desktop-dark.png) |
| FL-SC03-01 step 1, U03 | phone | ![FL-SC03-01 step 1, U03, light](../../images/01-win-and-price/u03-sales/1-statement-of-work-phone-light.png) | ![FL-SC03-01 step 1, U03, dark](../../images/01-win-and-price/u03-sales/1-statement-of-work-phone-dark.png) |
| FL-SC03-01 step 1, U03 | tablet | ![FL-SC03-01 step 1, U03, light](../../images/01-win-and-price/u03-sales/1-statement-of-work-tablet-light.png) | ![FL-SC03-01 step 1, U03, dark](../../images/01-win-and-price/u03-sales/1-statement-of-work-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-01-statement-of-work-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-01-statement-of-work-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-01-statement-of-work-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-01-statement-of-work-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-01-statement-of-work-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-01-statement-of-work-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-01-statement-of-work-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-01-statement-of-work-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-01 Engagement](../../data/e-sc03-01-engagement.md),
[E-SC03-02 Statement of work](../../data/e-sc03-02-statement-of-work.md), shown as the entity pages list them, with
their examples.

## Actions

- Create the engagement:
  [UC-SC03-01](../../use-cases/01-win-and-price/uc-sc03-01-win-an-engagement-and-write-its-statement-of-work.md), step
  1.
- Draft the statement of work:
  [UC-SC03-01](../../use-cases/01-win-and-price/uc-sc03-01-win-an-engagement-and-write-its-statement-of-work.md), step
  2.
- Price it:
  [UC-SC03-01](../../use-cases/01-win-and-price/uc-sc03-01-win-an-engagement-and-write-its-statement-of-work.md), step
  3.
- Send for signature:
  [UC-SC03-01](../../use-cases/01-win-and-price/uc-sc03-01-win-an-engagement-and-write-its-statement-of-work.md), step
  4.
- Sign: [UC-SC03-01](../../use-cases/01-win-and-price/uc-sc03-01-win-an-engagement-and-write-its-statement-of-work.md),
  step 5.

## States

- Normal: the engagement with client, model, versions of the statement of work, deliverables, team, plan and price.
- Empty: "No engagement yet", with New engagement.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the statement of work is not signed: time cannot be recorded on
  the engagement except on an approved pre-sales budget
  ([BR-SC03-02](../../business-rules/br-sc03-02-work-only-under-a-signed-statement.md)).
- Read-only: a signed version is read-only; a change makes a new version.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-02 Statement of work](../../data/e-sc03-02-statement-of-work.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-02 Statement of work | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U09, U24 | `u03-sales/s-sc03-01-statement-of-work-e-sc03-02-statement-of-work-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc03-01-statement-of-work-e-sc03-02-statement-of-work-active-phone-{light,dark}.png`, `u24-engagement-manager/s-sc03-01-statement-of-work-e-sc03-02-statement-of-work-active-{desktop,phone}-{light,dark}.png` |

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

## Shown in

- [FL-SC03-01 Win and price](../../flows/fl-sc03-01-win-and-price.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC03-02 Rate cards](s-sc03-02-rate-cards.md)
