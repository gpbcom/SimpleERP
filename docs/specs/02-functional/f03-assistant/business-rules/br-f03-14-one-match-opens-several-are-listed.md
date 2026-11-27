🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-14 One match opens, several are listed

# 📏 BR-F3-14 One match opens, several are listed

**Status:** ✅ specified

## Statement

A "find" request that matches one record, screen or setting the user may reach opens it at once; several matches give a
list of at most 10, best first, with "show all" opening the search results; none is said, as BR-F3-04.

## Why

Navigation by sentence must be quick. See [D165](../../../06-decisions/f03-assistant/d165-assistant-find.md).

## Examples

| Case | Result |
|---|---|
| "Durand's last quote" | Quote Q-2026-118 opens |
| "Martin's quotes" with 2 Martins | A list grouped by customer |
| "Leave settings" for an employee | Not reachable: "Leave settings are for HR; you can see your own leave in My leave" (BR-F3-06) |

## Applies to

- [UC-F3-05](../use-cases/05-find-and-get-guided/uc-f03-05-find-a-record-or-a-screen-get-guided.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-13 Drafted texts are traced](br-f03-13-drafted-texts-are-traced.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-15 Guidance matches the company's setup](br-f03-15-guidance-matches-the-company-s-setup.md)
