🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-07 Notaries, brokers, judicial officers and audit firms](README.md) ›
🖥️ S-SC11-23 Judicial officer

# 🖥️ S-SC11-23 Judicial officer

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the acts, services and fees.
- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md): the documents and the bills.

## Purpose

Record the acts, serve them and bill each fee within the regulated tariff.

## Entry points

Professional firm › Acts; the matter's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Act A-2026-3321: Summons to appear                                  Served   [Bill]              |
| Requester Mrs Roux   Recipient Mr Gil, 4 Rue Neuve    Served 2026-11-14 10:15 in person          |
| Tariff line          Fee      Travel   Disbursements   Total                                     |
| Summons               78.50    12.00    6.20            96.70                                    |
| Fee asked 90.00 above the tariff: cut to 78.50                                                   |
| Deadline of the case 2026-11-30    [Record another attempt]                                      |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-07 step 3, U36 | desktop | ![FL-SC11-07 step 3, U36, light](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/3-judicial-officer-desktop-light.png) | ![FL-SC11-07 step 3, U36, dark](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/3-judicial-officer-desktop-dark.png) |
| FL-SC11-07 step 3, U36 | phone | ![FL-SC11-07 step 3, U36, light](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/3-judicial-officer-phone-light.png) | ![FL-SC11-07 step 3, U36, dark](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/3-judicial-officer-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-23-judicial-officer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-23-judicial-officer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-23-judicial-officer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-23-judicial-officer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-23-judicial-officer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-23-judicial-officer-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-23-judicial-officer-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-23-judicial-officer-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Type of act | E-SC11-18 type | choice | yes while Requested | yes |
| Requester and recipient | E-SC11-18 requester, recipient | links and address | yes while Requested | yes |
| Service date and way | E-SC11-18 served on, served how | date, time, choice | yes while Requested | no |
| Tariff line and fee | E-SC11-18 tariff line, fee | text and amount | no | no |
| Travel and disbursements | E-SC11-18 travel, disbursements | amounts | yes while Served | no |
| Deadline of the case | E-SC11-18 deadline | link | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record an act | header | judicial officer, professional's assistant | an act Requested |
| Serve | act | judicial officer | the act becomes Served with its date |
| Bill | act | judicial officer, professional's assistant | the fee within the tariff, the act becomes Billed |
| Cancel | act | judicial officer | the act becomes Cancelled |

## States

- Normal: the act, its recipient, its service, the tariff line and the fee.
- Empty: No act yet, with New act.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a fee above the
  tariff or a service after the deadline, with the amount allowed.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC11-18 Service act](../../data/e-sc11-18-service-act.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-18 Service act | Requested | Badge "Requested"; a new record starts here; next: Served or Cancelled (UC-SC11-23); fields editable within the role | U36, U37 | `u36-professional/s-sc11-23-judicial-officer-e-sc11-18-service-act-requested-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-23-judicial-officer-e-sc11-18-service-act-requested-desktop-{light,dark}.png` |
| E-SC11-18 Service act | Served | Badge "Served"; next: Billed (BR-SC11-18); fields editable within the role | U36, U37 | `u36-professional/s-sc11-23-judicial-officer-e-sc11-18-service-act-served-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-23-judicial-officer-e-sc11-18-service-act-served-desktop-{light,dark}.png` |
| E-SC11-18 Service act | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-23-judicial-officer-e-sc11-18-service-act-billed-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-23-judicial-officer-e-sc11-18-service-act-billed-desktop-{light,dark}.png` |
| E-SC11-18 Service act | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-23-judicial-officer-e-sc11-18-service-act-cancelled-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-23-judicial-officer-e-sc11-18-service-act-cancelled-desktop-{light,dark}.png` |

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

- [FL-SC11-07](../../flows/fl-sc11-07-notaries-brokers-officers-and-auditors.md)

## Open questions

None.

---

⬅️ [S-SC11-22 Brokerage](s-sc11-22-brokerage.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-24 Audit firm](s-sc11-24-audit-firm.md)
