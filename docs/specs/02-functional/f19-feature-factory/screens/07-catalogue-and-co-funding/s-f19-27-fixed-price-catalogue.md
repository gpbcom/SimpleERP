🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-07 Similar features, catalogue, co-funding and maintenance](README.md) ›
🖥️ S-F19-27 Fixed-price catalogue

# 🖥️ S-F19-27 Fixed-price catalogue

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the changes and their prices, and their own orders.
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the changes they order for the company.

## Purpose

Choose a small ready-made change at a fixed price and a known date, and follow the order.

Prices come from the hosted edition's price catalogue, a data file kept by the SimpleERP team, never from the
specification
([D566](../../../../06-decisions/foundations/d566-answers-of-2026-11-15-after-the-benchmark-gap-round.md)); the amounts
on this page are examples.

## Entry points

Feature factory › Fixed-price catalogue; the chatbot's proposal; the request's page.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Fixed-price catalogue      Area [All v]       Spending limit left this month: 850 EUR          |
|---------------------------------------------------------------------------------------------|
| CHANGE                        AREA       PRICE (excl. VAT)  READY IN   YOUR ORDERS             |
| Add a field to a form         Forms      150 EUR            3 days     1 Ready to try          |
| Add a column to a report      Reports    120 EUR            3 days     -                       |
| Tweak a document template     Documents  180 EUR            5 days     1 Accepted              |
| [Open] [Order]       The price shown is the price charged. It does not change after you order.  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-07 step 2, U13 | desktop | ![FL-F19-07 step 2, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/2-fixed-price-catalogue-desktop-light.png) | ![FL-F19-07 step 2, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/2-fixed-price-catalogue-desktop-dark.png) |
| FL-F19-07 step 2, U13 | phone | ![FL-F19-07 step 2, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/2-fixed-price-catalogue-phone-light.png) | ![FL-F19-07 step 2, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/2-fixed-price-catalogue-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-27-fixed-price-catalogue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-27-fixed-price-catalogue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-27-fixed-price-catalogue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-27-fixed-price-catalogue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-27-fixed-price-catalogue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-27-fixed-price-catalogue-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-27-fixed-price-catalogue-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-27-fixed-price-catalogue-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Change | E-F19-17 catalogue entry | text | no | yes |
| Area | E-F19-17 area | forms, reports, documents, rules | no | yes |
| Price and delay | E-F19-17 price, delay | amount and days | no | yes |
| Where it applies | E-F19-17 target | form, report or template | yes while ordering | yes |
| Order state | E-F19-17 state | badge | by the factory and the owner | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Order | row | owner, administrator | freezes the price and date and opens the request |
| Cancel order | order | owner, administrator | possible before the build starts, no charge |
| Accept or refuse | order | owner | after the try-out; refusal closes with no charge |
| Ask for something else | footer | owner, administrator | opens the chatbot for a quote |

## States

- Normal: the catalogue changes with their fixed price and delay, and the company's orders.
- Empty: No order yet, with the catalogue's changes.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an order over
  the spending limit shows the limit and who can raise it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F19-17 Catalogue change](../../data/e-f19-17-catalogue-change.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-17 Catalogue change | Ordered | Badge "Ordered"; a new record starts here; next: Building or Cancelled (UC-F19-04, UC-F19-28); fields editable within the role | U13, U07 | `u13-owner/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-ordered-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-ordered-desktop-{light,dark}.png` |
| E-F19-17 Catalogue change | Building | Badge "Building"; next: Ready (UC-F19-07); fields editable within the role | U13, U07 | `u13-owner/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-building-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-building-desktop-{light,dark}.png` |
| E-F19-17 Catalogue change | Ready | Badge "Ready"; next: Accepted or Refused (BR-F19-16); fields editable within the role | U13, U07 | `u13-owner/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-ready-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-ready-desktop-{light,dark}.png` |
| E-F19-17 Catalogue change | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U13, U07 | `u13-owner/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-accepted-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-accepted-desktop-{light,dark}.png` |
| E-F19-17 Catalogue change | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U13, U07 | `u13-owner/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-refused-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-refused-desktop-{light,dark}.png` |
| E-F19-17 Catalogue change | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U07 | `u13-owner/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-cancelled-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f19-27-fixed-price-catalogue-e-f19-17-catalogue-change-cancelled-desktop-{light,dark}.png` |

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

- [FL-F19-07](../../flows/fl-f19-07-catalogue-and-co-funding.md)

## Open questions

None.

---

⬅️ [S-F19-26 Similar features](s-f19-26-similar-features.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-28 Co-funding](s-f19-28-co-funding.md)
