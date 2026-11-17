🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 📈 TC-15 Large lists, reports and dashboards

# 📈 TC-15 Large lists, reports and dashboards

**Status:** ✅ listed for the technical interviews

## Challenge

Keep lists, searches, reports and dashboards fast for large companies and long histories, across custom fields and
modules.

## Raised by

- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md)
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md)
- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md)
- [F21 Onboarding and module activation](../../02-functional/f21-onboarding-and-modules/README.md)

## Why it is hard

- The target is 95 % of screens within 1 second for 250 users working at once on one company.
- Reports mix modules and custom fields chosen by users.
- Competitive analysis keeps time series of prices and signals.

## Already decided

- [D19](../../06-decisions/foundations/d19-one-database-per-company.md) One database per company

## Options to weigh

- Read models or a reporting store next to the transactional database.
- Server-side paging, filtering and exports everywhere.
- Time-series storage for collected signals.

## Settled in

- 19b Performance and capacity ([chapter](../../../technical/infrastructure/performance-and-capacity.md))
- 19c Storage ([chapter](../../../technical/data/storage.md))
- Then the technical capabilities: [T1 Companies and data isolation](../t01-companies-and-data-isolation/README.md).

## Questions for the interview

- What history must stay online, and what moves to an archive?
- Must reports be live, or may they lag by minutes?

---

⬅️ [TC-14 Planning and calculation engines](tc-14-planning-and-calculation-engines.md) · ⬆️ [Up](README.md) ·
➡️ [TC-16 Files, media and archives](tc-16-files-media-and-archives.md)
