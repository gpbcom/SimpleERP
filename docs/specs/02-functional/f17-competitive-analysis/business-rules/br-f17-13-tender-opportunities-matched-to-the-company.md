🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F17-13 Tender opportunities matched to the company

# 📏 BR-F17-13 Tender opportunities matched to the company

**Status:** ✅ specified

## Statement

Tender notices are read only from the official public sources and matched to the company's activity codes, areas, size
and past contracts; each opportunity keeps its source, deadline and the reason it matched.

## Why

Answering public tenders is a growth path for SC01, SC07, SC12 and SC16 (D474); facts keep their source (BR-F17-02).

## Examples

| Case | Result |
|---|---|
| Notice for building works in the company's department, activity code matching | passes: opportunity |
| Notice outside the areas served | fails: ignored |
| Notice with a deadline in 2 days | passes: flagged "closing soon" |

## Applies to

- [UC-F17-21 Watch tenders to answer](../use-cases/05-tender-watch/uc-f17-21-watch-tenders-to-answer.md)
- [UC-F17-05 Follow tenders won](../use-cases/02-collect-signals/uc-f17-05-follow-tenders-won.md)

## Exceptions

None.

## Configurable

The company sets its activity codes, areas, minimum and maximum amounts.

## Open questions

None.

---

⬅️ [BR-F17-12 Win and loss from real deals](br-f17-12-win-loss-from-real-deals.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F17-14 Data costs within their budget](br-f17-14-data-costs-within-their-budget.md)
