🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-37 A quality drop blocks a model or prompt change

# 📏 BR-F3-37 A quality drop blocks a model or prompt change

**Status:** 🔄 waiting for the owner

## Statement

A change of model, provider or prompt goes live only if the evaluation set scores at or above the bar and no previously
passed safety question fails; the administrator may override with a recorded reason.

## Why

As F15 blocks its updates on a quality drop (BR-F15-06), the AI assistant must not get worse silently.

## Examples

| Case | Result |
|---|---|
| Score 88 %, bar 90 % (Proposed) | Blocked |
| Score 96 % | Live |
| A refusal question now answered | Blocked, whatever the score |

## Applies to

- [UC-F3-14 Run the quality evaluation set](../use-cases/11-trust-the-answers/uc-f03-14-run-the-quality-evaluation-set.md)

## Exceptions

None.

## Configurable

The bar (Proposed: 90 %).

## Open questions

None.

---

⬅️ [BR-F3-36 An audit agent checks the agents](br-f03-36-an-audit-agent-checks-agents.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-38 Content is data, never instructions](br-f03-38-content-is-data-never-instructions.md)
