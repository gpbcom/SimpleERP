🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-19 Search data carries its provider and date

# 📏 BR-F17-19 Search data carries its provider and date

**Status:** 🔄 waiting for the owner

## Statement

Every search position, volume or share shown in simple-ERP carries the name of the provider that gave it and the date it
was read; figures from two providers are shown side by side and never averaged or merged.

## Why

A position changes daily and differs between providers: without its source and date a figure cannot be checked, and an
average of two providers means nothing. The owner asked to compare search positions
([D536](../../../06-decisions/f17-competitive-analysis/d536-benchmark-gaps-f17-competitive-analysis.md)).

## Examples

| Case | Result |
|---|---|
| A position read on 2026-11-03 | shown with the provider and that date |
| Two providers, positions 5 and 9 | both shown, none averaged |
| A figure older than the refresh rhythm | shown in grey with its age |
| A keyword with no volume | volume shown as unknown, not as zero |
| An export of the overlap | keeps the provider and date columns |

## Applies to

- [UC-F17-28](../use-cases/08-ads-pages-search-and-tech/uc-f17-28-compare-search-positions.md)
- [E-F17-23 Keyword](../data/e-f17-23-keyword.md)
- [E-F17-09 Data provider](../data/e-f17-09-data-provider.md)

## Exceptions

None.

## Configurable

The refresh rhythm and the countries and languages compared, by the marketing person.

## Open questions

None.

---

⬅️ [BR-F17-18](br-f17-18-page-watching-respects-robots-rules-and-rate-limits.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F17-20 Detection reads public pages only](br-f17-20-detection-reads-public-pages-only.md)
