🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-36 An audit agent checks the agents

# 📏 BR-F3-36 An audit agent checks the agents

**Status:** ✅ specified

## Statement

A read-only audit agent checks agents' actions and their instructions against the company's written policies and reports
each month.

## Why

See [D301](../../../06-decisions/f03-assistant/d301-f3-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| Instruction contradicts the approval policy | Flagged to the administrator |

## Applies to

UC-F3-11

## Exceptions

None.

## Configurable

Policies and report frequency.

## Open questions

None.

---

⬅️ [BR-F3-35 Agents follow thresholds and amount limits](br-f03-35-agents-follow-thresholds-and-limits.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-37](br-f03-37-a-quality-drop-blocks-a-model-or-prompt-change.md)
