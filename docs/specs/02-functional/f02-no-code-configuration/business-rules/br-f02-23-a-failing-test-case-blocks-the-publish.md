🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-23 A failing test case blocks the publish

# 📏 BR-F2-23 A failing test case blocks the publish

**Status:** ✅ specified

## Statement

Every test case of the changed rules and workflows, and of those they trigger, is replayed at publish; one failure
blocks it.

## Why

A rule that worked must keep working (D459).

## Examples

| Case | Result |
|---|---|
| 200 cases, 1 fails | Blocked, the failure shown |
| All pass | Published |

## Applies to

- [UC-F2-24 Test rules and workflows with test cases](../use-cases/10-change-safely/uc-f02-24-test-rules-and-workflows-with-test-cases.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-22](br-f02-22-a-change-that-breaks-something-is-not-published-unread.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-24](br-f02-24-local-changes-are-kept-unless-a-legal-block-changed.md)
