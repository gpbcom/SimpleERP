🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-02 Customise documents and emails](README.md) › 🖥️ S-F2-07 Email template editor

# 🖥️ S-F2-07 Email template editor

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role, typically [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
  and [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) (D98)

## Purpose

Edit an outgoing email's subject and body, and the company's branding and sender.

## Entry points

Configuration › Emails.

## Wireframe

```text
+------------------------------------------------------------------+
| Emails > Invoice sent   [fr v]        [Send me a test] [Publish] |
|------------------------------------------------------------------|
| Subject [ Facture {invoice.number} de {company.name}         ]   |
| Body    [ Bonjour {contact.first_name}, ...                  ]   |
|         [ fields: + ]                                            |
|------------------------------------------------------------------|
| Branding: logo, colours, signature        Sender: invoices@acme.fr|
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-02 step 2, U07 | desktop | ![FL-F2-02 step 2, U07, light](../../images/02-customise-documents-and-emails/u07-administrator/2-email-template-desktop-light.png) | ![FL-F2-02 step 2, U07, dark](../../images/02-customise-documents-and-emails/u07-administrator/2-email-template-desktop-dark.png) |
| Error E3, U07 | desktop | ![Error E3, U07, light](../../images/02-customise-documents-and-emails/u07-administrator/e3-sender-test-failed-desktop-light.png) | ![Error E3, U07, dark](../../images/02-customise-documents-and-emails/u07-administrator/e3-sender-test-failed-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-07-email-template-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-07-email-template-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-07-email-template-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-07-email-template-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-07-email-template-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-07-email-template-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-07-email-template-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-07-email-template-editor-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-07 Email template](../../data/e-f02-07-email-template.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Edit subject and body | configurator | Draft |
| Send me a test | configurator | A real email to themselves |
| Publish | configurator | UC-F2-09 |

## States

- Normal: Edit an outgoing email's subject and body, and the company's branding and sender, as the wireframe shows.
- Empty: no custom template yet: the default email, with Edit.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: a required field removed; sender test failed.
- Read-only: for users who are not configurators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-07 Email template](../../data/e-f02-07-email-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-07 Email template | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-06); fields editable within the role | U07 | `u07-administrator/s-f02-07-email-template-editor-e-f02-07-email-template-draft-desktop-{light,dark}.png` |
| E-F2-07 Email template | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-07-email-template-editor-e-f02-07-email-template-published-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Field placeholders are announced by name.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F2-02 Customise documents and emails](../../flows/fl-f02-02-customise-documents-and-emails.md)

## Open questions

None.

---

⬅️ [S-F2-06 Document template editor](s-f02-06-document-template-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-08 Rule editor](../03-automate-with-a-rule/s-f02-08-rule-editor.md)
