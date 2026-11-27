🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-17 Mailboxes for named users, closed at offboarding

# 📏 BR-F18-17 Mailboxes for named users, closed at offboarding

**Status:** 🔄 waiting for the owner

## Statement

A mailbox on the company's domain belongs to a named user or a shared role address with named members; it follows the
user's lifecycle in F1, and is closed with its mail exported when the user is offboarded.

## Why

Mail on the domain is company data (D475) and follows F1's user lifecycle (UC-F1-05).

## Examples

| Case | Result |
|---|---|
| marie@company domain for user Marie | passes |
| contact@company domain shared by 3 users | passes |
| Mailbox with no owner | fails: refused |
| User offboarded | passes: mailbox closed, mail exported to the manager (Proposed) after 30 days |

## Applies to

- [UC-F18-23 Create mailboxes on the domain](../use-cases/03-domain-and-dns/uc-f18-23-create-mailboxes-on-the-domain.md)

## Exceptions

The owner may keep a leaver's address as a forward for (Proposed) 90 days.

## Configurable

Mailbox size per plan (Proposed).

## Open questions

None.

---

⬅️ [BR-F18-16 Every old address redirects](br-f18-16-every-old-address-redirects.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-18 Forms protected without tracking](br-f18-18-forms-protected-without-tracking.md)
