🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-05 Customer side](README.md) › 🖥️ S-F16-10 Help centre

# 🖥️ S-F16-10 Help centre

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md), who writes and publishes
- [U09 Customer](../../../../01-users/personas/u09-customer.md), who searches and reads

## Purpose

Publish public articles and let customers search them.

## Entry points

The public help centre link; the request form; Support menu, Help centre for the lead.

## Wireframe

```text
Help centre       [Search: refund delay          ]      Language [fr v]
-------------------------------------------------------------------------------
When will my refund arrive?        updated 2026-11-12     41 found it helpful
How to change my delivery address  updated 2026-10-03
-------------------------------------------------------------------------------
Editor (lead): title, body, languages, [Draft with the assistant] [Publish]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-05 step 1, U02 | desktop | ![FL-F16-05 step 1, U02, light](../../images/05-customer-side/u02-manager/1-help-centre-desktop-light.png) | ![FL-F16-05 step 1, U02, dark](../../images/05-customer-side/u02-manager/1-help-centre-desktop-dark.png) |
| FL-F16-05 step 1, U02 | phone | ![FL-F16-05 step 1, U02, light](../../images/05-customer-side/u02-manager/1-help-centre-phone-light.png) | ![FL-F16-05 step 1, U02, dark](../../images/05-customer-side/u02-manager/1-help-centre-phone-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/05-customer-side/u02-manager/e1-help-centre-refused-desktop-light.png) | ![Error E1, U02, dark](../../images/05-customer-side/u02-manager/e1-help-centre-refused-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/05-customer-side/u02-manager/e1-help-centre-refused-phone-light.png) | ![Error E1, U02, dark](../../images/05-customer-side/u02-manager/e1-help-centre-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-10-help-centre-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-10-help-centre-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-10-help-centre-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-10-help-centre-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-10-help-centre-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-10-help-centre-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-10-help-centre-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-10-help-centre-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title | E-F16-09 title | text | yes (lead) | yes |
| Body | E-F16-09 body | text | yes (lead) | yes |
| Language | E-F16-09 language | list | yes | yes |
| Status | E-F16-09 status | draft, published, archived | yes (lead) | yes |
| Helpful | E-F16-09 helpful | count | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Search | header | anyone | articles listed |
| Vote helpful | article | customer | vote counted |
| Publish | editor | support lead | article public |
| Archive | editor | support lead | article hidden |

## States

- Normal: search and articles for customers; the editor with drafts and published articles for the lead.
- Empty: "No article yet" for the lead; for customers, "No article matches" with the request form.
- Loading: the frame and titles show at once with placeholder rows for the articles; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an article holding customer data, refused at publishing.
- Read-only: customers read only; published articles are edited as a new draft.
- Offline: not available offline: publishing is done online; customers need the network to search. D38 keeps only
  today's schedule, time and intervention records offline. A banner says the connection is lost; what is on screen stays
  visible, every action is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-09 Help-centre article](../../data/e-f16-09-help-centre-article.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-09 Help-centre article | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F16-10); fields editable within the role | U02, U09 | `u02-manager/s-f16-10-help-centre-e-f16-09-help-centre-article-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-10-help-centre-e-f16-09-help-centre-article-draft-phone-{light,dark}.png` |
| E-F16-09 Help-centre article | Published | Badge "Published"; next: Archived (UC-F16-10); fields editable within the role | U02, U09 | `u02-manager/s-f16-10-help-centre-e-f16-09-help-centre-article-published-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-10-help-centre-e-f16-09-help-centre-article-published-phone-{light,dark}.png` |
| E-F16-09 Help-centre article | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U02, U09 | `u02-manager/s-f16-10-help-centre-e-f16-09-help-centre-article-archived-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-10-help-centre-e-f16-09-help-centre-article-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Public pages on phone and desktop; the editor on desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-05 Customer side](../../flows/fl-f16-05-customer-side.md)

## Open questions

None.

---

⬅️ [S-F16-09 Satisfaction survey](s-f16-09-satisfaction-survey.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-11 My requests](s-f16-11-my-requests.md)
