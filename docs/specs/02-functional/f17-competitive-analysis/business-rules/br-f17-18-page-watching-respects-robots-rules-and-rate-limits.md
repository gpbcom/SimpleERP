🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-18 Page watching respects robots rules and rate limits

# 📏 BR-F17-18 Page watching respects robots rules and rate limits

**Status:** ✅ specified

## Statement

A page is watched only when it is public, its robots rules and terms allow it, and the reads stay within the rate limit
set for the site; a page that needs a sign-in or hides behind a bot check is never watched, and a blocked page is not
retried by a trick.

## Why

Watching is useful only while it stays lawful and polite: a site that is overloaded or tricked closes its doors and
exposes the company to a claim. The owner asked to follow competitors' web pages
([D536](../../../06-decisions/f17-competitive-analysis/d536-benchmark-gaps-f17-competitive-analysis.md)). The
France-pack rule on collection stays in
[BR-F17-01 Collection follows the country pack](br-f17-01-analysis-follows-the-country-pack.md).

## Examples

| Case | Result |
|---|---|
| A public pricing page the robots rules allow | watched, one read per 10 seconds at most |
| A page forbidden by the robots rules | refused with the rule |
| A page behind a customer sign-in | refused: not public |
| A page that blocks the reads | Blocked after three failures, no retry by a trick |
| A page changing only a counter | no change recorded |

## Applies to

- [UC-F17-27](../use-cases/08-ads-pages-search-and-tech/uc-f17-27-watch-competitors-web-pages.md)
- [E-F17-22 Watched page](../data/e-f17-22-watched-page.md)
- [E-F17-15 Collection rule](../data/e-f17-15-collection-rule.md)

## Exceptions

None.

## Configurable

The rhythm of each page and the highest read rate, by the owner.

## Open questions

None.

---

⬅️ [BR-F17-17 Ads come only from public ad libraries](br-f17-17-ads-come-only-from-public-ad-libraries.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F17-19 Search data carries its provider and date](br-f17-19-search-data-carries-its-provider-and-date.md)
