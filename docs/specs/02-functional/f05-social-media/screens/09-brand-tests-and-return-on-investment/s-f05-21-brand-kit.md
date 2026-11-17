🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-09 Brand, tests and return on investment](README.md) › 🖥️ S-F5-21 Brand kit

# 🖥️ S-F5-21 Brand kit

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Keep logos, colours, fonts, tone and assets with their rights.

## Entry points

Marketing › Brand kit.

## Wireframe

```text
+------------------------------------------------------------------+
| Brand kit   Logo [img]  Colours #1E5AA8 #F2B705  Font Inter      |
| Tone: warm, short sentences, no jargon                          |
| Assets (40)   [search]                     [+ Upload]            |
| shop-front.jpg   agency, until 2026-12-31   used in 3 posts      |
| team.jpg         own photo                  used in 1 page       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-09 step 1, U12 | desktop | ![FL-F5-09 step 1, U12, light](../../images/09-brand-tests-and-return-on-investment/u12-marketing/1-brand-kit-desktop-light.png) | ![FL-F5-09 step 1, U12, dark](../../images/09-brand-tests-and-return-on-investment/u12-marketing/1-brand-kit-desktop-dark.png) |
| FL-F5-09 step 1, U12 | phone | ![FL-F5-09 step 1, U12, light](../../images/09-brand-tests-and-return-on-investment/u12-marketing/1-brand-kit-phone-light.png) | ![FL-F5-09 step 1, U12, dark](../../images/09-brand-tests-and-return-on-investment/u12-marketing/1-brand-kit-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/09-brand-tests-and-return-on-investment/u12-marketing/e1-brand-kit-refused-desktop-light.png) | ![Error E1, U12, dark](../../images/09-brand-tests-and-return-on-investment/u12-marketing/e1-brand-kit-refused-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/09-brand-tests-and-return-on-investment/u12-marketing/e1-brand-kit-refused-phone-light.png) | ![Error E1, U12, dark](../../images/09-brand-tests-and-return-on-investment/u12-marketing/e1-brand-kit-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-21-brand-kit-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-21-brand-kit-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-21-brand-kit-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-21-brand-kit-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-21-brand-kit-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-21-brand-kit-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-21-brand-kit-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-21-brand-kit-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Kit items, assets, rights, uses | E-F5-15 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Upload | marketing | Asset with its rights |

## States

- Normal: keep logos, colours, fonts, tone and assets with their rights.
- Empty: no kit yet: Add your logo.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users who are not marketing: they use, not change.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-15 Brand asset](../../data/e-f05-15-brand-asset.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-15 Brand asset | Draft | Badge "Draft"; a new record starts here; next: Expired (UC-F5-21); fields editable within the role | U12 | `u12-marketing/s-f05-21-brand-kit-e-f05-15-brand-asset-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-15 Brand asset | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-21-brand-kit-e-f05-15-brand-asset-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)

## Shown in

- [FL-F5-09 Brand, tests and return on investment](../../flows/fl-f05-09-brand-tests-and-return-on-investment.md)

## Open questions

None.

---

⬅️ [S-F5-20 WhatsApp Business](../08-pages-forms-surveys-and-whatsapp/s-f05-20-whatsapp-business.md) ·
⬆️ [Up](README.md) · ➡️ [S-F5-22 A/B test](s-f05-22-a-b-test.md)
