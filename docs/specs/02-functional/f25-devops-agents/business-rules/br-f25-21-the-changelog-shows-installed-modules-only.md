🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-21 The changelog shows installed modules only

# 📏 BR-F25-21 The changelog shows installed modules only

**Status:** 🔄 waiting for the owner

## Statement

The changelog shows an entry only for a module the company has installed; an entry for a module the company does not
have is never shown, counted or summarised for that company.

## Why

Release notes of modules a company does not use are noise and may reveal products it has not bought. The owner asked for
a customer-facing changelog ([D544](../../../06-decisions/f25-devops-agents/d544-benchmark-gaps-f25-devops-agents.md)).

## Examples

| Case | Result |
|---|---|
| A payroll entry, payroll installed | shown |
| A manufacturing entry, manufacturing not installed | not shown |
| A module installed after the release | older entries shown, marked as before installation |
| A module removed | its entries leave the list and stay in the history |
| The AI assistant asked about a module not installed | it says the module is not installed |

## Applies to

- [UC-F25-28](../use-cases/07-roadmap-beta-and-credits/uc-f25-28-follow-the-changelog-of-my-modules.md)
- [BR-F25-09 The customer is told in plain words](br-f25-09-customer-told-in-plain-words.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-20](br-f25-20-credits-go-to-confirmed-non-duplicate-reports-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-22 A contract gives each role its own files](br-f25-22-a-contract-gives-each-role-its-own-files.md)
