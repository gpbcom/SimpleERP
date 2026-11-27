🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-18 Forms protected without tracking

# 📏 BR-F18-18 Forms protected without tracking

**Status:** ✅ specified

## Statement

Every form of the site is protected against spam by checks that do not track visitors and need no cookie consent: a
hidden field, a time check, a limit per address and a content filter; a suspected message is kept aside, never lost.

## Why

Spam fills the leads (D475); protection must not break cookie consent (CR-FR-070).

## Examples

| Case | Result |
|---|---|
| Form filled in 2 seconds with the hidden field set | blocked, kept in spam |
| 30 messages from one address in an hour limit 5 | blocked after 5 |
| Genuine message flagged as spam | released by marketing, lead created |

## Applies to

- [UC-F18-24 Protect forms against spam](../use-cases/01-build-the-site/uc-f18-24-protect-forms-against-spam.md)
- [UC-F18-04 Add a contact page that feeds leads](../use-cases/01-build-the-site/uc-f18-04-add-a-contact-page-that-feeds-leads.md)

## Exceptions

None.

## Configurable

The limits per form; a stronger challenge only after repeated attacks.

## Open questions

None.

---

⬅️ [BR-F18-17](br-f18-17-mailboxes-for-named-users-closed-at-offboarding.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-19](br-f18-19-sector-templates-carry-the-sectors-mandatory-information.md)
