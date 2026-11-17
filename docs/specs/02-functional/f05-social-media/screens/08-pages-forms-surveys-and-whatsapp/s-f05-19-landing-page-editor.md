🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-08 Pages, forms, surveys and WhatsApp](README.md) › 🖥️ S-F5-19 Landing page editor

# 🖥️ S-F5-19 Landing page editor

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Build and publish a landing page with its form.

## Entry points

Marketing › Landing pages.

## Wireframe

```text
+------------------------------------------------------------------+
| Autumn sale   /autumn-sale       [Preview] [Publish]             |
| [Hero image]  "Up to 30 % off this week"                         |
| Form: Name [   ]  Email [   ]                                    |
|   [ ] I agree to receive offers by email (consent text v3)       |
| Visits 2,140   Submissions 120   Conversion 5.6 %                |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-08 step 1, U12 | desktop | ![FL-F5-08 step 1, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/1-landing-page-editor-desktop-light.png) | ![FL-F5-08 step 1, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/1-landing-page-editor-desktop-dark.png) |
| FL-F5-08 step 1, U12 | phone | ![FL-F5-08 step 1, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/1-landing-page-editor-phone-light.png) | ![FL-F5-08 step 1, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/1-landing-page-editor-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/e1-landing-page-editor-refused-desktop-light.png) | ![Error E1, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/e1-landing-page-editor-refused-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/e1-landing-page-editor-refused-phone-light.png) | ![Error E1, U12, dark](../../images/08-pages-forms-surveys-and-whatsapp/u12-marketing/e1-landing-page-editor-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-19-landing-page-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-19-landing-page-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-19-landing-page-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-19-landing-page-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-19-landing-page-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-19-landing-page-editor-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-19-landing-page-editor-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-19-landing-page-editor-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Blocks, form fields, consent texts, counts | E-F5-13 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | marketing | Page live |
| Submit | visitor | Lead created |

## States

- Normal: build and publish a landing page with its form.
- Empty: no page yet: Start from a template.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a published page for non-marketing users; visitors only fill the form.
- Offline: Not available offline: the page is served live to visitors
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F5-13 Landing page and form](../../data/e-f05-13-landing-page-and-form.md),
[E-F5-10 Consent and suppression record](../../data/e-f05-10-consent-and-suppression-record.md),
[E-F6-20 Lead](../../../f06-customers-and-sales/data/e-f06-20-lead.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-13 Landing page and form | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F5-19); fields editable within the role | U09, U12 | `u09-customer/s-f05-19-landing-page-editor-e-f05-13-landing-page-and-form-draft-phone-{light,dark}.png`, `u12-marketing/s-f05-19-landing-page-editor-e-f05-13-landing-page-and-form-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-13 Landing page and form | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f05-19-landing-page-editor-e-f05-13-landing-page-and-form-published-phone-{light,dark}.png`, `u12-marketing/s-f05-19-landing-page-editor-e-f05-13-landing-page-and-form-published-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Given | Badge "Given"; a new record starts here; next: Withdrawn or Suppressed (UC-F5-15, UC-F5-14); fields editable within the role | U09, U12 | `u09-customer/s-f05-19-landing-page-editor-e-f05-10-consent-and-suppression-record-given-phone-{light,dark}.png`, `u12-marketing/s-f05-19-landing-page-editor-e-f05-10-consent-and-suppression-record-given-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Withdrawn | Badge "Withdrawn"; next: Given (UC-F5-15); fields editable within the role | U09, U12 | `u09-customer/s-f05-19-landing-page-editor-e-f05-10-consent-and-suppression-record-withdrawn-phone-{light,dark}.png`, `u12-marketing/s-f05-19-landing-page-editor-e-f05-10-consent-and-suppression-record-withdrawn-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Suppressed | Badge "Suppressed"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f05-19-landing-page-editor-e-f05-10-consent-and-suppression-record-suppressed-phone-{light,dark}.png`, `u12-marketing/s-f05-19-landing-page-editor-e-f05-10-consent-and-suppression-record-suppressed-{desktop,phone}-{light,dark}.png` |
| E-F6-20 Lead | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U12 | `u09-customer/s-f05-19-landing-page-editor-e-f06-20-lead-active-phone-{light,dark}.png`, `u12-marketing/s-f05-19-landing-page-editor-e-f06-20-lead-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Editor on desktop; the page on any device.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-08 Pages, forms, surveys and WhatsApp](../../flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md)

## Open questions

None.

---

⬅️ [S-F5-18 Ticket scan](../07-events-and-ticketing/s-f05-18-ticket-scan.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-20 WhatsApp Business](s-f05-20-whatsapp-business.md)
