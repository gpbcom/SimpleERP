🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📦 [Decisions: F7 Purchasing and stock](README.md) ›
📜 D36 What a location holds

# 📜 D36 What a location holds

**Status:** ✅ decided

## Context

A company can have several locations (D32). What does each one hold of its own.

## Options

- Address and opening hours.
- Own stock.
- Own staff and manager.
- Own legal identity (SIRET).

## Choice

A location has its own address and opening hours, its own stock, and its own staff and manager. It has no legal identity
of its own.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

- Stock is kept per location, with transfers between locations (F7).
- Employees belong to a location; a location's manager approves for it, and permissions can be limited to a location
  (F1, F9, T2).
- Documents and schedules use the location's address and hours.
- French establishments have a SIRET each, kept on the site, optional
  ([D453](../f01-administration/d453-optional-siret-on-a-site.md)).

## Related

- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md)
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md)
- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md)

---

⬅️ [D35 Eight example companies](../ux/d35-eight-example-companies.md) · ⬆️ [Up](README.md) ·
➡️ [D37 Remote access](../security-and-compliance/d37-remote-access.md)
