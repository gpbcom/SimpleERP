🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-02 Customise documents and emails](README.md) › 🖥️ S-F2-06 Document template editor

# 🖥️ S-F2-06 Document template editor

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role, typically [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
  and [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) (D98)

## Purpose

Design a document template on an A4 page.

## Entry points

Configuration › Documents.

## Wireframe

```text
+------------------------------------------------------------------+
| Invoice > Standard (fr) [fr v]   [Blocks | HTML]  [Preview] [Publish]|
|-------------------+----------------------------------------------|
| Blocks            |  [logo]            ACME BATIMENT SAS          |
|  Header           |  Invoice INV-2026-0042      10/11/2026        |
|  Addresses        |  Customer: ...                               |
|  Lines table      |  +--------------------------------------+    |
|  Totals           |  | lines                                |    |
|  Conditions       |  +--------------------------------------+    |
|  Free text        |                          Total 1 240,00 EUR  |
|  Fields [picker]  |  [locked] SIREN, VAT, late-payment terms     |
+-------------------+----------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-02 step 1, U07 | desktop | ![FL-F2-02 step 1, U07, light](../../images/02-customise-documents-and-emails/u07-administrator/1-document-template-desktop-light.png) | ![FL-F2-02 step 1, U07, dark](../../images/02-customise-documents-and-emails/u07-administrator/1-document-template-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/02-customise-documents-and-emails/u07-administrator/e1-legal-mention-locked-desktop-light.png) | ![Error E1, U07, dark](../../images/02-customise-documents-and-emails/u07-administrator/e1-legal-mention-locked-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/02-customise-documents-and-emails/u07-administrator/e2-html-outside-address-desktop-light.png) | ![Error E2, U07, dark](../../images/02-customise-documents-and-emails/u07-administrator/e2-html-outside-address-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-06-document-template-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-06-document-template-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-06-document-template-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-06-document-template-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-06-document-template-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-06-document-template-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-06-document-template-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-06-document-template-editor-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-06 Document template](../../data/e-f02-06-document-template.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Add, move, style a block | configurator | Draft |
| Switch to HTML | configurator | Code mode |
| Preview | configurator | A real document rendered |
| Publish | configurator | UC-F2-09 |

## States

- Normal: Design a document template on an A4 page, as the wireframe shows.
- Empty: no template of that type yet: the company's default layout, with Copy to edit.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: broken HTML.
- Read-only: locked legal blocks (BR-F2-10).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Locked blocks show a lock.

Shown entities (VD-15): [E-F2-06 Document template](../../data/e-f02-06-document-template.md),
[E-F2-27 Legal mention](../../data/e-f02-27-legal-mention.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-06 Document template | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-05); fields editable within the role | U07, U12, U16 | `u07-administrator/s-f02-06-document-template-editor-e-f02-06-document-template-draft-desktop-{light,dark}.png`, `u12-marketing/s-f02-06-document-template-editor-e-f02-06-document-template-draft-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f02-06-document-template-editor-e-f02-06-document-template-draft-{desktop,phone}-{light,dark}.png` |
| E-F2-06 Document template | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-06-document-template-editor-e-f02-06-document-template-published-desktop-{light,dark}.png` |
| E-F2-27 Legal mention | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-06-document-template-editor-e-f02-27-legal-mention-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Blocks can be moved with the keyboard; generated PDFs are tagged for screen readers.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)

## Shown in

- [FL-F2-02 Customise documents and emails](../../flows/fl-f02-02-customise-documents-and-emails.md)

## Open questions

None.

---

⬅️ [S-F2-05 Record type gallery](../01-configure-a-record-type/s-f02-05-record-type-gallery.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-07 Email template editor](s-f02-07-email-template-editor.md)
