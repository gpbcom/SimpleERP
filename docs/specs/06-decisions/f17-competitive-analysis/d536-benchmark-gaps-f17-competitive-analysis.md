🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔭 [Decisions: F17 Competitive analysis](README.md) ›
📜 D536 Benchmark gaps of F17 Competitive analysis

# 📜 D536 Benchmark gaps of F17 Competitive analysis

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four
market-intelligence features that F17 did not cover: competitors' ads, changes on competitors' web pages,
search-position overlap and technology detection. F17 already follows registers, prices, jobs, tenders, patents, reviews
and news under lawful collection rules; these add the advertising, web and search sides.

## Options

- G91 Competitor ads: ads read from public ad libraries only, or no advertising follow-up.
- G92 Website changes: page watching within the robots rules and a rate limit, or no page follow-up.
- G93 Search overlap: search positions from a named provider with their date, or search positions read from the search
  engines' pages.
- G94 Technology detection: detection from public pages only, or no technology detection.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F17 gets four use cases in one new flow, FL-F17-08, each with its screen, its rule, its entity and its list. The search
figures come from the data providers of F17 and count against their budgets; nothing is read behind a sign-in. All at
full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G91 | Competitor ads | UC-F17-26: ads read only from public ad libraries | "Competitor ads" |
| G92 | Website changes | UC-F17-27: page watching that respects robots rules and rate limits | "Website changes" |
| G93 | Search overlap | UC-F17-28: search positions that always carry their provider and date | "Search overlap" |
| G94 | Technology detection | UC-F17-29: technology detection that reads public pages only | "Technology detection" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F17 Competitive analysis").

## Consequences

- G91 Competitor ads:
  [UC-F17-26](../../02-functional/f17-competitive-analysis/use-cases/08-ads-pages-search-and-tech/uc-f17-26-follow-competitors-ads.md),
  [S-F17-25](../../02-functional/f17-competitive-analysis/screens/08-ads-pages-search-and-tech/s-f17-25-competitor-ads.md)
  and
  [BR-F17-17](../../02-functional/f17-competitive-analysis/business-rules/br-f17-17-ads-come-only-from-public-ad-libraries.md),
  with [E-F17-21](../../02-functional/f17-competitive-analysis/data/e-f17-21-ad-record.md) Ad record and its list
  [S-F17-L21](../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l21-ad-records.md).
- G92 Website changes:
  [UC-F17-27](../../02-functional/f17-competitive-analysis/use-cases/08-ads-pages-search-and-tech/uc-f17-27-watch-competitors-web-pages.md),
  [S-F17-26](../../02-functional/f17-competitive-analysis/screens/08-ads-pages-search-and-tech/s-f17-26-page-watch.md)
  and
  [BR-F17-18](../../02-functional/f17-competitive-analysis/business-rules/br-f17-18-page-watching-respects-robots-rules-and-rate-limits.md),
  with [E-F17-22](../../02-functional/f17-competitive-analysis/data/e-f17-22-watched-page.md) Watched page and its list
  [S-F17-L22](../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l22-watched-pages.md).
- G93 Search overlap:
  [UC-F17-28](../../02-functional/f17-competitive-analysis/use-cases/08-ads-pages-search-and-tech/uc-f17-28-compare-search-positions.md),
  [S-F17-27](../../02-functional/f17-competitive-analysis/screens/08-ads-pages-search-and-tech/s-f17-27-search-overlap.md)
  and
  [BR-F17-19](../../02-functional/f17-competitive-analysis/business-rules/br-f17-19-search-data-carries-its-provider-and-date.md),
  with [E-F17-23](../../02-functional/f17-competitive-analysis/data/e-f17-23-keyword.md) Keyword and its list
  [S-F17-L23](../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l23-keywords.md).
- G94 Technology detection:
  [UC-F17-29](../../02-functional/f17-competitive-analysis/use-cases/08-ads-pages-search-and-tech/uc-f17-29-detect-a-sites-technologies.md),
  [S-F17-28](../../02-functional/f17-competitive-analysis/screens/08-ads-pages-search-and-tech/s-f17-28-tech-detection.md)
  and
  [BR-F17-20](../../02-functional/f17-competitive-analysis/business-rules/br-f17-20-detection-reads-public-pages-only.md),
  with [E-F17-24](../../02-functional/f17-competitive-analysis/data/e-f17-24-technology-record.md) Technology record and
  its list [S-F17-L24](../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l24-technology-records.md).
- Drawn in [FL-F17-08](../../02-functional/f17-competitive-analysis/flows/fl-f17-08-ads-pages-search-and-tech.md) Ads,
  pages, search and technologies.

## Related

- [FL-F17-08](../../02-functional/f17-competitive-analysis/flows/fl-f17-08-ads-pages-search-and-tech.md)
- [D382 Competitive analysis coverage](d382-competitive-analysis-coverage.md)
- [D383 Every lawful source, public or paid](d383-competitive-sources-lawful.md)
- [D474 F17 Competitive analysis: gaps and improvements](d474-f17-gaps-and-improvements.md)
- [BR-F17-01](../../02-functional/f17-competitive-analysis/business-rules/br-f17-01-analysis-follows-the-country-pack.md)
- [BR-F17-03](../../02-functional/f17-competitive-analysis/business-rules/br-f17-03-terms-and-robots-respected.md)

---

⬅️ [D535](../f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md) · ⬆️ [Up](README.md) ·
➡️ [D537](../f18-hosted-websites-and-domains/d537-benchmark-gaps-f18-hosted-websites-and-domains.md)
