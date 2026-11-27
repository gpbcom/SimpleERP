🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-01 Set up the stores](README.md) › 🖥️ S-SC02-05 Labels

# 🖥️ S-SC02-05 Labels

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)

## Purpose

Used to print shelf labels with unit prices
([UC-SC02-05](../../use-cases/01-set-up-the-stores/uc-sc02-05-print-shelf-labels-with-unit-prices.md)); to run sales
periods and markdowns
([UC-SC02-06](../../use-cases/01-set-up-the-stores/uc-sc02-06-run-sales-periods-and-markdowns.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-01 step 3, U23 | phone | ![FL-SC02-01 step 3, U23, light](../../images/01-set-up-the-stores/u23-store-manager/3-labels-phone-light.png) | ![FL-SC02-01 step 3, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/3-labels-phone-dark.png) |
| FL-SC02-01 step 3, U23 | desktop | ![FL-SC02-01 step 3, U23, light](../../images/01-set-up-the-stores/u23-store-manager/3-labels-desktop-light.png) | ![FL-SC02-01 step 3, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/3-labels-desktop-dark.png) |
| FL-SC02-01 step 3, U23 | tablet | ![FL-SC02-01 step 3, U23, light](../../images/01-set-up-the-stores/u23-store-manager/3-labels-tablet-light.png) | ![FL-SC02-01 step 3, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/3-labels-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-05-labels-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-05-labels-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-05-labels-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-05-labels-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-05-labels-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-05-labels-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-05-labels-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-05-labels-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-07 Shelf label](../../data/e-sc02-07-shelf-label.md),
[E-SC02-08 Markdown](../../data/e-sc02-08-markdown.md), shown as the entity pages list them, with their examples.

## Actions

- Open the labels to print:
  [UC-SC02-05](../../use-cases/01-set-up-the-stores/uc-sc02-05-print-shelf-labels-with-unit-prices.md), step 1.
- Print or update: [UC-SC02-05](../../use-cases/01-set-up-the-stores/uc-sc02-05-print-shelf-labels-with-unit-prices.md),
  step 2.
- Place and mark done:
  [UC-SC02-05](../../use-cases/01-set-up-the-stores/uc-sc02-05-print-shelf-labels-with-unit-prices.md), step 3.
- Check the shelf: [UC-SC02-05](../../use-cases/01-set-up-the-stores/uc-sc02-05-print-shelf-labels-with-unit-prices.md),
  step 4.
- Print the labels: [UC-SC02-06](../../use-cases/01-set-up-the-stores/uc-sc02-06-run-sales-periods-and-markdowns.md),
  step 3.

## States

- Normal: the labels to print per store with old and new price, unit price and batch state.
- Empty: "No label to print".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a unit price missing on a product sold by weight or volume: the
  label is blocked until the quantity is set ([BR-SC02-02](../../business-rules/br-sc02-02-every-product-priced.md)).
- Read-only: a done batch is read-only.
- Offline: printing on the store's printer works on the local network; electronic labels wait for the connection.

Shown entities (VD-15): [E-SC02-07 Shelf label](../../data/e-sc02-07-shelf-label.md),
[E-SC02-08 Markdown](../../data/e-sc02-08-markdown.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-07 Shelf label | To print | Badge "To print"; a new record starts here; next: Done (UC-SC02-05); fields editable within the role | U12, U17, U23 | `u12-marketing/s-sc02-05-labels-e-sc02-07-shelf-label-to-print-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc02-05-labels-e-sc02-07-shelf-label-to-print-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-05-labels-e-sc02-07-shelf-label-to-print-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-08 Markdown | Live | Badge "Live"; a new record starts here; next: Refused (UC-SC02-06); fields editable within the role | U12, U17, U23 | `u12-marketing/s-sc02-05-labels-e-sc02-08-markdown-live-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc02-05-labels-e-sc02-08-markdown-live-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-05-labels-e-sc02-08-markdown-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-08 Markdown | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U12, U17, U23 | `u12-marketing/s-sc02-05-labels-e-sc02-08-markdown-refused-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-sc02-05-labels-e-sc02-08-markdown-refused-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-05-labels-e-sc02-08-markdown-refused-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC02-01 Set up the stores](../../flows/fl-sc02-01-set-up-the-stores.md)

## Open questions

None.

---

⬅️ [S-SC02-04 Transfers](../02-keep-stock-right/s-sc02-04-transfers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-06 Sales periods](s-sc02-06-sales-periods.md)
