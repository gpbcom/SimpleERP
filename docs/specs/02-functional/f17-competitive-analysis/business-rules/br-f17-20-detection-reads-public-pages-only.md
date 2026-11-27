🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-20 Detection reads public pages only

# 📏 BR-F17-20 Detection reads public pages only

**Status:** 🔄 waiting for the owner

## Statement

Technology detection reads only the public pages of a site and the public headers that come with them, within the site's
robots rules and the read rate; it never scans ports, tries sign-ins, reads private files or uses what the site did not
publish.

## Why

What a page shows is public; probing a server is an intrusion. Keeping detection to public pages keeps it lawful and
keeps the findings checkable by anyone who opens the same page. The owner asked for technology detection
([D536](../../../06-decisions/f17-competitive-analysis/d536-benchmark-gaps-f17-competitive-analysis.md)).

## Examples

| Case | Result |
|---|---|
| A generator tag in a public page | a finding with that page as evidence |
| A script address shared by two tools | both possible, none sure |
| An open port found by a scan | never read: the detection does not scan |
| A private file path guessed | never tried |
| A technology stated by the customer on a call | added by hand and marked as stated |

## Applies to

- [UC-F17-29](../use-cases/08-ads-pages-search-and-tech/uc-f17-29-detect-a-sites-technologies.md)
- [E-F17-24 Technology record](../data/e-f17-24-technology-record.md)
- [E-F17-15 Collection rule](../data/e-f17-15-collection-rule.md)

## Exceptions

None.

## Configurable

The pages read per site, by the sales person within the owner's rate.

## Open questions

None.

---

⬅️ [BR-F17-19 Search data carries its provider and date](br-f17-19-search-data-carries-its-provider-and-date.md) ·
⬆️ [Up](README.md)
