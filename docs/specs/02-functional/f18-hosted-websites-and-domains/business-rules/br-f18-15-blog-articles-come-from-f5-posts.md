🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-15 Blog articles come from F5 posts

# 📏 BR-F18-15 Blog articles come from F5 posts

**Status:** ✅ specified

## Statement

A blog article is created from a post published in F5 with its text, images and date; posts written with AI help keep
their label, and an article removed in F5 is unpublished from the blog at the next publication.

## Why

Marketing writes once (D475); readers are told when content was written with AI help (CR-FR-056).

## Examples

| Case | Result |
|---|---|
| F5 post "Winter menu" published | passes: blog article on the preview |
| Post written with AI help | passes: article shows "written with AI help" |
| Post deleted in F5 | passes: article removed at the next publication |

## Applies to

- [UC-F18-21 Publish a blog fed by F5 posts](../use-cases/06-content-and-search/uc-f18-21-publish-a-blog-fed-by-f5-posts.md)

## Exceptions

Marketing may write an article directly in the blog; it then follows the same checks.

## Configurable

Which F5 channels feed the blog.

## Open questions

None.

---

⬅️ [BR-F18-14 Analytics only with consent](br-f18-14-analytics-only-with-consent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-16 Every old address redirects](br-f18-16-every-old-address-redirects.md)
