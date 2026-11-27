🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-25 Members-only content is never indexed

# 📏 BR-F18-25 Members-only content is never indexed

**Status:** 🔄 waiting for the owner

## Statement

A members-only page is never indexed: it carries the not-indexed mark, is left out of the sitemap and of the site's own
public search, and gives anyone who is not in its audience only a sign-in prompt, never a part of its content or its
title.

## Why

A search engine or a crawler that reads reserved content publishes it for everyone, and it cannot be called back. The
owner asked for members-only pages
[D537](../../../06-decisions/f18-hosted-websites-and-domains/d537-benchmark-gaps-f18-hosted-websites-and-domains.md).

## Examples

| Case | Result |
|---|---|
| A members page asked for by a search engine | the sign-in prompt only |
| A members page missing from the sitemap | correct |
| A members page found in the sitemap | held until removed |
| A page title shown in a public list | not allowed: titles of reserved pages are not shown |
| A member who leaves the group | loses access at once |

## Applies to

- [UC-F18-31](../use-cases/07-tests-visitors-and-accessibility/uc-f18-31-publish-members-only-pages.md)
- [E-F18-23 Page audience](../data/e-f18-23-page-audience.md)
- [E-F18-02 Page](../data/e-f18-02-page.md)
- [E-F1-17 Portal account](../../f01-administration/data/e-f01-17-portal-account.md)

## Exceptions

None.

## Configurable

The audience of each page, by the marketing person; the not-indexed mark cannot be switched off.

## Open questions

None.

---

⬅️ [BR-F18-24](br-f18-24-an-e-shop-publishes-its-accessibility-statement.md) · ⬆️ [Up](README.md)
