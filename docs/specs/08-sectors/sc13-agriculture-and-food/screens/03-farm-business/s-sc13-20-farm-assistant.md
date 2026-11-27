🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-03 Farm business](README.md) › 🖥️ S-SC13-20 Farm assistant

# 🖥️ S-SC13-20 Farm assistant

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to ask the AI assistant ([UC-SC13-20](../../use-cases/03-farm-business/uc-sc13-20-ask-the-assistant.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-03 step 6, U40 | phone | ![FL-SC13-03 step 6, U40, light](../../images/03-farm-business/u40-farmer/6-assistant-phone-light.png) | ![FL-SC13-03 step 6, U40, dark](../../images/03-farm-business/u40-farmer/6-assistant-phone-dark.png) |
| FL-SC13-03 step 6, U40 | desktop | ![FL-SC13-03 step 6, U40, light](../../images/03-farm-business/u40-farmer/6-assistant-desktop-light.png) | ![FL-SC13-03 step 6, U40, dark](../../images/03-farm-business/u40-farmer/6-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-20-farm-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-20-farm-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-20-farm-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-20-farm-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-20-farm-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-20-farm-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-20-farm-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-20-farm-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-03 Field operation](../../data/e-sc13-03-field-operation.md),
[E-SC13-05 Animal](../../data/e-sc13-05-animal.md), shown as the entity pages list them, with their examples.

## Actions

- Ask: [UC-SC13-20](../../use-cases/03-farm-business/uc-sc13-20-ask-the-assistant.md), step 1.
- Dictate a treatment: [UC-SC13-20](../../use-cases/03-farm-business/uc-sc13-20-ask-the-assistant.md), step 4.

## States

- Normal: the conversation with answers, links and dictated records.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses.
- Read-only: answers only for roles that cannot act.
- Offline: dictations are kept and processed when the network is back; answers need the network.

Shown entities (VD-15): [E-SC13-03 Field operation](../../data/e-sc13-03-field-operation.md),
[E-SC13-05 Animal](../../data/e-sc13-05-animal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-03 Field operation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40 | `u40-farmer/s-sc13-20-farm-assistant-e-sc13-03-field-operation-active-{desktop,phone}-{light,dark}.png` |
| E-SC13-05 Animal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40 | `u40-farmer/s-sc13-20-farm-assistant-e-sc13-05-animal-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-03 Farm business](../../flows/fl-sc13-03-farm-business.md)

## Open questions

None.

---

⬅️ [S-SC13-19 Farm reports](s-sc13-19-farm-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-21 Vineyard](../06-vineyards-contractors-and-cooperatives/s-sc13-21-vineyard.md)
