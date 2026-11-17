🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-01 Win the work](README.md) › 🖥️ S-SC01-01 Site

# 🖥️ S-SC01-01 Site

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to open a site ([UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-01 step 3, U22 | desktop | ![FL-SC01-01 step 3, U22, light](../../images/01-win-the-work/u22-site-manager/3-open-site-desktop-light.png) | ![FL-SC01-01 step 3, U22, dark](../../images/01-win-the-work/u22-site-manager/3-open-site-desktop-dark.png) |
| FL-SC01-01 step 3, U22 | phone | ![FL-SC01-01 step 3, U22, light](../../images/01-win-the-work/u22-site-manager/3-open-site-phone-light.png) | ![FL-SC01-01 step 3, U22, dark](../../images/01-win-the-work/u22-site-manager/3-open-site-phone-dark.png) |
| FL-SC01-01 step 3, U22 | tablet | ![FL-SC01-01 step 3, U22, light](../../images/01-win-the-work/u22-site-manager/3-open-site-tablet-light.png) | ![FL-SC01-01 step 3, U22, dark](../../images/01-win-the-work/u22-site-manager/3-open-site-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-01-site-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-01-site-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-01-site-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-01-site-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-01-site-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-01-site-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-01-site-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-01-site-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md),
[E-SC01-02 Quote lot](../../data/e-sc01-02-quote-lot.md), shown as the entity pages list them, with their examples.

## Actions

- Open the site from the quote: [UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md), step 2.
- Set the team and the phases: [UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md), step 3.
- Attach the documents: [UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md), step 4.
- Start the site: [UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md), step 5.

## States

- Normal: the site's header (reference, name, customer, address, state), its lots with budget and actual, the team, the
  phases and the documents.
- Empty: "No site yet", with Open a site from a signed quote.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the address is not found by the map lookup: the site manager
  types it by hand or places a pin; the site is not opened without an address.
- Read-only: field workers see their sites without the amounts; a closed site is read-only for all.
- Offline: the site's header, address and documents already opened stay readable on the phone; changes wait for the
  network.

Shown entities (VD-15): [E-SC01-02 Quote lot](../../data/e-sc01-02-quote-lot.md),
[E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-02 Quote lot | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U22 | `u03-sales/s-sc01-01-site-e-sc01-02-quote-lot-active-{desktop,phone,tablet}-{light,dark}.png`, `u22-site-manager/s-sc01-01-site-e-sc01-02-quote-lot-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Planned | Badge "Planned"; a new record starts here; next: Running (UC-SC01-01); fields editable within the role | U03, U22 | `u03-sales/s-sc01-01-site-e-sc01-01-construction-site-planned-{desktop,phone,tablet}-{light,dark}.png`, `u22-site-manager/s-sc01-01-site-e-sc01-01-construction-site-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Running | Badge "Running"; next: Accepted (UC-SC01-01); fields editable within the role | U03, U22 | `u03-sales/s-sc01-01-site-e-sc01-01-construction-site-running-{desktop,phone,tablet}-{light,dark}.png`, `u22-site-manager/s-sc01-01-site-e-sc01-01-construction-site-running-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Accepted | Badge "Accepted"; next: Closed (UC-SC01-14); fields editable within the role | U22 | `u22-site-manager/s-sc01-01-site-e-sc01-01-construction-site-accepted-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U22 | `u22-site-manager/s-sc01-01-site-e-sc01-01-construction-site-closed-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-01 Win the work](../../flows/fl-sc01-01-win-the-work.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC01-02 Quote by lots](s-sc01-02-quote-by-lots.md)
