🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-02 One USER feature, one ticket

# 📏 BR-F25-02 One USER feature, one ticket

**Status:** ✅ specified

## Statement

Each customer request becomes one GitHub feature of the USER family with exactly one ticket, labelled
USER-FEATURE-REQUEST or USER-REPORTED-BUG, written from the request in the ticket rules' format (GIT-10).

## Why

See [D433](../../../06-decisions/f25-devops-agents/d433-user-family-and-labels.md).

## Examples

| Case | Result |
|---|---|
| Bug reported in the app | USER feature, one USER-REPORTED-BUG ticket |

## Applies to

Every F25 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-01 Agents follow the country pack](br-f25-01-agents-follow-the-country-pack.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-03 Duplicates are merged](br-f25-03-duplicates-merged.md)
