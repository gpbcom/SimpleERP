🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D137 F2 notifications

# 📜 D137 F2 notifications

**Status:** ✅ decided

## Context

Which F2 notifications go to whom.

## Options

- Publish summary to administrators.
- Failures to authors.
- Human tasks to their people.
- A weekly digest.

## Choice

All four: the publish summary to administrators (D131); a failing rule or workflow, a loop stopped or an AI step out of
format to its author and the administrators; workflows' approvals and forms to their person, then their manager on
escalation; a weekly digest email to configurators with automation health and unused configuration.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

In-app and email, as F1 (D92).

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)

---

⬅️ [D136 F2 reports](d136-f2-reports.md) · ⬆️ [Up](README.md) ·
➡️ [D138 F3 Assistant scope](../f03-assistant/d138-f3-scope.md)
