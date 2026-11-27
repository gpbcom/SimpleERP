🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F17-10 Alerts have thresholds

# 📏 BR-F17-10 Alerts have thresholds

**Status:** ✅ specified

## Statement

An alert fires on a change above its threshold (price change, new product, new site, hiring burst, tender won) and at
most once a day per competitor, unless urgent.

## Why

See [D382](../../../06-decisions/f17-competitive-analysis/d382-competitive-analysis-coverage.md).

## Examples

| Case | Result |
|---|---|
| Price down 2 %, threshold 5 % | No alert |

## Applies to

Every F17 use case concerned.

## Exceptions

None.

## Configurable

Thresholds.

## Open questions

None.

---

⬅️ [BR-F17-09 Analyses are confidential by default](br-f17-09-analyses-are-confidential.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F17-11 Facts kept for a set period](br-f17-11-facts-kept-for-a-set-period.md)
