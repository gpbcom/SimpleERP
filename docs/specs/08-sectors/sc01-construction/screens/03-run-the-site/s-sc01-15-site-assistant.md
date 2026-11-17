🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-03 Run the site](README.md) › 🖥️ S-SC01-15 Site assistant

# 🖥️ S-SC01-15 Site assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Used to ask the AI assistant about a site
([UC-SC01-15](../../use-cases/03-run-the-site/uc-sc01-15-ask-the-assistant-about-a-site.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-03 step 3, U22 | phone | ![FL-SC01-03 step 3, U22, light](../../images/03-run-the-site/u22-site-manager/3-assistant-phone-light.png) | ![FL-SC01-03 step 3, U22, dark](../../images/03-run-the-site/u22-site-manager/3-assistant-phone-dark.png) |
| FL-SC01-03 step 3, U22 | desktop | ![FL-SC01-03 step 3, U22, light](../../images/03-run-the-site/u22-site-manager/3-assistant-desktop-light.png) | ![FL-SC01-03 step 3, U22, dark](../../images/03-run-the-site/u22-site-manager/3-assistant-desktop-dark.png) |
| FL-SC01-03 step 3, U22 | tablet | ![FL-SC01-03 step 3, U22, light](../../images/03-run-the-site/u22-site-manager/3-assistant-tablet-light.png) | ![FL-SC01-03 step 3, U22, dark](../../images/03-run-the-site/u22-site-manager/3-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-15-site-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-15-site-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-15-site-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-15-site-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-15-site-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-15-site-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-15-site-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-15-site-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md),
[E-SC01-05 Site diary entry](../../data/e-sc01-05-site-diary-entry.md), shown as the entity pages list them, with their
examples.

## Actions

- Ask about S-14: [UC-SC01-15](../../use-cases/03-run-the-site/uc-sc01-15-ask-the-assistant-about-a-site.md), step 1.
- Confirm a prepared action: [UC-SC01-15](../../use-cases/03-run-the-site/uc-sc01-15-ask-the-assistant-about-a-site.md),
  step 4.

## States

- Normal: the conversation with answers and links to the site's records, and prepared actions to confirm.
- Empty: suggested questions about the current site.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses and
  says which role can do it.
- Read-only: answers only; no prepared action for a role that cannot do it.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md),
[E-SC01-05 Site diary entry](../../data/e-sc01-05-site-diary-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-01 Construction site | Planned | Badge "Planned"; a new record starts here; next: Running (UC-SC01-01); fields editable within the role | U14, U22 | `u14-field-worker/s-sc01-15-site-assistant-e-sc01-01-construction-site-planned-phone-{light,dark}.png`, `u22-site-manager/s-sc01-15-site-assistant-e-sc01-01-construction-site-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Running | Badge "Running"; next: Accepted (UC-SC01-01); fields editable within the role | U14, U22 | `u14-field-worker/s-sc01-15-site-assistant-e-sc01-01-construction-site-running-phone-{light,dark}.png`, `u22-site-manager/s-sc01-15-site-assistant-e-sc01-01-construction-site-running-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Accepted | Badge "Accepted"; next: Closed (UC-SC01-14); fields editable within the role | U14, U22 | `u14-field-worker/s-sc01-15-site-assistant-e-sc01-01-construction-site-accepted-phone-{light,dark}.png`, `u22-site-manager/s-sc01-15-site-assistant-e-sc01-01-construction-site-accepted-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U14, U22 | `u14-field-worker/s-sc01-15-site-assistant-e-sc01-01-construction-site-closed-phone-{light,dark}.png`, `u22-site-manager/s-sc01-15-site-assistant-e-sc01-01-construction-site-closed-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-05 Site diary entry | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U14, U22 | `u14-field-worker/s-sc01-15-site-assistant-e-sc01-05-site-diary-entry-recorded-phone-{light,dark}.png`, `u22-site-manager/s-sc01-15-site-assistant-e-sc01-05-site-diary-entry-recorded-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC01-14 Site margin](../04-bill-and-subcontract/s-sc01-14-site-margin.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-16 Price revision](../06-revision-developers-bim-and-grants/s-sc01-16-price-revision.md)
