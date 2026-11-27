🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-04 Commissions and tips](README.md) ›
🖥️ S-SC17-16 Salon AI assistant

# 🖥️ S-SC17-16 Salon AI assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the answers and actions within their role.

## Purpose

Ask the AI assistant about the salon and confirm the actions it prepares.

## Entry points

Beauty and wellness › Ask the AI assistant; the phone's home screen.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Ask about the salon                                                                              |
| You: Who has not paid the deposit for tomorrow?                                                  |
| AI assistant: 3 bookings. Camille R. 14:30, Noor A. 15:30, Jules P. 17:00.                       |
| Sources: salon bookings, booking deposits (3 rows)                                               |
| Prepared: send a payment link to the 3 customers         [Confirm]  [Change]                     |
| [ Type your question                                        ]                                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-04 step 4, U23 | phone | ![FL-SC17-04 step 4, U23, light](../../images/04-commissions-and-tips/u23-store-manager/4-salon-assistant-phone-light.png) | ![FL-SC17-04 step 4, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/4-salon-assistant-phone-dark.png) |
| FL-SC17-04 step 4, U23 | desktop | ![FL-SC17-04 step 4, U23, light](../../images/04-commissions-and-tips/u23-store-manager/4-salon-assistant-desktop-light.png) | ![FL-SC17-04 step 4, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/4-salon-assistant-desktop-dark.png) |
| FL-SC17-04 step 4, U23 | tablet | ![FL-SC17-04 step 4, U23, light](../../images/04-commissions-and-tips/u23-store-manager/4-salon-assistant-tablet-light.png) | ![FL-SC17-04 step 4, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/4-salon-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-16-salon-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-16-salon-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-16-salon-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-16-salon-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-16-salon-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-16-salon-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-16-salon-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-16-salon-assistant-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question | F3 question | text or voice | yes | yes |
| Answer | F3 answer | text, list or figure | no | no |
| Sources | F3 sources | list of records | no | no |
| Prepared action | F3 prepared action | action and records | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask | footer | store manager | an answer from the data the manager may see |
| Confirm | action | store manager | the prepared action is done |
| Change | action | store manager | the action is edited before it is confirmed |

## States

- Normal: the conversation with the answers, the sources and the prepared actions.
- Empty: No question yet, with examples.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an answer
  refused for rights or missing data, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Phone first: one column, the sources folded.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-04 Commissions and tips](../../flows/fl-sc17-04-commissions-and-tips.md)

## Open questions

None.

---

⬅️ [S-SC17-15 Staff targets](s-sc17-15-staff-targets.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-17 Chair rental](../05-rentals-care-records-and-loyalty/s-sc17-17-chair-rental.md)
