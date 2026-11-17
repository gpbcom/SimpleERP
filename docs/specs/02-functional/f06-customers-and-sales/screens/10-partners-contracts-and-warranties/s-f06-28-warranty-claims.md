🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F6-28 Warranty claims

# 🖥️ S-F6-28 Warranty claims

**Status:** 🔄 waiting for the owner

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): their claims, from their phone.
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): every claim of the company.

## Purpose

Report a defect, check the guarantees, decide the remedy and follow the claim.

## Entry points

Customer portal › Report a defect, on a phone; Customers and sales › Warranty claims.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Claim WC-0412  Oak table SO-2290, delivered 2026-09-12             Claimed                  |
|---------------------------------------------------------------------------------------------|
| Customer  Karim D.     Defect  scratched top, photos (3)                                    |
| GUARANTEES  Legal conformity: applies  |  Commercial 1 year: applies                        |
| Remedy  [x] Replace  [ ] Repair  [ ] Price reduction  [ ] Refund                            |
| Decision  Accept under the legal guarantee      [Accept] [Refuse]                           |
| Follow-up  Replacement order SO-2402                                                        |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-10 step 5, U09 | phone | ![FL-F6-10 step 5, U09, light](../../images/10-partners-contracts-and-warranties/u09-customer/5-warranty-claims-phone-light.png) | ![FL-F6-10 step 5, U09, dark](../../images/10-partners-contracts-and-warranties/u09-customer/5-warranty-claims-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f06-28-warranty-claims-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f06-28-warranty-claims-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f06-28-warranty-claims-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f06-28-warranty-claims-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f06-28-warranty-claims-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f06-28-warranty-claims-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-28-warranty-claims-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-28-warranty-claims-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Order and item | E-F6-27 order line | text and link | no | yes |
| Defect and photos | E-F6-27 claim | text and images | yes for the customer | yes |
| Guarantees | E-F6-27 guarantee ends | two badges and dates | no | yes |
| Remedy | E-F6-27 remedy | list | yes | when accepted |
| Decision and reason | E-F6-27 decision | badge and text | yes | yes |
| Follow-up | E-F7-14, E-F6-04, credit note | links | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Report a defect | phone | customer | a claim is created and linked to the order |
| Accept | claim | office worker | the remedy starts |
| Refuse | claim | office worker | needs a reason; the customer can dispute it |
| Dispute | phone | customer | the claim reopens for the owner |

## States

- Normal: the claim, the two guarantees with their dates, the remedy and the decision.
- Empty: No claim yet, with Report a defect.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a claim with no
  delivery date shows what is missing and who can supply it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-27 Warranty](../../data/e-f06-27-warranty.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-27 Warranty | Covered | Badge "Covered"; a new record starts here; next: Claimed or Expired (UC-F6-31); fields editable within the role | U09, U16 | `u09-customer/s-f06-28-warranty-claims-e-f06-27-warranty-covered-phone-{light,dark}.png`, `u16-office-worker/s-f06-28-warranty-claims-e-f06-27-warranty-covered-{desktop,phone}-{light,dark}.png` |
| E-F6-27 Warranty | Claimed | Badge "Claimed"; next: Accepted or Refused (BR-F6-23); fields editable within the role | U09, U16 | `u09-customer/s-f06-28-warranty-claims-e-f06-27-warranty-claimed-phone-{light,dark}.png`, `u16-office-worker/s-f06-28-warranty-claims-e-f06-27-warranty-claimed-{desktop,phone}-{light,dark}.png` |
| E-F6-27 Warranty | Accepted | Badge "Accepted"; next: Resolved (UC-F6-31); fields editable within the role | U09, U16 | `u09-customer/s-f06-28-warranty-claims-e-f06-27-warranty-accepted-phone-{light,dark}.png`, `u16-office-worker/s-f06-28-warranty-claims-e-f06-27-warranty-accepted-{desktop,phone}-{light,dark}.png` |
| E-F6-27 Warranty | Refused | Badge "Refused"; next: Claimed (UC-F6-31); fields editable within the role | U09, U16 | `u09-customer/s-f06-28-warranty-claims-e-f06-27-warranty-refused-phone-{light,dark}.png`, `u16-office-worker/s-f06-28-warranty-claims-e-f06-27-warranty-refused-{desktop,phone}-{light,dark}.png` |
| E-F6-27 Warranty | Resolved | Badge "Resolved"; final: read-only, no next state; the history shows how it got here | U09, U16 | `u09-customer/s-f06-28-warranty-claims-e-f06-27-warranty-resolved-phone-{light,dark}.png`, `u16-office-worker/s-f06-28-warranty-claims-e-f06-27-warranty-resolved-{desktop,phone}-{light,dark}.png` |
| E-F6-27 Warranty | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U09, U16 | `u09-customer/s-f06-28-warranty-claims-e-f06-27-warranty-expired-phone-{light,dark}.png`, `u16-office-worker/s-f06-28-warranty-claims-e-f06-27-warranty-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The customer's report is built for a phone: pick the item, describe the defect, add photos with the camera, send. The
office worker's screen is desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-10](../../flows/fl-f06-10-partners-contracts-and-warranties.md)

## Open questions

None.

---

⬅️ [S-F6-27 Solvency check](s-f06-27-solvency-check.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L01 Customer records](../00-lists/s-f06-l01-customer-records.md)
