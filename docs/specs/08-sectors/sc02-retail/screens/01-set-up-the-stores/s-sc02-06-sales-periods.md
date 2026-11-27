🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-01 Set up the stores](README.md) › 🖥️ S-SC02-06 Sales periods

# 🖥️ S-SC02-06 Sales periods

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to run sales periods and markdowns
([UC-SC02-06](../../use-cases/01-set-up-the-stores/uc-sc02-06-run-sales-periods-and-markdowns.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-01 step 4, U12 | desktop | ![FL-SC02-01 step 4, U12, light](../../images/01-set-up-the-stores/u12-marketing/4-sales-period-desktop-light.png) | ![FL-SC02-01 step 4, U12, dark](../../images/01-set-up-the-stores/u12-marketing/4-sales-period-desktop-dark.png) |
| FL-SC02-01 step 4, U12 | phone | ![FL-SC02-01 step 4, U12, light](../../images/01-set-up-the-stores/u12-marketing/4-sales-period-phone-light.png) | ![FL-SC02-01 step 4, U12, dark](../../images/01-set-up-the-stores/u12-marketing/4-sales-period-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/01-set-up-the-stores/u12-marketing/e1-sales-not-eligible-desktop-light.png) | ![Error E1, U12, dark](../../images/01-set-up-the-stores/u12-marketing/e1-sales-not-eligible-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/01-set-up-the-stores/u12-marketing/e1-sales-not-eligible-phone-light.png) | ![Error E1, U12, dark](../../images/01-set-up-the-stores/u12-marketing/e1-sales-not-eligible-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-06-sales-periods-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-06-sales-periods-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-06-sales-periods-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-06-sales-periods-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-06-sales-periods-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-06-sales-periods-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-06-sales-periods-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-06-sales-periods-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-08 Markdown](../../data/e-sc02-08-markdown.md), shown as the entity pages list them, with their
examples.

## Actions

- Prepare the markdown:
  [UC-SC02-06](../../use-cases/01-set-up-the-stores/uc-sc02-06-run-sales-periods-and-markdowns.md), step 1.
- Check eligibility: [UC-SC02-06](../../use-cases/01-set-up-the-stores/uc-sc02-06-run-sales-periods-and-markdowns.md),
  step 2.
- Apply on the start date:
  [UC-SC02-06](../../use-cases/01-set-up-the-stores/uc-sc02-06-run-sales-periods-and-markdowns.md), step 4.

## States

- Normal: the markdowns with kind, dates, rate, reference price, stores, channels and the items left out.
- Empty: "No markdown planned", with New markdown.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an item held under one month: it is left out of the sales
  markdown with the reason ([BR-SC02-04](../../business-rules/br-sc02-04-sales-only-in-the-legal-periods.md)).
- Read-only: a running markdown can only be ended early.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC02-08 Markdown](../../data/e-sc02-08-markdown.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-08 Markdown | Live | Badge "Live"; a new record starts here; next: Refused (UC-SC02-06); fields editable within the role | U12, U23 | `u12-marketing/s-sc02-06-sales-periods-e-sc02-08-markdown-live-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-06-sales-periods-e-sc02-08-markdown-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-08 Markdown | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U12, U23 | `u12-marketing/s-sc02-06-sales-periods-e-sc02-08-markdown-refused-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-06-sales-periods-e-sc02-08-markdown-refused-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC02-01 Set up the stores](../../flows/fl-sc02-01-set-up-the-stores.md)

## Open questions

None.

---

⬅️ [S-SC02-05 Labels](s-sc02-05-labels.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-07 Store count](../02-keep-stock-right/s-sc02-07-store-count.md)
