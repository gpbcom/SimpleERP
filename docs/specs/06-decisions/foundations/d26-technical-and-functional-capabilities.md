🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D26 Technical and functional capabilities

# 📜 D26 Technical and functional capabilities

**Status:** ✅ decided

## Context

The owner asked to tell technical capabilities from functional ones (ticket GH-2).

## Options

- The split T1 to T10 and F1 to F14, with UX as a section of its own.
- Keep the P, B and X IDs, tagged.

## Choice

Technical capabilities T1 to T11 (what the platform provides) and functional capabilities F1 to F15 (what users do),
with UX as a cross-cutting section. The table below maps the earlier IDs.

| Earlier ID | New ID | Capability | Step | Needs |
|---|---|---|---|---|
| P1 | T1, F1 | Companies: one or several per install, one database each | 1. Platform | |
| P2 | T2, F1 | Users, roles, record rules and sign-in | 1. Platform | P1 |
| P3 | T3 | Audit trail: who did what, when, through which channel | 1. Platform | P2 |
| P4 | F2 | No-code configuration: custom fields, statuses, forms, document templates, workflows | 1. Platform | P2 |
| P5 | T4, F14 | Plugins: install, update and remove modules built on the public API | 1. Platform | P4, P6 |
| P6 | T5 | API and webhooks | 1. Platform | P2 |
| P7 | T6 | MCP and A2A, both ways | 1. Platform | P6 |
| P8 | T7 | AI providers: local models by default, an external provider per feature | 1. Platform | P1 |
| P9 | F3, T8 | Assistant: answers from the ERP's data within the user's permissions | 1. Platform | P2, P7, P8 |
| P10 | F4 | Meetings: imported transcripts, the meeting bot, customisable summaries | 1. Platform | P8 |
| B1 | F6 | Customers and sales, with the customer portal | 2. Customers and sales | Platform |
| B2 | F7 | Purchasing and stock, with the supplier portal | 3. Purchasing and stock | B1 |
| B3 | F8 | Accounting, with the external accountant's access | 4. Accounting | B1, B2 |
| B4 | F9 | HR and projects, with employee self-service | 5. HR and projects | B3 |
| X1 | F10 | Point of sale (plugin) | 6. Plugins | B1, B2, B3 |
| X2 | F11 | Online shop (plugin) | 6. Plugins | B1, B2 |
| X3 | F12 | Manufacturing (plugin) | 6. Plugins | B2 |
| X4 | F13 | Payroll (plugin) | 6. Plugins | B3, B4 |

New in GH-2, with no earlier ID: F5 social media, F15 legal assistant, T8 RAG platform (Milvus), T9 install,
backups and updates, T10 translations and notifications, T11 legal corpora.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Every page uses the new IDs. The earlier IDs stay in the table above, so that the earlier draft can be followed.

## Related

- [Functional capabilities](../../02-functional/README.md)
- [Technical capabilities](../../03-technical/README.md)
- [Roadmap](../../00-vision/roadmap/roadmap.md)

---

⬅️ [D25 First-version targets](d25-first-version-targets.md) · ⬆️ [Up](README.md) ·
➡️ [D27 RAG platform on Milvus](d27-rag-platform-on-milvus.md)
