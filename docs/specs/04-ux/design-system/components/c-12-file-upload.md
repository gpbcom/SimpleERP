🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-12 File upload

# 🧩 C-12 File upload

**Status:** 🔄 waiting for the owner

## Purpose

Adds files to SimpleERP: a logo, an import file, a receipt photo, a document to a knowledge base, a pack.

## Anatomy

```text
+--------------------------------------------+
|  Drop a file here, or [Choose a file]       |
|  CSV or Excel, up to 20 MB                  |
+--------------------------------------------+
  invoices-2025.xlsx   1.2 MB   [=====   ] 60 %   [x]
```

A drop area with a button, the accepted formats and size, then one line per file with its progress.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-12-file-upload-desktop-light.png) | ![Variants and states, dark](../images/c-12-file-upload-desktop-dark.png) |

## Variants

- **Drop area:** on desktops, for one or several files.
- **Button only:** in a [C-02 Form field](c-02-form-field.md), such as "Logo [Upload...]" on
  [S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).
- **Camera:** on phones, a photo of a receipt or a page (Proposed: the phone's camera or files), as on
  [S-F3-11 Phone assistant](../../../02-functional/f03-assistant/screens/09-assistant-on-a-phone/s-f03-11-phone-assistant.md).

## States

| State | Look |
|---|---|
| Default | `color-border-strong` dashed edge (Proposed) |
| Drag over | (Proposed) `color-primary` edge and a tinted fill |
| Uploading | A progress bar per file, with Cancel |
| Read | (Proposed) For files the AI reads, "Reading..." then what was found |
| Done | The file's name, size and a remove button |
| Error | The [error message pattern](../patterns/error-messages.md): wrong format or too large, with the formats accepted ("The document cannot be read: said, with the formats accepted", F15) |

## Tokens

`color-border-strong`, `color-primary`, `color-surface-alt`, `color-error`; radius 8 px ([Tokens](../tokens.md));
`font-body` and `font-caption`; icons at 20 px ([Iconography](../../visual-identity/iconography.md)).

## Accessibility

- The button works without drag and drop; the drop area is not the only way in.
- Progress and results are announced; each file's remove button is named after the file.
- Accepted formats and size are written before choosing, not only after an error.

## Do and don't

- Do say the formats and the size limit (Proposed: limits per use, such as 20 MB for imports).
- Do show what the AI read from a file before it is used.
- (Proposed) Don't lose the other files when one fails.

## Used in

[S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md),
[S-F2-06 Document template editor](../../../02-functional/f02-no-code-configuration/screens/02-customise-documents-and-emails/s-f02-06-document-template-editor.md),
[S-F2-11 Packs](../../../02-functional/f02-no-code-configuration/screens/06-share-a-configuration/s-f02-11-packs.md),
[S-F3-03 Writing style settings](../../../02-functional/f03-assistant/screens/04-summarise-or-draft/s-f03-03-writing-style-settings.md),
[S-F3-08 Knowledge item editor](../../../02-functional/f03-assistant/screens/07-manage-knowledge/s-f03-08-knowledge-item-editor.md)
and
[S-F3-11 Phone assistant](../../../02-functional/f03-assistant/screens/09-assistant-on-a-phone/s-f03-11-phone-assistant.md);
and the [Import and export pattern](../patterns/import-export.md).

## Open questions

None.

---

⬅️ [Chat panel](c-11-chat-panel.md) · ⬆️ [Up](README.md) · ➡️ [Stepper](c-13-stepper.md)
