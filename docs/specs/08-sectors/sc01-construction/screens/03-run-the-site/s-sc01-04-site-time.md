🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-03 Run the site](README.md) › 🖥️ S-SC01-04 Site time

# 🖥️ S-SC01-04 Site time

**Status:** ✅ specified

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)

## Purpose

Used to record time and materials per site
([UC-SC01-04](../../use-cases/03-run-the-site/uc-sc01-04-record-time-and-materials-per-site.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-03 step 1, U14 | phone | ![FL-SC01-03 step 1, U14, light](../../images/03-run-the-site/u14-field-worker/1-time-and-materials-phone-light.png) | ![FL-SC01-03 step 1, U14, dark](../../images/03-run-the-site/u14-field-worker/1-time-and-materials-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc01-04-site-time-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc01-04-site-time-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc01-04-site-time-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc01-04-site-time-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc01-04-site-time-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc01-04-site-time-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-04-site-time-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-04-site-time-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-04 Site time and material entry](../../data/e-sc01-04-site-time-and-material-entry.md), shown as
the entity pages list them, with their examples.

## Actions

- Open today's site: [UC-SC01-04](../../use-cases/03-run-the-site/uc-sc01-04-record-time-and-materials-per-site.md),
  step 1.
- Enter hours and materials:
  [UC-SC01-04](../../use-cases/03-run-the-site/uc-sc01-04-record-time-and-materials-per-site.md), step 2.
- Check the day: [UC-SC01-04](../../use-cases/03-run-the-site/uc-sc01-04-record-time-and-materials-per-site.md), step 4.

## States

- Normal: today's site with its lots, the hours and materials entered and their sync state.
- Empty: "Nothing entered today", with Add hours.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a worker without a valid construction card: the entry is kept but
  flagged to the site manager ([BR-SC01-07](../../business-rules/br-sc01-07-site-workers-have-their-card.md)).
- Read-only: validated days are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  today's sites, lots and the materials list are kept on the phone; entries and photos wait in the queue and sync in
  order,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC01-04 Site time and material entry](../../data/e-sc01-04-site-time-and-material-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-04 Site time and material entry | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U14, U22 | `u14-field-worker/s-sc01-04-site-time-e-sc01-04-site-time-and-material-entry-recorded-phone-{light,dark}.png`, `u22-site-manager/s-sc01-04-site-time-e-sc01-04-site-time-and-material-entry-recorded-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-03 Run the site](../../flows/fl-sc01-03-run-the-site.md)

## Open questions

None.

---

⬅️ [S-SC01-03 Site planning](../02-prepare-the-site/s-sc01-03-site-planning.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-05 Site diary](s-sc01-05-site-diary.md)
