🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-17 Ads come only from public ad libraries

# 📏 BR-F17-17 Ads come only from public ad libraries

**Status:** ✅ specified

## Statement

Ads are read only from public ad libraries and from the competitor's own public pages; an ad record keeps the library's
name, its address and the date it was read, and never holds any information about the people the ad was shown to.

## Why

The ads are public by design, but a signed-in feed, a fake account or a targeting profile is not. The owner asked to
follow competitors' ads
([D536](../../../06-decisions/f17-competitive-analysis/d536-benchmark-gaps-f17-competitive-analysis.md)). The
France-pack rule on lawful collection stays in
[BR-F17-01 Collection follows the country pack](br-f17-01-analysis-follows-the-country-pack.md).

## Examples

| Case | Result |
|---|---|
| A public ad library listing the competitor's ads | read and recorded |
| A social network's signed-in feed | refused: not a public library |
| An ad shown only to a targeted audience, not listed | not recorded |
| A library giving a reach range | the range is kept as given |
| A library that forbids automatic reading in its terms | skipped and listed |

## Applies to

- [UC-F17-26](../use-cases/08-ads-pages-search-and-tech/uc-f17-26-follow-competitors-ads.md)
- [E-F17-21 Ad record](../data/e-f17-21-ad-record.md)
- [E-F17-15 Collection rule](../data/e-f17-15-collection-rule.md)

## Exceptions

None.

## Configurable

The libraries read for each competitor, by the owner or the marketing person.

## Open questions

None.

---

⬅️ [BR-F17-16 Call topics feed cards without people](br-f17-16-call-topics-feed-cards-without-people.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F17-18](br-f17-18-page-watching-respects-robots-rules-and-rate-limits.md)
