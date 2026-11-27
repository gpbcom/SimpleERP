🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-07 Posts queue within network limits

# 📏 BR-F5-07 Posts queue within network limits

**Status:** ✅ specified

## Statement

Each network's rate limits and costs are shown per account; posts queue within the limits and the author sees when each
will go out; the app used per account is the install's own app, registered by the company or its IT provider, its keys
in the vault; in the hosted edition, the publisher's shared app may relay posts under its own terms (D250, clarified
after the review of 2026-11-12).

## Why

Networks block apps that exceed their limits. See [D250](../../../06-decisions/f05-social-media/d250-network-apps.md).

## Examples

| Case | Result |
|---|---|
| 30 posts for X at once | Queued within X's limit, times shown |
| The hosted relay's quota exhausted | The company's own app is proposed |

## Applies to

- [UC-F5-01](../use-cases/01-publish-a-post/uc-f05-01-prepare-and-schedule-a-post.md)
- [UC-F5-07](../use-cases/04-connect-accounts/uc-f05-07-connect-the-company-s-accounts.md)

## Exceptions

None.

## Configurable

The app per account.

## Open questions

None.

---

⬅️ [BR-F5-06 Leads traced through tracked links](br-f05-06-leads-traced-through-tracked-links.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-08 Marketing messages need consent](br-f05-08-marketing-needs-consent.md)
