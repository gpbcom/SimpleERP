🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-07 Notaries, brokers, judicial officers and audit firms](README.md) ›
🖥️ S-SC11-21 Notary

# 🖥️ S-SC11-21 Notary

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the deeds, funds and payments.
- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md): the documents and identities of each
  deed.

## Purpose

Prepare a deed, hold its funds at the state deposit bank and pay out only after the signature.

## Entry points

Professional firm › Deeds; the matter of the deed; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Deed D-2026-0417: Sale of 12 Rue des Lilas                           Ready to sign   [Sign]      |
| Parties  Mrs Roux (seller)  Mr and Mrs Gil (buyers)      Price 300,000.00 EUR                    |
| Documents  14 of 15   Missing: energy diagnostic                                                 |
| Funds held at the deposit bank   Received 312,500.00   Paid 0.00   Balance 312,500.00            |
| Payments to make after the signature: seller 296,200.00  taxes 12,100.00  mortgage release 4,200 |
| [Record a fund]  [Pay]  [Close]                                                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-07 step 1, U36 | desktop | ![FL-SC11-07 step 1, U36, light](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/1-notary-desktop-light.png) | ![FL-SC11-07 step 1, U36, dark](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/1-notary-desktop-dark.png) |
| FL-SC11-07 step 1, U36 | phone | ![FL-SC11-07 step 1, U36, light](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/1-notary-phone-light.png) | ![FL-SC11-07 step 1, U36, dark](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/1-notary-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-21-notary-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-21-notary-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-21-notary-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-21-notary-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-21-notary-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-21-notary-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-21-notary-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-21-notary-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind and parties | E-SC11-16 kind, parties | choice and links | yes while Preparing | yes |
| Property or company | E-SC11-16 subject | text | yes while Preparing | yes |
| Price | E-SC11-16 price | amount | yes while Preparing | no |
| Documents | E-SC11-16 documents | checklist | yes | no |
| Funds held | E-SC11-16 funds received, paid | amounts | no | no |
| Signed on | E-SC11-16 signed on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record a fund | deed | notary, professional's assistant | a fund received, held at the deposit bank for this deed |
| Sign | deed | notary | the deed becomes Signed |
| Pay | deed | notary | a payment from the deed's funds, after the signature |
| Close | deed | notary | the deed becomes Closed when its funds are at zero |

## States

- Normal: the deed, its parties, its documents and the funds held and paid.
- Empty: No deed yet, with New deed.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a payment
  before the signature or from another deed's funds, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC11-16 Deed](../../data/e-sc11-16-deed.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-16 Deed | Preparing | Badge "Preparing"; a new record starts here; next: Ready to sign or Cancelled (UC-SC11-21); fields editable within the role | U36, U37 | `u36-professional/s-sc11-21-notary-e-sc11-16-deed-preparing-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-21-notary-e-sc11-16-deed-preparing-desktop-{light,dark}.png` |
| E-SC11-16 Deed | Ready to sign | Badge "Ready to sign"; next: Signed (UC-SC11-21); fields editable within the role | U36, U37 | `u36-professional/s-sc11-21-notary-e-sc11-16-deed-ready-to-sign-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-21-notary-e-sc11-16-deed-ready-to-sign-desktop-{light,dark}.png` |
| E-SC11-16 Deed | Signed | Badge "Signed"; next: Closed (BR-SC11-16); fields editable within the role | U36, U37 | `u36-professional/s-sc11-21-notary-e-sc11-16-deed-signed-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-21-notary-e-sc11-16-deed-signed-desktop-{light,dark}.png` |
| E-SC11-16 Deed | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-21-notary-e-sc11-16-deed-closed-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-21-notary-e-sc11-16-deed-closed-desktop-{light,dark}.png` |
| E-SC11-16 Deed | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-21-notary-e-sc11-16-deed-cancelled-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-21-notary-e-sc11-16-deed-cancelled-desktop-{light,dark}.png` |

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

⬅️ [S-SC11-20 Matter assistant](../02-matters-and-documents/s-sc11-20-matter-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-22 Brokerage](s-sc11-22-brokerage.md)
