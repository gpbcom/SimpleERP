🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-02 Every paid call is metered

# 📏 BR-F22-02 Every paid call is metered

**Status:** ✅ specified

## Statement

Each paid call (AI request, connector action, scraping page, data provider query) records its company, user, module,
feature, provider, units and cost where it is made, before its result is returned.

## Why

See [D397](../../../06-decisions/f22-unified-cost-management/d397-cost-management-coverage.md).

## Examples

| Case | Result |
|---|---|
| Assistant answer by an outside model | 1 840 tokens, 0.011 EUR, F3 |

## Applies to

Every F22 use case concerned.

- [UC-F22-24 Read the cost KPIs](../use-cases/06-savings-and-kpis/uc-f22-24-read-the-cost-kpis.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F22-01 Bills and allocations follow the country pack](br-f22-01-costs-follow-the-country-pack.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F22-03 Prices versioned per provider](br-f22-03-prices-versioned-per-provider.md)
