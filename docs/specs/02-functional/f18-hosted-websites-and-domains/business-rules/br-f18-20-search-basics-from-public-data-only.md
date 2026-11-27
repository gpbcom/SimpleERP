🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-20 Search basics from public data only

# 📏 BR-F18-20 Search basics from public data only

**Status:** ✅ specified

## Statement

The sitemap, page titles, descriptions and structured data (organisation, products, opening hours, job postings) are
generated from the ERP's public data and regenerated at each publication; nothing private reaches them.

## Why

Sites must be found (D475) and built from the ERP's data (BR-F18-02).

## Examples

| Case | Result |
|---|---|
| Opening hours of the restaurant in its structured data | passes |
| Job posting with salary range published in F9 | passes |
| Internal cost price in structured data | fails: never included |

## Applies to

- [UC-F18-21 Publish a blog fed by F5 posts](../use-cases/06-content-and-search/uc-f18-21-publish-a-blog-fed-by-f5-posts.md)
- [UC-F18-26 Set the search-engine basics](../use-cases/06-content-and-search/uc-f18-26-set-the-search-engine-basics.md)
- [UC-F18-14 Run the automatic checks](../use-cases/04-test-and-publish/uc-f18-14-run-the-automatic-checks.md)

## Exceptions

Pages marked "not indexed" are left out of the sitemap.

## Configurable

Marketing edits titles and descriptions per page.

## Open questions

None.

---

⬅️ [BR-F18-19](br-f18-19-sector-templates-carry-the-sectors-mandatory-information.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-21](br-f18-21-sites-backed-up-daily-restored-to-the-preview.md)
