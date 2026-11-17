🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-16 Every old address redirects

# 📏 BR-F18-16 Every old address redirects

**Status:** ✅ specified

## Statement

When a site replaces an older one, or a page moves, every address that existed is redirected permanently to its new page
or the closest one; no address that existed answers "not found" after publication.

## Why

Search ranking and links are kept when a site is replaced (D475).

## Examples

| Case | Result |
|---|---|
| Old /nos-services redirected to /services | passes |
| Old address with no match redirected to the home page and flagged | passes |
| Old address answering not found after publication | fails: the check fails |
| Redirect loop | fails: refused |

## Applies to

- [UC-F18-22 Redirect the old site's addresses](../use-cases/03-domain-and-dns/uc-f18-22-redirect-the-old-sites-addresses.md)
- [UC-F18-10 Connect an existing domain](../use-cases/03-domain-and-dns/uc-f18-10-connect-an-existing-domain.md)
- [UC-F18-14 Run the automatic checks](../use-cases/04-test-and-publish/uc-f18-14-run-the-automatic-checks.md)

## Exceptions

Addresses the owner marks "gone" answer "gone" on purpose.

## Configurable

Marketing maps the addresses; the default target is the home page.

## Open questions

None.

---

⬅️ [BR-F18-15 Blog articles come from F5 posts](br-f18-15-blog-articles-come-from-f5-posts.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-17](br-f18-17-mailboxes-for-named-users-closed-at-offboarding.md)
